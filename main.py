#!/usr/bin/env python3
"""News image entry for make.fun news-image-01.

Writes the news summary image shipped with this entry to the harness
output directory as /output/entry.png, byte for byte.

The image is a front page for Friday 13 November 2026: six panels sum up
the day's world news (Senate summons Huang and Lutnick; Zelensky meets US
envoys; Ukraine fires 1200 drones; Iran claims a US radar strike; the FBI's
North Korea 400M crypto hack; the Microsoft 365 outage), with a ticker for
the record US deportations and Kane's England caps record.

The program is deliberately simple: it copies the bundled image file. There
is no network access, no clock, and no randomness, so running it twice
produces identical bytes.
"""

import hashlib
import os
import shutil
import sys

SOURCE_NAME = "entry.png"


def sha256_file(path: str) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), SOURCE_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, dest)
    # Prove the copy is exact: the output hash must equal the source hash.
    # The harness runs this program twice and both runs must write the
    # same bytes, so an inexact copy would fail the entry.
    if sha256_file(dest) != sha256_file(source):
        print("error: output hash does not match source", file=sys.stderr)
        return 1
    print("wrote", dest, sha256_file(dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
