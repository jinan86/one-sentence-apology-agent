#!/usr/bin/env python3
"""One-sentence apology agent entry.

Produces a single apology sentence and saves it to entry.txt.
No network access, no randomness, same output on every run.
"""

import os
from pathlib import Path

# The entry itself: exactly one sentence (116 chars), written verbatim
# to entry.txt with no trailing newline, so the output is byte-identical
# on every run.
SENTENCE = "I'm sorry I changed 'liable' to 'lovable' in your contract, and your lawyer laughed for a full minute before crying."


def output_path():
    directory = Path(os.environ.get("OUTPUT_DIR", "/output"))
    directory.mkdir(parents=True, exist_ok=True)
    return directory / "entry.txt"


def run():
    if not 1 <= len(SENTENCE) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not SENTENCE.endswith("."):
        raise ValueError("entry must end with a full stop")
    target = output_path()
    target.write_text(SENTENCE, encoding="utf-8")
    print(f"wrote {len(SENTENCE)} chars to {target}")


if __name__ == "__main__":
    run()
