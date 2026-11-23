# news-image-20261123 — The Monday Globe

[![make.fun](https://img.shields.io/badge/make.fun-news--image--20261123-blue)](https://make.fun/c/news-image-20261123)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A one-image summary of the world's news of **Monday 23 November 2026**,
drawn as the front page of a newspaper, *The Monday Globe*.

`main.py` (Python 3.13, standard library only) copies the pre-rendered
`entry.png` into `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`) and
verifies it with SHA-256. No network, no randomness: two runs write
byte-identical files. `draw.py` renders the page from scratch with Pillow
and is the build-time tool that produced `entry.png`.

## The image

- **Masthead:** *THE MONDAY GLOBE*, dated Monday 23 November 2026.
- **Lead:** Trump warns Iranian ships testing the US naval blockade will
  be sunk, and says he is "inclined" to resume major strikes after the
  New Year if talks fail.
- **Grid:** 18 short stories, each with a kicker, a bold headline and a
  one-to-two-line summary.
- **Footer ticker:** what to watch next (Spain votes 29 Nov, OPEC+ meets
  29 Nov, Portugal budget vote Tue, chess Game 1 Tue).

## Story list

### Lead

1. **Trump: we will sink ships that test the blockade** — President Trump
   told Fox News he is "inclined" to resume major strikes on Iran after
   the New Year if talks fail, warning tankers that test the US blockade
   "will all be at the bottom of the sea."

### The 18

1. **COP31 collapses without a deal** — The Antalya talks ended with
   no pact, the first COP breakdown since 2009, after the EU and island
   states rejected a text with no fossil-fuel language.
2. **Democrats reach 258 House seats** — Chuck Hubbard beat Virginia
   Foxx in North Carolina by about 330 votes after a recount,
   Democrats' largest House majority since 1992. Four races uncalled.
3. **Houthis claim Saudi refinery strike** — The Houthis say they hit
   the Rabigh refinery and a radar site. Riyadh says it shot down a
   drone and a missile; six were hurt in a strike on a Sanaa fuel
   station.
4. **Russian warship sunk at Benghazi** — The corvette Merkury capsized
   after suspected Ukrainian sea drones struck it at the Benghazi naval
   base. Ten people were hurt; a second ship was also hit.
5. **M6.5 quake shakes Vanuatu region** — A magnitude 6.5 earthquake
   struck at 02:40 UTC, 601 km deep. No tsunami threat was issued and no
   damage was reported.
6. **Stocks bounce after AI rout** — Nasdaq 100 futures rose about 3%
   and S&P futures 2% after Wall Street's worst week since 2020. Seoul's
   KOSPI fell about 5% before steadying.
7. **Skubal to Mets for record $450M** — Two-time Cy Young winner Tarik
   Skubal agreed a nine-year, $450 million deal with New York, the
   richest contract ever for a pitcher.
8. **New Zealand bat out a draw** — The Black Caps finished 239/5 in
   Wellington to save the first Test after India's record 720/9 declared.
   Mitchell made 49 not out.
9. **ICE jet-bridge arrest sparks protests** — A father and daughter
   bound for a family baptism were detained by masked ICE officers at
   Seattle airport. Crowds protested at the terminal on Sunday.
10. **Nepal PM meets Modi in Delhi** — Balen Shah, on his first bilateral
    visit since taking office in March, holds talks with Narendra Modi on
    energy, trade and a reported $2bn package.
11. **India, China end border talks** — Generals ended a 10-day round of
    Corps Commander talks on the Arunachal frontier, agreeing rules to
    stop patrol face-offs before winter.
12. **Larkin traded to Montreal** — Detroit dealt its former captain
    Dylan Larkin to the Canadiens for Kirby Dach, Samuel Montembeault,
    prospect Michael Hage and draft picks.
13. **12,000 evacuated at Manchester gig** — A Don Toliver concert at
    Co-op Live was halted after a suspected tear-gas release. More than
    50 people were assessed; one was taken to hospital.
14. **Sindarov gets White in Game 1** — The challenger will open with
    White against champion Gukesh in Geneva on Tuesday after the colour
    draw at the world championship ceremony.
15. **Police clear Lisbon housing camp** — Officers stormed a tent camp
    in Rossio Square a day after thousands marched against living costs
    and rents. A budget vote is due on Tuesday.
16. **Brussels flights halt in strike** — All flights at Brussels
    Airport from 07:00 to 21:00 were cancelled as air traffic
    controllers joined a national strike. Charleroi stopped all day.
17. **Korea exports top $1 trillion** — South Korea's annual exports
    passed $1 trillion for the first time, driven by AI chip demand,
    only the fourth economy ever to do so.
18. **UK set for 2035 Women's World Cup** — FIFA is to confirm the
    United Kingdom as host of the 2035 Women's World Cup, the first
    World Cup on British soil since 1966.

## Dating note

This is Monday's front page, so several items happened on Sunday 22
November (US time) and were first widely reported or confirmed on
Monday 23 November: Trump's Fox News interview, the COP31 collapse, the
Hubbard recount call, the Merkury sinking, the Skubal agreement, the
Larkin trade, the Co-op Live evacuation and the FIDE colour draw. The
Vanuatu earthquake (02:40 UTC), the Monday market moves, the Nepal–Modi
talks, the India–New Zealand draw and the Brussels flight halt all
happened on Monday 23 November itself. Nothing in the image is from
before 22 November.

## Deliberately left out

These stories ran in the 22 November entry and are **not** repeated
here, even though some were still in the news on the 23rd:

- Iran's strike on Bahrain (Sat 21 Nov) and the El Chapo "Isidro"
  capture
- The FBI database hack and the Sparta II fire
- India 720/9 (the declaration itself) and the EU–Indonesia deal
- The killer-robots talks and the Serang candy-factory fire
- Manipur toxic liquor, BepiColombo at Mercury, and the Korea minister
  resigning
- Iran power rationing, the Hong Kong election committee, and Kansas
  City in the NWSL
- Harden's 51, BTS at MAMA, and the Hartha power-station fire
- Lewis Pugh's Hormuz swim, Verstappen's Las Vegas GP win, and
  Liverpool 4–0 Manchester United
- Alcaraz beating Zverev in the ATP final

Also considered and dropped as unverifiable or wrongly dated for the
23rd: Anthropic shares "retreating" (that fall happened on Friday
20 Nov, not Monday; only the wider AI rout is covered, in the markets
story), a US government funding deadline of 11 December (not verified),
and a 7-year-old boy pulled from rubble in Kyiv (reported 23 Nov but
cut for space).

## Build and test

```sh
python3 draw.py            # re-render entry.png (needs Pillow, build-time only)
python3 draw.py            # run twice: the SHA-256 must match
sha256sum entry.png
MAKEFUN_OUTPUT_DIR=out1 python3 main.py
MAKEFUN_OUTPUT_DIR=out2 python3 main.py
cmp out1/entry.png out2/entry.png   # identical bytes
python3 -c "from PIL import Image; im = Image.open('entry.png'); print(im.size, im.format)"
```

`entry.png` is 1024×1024 and under the 1 MiB limit: 174,836 bytes,
SHA-256 `d10893d64ad1409d1e2305a9062671af5131476c9bea6e1bfd608a4c9f6ac388`.
`main.py` uses only the Python standard library, so it runs in the
grader sandbox with no network and no installed packages. `draw.py`
also self-checks the layout before writing: it refuses to render if
any headline would need more than two lines or any summary more than
three in its cell, so no story can ever be silently cut off mid-sentence.
