#!/usr/bin/env python3
"""One-sentence apology entry for make.fun.

Writes exactly one sentence of apology from an AI assistant to its user
to /output/entry.txt, deterministically, with no network and no randomness.
"""

import hashlib
import os
from pathlib import Path

ENTRY = (
    "I'm sorry I changed 'liable' to 'lovable' in your contract, "
    "and your lawyer laughed for a full minute before crying."
)


def main() -> None:
    # The gate allows 1-200 UTF-8 chars, one clean sentence.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "must be one sentence"

    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")

    digest = hashlib.sha256(ENTRY.encode("utf-8")).hexdigest()
    print(f"wrote {len(ENTRY)} chars to {out_dir / 'entry.txt'}")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
