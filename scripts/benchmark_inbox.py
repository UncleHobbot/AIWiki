#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/benchmark_inbox.py
==========================
Benchmark sequential vs parallel fetch on a synthetic batch of inbox items.

Creates simulated items whose fetch durations mirror real observed averages,
runs both approaches timed, and prints a wall-clock comparison table.

Usage:
    python scripts/benchmark_inbox.py [--items 20] [--workers 8] [--runs 3]
                                      [--speedup 10] [--json]

Options:
    --items N       Batch size (default: 20)
    --workers N     Thread pool size for parallel run (default: 8)
    --runs N        Number of repetitions to average (default: 3)
    --speedup N     Factor by which simulated sleep is compressed (default: 10)
                    e.g. 10 means a "15s" fetch actually waits 1.5s
    --json          Emit full JSON report to stdout in addition to log output
"""

import io
import json
import sys
import time
import random
import datetime
import statistics
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


def log(msg: str, level: str = "INFO") -> None:
    safe = msg.encode("ascii", errors="replace").decode("ascii")
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {level}: {safe}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Simulated fetch timing distributions (seconds, real-world observed ranges)
# ---------------------------------------------------------------------------
#
# Basis:
#   link     — HTTP fetch + extraction via fetch_url.py; varies by site speed
#   youtube  — yt-dlp transcript download; short videos < 30s
#   twitter  — tweet fetch + t.co expansion
#   clipping — local file read; essentially I/O only
#   paper    — arxiv HTML or PDF fetch; usually larger payloads
#   post     — no network; just text parsing
#   reddit   — Reddit API; 14 subreddits x ~15s average
#
FETCH_TIMING = {
    #           (min_s, max_s, label)
    "link":     (5.0,  15.0,  "HTTP fetch"),
    "youtube":  (20.0, 60.0,  "transcript download"),
    "twitter":  (3.0,   8.0,  "tweet + t.co expand"),
    "clipping": (0.05,  0.5,  "local file read"),
    "paper":    (8.0,  25.0,  "arxiv/paper fetch"),
    "post":     (0.01,  0.1,  "text parse"),
    "reddit":   (10.0, 30.0,  "Reddit API / subreddit"),
}

# Distribution across types for a mixed 20-item inbox batch
BATCH_DISTRIBUTION = {
    "link":     5,
    "youtube":  4,
    "twitter":  3,
    "clipping": 3,
    "paper":    2,
    "post":     2,
    "reddit":   1,   # represents 1 subreddit scan (14 in real use)
}


# ---------------------------------------------------------------------------
# Simulation helpers
# ---------------------------------------------------------------------------

def generate_batch(n: int) -> list:
    """
    Build n synthetic items distributed proportionally across source types.
    Shuffled so parallel workers see a realistic mix, not all-slow then all-fast.
    """
    types = list(FETCH_TIMING.keys())
    # Scale BATCH_DISTRIBUTION to hit exactly n items
    total_weight = sum(BATCH_DISTRIBUTION.values())
    items = []
    remainder_pool: list = []
    for t in types:
        count = int(round(BATCH_DISTRIBUTION[t] / total_weight * n))
        for i in range(count):
            items.append({"type": t, "url": f"https://example.com/{t}/{i+1}"})
        # Track fractional remainders for adjustment
        remainder_pool.extend([t] * (BATCH_DISTRIBUTION[t] * n % total_weight > 0))
    # Pad or trim to exactly n
    while len(items) < n:
        t = remainder_pool.pop(0) if remainder_pool else "link"
        items.append({"type": t, "url": f"https://example.com/{t}/extra"})
    items = items[:n]
    random.shuffle(items)
    return items


def simulated_fetch(item: dict, speedup: float = 1.0) -> dict:
    """Simulate a fetch with a realistic random delay (compressed by speedup)."""
    t = item["type"]
    lo, hi, _ = FETCH_TIMING[t]
    real_delay = random.uniform(lo, hi)
    time.sleep(real_delay / speedup)
    return {
        "type": t,
        "url": item["url"],
        "success": True,
        "fetch_time_s": real_delay,   # report the real (uncompressed) duration
    }


# ---------------------------------------------------------------------------
# Benchmark runners
# ---------------------------------------------------------------------------

def run_sequential(items: list, speedup: float) -> tuple:
    """Process items one by one."""
    t0 = time.monotonic()
    results = [simulated_fetch(item, speedup) for item in items]
    return time.monotonic() - t0, results


def run_parallel(items: list, workers: int, speedup: float) -> tuple:
    """Process items concurrently with ThreadPoolExecutor."""
    t0 = time.monotonic()
    results = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(simulated_fetch, item, speedup): item for item in items}
        for future in as_completed(futures):
            results.append(future.result())
    return time.monotonic() - t0, results


# ---------------------------------------------------------------------------
# Reporting helpers
# ---------------------------------------------------------------------------

def _fmt_time(seconds: float) -> str:
    if seconds >= 60:
        return f"{seconds/60:.1f} min ({seconds:.0f}s)"
    return f"{seconds:.0f}s"


def _type_summary(results: list) -> dict:
    by_type: dict = defaultdict(list)
    for r in results:
        by_type[r["type"]].append(r["fetch_time_s"])
    return {
        t: {
            "count": len(times),
            "avg_s": round(statistics.mean(times), 1),
            "max_s": round(max(times), 1),
            "total_s": round(sum(times), 1),
        }
        for t, times in by_type.items()
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(
        description="Benchmark sequential vs parallel inbox fetch (simulated timing)."
    )
    parser.add_argument("--items", type=int, default=20, help="Batch size (default: 20)")
    parser.add_argument("--workers", type=int, default=8,
                        help="Parallel thread count (default: 8)")
    parser.add_argument("--runs", type=int, default=3,
                        help="Repetitions to average (default: 3)")
    parser.add_argument("--speedup", type=float, default=10.0,
                        help="Simulation speed multiplier (default: 10x)")
    parser.add_argument("--json", action="store_true",
                        help="Emit JSON report to stdout")
    args = parser.parse_args()

    log(f"Benchmark: {args.items} items | {args.workers} workers | "
        f"{args.runs} run(s) | {args.speedup}x speedup")

    items = generate_batch(args.items)
    dist = Counter(i["type"] for i in items)
    log("Item distribution: " + ", ".join(f"{t}={c}" for t, c in sorted(dist.items())))
    log("")

    # --- Theoretical estimate (no simulation needed) ---
    theory_seq = sum(
        dist.get(t, 0) * ((lo + hi) / 2)
        for t, (lo, hi, _) in FETCH_TIMING.items()
    )
    # Parallel wall time = slowest type's total work / workers (for that type)
    # (simplified: max of per-type totals since each type runs in parallel with others)
    type_totals = {
        t: dist.get(t, 0) * ((lo + hi) / 2)
        for t, (lo, hi, _) in FETCH_TIMING.items()
    }
    bottleneck_type = max(type_totals, key=type_totals.get)
    # With unlimited workers, parallel time ≈ max single item in slowest type
    # With workers=N, it's ceil(count/N) * avg for that type.
    bottleneck_items = dist.get(bottleneck_type, 1)
    bt_lo, bt_hi, _ = FETCH_TIMING[bottleneck_type]
    bt_avg = (bt_lo + bt_hi) / 2
    import math
    theory_par = math.ceil(bottleneck_items / args.workers) * bt_avg
    theory_speedup = theory_seq / theory_par if theory_par > 0 else 1.0

    log("--- Theoretical estimates (based on observed fetch averages) ---")
    log(f"  Sequential:   {_fmt_time(theory_seq)}")
    log(f"  Parallel:     {_fmt_time(theory_par)}  [bottleneck: {bottleneck_type}]")
    log(f"  Speedup:      {theory_speedup:.1f}x")
    log(f"  Time saved:   {_fmt_time(theory_seq - theory_par)} "
        f"({(theory_seq - theory_par)/theory_seq*100:.0f}%)")
    log("")

    # --- Simulated runs ---
    log(f"Running {args.runs} simulated pass(es) at {args.speedup}x speed...")
    seq_wall_times: list = []
    par_wall_times: list = []
    last_seq_results: list = []
    last_par_results: list = []

    for run in range(1, args.runs + 1):
        batch = generate_batch(args.items)   # fresh shuffle each run
        log(f"  Run {run}/{args.runs}: sequential...", "DEBUG")
        sw, last_seq_results = run_sequential(batch, args.speedup)
        seq_wall_times.append(sw * args.speedup)   # de-compress back to real seconds

        log(f"  Run {run}/{args.runs}: parallel ({args.workers} workers)...", "DEBUG")
        pw, last_par_results = run_parallel(batch, args.workers, args.speedup)
        par_wall_times.append(pw * args.speedup)

        log(f"  Run {run}: seq={seq_wall_times[-1]:.0f}s  par={par_wall_times[-1]:.0f}s  "
            f"speedup={seq_wall_times[-1]/par_wall_times[-1]:.1f}x")

    seq_avg = statistics.mean(seq_wall_times)
    par_avg = statistics.mean(par_wall_times)
    sim_speedup = seq_avg / par_avg if par_avg > 0 else 1.0
    sim_saved = seq_avg - par_avg
    sim_pct = sim_saved / seq_avg * 100 if seq_avg > 0 else 0

    log("")
    log("=" * 60)
    log("BENCHMARK RESULTS")
    log("=" * 60)
    log(f"Batch size : {args.items} items  ({args.workers} parallel workers)")
    log(f"Simulated wall-clock times (averaged over {args.runs} run(s)):")
    log(f"  Sequential (current) : {_fmt_time(seq_avg)}")
    log(f"  Parallel   (new)     : {_fmt_time(par_avg)}")
    log(f"  Speedup              : {sim_speedup:.1f}x")
    log(f"  Time saved           : {_fmt_time(sim_saved)} ({sim_pct:.0f}%)")
    log("")
    log("Theoretical real-world estimates:")
    log(f"  Sequential (current) : {_fmt_time(theory_seq)}")
    log(f"  Parallel   (new)     : {_fmt_time(theory_par)}")
    log(f"  Speedup              : {theory_speedup:.1f}x")
    log(f"  Time saved           : {_fmt_time(theory_seq - theory_par)} "
        f"({(theory_seq - theory_par)/theory_seq*100:.0f}%)")

    # Per-type breakdown (last parallel run)
    type_stats = _type_summary(last_par_results)
    log("")
    log("Per-type breakdown (simulated, last parallel run):")
    log(f"  {'type':12s} {'count':>6} {'avg_s':>8} {'max_s':>8} {'subtotal':>10}")
    log(f"  {'-'*12} {'-'*6} {'-'*8} {'-'*8} {'-'*10}")
    for t, s in sorted(type_stats.items(), key=lambda x: -x[1]["total_s"]):
        log(f"  {t:12s} {s['count']:>6} {s['avg_s']:>7.1f}s {s['max_s']:>7.1f}s "
            f"{s['total_s']:>9.1f}s")

    # --- Persist report ---
    report = {
        "benchmark_date": datetime.datetime.utcnow().isoformat() + "Z",
        "config": {
            "items": args.items,
            "workers": args.workers,
            "runs": args.runs,
            "speedup_factor": args.speedup,
        },
        "item_distribution": dict(dist),
        "theoretical": {
            "sequential_s": round(theory_seq, 1),
            "parallel_s": round(theory_par, 1),
            "speedup": round(theory_speedup, 2),
            "time_saved_s": round(theory_seq - theory_par, 1),
            "pct_saved": round((theory_seq - theory_par) / theory_seq * 100, 1),
            "bottleneck_type": bottleneck_type,
        },
        "simulated": {
            "sequential_avg_s": round(seq_avg, 1),
            "parallel_avg_s": round(par_avg, 1),
            "speedup": round(sim_speedup, 2),
            "time_saved_s": round(sim_saved, 1),
            "pct_saved": round(sim_pct, 1),
            "raw_seq_wall_times_s": [round(t, 1) for t in seq_wall_times],
            "raw_par_wall_times_s": [round(t, 1) for t in par_wall_times],
        },
        "type_breakdown": type_stats,
    }

    out_path = Path(".state/benchmark_results.json")
    out_path.parent.mkdir(exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
        f.write("\n")
    log(f"\nFull report saved: {out_path}")

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))

    return 0


if __name__ == "__main__":
    sys.exit(main())
