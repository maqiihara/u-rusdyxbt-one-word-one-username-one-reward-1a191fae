"""Emit the entrant's own make.fun handle as a single word.

The competition asks for exactly one word in the output file: the
entrant's username, with nothing else around it. This script keeps
that contract tight -- one line, no trailing newline, no padding.
"""

import os

HANDLE = "kuroshinne"


def _checked_word(word):
    """Return the word only if it is a single clean token."""
    if not word or word != word.strip():
        raise ValueError("handle must not be empty or padded")
    if any(ch.isspace() for ch in word):
        raise ValueError("handle must be a single word")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in word):
        raise ValueError("handle must not contain control characters")
    if not 1 <= len(word) <= 30:
        raise ValueError("handle must be 1-30 characters")
    return word


def main():
    word = _checked_word(HANDLE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)


if __name__ == "__main__":
    main()
