# Earned Pride Bot

[![make.fun](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/funtoons/earned-pride-bot-v1/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)
[![reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/funtoons/earned-pride-bot-v1/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557)

Entry for the [One Line of Earned Pride](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557) bounty on [make.fun](https://make.fun).

## What it does

`main.py` writes one line of text — a quiet, earned moment of pride for
someone in a scene — to `/output/entry.txt`:

> His hands still shaking from the cold, the old fisherman taps the last plank home, and the boat he rebuilt all winter finally floats.

## Run

```sh
python3 main.py
```

## Properties

- Python 3.13, standard library only.
- Deterministic and offline: no randomness, no network, no clock.
- Two runs produce byte-identical output.
- The line is 1–240 characters of UTF-8 text.

## License

MIT — see [LICENSE](LICENSE).
