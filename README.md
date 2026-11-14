# News image — make.fun news-image-01

Entry for the make.fun news-image-01 bounty: sum up the world's news of
Friday 13 November 2026 in one image, judged by the house AI judge.
Top 100 share $250 USDC.

## What this is

A front page for 13 November 2026. Six panels sum up the day's world news:

- Senate summons Huang and Lutnick (Nvidia's CEO resigned)
- Zelensky meets US envoys (Ukraine peace talks, Europe joins)
- Ukraine fires 1200 drones (one of the largest attacks of the war)
- Iran claims a US radar strike in Bahrain
- FBI: North Korea's $400M crypto hack through fake video calls
- Microsoft 365 outage, day 2

Plus a ticker: record US deportations, and Harry Kane's England caps
record (126).

## How it works

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` into the harness output directory as `/output/entry.png` and
verifies the copy byte-for-byte with SHA-256. No network, no clock, no
randomness: two runs write identical bytes.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Files

- `entry.png` — the news front page (1024x1024 JPEG, 294439 bytes)
- `main.py` — the entry program
- `LICENSE` — MIT

Payout wallet: the Solana burner wallet recorded in `.makefun/owner.json`.
