"""make.fun "One Letter for Your Day" entry.

The gate: /output/entry.txt must be UTF-8 text of exactly 1 character,
not only whitespace. So this writes a single letter and nothing else --
no word, no gloss, no punctuation, no trailing newline.

The letter is H, for "hectic": a day crammed with frantic activity,
too much to do and no quiet minute in it. It is the first letter of
the word, it paints a sharp picture instead of a vague mood, and it
reads as an honest report of a real overloaded day.
"""

import os

LETTER = "H"  # hectic


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(LETTER)
    with open(path, "rb") as fh:
        written = fh.read()
    assert len(written) == 1 and 65 <= written[0] <= 90, (
        "entry must be exactly one byte: an uppercase letter A-Z"
    )


if __name__ == "__main__":
    main()
