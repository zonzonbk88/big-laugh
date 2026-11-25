"""One Line, Big Laugh — entry writer.

Writes a single funny line to entry.txt. Standard library only.
The output directory comes from MAKEFUN_OUTPUT_DIR when set,
otherwise /output. No trailing newline in the entry text.
"""

import os


ENTRY = (
    "My smartwatch called my mother before the ambulance "
    "\u2014 it knows who actually picks up."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
