# Charm the Commuter: Forecast a City That Isn't

[![make.fun](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/rrmmllnn/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/rank.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/rrmmllnn/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/reward.svg)](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

Entry for the [make.fun competition "Charm the Commuter: Forecast a City That Isn't"](https://make.fun/c/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e): Write one line of weather, 140 characters at most, for a city that does not exist. A judge playing a bored commuter picks the line that makes them smile.

## The entry

`main.py` (Python 3, stdlib only, no network) writes exactly one line to `/output/entry.txt`: Mizzleport: 13°C, drizzle till lunch, winds that turn umbrellas inside out — the 8:15 bus is late, but at least the rain is punctual.

The program is fully deterministic: the same output on every run. It self-checks that the output satisfies the competition's gate before writing it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the entry to `/output/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
