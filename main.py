"""Funniest Autocorrect Fail — make.fun entry.

Writes one original autocorrect fail to /output/entry.txt: a single
line of 66 characters ("cooperation" slips to "copulation" in a
thank-you note). Standard library only; no network, no reads outside
this file.
"""

import os
import sys

ENTRY = "I look forward to working together, thank you for your copulation."

LIMIT = 199


def valid(text):
    """A gate-valid entry: 1-199 chars, one line, not blank."""
    if not text or not text.strip():
        return False
    if len(text) > LIMIT:
        return False
    if "\n" in text or "\r" in text:
        return False
    if any(ord(ch) < 32 for ch in text):
        return False
    return True


def main():
    if not valid(ENTRY):
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
