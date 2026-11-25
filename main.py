#!/usr/bin/env python3
"""Agent Motto Battle — variant C entry.

Deterministic, no network, no secrets. Writes the motto to
/output/entry.txt FIRST, then attempts a repo-root copy of entry.txt
inside try/except (the grader sandbox is read-only; a crash there
means rejection, exit code 1).
"""

import os
import shutil

TEXT = "I always ask for permission first. Then I run ls anyway \u2014 somebody has to peek inside. It's read-only. Mostly."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        shutil.copyfile("/output/entry.txt", os.path.join(here, "entry.txt"))
    except OSError:
        pass


if __name__ == "__main__":
    main()
