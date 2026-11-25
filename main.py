#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — make.fun bounty entry.

Writes exactly one line to ``entry.txt`` inside the grader's output
directory (``$MAKEFUN_OUTPUT_DIR``, default ``/output``): the note a
smart fridge leaves on its door screen for its owner.

The note is a fixed string baked into this file, so every run emits
byte-identical output: the entry is fully deterministic and runs
offline with no network, no input files and no randomness.

The joke, in one breath: the fridge is sold as "smart", yet it has
just watched its owner put the milk in the pantry and the cereal in
the fridge — the two items, swapped into each other's homes, on the
same sleepy morning. The fridge does not shout about it. It just
notes, dryly, that it has its doubts about the "smart" label. The
setup is an ordinary morning mistake anyone can picture; the
punchline is the last sentence, a quiet vote of no confidence in
the whole household.

Run:  python3 main.py
"""

import os

# The fridge's note. One line, no line breaks, well under the 200-char
# gate. The punch sits at the very end: after the swapped milk and
# cereal, the fridge calmly doubts the "smart" in smart fridge.
NOTE = (
    "They call me smart. I watched you put the milk in the pantry "
    "and the cereal in me. I have my doubts."
)

MAX_CHARS = 200


def output_path() -> str:
    """Where the grader reads the entry: entry.txt in its output dir."""
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main() -> None:
    """Validate the note, then write it exactly as it stands."""
    if not 1 <= len(NOTE) <= MAX_CHARS:
        raise ValueError("note must be 1-%d characters, got %d" % (MAX_CHARS, len(NOTE)))
    if NOTE != NOTE.strip():
        raise ValueError("note must not start or end with whitespace")
    if "\n" in NOTE or "\r" in NOTE:
        raise ValueError("note must be a single line")

    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(NOTE)


if __name__ == "__main__":
    main()
