#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261117.

The image is pre-rendered (see README.md): this program simply copies the
bundled entry.png byte for byte to the harness output directory. It uses
only the Python standard library, needs no network, and is deterministic.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    source = HERE / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    # Guard against a truncated write: the copy must land whole.
    if target.stat().st_size != source.stat().st_size:
        raise SystemExit("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
