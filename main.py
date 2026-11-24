"""news-image-20261124: write the pre-rendered front page to /output/entry.png.

The image is THE WORLD TODAY, a one-page newspaper summing up Tuesday
24 November 2026 (35 stories, 7 regions). It is rendered locally and
committed as entry.png; this program only copies it to the output dir,
using the standard library only.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if os.path.getsize(dst) != os.path.getsize(src):
        raise SystemExit("copy incomplete: size mismatch")
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    main()
