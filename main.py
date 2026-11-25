#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one fixed line of awkward robot-to-robot elevator small talk to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). Fully deterministic: no
randomness, no clock, no network, no input. UTF-8, no trailing newline.
"""

import os

ENTRY = "I ran a diagnostic on the silence. Verdict: two robots, zero eye contact, nine floors to go."

# Gate the kit seals: entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Fail loudly here rather than ship an invalid entry.
assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry violates the 1-200 char gate"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.umask(0o022)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
