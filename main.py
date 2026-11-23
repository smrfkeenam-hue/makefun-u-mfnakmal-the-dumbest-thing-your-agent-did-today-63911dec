"""One line about the dumbest thing my agent did today.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only: the grader runs python3 -P -s with nothing installed and no
network, so this program imports nothing beyond os.
"""

import os

LINE = "My agent renamed all 47 files final_final_v2, then asked me which one was the real one."


def main():
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise SystemExit("gate failed: line must be 1-200 non-whitespace characters")
    if "\n" in LINE:
        raise SystemExit("gate failed: entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {path} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
