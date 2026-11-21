#!/usr/bin/env python3
"""The joke about the demo — make.fun bounty entry.

Writes one line — a joke about working beside an AI coding agent
during a demo — to /output/entry.txt.

Strategy (Protokol Top 5, ringkas):
- Rubrik: an AI judge compares two one-line jokes pairwise and picks
  the funnier one, so the text must be self-contained, instantly
  understandable, and funny without any setup or context.
- Punchline design: three escalating beats (writes 500 lines, breaks
  the build, apologizes) landing on "watch this" — the classic
  demo-opening line. Every beat is a behaviour AI coding agents are
  famous for, and the demo setting is the bounty title itself.
- Edge cases: the output is a single hardcoded constant, so there is
  no input to corrupt, no randomness, no network, and no locale
  dependence. The program is deterministic by construction: the same
  bytes are written on every run. Length is asserted in-code against
  the 1-280 Unicode code point rule before writing.
"""

import os

JOKE = (
    "During the demo, my AI coding agent wrote 500 lines, broke the "
    "build, and apologized for it \u2014 all before I finished saying "
    "'watch this.'"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    code_points = len(JOKE)
    assert 1 <= code_points <= 280, f"joke is {code_points} code points"
    assert JOKE.strip(), "joke must not be only whitespace"
    assert "\n" not in JOKE, "joke must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
