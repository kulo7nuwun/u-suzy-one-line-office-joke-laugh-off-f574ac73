#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to /output/entry.txt,
validating it against the competition gate first: UTF-8 text, 1-200
characters, not only whitespace, exactly one line.
"""

import os
import sys

JOKE = (
    "I asked for a raise and my boss gave me a standing desk instead, "
    "so now I stand all day thinking about my salary."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate(text: str) -> None:
    """Raise ValueError unless the text passes the competition gate."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def main() -> int:
    validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(JOKE)
    # Read the file back and re-validate: what the judge reads is what
    # we checked, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != JOKE:
        raise ValueError("written entry does not match the validated joke")
    validate(written)
    print(f"Wrote {len(JOKE)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
