# -*- coding: utf-8 -*-
"""Static site generator for the pic à bec redesign prototype.

Emits plain .html files — no runtime dependency of any kind. Run:
    python3 build/build.py
"""
import os, re, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import P, CATS, COLOR_HEX, BASE, in_cat, BY_KEY

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSSDIR = os.path.join(ROOT, "build", "css")

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def img(pid, slug, kind="large_default"):
    return "%s/%s-%s/%s.jpg" % (BASE, pid, kind, slug)

def cover(p, kind="large_default"):
    return img(p["gallery"][0], p["slug"], kind)

def alt_img(p, kind="large_default"):
    g = p["gallery"]
    return img(g[1] if len(g) > 1 else g[0], p["slug"], kind)

def price_str(v):
    s = "%.2f" % v
    ip, dp = s.split(".")
    ip = re.sub(r"(?<=\d)(?=(\d{3})+$)", " ", ip)
    return "%s,%s zł" % (ip, dp)

def plural(n):
    if n == 1: return "produkt"
    if n % 10 in (2, 3, 4) and not (12 <= n % 100 <= 14): return "produkty"
    return "produktów"

# ---------------------------------------------------------------------------
# icons
# ---------------------------------------------------------------------------
ICON = {
 "search": '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><circle cx="9" cy="9" r="6"/><path d="M13.5 13.5 18 18"/></svg>',
 "user":   '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><circle cx="10" cy="6.6" r="3.4"/><path d="M3.6 17.4c.7-3.5 3.3-5.4 6.4-5.4s5.7 1.9 6.4 5.4"/></svg>',
 "bag":    '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><path d="M4.4 6.3h11.2l.9 11.1H3.5z"/><path d="M7.3 8.4V5.6a2.7 2.7 0 0 1 5.4 0v2.8"/></svg>',
 "heart":  '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><path d="M10 16.5S3.4 12.6 3.4 8.2a3.4 3.4 0 0 1 6.6-1.2 3.4 3.4 0 0 1 6.6 1.2c0 4.4-6.6 8.3-6.6 8.3z"/></svg>',
 "close":  '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><path d="M5 5l10 10M15 5L5 15"/></svg>',
 "arrow":  '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><path d="M3.5 10h13M11.5 5l5 5-5 5"/></svg>',
 "arrowl": '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><path d="M16.5 10h-13M8.5 5l-5 5 5 5"/></svg>',
 "arrowup":'<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><path d="M10 16.5v-13M5 8.5l5-5 5 5"/></svg>',
 "filter": '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><path d="M2.5 5.5h15M5 10h10M8 14.5h4"/></svg>',
 "truck":  '<svg viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><path d="M2 6.5h13v10H2z"/><path d="M15 9.5h4.5l3 3.5v3.5H15z"/><circle cx="7" cy="19" r="2.2"/><circle cx="18.5" cy="19" r="2.2"/></svg>',
 "shield": '<svg viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><path d="M13 2.5l8.5 3.2v6.4c0 5.2-3.5 9.3-8.5 11.4-5-2.1-8.5-6.2-8.5-11.4V5.7z"/><path d="M9.4 12.8l2.6 2.6 4.8-5.2"/></svg>',
 "return": '<svg viewBox="0 0 26 26" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><path d="M4 13a9 9 0 1 1 2.8 6.5"/><path d="M4 8.4V13h4.6"/></svg>',
 "check":  '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><path d="M4 10.5l4 4 8-9"/></svg>',
 "lock":   '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><rect x="4" y="8.5" width="12" height="8.5"/><path d="M7 8.5V6a3 3 0 0 1 6 0v2.5"/></svg>',
 "ig":     '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><rect x="3" y="3" width="14" height="14" rx="4"/><circle cx="10" cy="10" r="3.4"/><circle cx="14.2" cy="5.9" r=".9" fill="currentColor" stroke="none"/></svg>',
 "fb":     '<svg viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.25" aria-hidden="true"><rect x="3" y="3" width="14" height="14" rx="4"/><path d="M12.6 6.6h-1.1c-.9 0-1.6.7-1.6 1.6v1.4m-1.9 0h3.8m-1.9 0V17"/></svg>',
 "grid":   '<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1" aria-hidden="true"><rect x="4" y="4" width="14" height="14"/><rect x="22" y="4" width="14" height="14"/><rect x="4" y="22" width="14" height="14"/><rect x="22" y="22" width="14" height="14"/></svg>',
}

# ---------------------------------------------------------------------------
# shared copy (verbatim from the live store)
# ---------------------------------------------------------------------------
BENEFITS = [
 ("truck",  "Darmowa wysyłka", "Przy zamówieniach powyżej 125 USD dostawa na terenie całego kraju jest bezpłatna"),
 ("shield", "Świetna jakość",  "30-dniowa 100% gwarancja satysfakcji i najlepszej jakości oraz materiałów."),
 ("return", "Wymiana i zwroty","Bezpłatne zwroty i wymiany za pośrednictwem poczty lub poprzez dostarczenie kodu QR"),
]

NAV = [
 ("Kobieta", "category.html", [
    ("Sukienki i spódnice", "category-sukienki.html"),
    ("Koszulki polo i topy", "category-kobieta-polo.html"),
    ("Spodnie", "category-kobieta-spodnie.html")]),
 ("Mężczyzna", "category-mezczyzna.html", [
    ("Koszulki polo i topy", "category-mezczyzna-polo.html"),
    ("Spodnie", "category-mezczyzna-spodnie.html")]),
 ("Dodatki", "category-dodatki.html", [
    ("Czapki", "category-czapki.html"),
    ("Skarpetki", "category-skarpetki.html"),
    ("Paski", "category-paski.html"),
    ("Buty", "category-buty.html")]),
 ("Nowa kolekcja", "nowa-kolekcja.html", []),
]

FOOTER_COLS = [
 ("Kobiety", [("Sukienki i spódnice", "category-sukienki.html"), ("Koszulki polo i topy", "category-kobieta-polo.html"),
              ("Spodnie", "category-kobieta-spodnie.html"), ("Zobacz wszystko", "category.html")]),
 ("Mężczyźni", [("Koszulki polo i topy", "category-mezczyzna-polo.html"), ("Spodnie", "category-mezczyzna-spodnie.html"),
                ("Zobacz wszystko", "category-mezczyzna.html")]),
 ("Dodatki", [("Czapki", "category-czapki.html"), ("Paski", "category-paski.html"),
              ("Skarpetki", "category-skarpetki.html"), ("Buty", "category-buty.html")]),
 ("O Pic à bec", [("O nas", "o-nas.html"), ("Kontakt", "kontakt.html"), ("Wysyłka", "wysylka.html"),
                  ("Zwroty i wymiany", "zwroty-i-wymiany.html"), ("Regulamin", "regulamin.html"),
                  ("Polityka prywatności", "regulamin.html"), ("Polityka cookies", "regulamin.html")]),
 ("Konto", [("Logowanie", "login.html"), ("Moje konto", "account.html"), ("Koszyk", "cart.html")]),
]

# ---------------------------------------------------------------------------
# partials
# ---------------------------------------------------------------------------
def head(title, body_class, desc="pic à bec — odzież inspirowana światem golfa."):
    return f"""<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#1E2A21">
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body class="{body_class}">
<a class="skip-link" href="#main-content">Przejdź do treści</a>
"""

def header(active="", transparent=False):
    cls = "header js-sticky-header" + (" header--transparent" if transparent else "")
    nav = []
    for label, href, subs in NAV:
        cur = " pic-menu__link--current" if label == active else ""
        item = [f'<li class="pic-menu__item">',
                f'<a class="pic-menu__link{cur}" href="{href}">{label}</a>']
        if subs:
            item.append('<div class="pic-menu__sub"><p class="pic-menu__sub-title">Kategorie</p><ul>')
            for s_label, s_href in subs:
                item.append(f'<li><a class="pic-menu__sub-link" href="{s_href}">{s_label}</a></li>')
            item.append(f'</ul><a class="pic-menu__sub-link pic-menu__sub-link--all" href="{href}">Zobacz wszystko</a></div>')
        item.append('</li>')
        nav.append("".join(item))
    nav = "".join(nav)

    return f"""
<div class="header-banner">
  <div class="container header-banner__inner">
    <span class="header-banner__text"><span class="long">Darmowa wysyłka przy zamówieniach powyżej 125 USD</span><span class="short">Darmowa wysyłka · 30 dni na zwrot</span></span>
    <span class="header-banner__sep" aria-hidden="true"></span>
    <span class="header-banner__text header-banner__item--secondary">30-dniowa gwarancja satysfakcji</span>
    <span class="header-banner__sep" aria-hidden="true"></span>
    <span class="header-banner__text header-banner__item--secondary">Bezpłatne zwroty i wymiany</span>
  </div>
</div>

<header id="header" class="{cls}" data-ps-ref="header">
  <div class="container">
    <div class="header-pic__inner">
      <div class="header-pic__left">
        <button type="button" class="btn-icon header-pic__menu-btn" data-open="header-menu-panel" aria-label="Otwórz menu" aria-controls="header-menu-panel">
          <span class="bars" aria-hidden="true"></span>
        </button>
        <nav class="pic-menu" aria-label="Menu główne"><ul class="pic-menu" style="display:contents">{nav}</ul></nav>
      </div>

      <a class="header-pic__logo" href="index.html">pic <em>à</em> bec</a>

      <div class="header-pic__right">
        <button type="button" class="btn-icon header-pic__action-btn" data-search-toggle aria-expanded="false" aria-controls="header-search" aria-label="Szukaj">{ICON['search']}</button>
        <a class="btn-icon header-pic__action-btn" href="login.html" aria-label="Moje konto">{ICON['user']}</a>
        <button type="button" class="btn-icon header-pic__action-btn" data-open="blockcart-drawer" aria-label="Koszyk">
          {ICON['bag']}<span class="header-pic__cart-badge" aria-hidden="true">0</span>
        </button>
      </div>
    </div>
  </div>

  <div class="header-pic__search-bar" id="header-search">
    <div class="container">
      <form class="ps-searchbar__form js-search-form" role="search">
        <span class="ps-searchbar__magnifier" aria-hidden="true">{ICON['search']}</span>
        <label class="visually-hidden" for="search-input">Szukaj w sklepie</label>
        <input class="ps-searchbar__input" id="search-input" type="search" name="s" placeholder="Czego szukasz?" autocomplete="off">
        <button type="button" class="ps-searchbar__clear" data-search-toggle>Zamknij</button>
      </form>
      <div class="ps-searchbar__suggest">
        <span class="eyebrow">Popularne</span>
        <a class="chip" href="search.html?q=polo">polo</a>
        <a class="chip" href="search.html?q=czapka">czapka</a>
        <a class="chip" href="search.html?q=spodnie">spodnie</a>
        <a class="chip" href="search.html?q=skarpetki">skarpetki</a>
      </div>
    </div>
  </div>
</header>
"""

def mobile_panel():
    items = []
    for label, href, subs in NAV:
        if subs:
            sub = "".join(f'<a class="pic-menu-m__sub-link" href="{h}">{l}</a>' for l, h in subs)
            sub += f'<a class="pic-menu-m__sub-link" href="{href}">Zobacz wszystko</a>'
            items.append(f"""<li class="pic-menu-m__item">
  <button type="button" class="pic-menu-m__toggle" data-toggle data-toggle-exclusive aria-expanded="false">{label}<span class="chev" aria-hidden="true"></span></button>
  <div class="pic-menu-m__sub"><div><div class="pic-menu-m__sub-inner">{sub}</div></div></div>
</li>""")
        else:
            items.append(f'<li class="pic-menu-m__item"><a class="pic-menu-m__link" href="{href}">{label}</a></li>')
    return f"""
<div id="overlay" class="overlay"></div>

<div id="header-menu-panel" class="js-panel" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="header-menu-panel__head">
    <span class="eyebrow">Menu</span>
    <button type="button" class="btn-icon" data-close aria-label="Zamknij menu">{ICON['close']}</button>
  </div>
  <div class="header-menu-panel__body">
    <form class="ps-searchbar__form js-search-form" role="search" style="padding-top:0;border-bottom:1px solid var(--color-line);padding-bottom:var(--space-xs)">
      <span class="ps-searchbar__magnifier" aria-hidden="true">{ICON['search']}</span>
      <label class="visually-hidden" for="m-search">Szukaj</label>
      <input class="ps-searchbar__input" id="m-search" type="search" placeholder="Szukaj" style="font-size:1.125rem;height:34px">
    </form>
    <ul data-toggle-group style="margin-top:var(--space-sm)">{''.join(items)}</ul>
    <nav class="panel-links" aria-label="Konto i obsługa klienta">
      <a href="login.html">{ICON['user']} Zaloguj się</a>
      <a href="cart.html">{ICON['bag']} Koszyk</a>
      <a href="kontakt.html">Kontakt</a>
      <a href="wysylka.html">Wysyłka</a>
      <a href="zwroty-i-wymiany.html">Zwroty i wymiany</a>
      <a href="o-nas.html">O nas</a>
    </nav>
  </div>
  <div class="header-menu-panel__foot">
    <div class="panel-selectors">
      <label class="visually-hidden" for="m-lang">Język</label>
      <select class="form-select" id="m-lang"><option>Polski</option><option>English</option></select>
      <label class="visually-hidden" for="m-cur">Waluta</label>
      <select class="form-select" id="m-cur"><option>PLN zł</option><option>EUR €</option></select>
    </div>
  </div>
</div>

<div id="blockcart-drawer" class="blockcart-drawer js-panel" role="dialog" aria-modal="true" aria-label="Koszyk">
  <div class="blockcart-drawer__head">
    <span class="blockcart-drawer__title">Twój koszyk</span>
    <button type="button" class="btn-icon" data-close aria-label="Zamknij koszyk">{ICON['close']}</button>
  </div>
  <div class="blockcart-drawer__body" id="blockcart-body"></div>
  <div class="blockcart-drawer__foot" id="blockcart-foot">
    <p class="blockcart-drawer__ship">{ICON['truck']}<span id="blockcart-ship"></span></p>
    <div class="blockcart-drawer__total"><span>Razem</span><strong id="blockcart-total">0,00 zł</strong></div>
    <a class="btn btn--primary btn--full" href="checkout.html">Przejdź do kasy</a>
    <a class="btn btn--outline btn--full" href="cart.html">Zobacz koszyk</a>
  </div>
</div>

<div class="toast" id="toast" role="status" aria-live="polite">{ICON['check']}<span id="toast-text"></span></div>
"""

def footer():
    cols = []
    for i, (title, links) in enumerate(FOOTER_COLS):
        lis = "".join(f'<li><a href="{h}">{l}</a></li>' for l, h in links)
        cols.append(f"""<div class="footer-pic__col">
  <button type="button" class="footer-pic__toggle" data-toggle aria-expanded="false"><span class="footer-pic__heading">{title}</span><span class="footer-pic__chevron" aria-hidden="true"></span></button>
  <div class="footer-pic__body"><div><ul class="footer-pic__nav-list">{lis}</ul></div></div>
</div>""")
    return f"""
<footer class="footer-pic">
  <div class="container">
    <div class="footer-news">
      <div class="footer-news__grid">
        <div>
          <p class="footer-news__title">Zapisz się na listę pic à bec</p>
          <p class="footer-news__text">Informacje o nowych kolekcjach, dostawach rozmiarów i wydarzeniach na polu golfowym. Bez hałasu.</p>
        </div>
        <div>
          <form class="footer-news__form" onsubmit="return false">
            <label class="visually-hidden" for="news-mail">Adres e-mail</label>
            <input id="news-mail" type="email" placeholder="Adres e-mail" autocomplete="email">
            <button type="submit">Zapisz się</button>
          </form>
          <div class="form-check footer-news__consent">
            <input class="form-check-input" type="checkbox" id="news-consent">
            <label class="form-check-label" for="news-consent">Wyrażam zgodę na otrzymywanie informacji handlowych zgodnie z <a href="regulamin.html">polityką prywatności</a>.</label>
          </div>
        </div>
      </div>
    </div>

    <div class="footer-pic__top">
      <div class="footer-pic__grid">
        <div class="footer-pic__brand">
          <a class="footer-pic__logo" href="index.html">pic à bec</a>
          <p class="footer-pic__tagline">Marka odzieżowa inspirowana światem golfa, łącząca elegancję, funkcjonalność i nowoczesny minimalizm.</p>
          <div class="footer-pic__social-icons">
            <a class="footer-pic__social-icon" href="https://www.instagram.com/picabec/" aria-label="Instagram">{ICON['ig']}</a>
            <a class="footer-pic__social-icon" href="https://www.facebook.com/profile.php?id=61590259266431" aria-label="Facebook">{ICON['fb']}</a>
          </div>
        </div>
        {''.join(cols)}
      </div>
    </div>

    <div class="footer-pic__bottom">
      <span>© 2026 — Copyright All Right Reserved. Projekt i wykonanie: Design Partners</span>
      <div class="footer-pic__bottom-right">
        <span class="footer-pic__pay"><i>Visa</i><i>Mastercard</i><i>BLIK</i><i>Przelewy24</i></span>
        <a class="footer-pic__scroll-btn" href="#header">Do góry {ICON['arrowup']}</a>
      </div>
    </div>
  </div>
</footer>
"""

FOOT_JS = '<script src="assets/js/main.js"></script>\n</body>\n</html>\n'

def breadcrumb(items):
    lis = []
    for i, (label, href) in enumerate(items):
        last = i == len(items) - 1
        if last:
            lis.append(f'<li class="breadcrumb-item" aria-current="page">{label}</li>')
        else:
            lis.append(f'<li class="breadcrumb-item"><a class="breadcrumb-link" href="{href}">{label}</a></li>')
    return f"""<div class="breadcrumb__wrapper"><div class="container"><nav aria-label="Ścieżka nawigacji"><ol class="breadcrumb">{''.join(lis)}</ol></nav></div></div>"""

# ---------------------------------------------------------------------------
# product card
# ---------------------------------------------------------------------------
def swatches(p, limit=4):
    if not p["colors"]:
        return ""
    out = []
    for c in p["colors"][:limit]:
        out.append(f'<span class="color" style="--swatch:{COLOR_HEX.get(c,"#ccc")}" title="{c}"></span>')
    if len(p["colors"]) > limit:
        out.append(f'<span class="more">+{len(p["colors"])-limit}</span>')
    return f'<div class="product-miniature__variants" aria-hidden="true">{"".join(out)}</div>'

def product_card(p, lazy=True):
    out = p["stock"] == "out"
    flags = []
    if p["stock"] == "low":
        flags.append('<li class="badge low">Ostatnie sztuki</li>')
    if out:
        flags.append('<li class="badge out">Chwilowo niedostępny</li>')
    flags_html = f'<ul class="product-flags">{"".join(flags)}</ul>' if flags else ""

    if out:
        price_html = '<div class="product-miniature__price product-miniature__price--unavailable">Obecnie brak na stanie</div>'
    else:
        price_html = f'<div class="product-miniature__price num">{price_str(p["price"])}</div>'

    quick = ""
    if not out:
        sizes = "".join(
            f'<button type="button" class="quick-add__size js-add-to-cart" data-key="{p["key"]}" data-name="{p["name"]}" '
            f'data-sub="{p["sub"]}" data-href="{p["file"]}" data-img="{cover(p)}" data-price="{p["price"]}" '
            f'data-color="{p["colors"][0] if p["colors"] else ""}" data-size="{s}">{s}</button>' for s in p["sizes"])
        quick = f"""<div class="product-miniature__actions"><div class="quick-add">
      <span class="quick-add__label">Szybki wybór rozmiaru</span>
      <div class="quick-add__sizes">{sizes}</div>
    </div></div>"""

    loading = ' loading="lazy"' if lazy else ''
    return f"""<article class="product-miniature{' product-miniature--out' if out else ''}"
  data-name="{p['name']} {p['sub']}" data-price="{p['price'] or 0}" data-group="{p['group']}"
  data-search="{p['name']} {p['sub']} {p['group']} {' '.join(p['colors'])} {' '.join(p['sizes'])}"
  data-colors="{'|'.join(p['colors'])}" data-sizes="{'|'.join(p['sizes'])}">
  <div class="product-miniature__inner">
    <div class="product-miniature__top">
      <a class="product-miniature__image imgframe" href="{p['file']}" aria-label="{p['full']}">
        <img src="{cover(p)}" alt="{p['full']}"{loading} decoding="async">
      </a>
      <span class="product-miniature__image product-miniature__image--alt imgframe" aria-hidden="true">
        <img src="{alt_img(p)}" alt=""{loading} decoding="async">
      </span>
      {flags_html}
      <button type="button" class="product-miniature__wish" aria-pressed="false" aria-label="Dodaj do ulubionych">{ICON['heart']}</button>
      {quick}
    </div>
    <div class="product-miniature__body">
      <h3 class="product-miniature__title"><a href="{p['file']}">{p['name'].replace('No. ', 'No.&nbsp;')}</a></h3>
      <p class="product-miniature__subtitle">{p['sub']}</p>
      {swatches(p)}
      {price_html}
    </div>
  </div>
</article>"""

# ---------------------------------------------------------------------------
# filter drawer
# ---------------------------------------------------------------------------
SORTS = [("default","Dostępne"),("price-asc","Cena, rosnąco"),("price-desc","Cena, malejąco"),
         ("name-asc","Nazwa, A do Z"),("name-desc","Nazwa, Z do A")]

def filter_panel(products):
    groups, colors, sizes = [], [], []
    for p in products:
        if p["group"] not in groups: groups.append(p["group"])
        for c in p["colors"]:
            if c not in colors: colors.append(c)
        for s in p["sizes"]:
            if s not in sizes: sizes.append(s)
    maxp = max([p["price"] for p in products if p["price"]] or [1000])

    def count(kind, v):
        n = 0
        for p in products:
            if kind == "group" and p["group"] == v: n += 1
            if kind == "color" and v in p["colors"]: n += 1
        return n

    gh = "".join(f"""<label class="search-filters__form-check">
      <input class="form-check-input js-filter" type="checkbox" data-facet="group" value="{g}">
      <span class="form-check-label">{g}<span class="magnitude">{count('group',g)}</span></span></label>""" for g in groups)
    ch = "".join(f"""<label class="search-filters__form-check search-filters__form-check--color">
      <input class="form-check-input js-filter" type="checkbox" data-facet="color" value="{c}">
      <span class="form-check-label"><span class="color" style="--swatch:{COLOR_HEX.get(c,'#ccc')}"></span>{c}<span class="magnitude">{count('color',c)}</span></span></label>""" for c in colors)
    sh = "".join(f"""<label class="filter-size"><input class="js-filter" type="checkbox" data-facet="size" value="{s}"><span>{s}</span></label>""" for s in sizes)
    so = "".join(f"""<label class="sort-option"><input class="form-check-input js-sort-radio" type="radio" name="sort-m" value="{v}"{' checked' if v=='default' else ''}><span>{l}</span></label>""" for v, l in SORTS)

    return f"""
<div id="filter-panel" class="pic-filter-panel js-panel" role="dialog" aria-modal="true" aria-label="Filtry i sortowanie">
  <div class="pic-filter-panel__header">
    <span class="pic-filter-panel__title">Filtruj i sortuj</span>
    <button type="button" class="btn-icon" data-close aria-label="Zamknij filtry">{ICON['close']}</button>
  </div>
  <div class="pic-filter-panel__body" data-toggle-group>
    <div class="search-filters__group">
      <button type="button" class="search-filters__toggle" data-toggle aria-expanded="true">Sortowanie<span class="sign" aria-hidden="true"></span></button>
      <div class="search-filters__panel"><div><div class="sort-list">{so}</div></div></div>
    </div>
    <div class="search-filters__group">
      <button type="button" class="search-filters__toggle" data-toggle aria-expanded="true">Kategoria<span class="sign" aria-hidden="true"></span></button>
      <div class="search-filters__panel"><div><div class="search-filters__inner">{gh}</div></div></div>
    </div>
    <div class="search-filters__group">
      <button type="button" class="search-filters__toggle" data-toggle aria-expanded="true">Kolor<span class="sign" aria-hidden="true"></span></button>
      <div class="search-filters__panel"><div><div class="search-filters__inner">{ch}</div></div></div>
    </div>
    <div class="search-filters__group">
      <button type="button" class="search-filters__toggle" data-toggle aria-expanded="true">Rozmiar<span class="sign" aria-hidden="true"></span></button>
      <div class="search-filters__panel"><div><div class="filter-sizes">{sh}</div></div></div>
    </div>
    <div class="search-filters__group">
      <button type="button" class="search-filters__toggle" data-toggle aria-expanded="true">Cena<span class="sign" aria-hidden="true"></span></button>
      <div class="search-filters__panel"><div><div class="filter-price">
        <div class="filter-price__range"><span>0 zł</span><span id="filter-price-out">{price_str(maxp)}</span></div>
        <label class="visually-hidden" for="filter-price">Cena maksymalna</label>
        <input type="range" id="filter-price" min="100" max="{int(maxp)}" step="10" value="{int(maxp)}">
      </div></div></div>
    </div>
  </div>
  <div class="pic-filter-panel__footer">
    <button type="button" class="pic-filter-panel__clear" id="filter-clear">Wyczyść</button>
    <button type="button" class="btn btn--primary" data-close>Pokaż produkty</button>
  </div>
</div>"""

# ---------------------------------------------------------------------------
# listing page
# ---------------------------------------------------------------------------
def listing_page(fname, title, desc, products, crumbs, subs=None, active_nav="", eyebrow="Kolekcja"):
    n = len(products)
    sort_opts = "".join(f'<option value="{v}">{l}</option>' for v, l in SORTS)
    sub_html = ""
    if subs:
        cur_attr = ' aria-current="true"'
        chips = "".join('<a href="%s"%s>%s</a>' % (h, cur_attr if h == fname else "", l) for l, h in subs)
        sub_html = f'<div class="subcategory"><div class="subcategory__list">{chips}</div></div>'

    cards = "".join(product_card(p, lazy=(i > 3)) for i, p in enumerate(products))
    empty = f"""<div class="empty-state" id="grid-empty"{'' if n == 0 else ' hidden'}>
  <span class="empty-state__icon">{ICON['grid']}</span>
  <h2 class="h3">Bądźcie czujni!</h2>
  <p>W tym miejscu zostanie wyświetlonych więcej produktów w miarę ich dodawania. W międzyczasie zajrzyj do pozostałych kategorii.</p>
  <a class="btn btn--outline" href="category-dodatki.html">Zobacz dodatki</a>
</div>"""

    toolbar = "" if n == 0 else f"""
<div id="js-product-list-top">
  <div class="container">
    <div class="products__selection">
      <button type="button" class="pic-filter-btn" data-open="filter-panel">
        <span class="pic-filter-btn__icon" aria-hidden="true">{ICON['filter']}</span>Filtruj i sortuj
        <span class="pic-filter-btn__count" id="filter-count" hidden>0</span>
      </button>
      <span class="products__count" id="products-count">{n} {plural(n)}</span>
      <div class="sort-inline">
        <label for="sort-select">Sortuj wg</label>
        <select class="form-select js-sort" id="sort-select">{sort_opts}</select>
      </div>
    </div>
  </div>
</div>"""

    return (head(f"{title} — pic à bec", "page-category") + header(active_nav) + breadcrumb(crumbs) + f"""
<main id="main-content" class="wrapper">
  <section class="category-head">
    <div class="container">
      <div class="category-head__grid">
        <div>
          <span class="eyebrow">{eyebrow}</span>
          <h1 class="page-title-section" style="margin-top:var(--space-2xs)">{title}</h1>
        </div>
        <div>
          <p class="category-head__desc" id="cat-desc">{desc}</p>
          <button type="button" class="category-head__more" data-desc-toggle aria-expanded="false" aria-controls="cat-desc"><span class="more-less"></span></button>
        </div>
      </div>
      {sub_html}
    </div>
  </section>
  {toolbar}
  <div class="container">
    <div class="active-filters__list" id="active-filters"></div>
    <h2 class="visually-hidden">Produkty</h2>
    <div class="products{' products--wide' if n > 7 else ''}" id="js-product-grid">{cards}</div>
    {empty}
    {'' if n == 0 else '''<nav class="pagination" aria-label="Paginacja">
      <span class="pagination__nav" aria-disabled="true">Poprzednia</span>
      <a class="pagination__number current" href="#" aria-current="page">1</a>
      <span class="pagination__nav" aria-disabled="true">Następna</span>
    </nav>'''}
  </div>
</main>
""" + footer() + mobile_panel() + (filter_panel(products) if n else "") + FOOT_JS)

# ---------------------------------------------------------------------------
# writer
# ---------------------------------------------------------------------------
def write(name, html):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(html)

def build_css():
    parts = []
    for f in sorted(os.listdir(CSSDIR)):
        if f.endswith(".css"):
            parts.append(open(os.path.join(CSSDIR, f), encoding="utf-8").read())
    out = os.path.join(ROOT, "assets", "css", "styles.css")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n\n".join(parts))
    return len("\n\n".join(parts))
