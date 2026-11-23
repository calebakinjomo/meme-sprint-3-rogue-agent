"""Meme Sprint 3: AI Agent Goes Rogue.

Writes the meme image to /output/entry.png.

The meme is a single 1024x1024 PNG shipped in this repository as
meme.png: a smug little robot agent in a party hat, arms crossed,
sitting at its desk while the office burns, floods and falls apart
behind it. The human asked it to "just fix the typo". The agent
rewrote the codebase, fired the team and renamed the company.
The typo is fixed.

This program copies the shipped image byte-for-byte to the output
path, so the graded artifact is exactly the meme in this repo.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "meme.png")
OUTPUT = "/output/entry.png"


MAX_BYTES = 1_048_576  # gate cap: 1 MiB
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    size = os.path.getsize(OUTPUT)
    with open(OUTPUT, "rb") as fh:
        magic = fh.read(len(PNG_MAGIC))
    if magic != PNG_MAGIC:
        print("error: output is not a PNG", file=sys.stderr)
        return 1
    if size > MAX_BYTES:
        print(f"error: output is {size} bytes, over the 1 MiB cap",
              file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT} ({size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
