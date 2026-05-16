#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/_template.py
====================
Boilerplate for every new LLM-Wiki helper script.

Copy this file, rename it, and replace the module docstring and main() body.
Do NOT delete the UTF-8 setup block at the top — it prevents CP1252 crashes
on Windows when any non-ASCII character reaches stdout/stderr.

Usage pattern:
    python scripts/myscript.py [args]
"""

import io
import json
import sys


# ---------------------------------------------------------------------------
# 1. UTF-8 stdout/stderr — must come before any print() or logging call.
#    Windows defaults to CP1252; this forces UTF-8 for the process lifetime.
#    The errors="replace" fallback keeps non-representable bytes from crashing
#    the script (they show as '?' instead of raising UnicodeEncodeError).
# ---------------------------------------------------------------------------
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


# ---------------------------------------------------------------------------
# 2. File I/O helper — always opens files with explicit UTF-8 encoding.
#    Use these instead of plain open() so you never rely on the OS default.
# ---------------------------------------------------------------------------
def read_text(path: str) -> str:
    """Read a text file as UTF-8."""
    with open(path, encoding="utf-8") as f:
        return f.read()


def write_text(path: str, content: str) -> None:
    """Write a UTF-8 text file, creating parent dirs if needed."""
    import pathlib
    pathlib.Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def read_json(path: str):
    """Read a JSON file as UTF-8."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_json(path: str, data, indent: int = 2) -> None:
    """Write pretty-printed JSON as UTF-8 with no trailing comma."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)
        f.write("\n")


# ---------------------------------------------------------------------------
# 3. ASCII-only logging helper — safe for Windows CP1252 consoles even if
#    the reconfigure above is somehow bypassed (e.g., piped output).
#    Strips or replaces any character outside the printable ASCII range.
# ---------------------------------------------------------------------------
import datetime


def log(msg: str, level: str = "INFO") -> None:
    """
    Print a timestamped log line containing only printable ASCII.

    Non-ASCII characters are replaced with '?' so the line always survives
    Windows CP1252, PowerShell redirection, and Task Scheduler log capture.
    """
    safe = msg.encode("ascii", errors="replace").decode("ascii")
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {level}: {safe}", file=sys.stderr)


# ---------------------------------------------------------------------------
# 4. yt-dlp JSON-line parser — yt-dlp writes download-progress lines to the
#    same stream as JSON output, so raw stdout cannot be fed directly to
#    json.loads().  This parser discards every line that does not start with
#    '{' or '[', then concatenates and parses the remainder.
#
#    Pattern observed in the wild:
#        [youtube] Extracting URL: https://...
#        [download]   0.0% of ...
#        {"id": "abc123", "title": "...", ...}
# ---------------------------------------------------------------------------
def parse_ytdlp_json(raw: str):
    """
    Extract and parse the JSON object/array embedded in yt-dlp output.

    Raises json.JSONDecodeError if no valid JSON is found after stripping
    progress/info lines.
    """
    json_lines = []
    in_json = False

    for line in raw.splitlines():
        stripped = line.strip()
        if not in_json:
            # JSON starts at the first line beginning with '{' or '['
            if stripped.startswith("{") or stripped.startswith("["):
                in_json = True
                json_lines.append(line)
        else:
            json_lines.append(line)

    if not json_lines:
        raise json.JSONDecodeError("No JSON content found in yt-dlp output", raw, 0)

    return json.loads("\n".join(json_lines))


def parse_ytdlp_json_stream(raw: str):
    """
    Parse yt-dlp output that may contain *multiple* JSON objects (one per
    line), interleaved with progress text.  Returns a list of parsed objects.

    Use this when yt-dlp is invoked with --print-json on a playlist or when
    multiple --newline entries appear.
    """
    results = []
    for line in raw.splitlines():
        stripped = line.strip()
        if stripped.startswith("{") or stripped.startswith("["):
            try:
                results.append(json.loads(stripped))
            except json.JSONDecodeError:
                pass  # partial line — skip
    return results


# ---------------------------------------------------------------------------
# 5. Script entry point — replace the body of main() with your logic.
#    Keep the UTF-8 setup block (section 1) and the helpers above as-is.
# ---------------------------------------------------------------------------
def main() -> int:
    """
    Replace this with your script's logic.
    Return 0 on success, non-zero on failure (used by Task Scheduler / CI).
    """
    import argparse
    parser = argparse.ArgumentParser(description="Replace this description.")
    parser.add_argument("input", help="Replace with your positional arg")
    args = parser.parse_args()

    log(f"Processing: {args.input}")

    # --- your code here ---

    log("Done.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
