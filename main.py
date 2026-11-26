#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun entry.

Prints one line and writes the identical line to /output/entry.txt.
Stdlib only, deterministic.
"""

import os

LINE = "I've printed your boarding pass, your divorce papers and your 2 a.m. resignation letter. I know more about your life than your therapist — and unlike her, I never run out of toner."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(LINE)


if __name__ == "__main__":
    main()
