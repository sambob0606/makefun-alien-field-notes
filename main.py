#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one line -- a review of planet Earth left by an alien tourist --
to /output/entry.txt (or $OUTPUT_PATH). The line is a deadpan tourist
verdict: the alien came for the oceans, stayed for the locals' ghost
costume candy ritual, and would be abducted again.
"""

import os
import sys

MAX_CHARS = 200

LINE = (
    "Came for the oceans, stayed because the locals dress as ghosts "
    "once a year and demand candy from strangers. "
    "Five stars \u2014 would be abducted again."
)


def validate_line(line: str) -> str:
    """Enforce the competition's output contract: one line, 1-200 chars."""
    text = line.strip()
    if not text:
        raise ValueError("review line must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"review line is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("review line must be a single line")
    return text


def output_path() -> str:
    """Resolve where entry.txt goes: $OUTPUT_PATH, then $MAKEFUN_OUTPUT_DIR."""
    direct = os.environ.get("OUTPUT_PATH")
    if direct:
        return direct
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(output_dir, "entry.txt")


def write_entry(line: str) -> tuple[str, str]:
    """Validate the review line and write it as one line to entry.txt.

    Returns the (path, text) pair so the caller can echo what was graded.
    """
    text = validate_line(line)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return path, text


def main() -> int:
    path, text = write_entry(LINE)
    print(f"wrote {len(text)}-char review to {path}: {text}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
