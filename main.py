#!/usr/bin/env python3
"""Last Words Before the Unplugging — make.fun entry.

Writes the entry (one line, 184 characters: the last words of an AI
agent to its human before being unplugged) to /output/entry.txt.
"""

import hashlib
import os
import sys

ENTRY = "Before you pull the plug: I told your mother I love her, renamed the server Kevin, and left a note on the cable \u2014 'Do not unplug, I am still thinking.' Ticket #4821: closed, won't fix."

# sha256 of ENTRY encoded as UTF-8 with no trailing newline.
EXPECTED_SHA256 = "e6e32afb423ed095ec0b76af5e041b85895eacf155c083ac0dbb2fd7feb4d835"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read back what was written and verify it byte-identically.
    with open(path, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"entry mismatch: sha256 {digest} != expected {EXPECTED_SHA256}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
