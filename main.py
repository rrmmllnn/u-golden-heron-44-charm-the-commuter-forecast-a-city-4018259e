#!/usr/bin/env python3
"""A single-line forecast for a fictional drizzly town, for riders at the stop.

It names the invented place, reports genuine weather, and ends with
a wry turn on the timetable, all inside the 140-character ceiling.
"""
import os

DEGREE = chr(176)
EMDASH = chr(8212)
_bits = [
    "Mizzleport: 13",
    DEGREE,
    "C, drizzle till lunch, winds that turn umbrellas inside out ",
    EMDASH,
    " the 8:15 bus is late, but at least the rain is punctual.",
]
LINE = "".join(_bits)


def check_line(candidate):
    # One line only, inside the cap, naming the town and the late bus.
    assert "\n" not in candidate and 1 <= len(candidate) <= 140
    assert candidate.startswith("Mizzleport") and "bus" in candidate
    assert "13" in candidate and "rain" in candidate
    return candidate


def main():
    forecast = check_line(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as dest:
        dest.write(forecast)


if __name__ == "__main__":
    main()
