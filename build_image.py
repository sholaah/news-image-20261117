"""Build entry.png for make.fun news-image-20261117.

The base illustration (assets/) was generated in-session as an editorial
world-map scene of 17 November 2026's top stories:
  - Ukraine's "unprecedented operation" severely damages the Crimean
    Bridge; Zelenskyy hails it, the bridge closes, Kyiv's bridges are hit
    in reply (the burning bridge at the centre)
  - Iran fires drones at the US radar system in Bahrain (Sheikh Isa base);
    tankers are struck near Hormuz as a third US carrier arrives
    (drones, radar dome and tanker at the right)
  - Trump travels to Asia ahead of the APEC trilateral with Xi and Putin;
    Japan scrambles jets after Russian aircraft violate its airspace
    (summit tower, flags and jets at upper right)
  - Wall Street's sell-off: the Dow tumbles 849 points as tech slides
    ahead of Nvidia earnings (red arrow and falling coins at upper left)
  - Five European governments unveil a joint Rwanda return hub for
    rejected asylum seekers (the jet over the savanna at the bottom)
This script frames it as a front page: masthead on top, headline strips
below, and exports a PNG of at most 1024x1024 and 1 MiB.
"""
from PIL import Image, ImageDraw, ImageFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "media-generation-world-17nov-0-ae187168-52f6-4571-a63f-4520914efa8b.png")
OUT = os.path.join(HERE, "entry.png")
FONT_DIR = "/usr/share/fonts/truetype/dejavu"
NAVY = (9, 24, 43)
GOLD = (242, 193, 78)
WHITE = (245, 247, 250)

W, H = 1024, 1024
TOP_H, BOT_H = 98, 146


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def centered(draw, y, text, fnt, fill):
    box = draw.textbbox((0, 0), text, font=fnt)
    draw.text(((W - (box[2] - box[0])) // 2, y), text, font=fnt, fill=fill)


def main():
    art = Image.open(SRC).convert("RGB")
    art = art.resize((W, H - TOP_H - BOT_H), Image.LANCZOS)
    page = Image.new("RGB", (W, H), NAVY)
    page.paste(art, (0, TOP_H))
    draw = ImageDraw.Draw(page)

    centered(draw, 12, "THE WORLD TODAY", font("DejaVuSans-Bold.ttf", 46), WHITE)
    centered(draw, 66, "TUESDAY · 17 NOVEMBER 2026", font("DejaVuSans-Bold.ttf", 22), GOLD)

    headlines = [
        ((231, 76, 60), "UKRAINE'S 'UNPRECEDENTED' STRIKE CRIPPLES CRIMEAN BRIDGE"),
        ((230, 126, 34), "IRANIAN DRONES TARGET U.S. RADAR IN BAHRAIN"),
        ((242, 193, 78), "TRUMP IN ASIA: XI & PUTIN TRILATERAL AHEAD AT APEC"),
        ((93, 173, 226), "DOW TUMBLES 849 POINTS AS TECH SELLS OFF"),
    ]
    fnt = font("DejaVuSans-Bold.ttf", 24)
    y = H - BOT_H + 10
    for color, text in headlines:
        draw.rectangle([28, y + 4, 44, y + 20], fill=color)
        draw.text((58, y), text, font=fnt, fill=WHITE)
        y += 34

    page.save(OUT, optimize=True)
    if os.path.getsize(OUT) > 1024 * 1024:
        page.quantize(colors=256, method=Image.MEDIANCUT).save(OUT, optimize=True)
    print("entry.png:", page.size, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
