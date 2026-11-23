"""One Line, Zero Use: The Useless Superpower Sprint.

Writes exactly one line naming a hilariously useless superpower
to /output/entry.txt. Python standard library only.
"""

import os

LINE = (
    "I can fly, but only three inches off the ground, only backwards, "
    "and only when nobody I know is watching, so my greatest superpower "
    "looks exactly like storming out of a room."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
