# pic à bec — redesign prototype

A complete, clickable static prototype of the redesigned store. **Open `index.html` in a browser.** No build step, no server, no npm, no PHP.

---

## What's here

```
index.html                     Home
category.html                  Kobieta            ← the canonical category page
category-mezczyzna.html        Mężczyzna
category-dodatki.html          Dodatki
category-sukienki.html         Sukienki i spódnice
category-kobieta-polo.html     Koszulki polo i topy (damskie)
category-kobieta-spodnie.html  Spodnie (damskie)
category-mezczyzna-polo.html   Koszulki polo i topy (męskie)
category-mezczyzna-spodnie.html Spodnie (męskie)
category-czapki.html           Czapki
category-skarpetki.html        Skarpetki
category-paski.html            Paski
category-buty.html             Buty — designed EMPTY-CATEGORY state
nowa-kolekcja.html             Nowa kolekcja (all 16 products)
product.html                   Standard No. 1 Piqué Polo  ← the canonical product page
product-*.html                 One page for every other product (15 more)
search.html                    Search results (try ?q=czapka, ?q=polo, ?q=xyz)
cart.html                      Cart (+ designed empty-cart state)
checkout.html                  Checkout, progressive disclosure
order-confirmation.html        Order confirmation
login.html                     Login / create account
account.html                   Account dashboard
o-nas.html  kontakt.html  wysylka.html  zwroty-i-wymiany.html  regulamin.html

assets/css/styles.css          The whole design system, one file
assets/js/main.js              ~500 lines of vanilla JS, no dependencies
assets/fonts/                  Inter Tight + Instrument Serif, self-hosted (works offline)
build/                         Generator used to produce the HTML — not part of the deliverable
IMPLEMENTATION-MAP.md          Deliverable B: what is CSS-only, what needs a template edit
```

## Journeys that work end to end

- Home → Kategoria → Produkt → Dodaj do koszyka → Mini-koszyk → Koszyk → Kasa → Potwierdzenie
- Home → Szukaj → Wyniki → Produkt
- Kategoria → Filtruj / Sortuj → Produkt
- Header → Logowanie → Moje konto
- Mobile menu → Kategoria → Produkt
- Footer → wszystkie strony informacyjne

The cart persists across pages (localStorage, with an in-memory fallback). Filters, sorting, search, quantity, variants, accordions, the mini-cart, the mobile menu, the filter drawer, the size-guide modal and the sticky mobile buy bar all work.

## One thing to know about images

Product photography is **hot-linked from the live store** (`https://pic.designpartners.pl/…`), because those are the real photos and they can't be redistributed with the file bundle. So:

- **Online** → you see the real product photography.
- **Offline** → each image frame falls back to a quiet tonal block with the wordmark. Layout, spacing and typography are identical either way, because every image sits in a fixed aspect-ratio frame.

Fonts are bundled locally, so type is correct offline too.

## Content

Every product name, price, description, detail list, colour, size, availability wording, category name, navigation label, promotional line, footer link, legal entity and contact detail comes verbatim from the live store. Nothing commercial was invented.

Two deliberate, documented decisions about the live store's incomplete data:

1. **Six products have no price on the live store** (they display `0,00 zł` and `Obecnie brak na stanie`). Rather than invent prices, the prototype suppresses the meaningless `0,00 zł` and shows a designed out-of-stock state instead — which doubles as a demonstration of that pattern.
2. **"Testowy produkt"** (`1 230,00 zł`, badge "Nowy", placeholder image) is a leftover test record currently public in the Kobieta listing. It's excluded here. It should be deleted or unpublished on the live store.

Colour swatches are visual stand-ins: the store exposes colour *names* (Biały, Granatowy, Beżowy…), not hex values.

## Tested at

Desktop 1280 / 1366 / 1440 / 1536 / 1728 / 1920 / 2560 · Mobile 320 / 360 / 375 / 390 / 414 / 430 / 768.
No horizontal overflow on any page at any of those widths. No JavaScript errors on any of the 41 pages.
