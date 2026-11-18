# The World Today — 17 November 2026

[![make.fun · news-image-20261117](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![rank](https://make.fun/badge/news-image-20261117/sholaah/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)
[![reward](https://make.fun/badge/news-image-20261117/sholaah/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261117)

Entry for the make.fun bounty **"Sum up 17 November's world news in one image"**
(news-image-20261117).

`main.py` (Python 3.13, standard library only) copies `entry.png` — a
1024×1024 front page of Tuesday 17 November 2026 — to the harness output
(`/output/entry.png`, or `$MAKEFUN_OUTPUT_DIR/entry.png`) and verifies the
copy's SHA-256 against the source. It runs offline and writes identical
bytes on every run.

## What the image sums up

One editorial world map whose flashpoints are the day's top stories:

- **Ukraine's "unprecedented operation" against the Crimean Bridge** —
  Zelenskyy hailed the strike that severely damaged and closed the bridge
  linking Russia to Crimea; the burning, collapsing span at the centre.
- **Iranian drones target the U.S. radar system in Bahrain** (Sheikh Isa
  base; Bahrain said the attack was intercepted), while tankers are struck
  near Hormuz and a third U.S. carrier arrives — drones, radar dome and
  tanker at the right.
- **Trump travels to Asia** ahead of the APEC trilateral with Xi and Putin,
  and **Japan scrambles jets** after Russian aircraft violate its airspace —
  summit tower, flags and jets at upper right.
- **Wall Street's sell-off** — the Dow tumbles 849 points as tech slides
  ahead of Nvidia earnings; the red arrow and falling coins at upper left.
- **The Kava Lend exploit** — an attacker abused a lending market left
  dormant since BUSD minting stopped, borrowed 55.2M KAVA (about $3.8M)
  and halved the token's price; the hooded figure at the code screens,
  upper left.
- **Crypto's brutal week** — bitcoin stalled below $65,000, under its
  200-week average, after roughly $230B was wiped from total crypto
  value in three days and up to $2B of leveraged positions liquidated;
  the giant coin under its plunging chart at the bottom.

The base illustration was generated in-session and framed with a masthead
and headline strips by `build_image.py` (Pillow). The day's stories were
compiled from wire and front-page reports of 17 Nov 2026.

## Design

The illustration is a flat red/black/navy icon collage in the style of
*The Economist*'s "The World Ahead" covers — a circular globe of small
iconic scenes, one per story. The layout mirrors those covers too:
a small red masthead box and a large date title over the full-bleed
collage, with no headline strips.

## License

MIT — see `LICENSE`.
