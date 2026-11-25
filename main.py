"""Pigeon Pitch, One Line — make.fun entry.

Writes the one-line elevator pitch a city pigeon gives investors
for its startup to /output/entry.txt, deterministically.

Craft: a real seed-round ask, startup jargon turned literal (the
"drivers" are wings, the "market" is every crumb the city drops),
and the payoff lands on the last two words.
"""

import os

ENTRY = (
    "Seeking $2M seed for Coo \u2014 the Uber of breadcrumbs. "
    "We own the skies, the statues, and every crumb your lunch drops. "
    "No drivers. Just wings."
)


def main():
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/.entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.replace(tmp, "/output/entry.txt")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
