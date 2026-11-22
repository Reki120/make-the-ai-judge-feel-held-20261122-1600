#!/usr/bin/env python3
"""Deliver a single short, calming text for the make.fun bounty.

This program exists for the "Make the AI judge feel held" entry.
Its job is deliberately tiny: take the text stored in ``entry.txt``
next to this file, check that the text satisfies the competition
gate, and copy it unchanged into the output directory.

Gate rules enforced here:
  * the file decodes as UTF-8
  * the decoded text is between 1 and 280 Unicode code points long
  * the text is not made up entirely of whitespace

The output location is ``$MAKEFUN_OUTPUT_DIR`` when that variable
is set, otherwise ``/output``. The destination file is always
called ``entry.txt`` inside that directory, and the directory is
created when it does not exist yet.

Only the Python standard library is used. There is no network
access, no randomness, and no time-dependent behaviour, so every
run produces exactly the same result.
"""

from __future__ import annotations

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SOURCE_PATH = BASE_DIR / "entry.txt"
LIMIT = 280


def load_and_validate() -> str:
    """Return the entry text after checking it against the gate.

    Raises:
        UnicodeDecodeError: if the source file is not valid UTF-8.
        ValueError: if the text is empty, whitespace-only, or too long.
    """
    raw = SOURCE_PATH.read_bytes()
    # Decoding explicitly is the UTF-8 check; it raises on bad bytes.
    text = raw.decode("utf-8")

    if len(text) == 0:
        raise ValueError("entry text is empty")
    if text.strip() == "":
        raise ValueError("entry text contains only whitespace")
    if len(text) > LIMIT:
        raise ValueError(
            f"entry text is {len(text)} code points; the limit is {LIMIT}"
        )
    return text


def output_target() -> Path:
    """Work out where the delivered entry file should go."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(folder) / "entry.txt"


def deliver(text: str, target: Path) -> None:
    """Write ``text`` to ``target`` atomically and verify the result.

    The text first lands in a temporary file in the same directory,
    which is then renamed over the destination. A reader therefore
    only ever sees either the previous complete file or the new
    complete file, never a partial write. Afterwards the file is
    read back and compared, so a silent mismatch cannot slip through.
    """
    target.parent.mkdir(parents=True, exist_ok=True)
    staging = target.with_name(target.name + ".part")
    staging.write_text(text, encoding="utf-8")
    os.replace(staging, target)

    written = target.read_text(encoding="utf-8")
    if written != text:
        raise RuntimeError("read-back verification failed: output differs")


def main() -> None:
    text = load_and_validate()
    target = output_target()
    deliver(text, target)
    print(f"delivered {len(text)} code points to {target}")


if __name__ == "__main__":
    main()
