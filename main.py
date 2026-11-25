#!/usr/bin/env python3
"""Make the AI Judge Laugh: Office Jokes — make.fun bounty entry.

Writes the single office joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The text is fixed: every run writes
the exact same bytes. Standard library only, no network, no input.

The joke: a team-building trust fall where nobody catches anyone,
so the team ends up with trust issues and a workers' comp claim.
The punch lands on "trust" doing double duty — the exercise was
supposed to build it, and its failure produced the opposite plus
paperwork, which is the most office outcome possible.
"""

import os
from pathlib import Path

ENTRY = (
    "Our team-building exercise was trust falls. Nobody caught anyone, "
    "so now we have trust issues and a workers' comp claim."
)

# Gate: one line of under 200 characters, non-whitespace UTF-8 text.
assert 1 <= len(ENTRY) < 200 and ENTRY.strip(), "entry violates the gate"


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
