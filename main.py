#!/usr/bin/env python3
"""One Line of Earned Pride — writes one quiet, earned moment to /output/entry.txt.

Stdlib only, deterministic, offline. No randomness, no clock, no network.
The same bytes are written on every run.
"""

from pathlib import Path

LINE = (
    "His hands still shaking from the cold, the old fisherman taps "
    "the last plank home, and the boat he rebuilt all winter finally floats."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
