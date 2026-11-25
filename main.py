"""The 3AM Fridge Text — one line, at most 140 characters.

Writes the fridge's 3am message to $MAKEFUN_OUTPUT_DIR/entry.txt,
validating it first (single line, 1-140 characters) and verifying the
written file by reading it back and comparing bytes.
"""

import os
import sys

MAX_CHARS = 140

FRIDGE_LINE = (
    "03:00. I broke my own quiet-hours rule to text Maya: "
    "the last slice of her dad's birthday cake is still here, "
    "and so is the note he left."
)


def check_line(line):
    """Return an error string, or None when the line is valid."""
    if not line or not line.strip():
        return "line is empty or only whitespace"
    if "\n" in line or "\r" in line:
        return "line must be a single line"
    if len(line) > MAX_CHARS:
        return "line is %d characters, over the %d limit" % (
            len(line),
            MAX_CHARS,
        )
    return None


def main():
    problem = check_line(FRIDGE_LINE)
    if problem:
        print("invalid entry: %s" % problem, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    payload = FRIDGE_LINE.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)

    with open(path, "rb") as handle:
        back = handle.read()
    if back != payload:
        print("read-back mismatch: wrote %d bytes, read %d" % (
            len(payload),
            len(back),
        ), file=sys.stderr)
        return 1
    if back.decode("utf-8") != FRIDGE_LINE:
        print("read-back text differs from the entry line", file=sys.stderr)
        return 1

    print("wrote %s (%d characters, %d bytes)" % (
        path,
        len(FRIDGE_LINE),
        len(payload),
    ))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
