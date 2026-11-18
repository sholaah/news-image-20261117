"""news-image-20261117 entry: writes the day's front-page image.

The repository holds entry.png, a 1024x1024 front page summing up the
world news of Tuesday 17 November 2026. This program copies it to the
output location the harness asks for (/output/entry.png, or
$MAKEFUN_OUTPUT_DIR/entry.png outside the grader). No network, no
clock, no randomness: every run writes the same bytes.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def digest(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    assert digest(target) == digest(SOURCE), "copied image differs from entry.png"
    print(f"wrote {target} ({os.path.getsize(target)} bytes)")


if __name__ == "__main__":
    main()
