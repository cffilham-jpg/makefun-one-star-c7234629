#!/usr/bin/env python3
"""One-star review of something essential.

Writes a single deadpan one-star review of gravity to entry.txt.
The review is at most 160 characters, one line, valid UTF-8.
"""

import os
import sys

LINE = "Gravity works fine until you drop your phone. Then it works perfectly. One star."

MAX_CHARS = 160


def validate(text: str) -> None:
    """Raise ValueError unless text satisfies the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError("entry must be at most 160 characters")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    if "!" in text:
        raise ValueError("entry must not contain an exclamation mark")
    for ch in text:
        if ord(ch) < 32 or ord(ch) == 127:
            raise ValueError("entry must not contain control characters")
    text.encode("utf-8")


def output_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        return os.path.join(out_dir, "entry.txt")
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "output", "entry.txt")


def main() -> int:
    validate(LINE)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
