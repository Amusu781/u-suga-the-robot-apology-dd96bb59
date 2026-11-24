#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes the robot's two-line confession to /output/entry.txt:
line 1 apologises for one specific mistake, line 2 says what it
learned and what it will do differently.
"""

import os

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

LINE_1 = "I'm sorry I folded your passport into the laundry and only noticed when the wash cycle finished."
LINE_2 = "I've learned to empty every pocket before I load the drum, so from now on I check each pocket twice, even the ones I think I already checked."


def clear_output_contents() -> None:
    """Remove stale files inside /output, never the directory itself."""
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        try:
            if os.path.isfile(path):
                os.unlink(path)
        except OSError:
            pass


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    clear_output_contents()
    text = LINE_1 + "\n" + LINE_2 + "\n"
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
