#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
scripts/log_run.py
==================
Append a timestamped entry to log.md.

Each wiki command calls this as its final step so log.md is never skipped.

Usage:
    python scripts/log_run.py <command> <message>

Examples:
    python scripts/log_run.py "/wiki-reddit" "14 subs, 2 created: foo (tools), bar (news). Index: 94."
    python scripts/log_run.py "/wiki-links" "5 URLs processed. 3 created, 1 updated, 1 failed."

Output line format:
    **HH:MM /command** — <message>

The script finds or creates today's ## YYYY-MM-DD heading automatically.
"""

import io
import sys
import datetime
import pathlib

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

LOG_FILE = pathlib.Path(__file__).parent.parent / "log.md"


def append_log(command: str, message: str) -> None:
    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M")
    entry = f"**{time_str} {command}** — {message}"

    text = LOG_FILE.read_text(encoding="utf-8") if LOG_FILE.exists() else "# LLM Wiki — Activity Log\n"

    heading = f"## {today}"
    if heading in text:
        # Insert entry just before the next ## heading (or at end)
        lines = text.splitlines(keepends=True)
        insert_at = len(lines)
        found_heading = False
        for i, line in enumerate(lines):
            if line.strip() == heading:
                found_heading = True
            elif found_heading and line.startswith("## "):
                insert_at = i
                break

        lines.insert(insert_at, "\n" + entry + "\n")
        text = "".join(lines)
    else:
        # Append new date heading + entry
        text = text.rstrip("\n") + f"\n\n---\n\n{heading}\n\n{entry}\n"

    LOG_FILE.write_text(text, encoding="utf-8")
    print(f"[log.md] {entry}")


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: log_run.py <command> <message>", file=sys.stderr)
        print('Example: log_run.py "/wiki-reddit" "14 subs, 2 entries created."', file=sys.stderr)
        return 1
    command = sys.argv[1]
    message = " ".join(sys.argv[2:])
    append_log(command, message)
    return 0


if __name__ == "__main__":
    sys.exit(main())
