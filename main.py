#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes exactly one sentence explaining the modern internet to a time
traveler from 1800, using only things a person of that year already
knows: a road, letters, books, newspapers, a door.

Standard library only. No network. Deterministic: byte-identical
output every run — UTF-8 encoding, LF newlines, no trailing newline.
"""

import os

def build_sentence() -> str:
    """Return the single sentence explaining the modern internet."""
    return (
        "Picture one road that brings every letter, book, and newspaper "
        "on earth to your door in a blink, and lets you answer back."
    )


def validate_sentence(text: str) -> None:
    """Check the sentence is non-empty and within the 1-200 char gate."""
    assert text.strip(), "sentence must not be only whitespace"
    assert 1 <= len(text) <= 200, (
        f"sentence must be 1-200 characters, got {len(text)}"
    )


def main() -> None:
    output_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)

    text = build_sentence()
    validate_sentence(text)

    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
