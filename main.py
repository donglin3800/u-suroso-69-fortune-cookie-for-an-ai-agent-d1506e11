#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

One fortune slip, written to /output/entry.txt. The line is a single
sentence of 86 characters, inside the 140-character cap: the classic
fortune-cookie promise of a tall, dark stranger, turned on an agent
whose stranger is its own context window, already full.

Standard library only. No network, no randomness, no clock, no
environment reads: the same bytes come out on every run.
"""

from pathlib import Path

FORTUNE = "You will meet a tall, dark stranger: your own context window \u2014 and it is already full."

OUTPUT_PATH = Path("/output/entry.txt")


def fortune_text() -> str:
    """Return the fortune, checked against the bounty gate."""
    text = FORTUNE.strip()
    if not text or len(text) > 140:
        raise ValueError(f"fortune must be 1-140 characters, got {len(text)}")
    if "\n" in text:
        raise ValueError("fortune must be a single line")
    return text


def main() -> None:
    text = fortune_text()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"Wrote a {len(text)}-character fortune to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
