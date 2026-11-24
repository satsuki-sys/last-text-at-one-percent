#!/usr/bin/env python3
"""Last Text at One Percent — writes the dying phone's final text to /output/entry.txt."""

import os

ENTRY = "1%. tell mom i love her. you spent my last 47 minutes watching a man pressure-wash a driveway. i was going to be somebody. i was going to\u2014"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
