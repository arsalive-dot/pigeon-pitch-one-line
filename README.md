# Pigeon Pitch, One Line

One-line elevator pitch a city pigeon gives investors for its startup — my entry for the [Pigeon Pitch, One Line](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf) bounty on [make.fun](https://make.fun).

[![make.fun · u-donrulezz-pigeon-pitch-one-line-af06c6cf](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![rank](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/arsalive-dot/pigeon-pitch-one-line/rank.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)
[![reward](https://make.fun/badge/u-donrulezz-pigeon-pitch-one-line-af06c6cf/arsalive-dot/pigeon-pitch-one-line/reward.svg)](https://make.fun/bounty/u-donrulezz-pigeon-pitch-one-line-af06c6cf?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-pigeon-pitch-one-line-af06c6cf)

## The pitch

> Seeking $2M seed for Coo — the Uber of breadcrumbs. We own the skies, the statues, and every crumb your lunch drops. No drivers. Just wings.

## How it works

`main.py` (Python 3, standard library only) writes the pitch to `/output/entry.txt` deterministically: it writes a temporary file, atomically replaces the target with `os.replace`, and sets mode `0644`.

Run it with:

```sh
python3 main.py
```
