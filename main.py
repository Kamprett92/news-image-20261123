#!/usr/bin/env python3
"""Entry point for the news-image-20261123 make.fun entry.

Copies the pre-rendered front page (entry.png, drawn by draw.py) into
the output directory the harness provides. Standard library only, no
network, fully deterministic: the same input bytes always produce the
same output bytes.

Usage:
    MAKEFUN_OUTPUT_DIR=/output python3 main.py
    (defaults to /output when the variable is not set)
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    source_sum = sha256_of(SOURCE)
    shutil.copyfile(SOURCE, target)
    size = os.path.getsize(target)
    checksum = sha256_of(target)
    print("wrote {} ({} bytes, sha256 {})".format(target, size, checksum))
    if checksum != source_sum:
        print("error: copied bytes differ from entry.png", file=sys.stderr)
        return 1
    if size > 1048576:
        print("error: entry.png is over the 1 MiB limit", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
