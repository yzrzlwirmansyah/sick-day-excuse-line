"""The Funniest Sick-Day Excuse entry.

A worker calls in sick because a sneeze while putting on a sock threw
their back out, and the one-sock detail proves the story is still live.
"""

from __future__ import annotations

import os
from pathlib import Path

ENTRY = "I sneezed putting on a sock and threw my back out. Still wearing one sock, for context."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
