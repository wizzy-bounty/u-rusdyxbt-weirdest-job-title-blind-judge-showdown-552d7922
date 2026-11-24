#!/usr/bin/env python3
"""Weirdest Job Title entry — program/v1.

Writes a single job title to entry.txt in the directory pointed to by
MAKEFUN_OUTPUT_DIR (fallback /output), then prints the character count
and the output path.

Gate (enforced here before writing):
- text is UTF-8
- length is 1-60 characters
- not whitespace-only
- nothing but the job title itself
"""

import os
import sys

JOB_TITLE = "Professional Mourner for Strangers' Funerals"


def validate_entry(title: str) -> tuple[str | None, int]:
    """Validate the job title text; return (validated text, 0) or (None, 1)."""
    # Gate: length 1-60 characters.
    length = len(title)
    if not 1 <= length <= 60:
        print(f"error: title length {length} outside 1-60 range", file=sys.stderr)
        return None, 1

    # Gate: not whitespace-only.
    if not title.strip():
        print("error: title is whitespace-only", file=sys.stderr)
        return None, 1

    # Gate: UTF-8 encodable.
    try:
        title.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: title is not UTF-8: {exc}", file=sys.stderr)
        return None, 1

    return title, 0


def main() -> int:
    title, err = validate_entry(JOB_TITLE)
    if err:
        return err

    length = len(title)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")

    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(title + "\n")

    print(f"length: {length} characters")
    print(f"output: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
