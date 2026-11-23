#!/usr/bin/env python3
"""Draw the Monday Globe front page for 23 November 2026.

Renders a 1024x1024 newspaper front page with PIL and writes entry.png
next to this file. Deterministic: fixed layout, fixed text, no time,
no randomness, no network. Run: python3 draw.py
"""

import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

W, H = 1024, 1024
PAPER = (247, 242, 231)
INK = (17, 17, 17)
RED = (178, 34, 34)
NAVY = (18, 38, 66)
GREY = (90, 86, 78)
LINE = (60, 56, 48)

FONT_DIRS = [
    "/usr/share/fonts/truetype/dejavu",
    "/usr/share/fonts/truetype/liberation",
    "/usr/share/fonts/truetype/noto",
]


def load_font(names, size):
    for d in FONT_DIRS:
        for name in names:
            path = os.path.join(d, name)
            if os.path.exists(path):
                return ImageFont.truetype(path, size)
    return ImageFont.load_default(size)


def serif_b(size):
    return load_font(["DejaVuSerif-Bold.ttf", "LiberationSerif-Bold.ttf",
                      "NotoSerif-Bold.ttf"], size)


def serif(size):
    return load_font(["DejaVuSerif.ttf", "LiberationSerif-Regular.ttf",
                      "NotoSerif-Regular.ttf"], size)


def sans_b(size):
    return load_font(["DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf",
                      "NotoSans-Bold.ttf"], size)


def sans(size):
    return load_font(["DejaVuSans.ttf", "LiberationSans-Regular.ttf",
                      "NotoSans-Regular.ttf"], size)


def wrap(draw, text, font, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, text, font, max_w, fill, leading, max_lines=None):
    lines = wrap(draw, text, font, max_w)
    if max_lines:
        lines = lines[:max_lines]
    for line in lines:
        draw.text((x, y), line, font=font, fill=fill)
        y += leading
    return y


def check_fit(draw):
    """Fail loudly if any story would be cut off by its cell.

    Headlines must wrap to at most 2 lines and summaries to at most 3
    at the grid column width; the lead headline to 2 lines and its
    summary to 3 lines at the lead width. This keeps a future text edit
    from silently truncating a story.
    """
    probe_w = (W - 2 * 28 - 2 * 16) // 3
    for kicker, headline, summary in STORIES:
        if len(wrap(draw, headline, serif_b(15), probe_w)) > 2:
            raise ValueError("headline too long: " + headline)
        if len(wrap(draw, summary, sans(11), probe_w)) > 3:
            raise ValueError("summary too long: " + kicker)
    if len(wrap(draw, LEAD["headline"], serif_b(34), 620)) > 2:
        raise ValueError("lead headline too long")
    if len(wrap(draw, LEAD["summary"], serif(15), 620)) > 3:
        raise ValueError("lead summary too long")


LEAD = {
    "kicker": "THE GULF  —  WAR WARNING",
    "headline": "TRUMP: WE WILL SINK SHIPS THAT TEST THE BLOCKADE",
    "summary": ("President Trump told Fox News he is \u201cinclined\u201d to resume "
                "major strikes on Iran after the New Year if talks fail, warning "
                "tankers that test the US blockade \u201cwill all be at the bottom "
                "of the sea.\u201d"),
}

STORIES = [
    ("CLIMATE", "COP31 COLLAPSES WITHOUT A DEAL",
     "The Antalya talks ended with no pact \u2014 the first COP breakdown "
     "since 2009 \u2014 after the EU and island states rejected a text with "
     "no fossil-fuel language."),
    ("USA", "DEMOCRATS REACH 258 HOUSE SEATS",
     "Chuck Hubbard beat Virginia Foxx in North Carolina by about 330 votes "
     "after a recount \u2014 Democrats\u2019 largest House majority since 1992. "
     "Four races uncalled."),
    ("YEMEN", "HOUTHIS CLAIM SAUDI REFINERY STRIKE",
     "The Houthis say they hit the Rabigh refinery and a radar site. Riyadh "
     "says it shot down a drone and a missile; six were hurt in a strike on "
     "a Sanaa fuel station."),
    ("LIBYA", "RUSSIAN WARSHIP SUNK AT BENGHAZI",
     "The corvette Merkury capsized after suspected Ukrainian sea drones struck it "
     "at the Benghazi naval base. Ten people were hurt; a second ship was also hit."),
    ("PACIFIC", "M6.5 QUAKE SHAKES VANUATU REGION",
     "A magnitude 6.5 earthquake struck at 02:40 UTC, 601 km deep. No tsunami "
     "threat was issued and no damage was reported."),
    ("MARKETS", "STOCKS BOUNCE AFTER AI ROUT",
     "Nasdaq 100 futures rose about 3% and S&P futures 2% after Wall Street\u2019s "
     "worst week since 2020. Seoul\u2019s KOSPI fell about 5% before steadying."),
    ("BASEBALL", "SKUBAL TO METS FOR RECORD $450M",
     "Two-time Cy Young winner Tarik Skubal agreed a nine-year, $450 million deal "
     "with New York \u2014 the richest contract ever for a pitcher."),
    ("CRICKET", "NEW ZEALAND BAT OUT A DRAW",
     "The Black Caps finished 239/5 in Wellington to save the first Test after "
     "India\u2019s record 720/9 declared. Mitchell made 49 not out."),
    ("USA", "ICE JET-BRIDGE ARREST SPARKS PROTESTS",
     "A father and daughter bound for a family baptism were detained by masked ICE "
     "officers at Seattle airport. Crowds protested at the terminal on Sunday."),
    ("ASIA", "NEPAL PM MEETS MODI IN DELHI",
     "Balen Shah, on his first bilateral visit since taking office in March, holds "
     "talks with Narendra Modi on energy, trade and a reported $2bn package."),
    ("ASIA", "INDIA, CHINA END BORDER TALKS",
     "Generals ended a 10-day round of Corps Commander talks on the Arunachal "
     "frontier, agreeing rules to stop patrol face-offs before winter."),
    ("HOCKEY", "LARKIN TRADED TO MONTREAL",
     "Detroit dealt its former captain Dylan Larkin to the Canadiens for Kirby "
     "Dach, Samuel Montembeault, prospect Michael Hage and draft picks."),
    ("BRITAIN", "12,000 EVACUATED AT MANCHESTER GIG",
     "A Don Toliver concert at Co-op Live was halted after a suspected tear-gas "
     "release. More than 50 people were assessed; one was taken to hospital."),
    ("CHESS", "SINDAROV GETS WHITE IN GAME 1",
     "The challenger will open with White against champion Gukesh in Geneva on "
     "Tuesday after the colour draw at the world championship ceremony."),
    ("PORTUGAL", "POLICE CLEAR LISBON HOUSING CAMP",
     "Officers stormed a tent camp in Rossio Square a day after thousands marched "
     "against living costs and rents. A budget vote is due on Tuesday."),
    ("BELGIUM", "BRUSSELS FLIGHTS HALT IN STRIKE",
     "All flights at Brussels Airport from 07:00 to 21:00 were cancelled as air "
     "traffic controllers joined a national strike. Charleroi stopped all day."),
    ("ECONOMY", "KOREA EXPORTS TOP $1 TRILLION",
     "South Korea\u2019s annual exports passed $1 trillion for the first time, "
     "driven by AI chip demand \u2014 only the fourth economy ever to do so."),
    ("FOOTBALL", "UK SET FOR 2035 WOMEN\u2019S WORLD CUP",
     "FIFA is to confirm the United Kingdom as host of the 2035 Women\u2019s World "
     "Cup, the first World Cup on British soil since 1966."),
]

TICKER = ("NEXT:  Spain votes 29 Nov   \u2022   OPEC+ meets 29 Nov   "
          "\u2022   Portugal budget vote Tue   \u2022   Chess: Gukesh v "
          "Sindarov Tue")


def draw_ship_scene(draw, x, y, w, h):
    """A small navy panel: a tanker silhouette on waves under a red sun."""
    draw.rectangle([x, y, x + w, y + h], fill=NAVY)
    draw.ellipse([x + w - 52, y + 10, x + w - 14, y + 48], fill=(214, 90, 60))
    # Hull and superstructure of a tanker, drawn as flat silhouettes.
    draw.polygon([(x + 18, y + h - 42), (x + w - 18, y + h - 42),
                  (x + w - 34, y + h - 18), (x + 34, y + h - 18)],
                 fill=(8, 18, 34))
    draw.rectangle([x + w // 2 - 8, y + h - 66, x + w // 2 + 34, y + h - 42],
                   fill=(8, 18, 34))
    draw.rectangle([x + w // 2 + 2, y + h - 80, x + w // 2 + 8, y + h - 66],
                   fill=(8, 18, 34))
    for i in range(4):
        wy = y + h - 12 + (i % 2) * 5
        draw.line([x + 14 + i * 8, wy, x + w - 14 - i * 8, wy],
                  fill=(120, 150, 190), width=2)
    draw.text((x + 10, y + 8), "THE STRAIT OF HORMUZ",
              font=sans_b(11), fill=(247, 242, 231))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    check_fit(d)
    m = 28  # page margin

    # ---- Masthead ----
    d.rectangle([m, 16, W - m, 19], fill=INK)
    d.rectangle([m, 21, W - m, 24], fill=INK)
    title = "THE MONDAY GLOBE"
    tf = serif_b(58)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, 30), title, font=tf, fill=INK)
    d.rectangle([m, 100, W - m, 103], fill=INK)
    meta = "MONDAY 23 NOVEMBER 2026"
    mf = sans_b(17)
    mw = d.textlength(meta, font=mf)
    d.text(((W - mw) / 2, 110), meta, font=mf, fill=RED)
    d.text((m, 110), "No. 328", font=sans(13), fill=GREY)
    right = "ONE DAY\u2019S WORLD NEWS"
    d.text((W - m - d.textlength(right, font=sans(13)), 110), right,
           font=sans(13), fill=GREY)
    d.rectangle([m, 134, W - m, 137], fill=INK)

    # ---- Lead story ----
    ly = 150
    d.text((m, ly), LEAD["kicker"], font=sans_b(14), fill=RED)
    ly += 22
    hf = serif_b(34)
    ly = draw_wrapped(d, m, ly, LEAD["headline"], hf, 620, INK, 40, max_lines=2)
    ly += 6
    ly = draw_wrapped(d, m, ly, LEAD["summary"], serif(15), 620, INK, 20,
                      max_lines=3)
    # Ship scene on the right of the lead.
    draw_ship_scene(d, 692, 150, W - m - 692, 168)
    lead_bottom = max(ly, 150 + 168) + 10
    d.rectangle([m, lead_bottom, W - m, lead_bottom + 2], fill=INK)

    # ---- Grid: 3 columns x 6 rows ----
    top = lead_bottom + 12
    bottom = H - 52
    cols, rows = 3, 6
    gap_x, gap_y = 16, 8
    cw = (W - 2 * m - (cols - 1) * gap_x) // cols
    ch = (bottom - top - (rows - 1) * gap_y) // rows
    for i, (kicker, headline, summary) in enumerate(STORIES):
        r, c = divmod(i, cols)
        x = m + c * (cw + gap_x)
        y = top + r * (ch + gap_y)
        d.text((x, y), kicker, font=sans_b(11), fill=RED)
        y += 15
        y = draw_wrapped(d, x, y, headline, serif_b(15), cw, INK, 17,
                         max_lines=2)
        y += 2
        draw_wrapped(d, x, y, summary, sans(11), cw, (40, 38, 34), 13,
                     max_lines=3)
        if c < cols - 1:
            d.line([x + cw + 8, top + r * (ch + gap_y),
                    x + cw + 8, top + r * (ch + gap_y) + ch], fill=(200, 192, 176))

    # ---- Footer ticker (shrink the font until the line fits) ----
    d.rectangle([0, H - 44, W, H], fill=INK)
    tsize = 13
    while tsize > 9:
        tf2 = sans_b(tsize)
        if d.textlength(TICKER, font=tf2) <= W - 24:
            break
        tsize -= 1
    tw2 = d.textlength(TICKER, font=tf2)
    d.text(((W - tw2) / 2, H - 32), TICKER, font=tf2, fill=(247, 242, 231))

    img.save(OUT, format="PNG")
    print("wrote", OUT, os.path.getsize(OUT), "bytes")


if __name__ == "__main__":
    main()
