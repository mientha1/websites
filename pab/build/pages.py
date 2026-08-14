# -*- coding: utf-8 -*-
"""Page templates for the pic à bec prototype."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import P, CATS, COLOR_HEX, BASE, in_cat, BY_KEY
from build import (head, header, footer, mobile_panel, breadcrumb, product_card,
                   listing_page, filter_panel, write, build_css, ICON, BENEFITS,
                   price_str, plural, img, cover, alt_img, FOOT_JS, swatches, SORTS)

HERO_IMG = BASE + "/img/cms/2026_03_16_pica_bec5649.jpg"

BRAND_LEDE = ("pic à bec to marka odzieżowa inspirowana światem golfa, łącząca elegancję, "
              "funkcjonalność i nowoczesny minimalizm.")

# ===========================================================================
# HOME
# ===========================================================================
def build_home():
    tiles = [
        ("Kobieta", "category.html", BY_KEY["elan-sleeveless-polo"], "6 modeli"),
        ("Mężczyzna", "category-mezczyzna.html", BY_KEY["standard-pique-polo"], "4 modele"),
        ("Dodatki", "category-dodatki.html", BY_KEY["cap-basic"], "6 modeli"),
    ]
    tiles_html = "".join(f"""<a class="cat-tile reveal" href="{href}">
  <span class="imgframe"><img src="{cover(p,'large_default')}" alt="{title}" loading="lazy" decoding="async"></span>
  <span class="cat-tile__overlay">
    <span><span class="cat-tile__title">{title}</span><span class="cat-tile__meta" style="display:block;margin-top:4px">{meta}</span></span>
    <span class="cat-tile__arrow" aria-hidden="true">{ICON['arrow']}</span>
  </span>
</a>""" for title, href, p, meta in tiles)

    new_keys = ["standard-pique-polo", "elan-sleeveless-polo", "elan-ls-polo", "kolarki-elan"]
    new_html = "".join(product_card(BY_KEY[k]) for k in new_keys)

    acc_keys = ["rive-belt", "foulard", "cap-basic", "crew-socks"]
    acc_html = "".join(product_card(BY_KEY[k]) for k in acc_keys)

    ben = "".join(f"""<div class="benefit reveal">
  <span class="benefit__icon" aria-hidden="true">{ICON[i]}</span>
  <h3 class="benefit__title">{t}</h3>
  <p class="benefit__text">{d}</p>
</div>""" for i, t, d in BENEFITS)

    return head("pic à bec — odzież inspirowana światem golfa", "page-index") + header("", transparent=True) + f"""
<main id="main-content" class="wrapper">

  <section class="hero">
    <div class="hero__media"><img src="{HERO_IMG}" alt="Kolekcja pic à bec wiosna – lato 2026" fetchpriority="high" decoding="async"></div>
    <div class="hero__inner">
      <div class="container">
        <div class="hero__grid">
          <div>
            <span class="eyebrow eyebrow--light">Kolekcja wiosna – lato 2026</span>
            <h1 class="hero__title">Sportowa elegancja, <em>bez przesady</em></h1>
          </div>
          <div class="hero__aside">
            <p class="hero__text">{BRAND_LEDE}</p>
            <div class="hero__cta">
              <a class="btn btn--light btn--lg" href="nowa-kolekcja.html">Zobacz nową kolekcję</a>
            </div>
            <div class="hero__links">
              <a href="category.html">Kobieta</a><span aria-hidden="true">/</span><a href="category-mezczyzna.html">Mężczyzna</a><span aria-hidden="true">/</span><a href="category-dodatki.html">Dodatki</a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <span class="hero__scroll">Przewiń</span>
  </section>

  <section class="section section--tight">
    <div class="container">
      <div class="strip">
        <span>Golf i tenis</span><span>Ponadczasowe sylwetki</span><span>OEKO-TEX® STANDARD 100</span>
        <span>Wyprodukowano w Polsce i we Włoszech</span>
      </div>
    </div>
  </section>

  <section class="section section--flush-top">
    <div class="container">
      <div class="section__head">
        <div class="section__head-text">
          <span class="eyebrow">Kolekcja</span>
          <h2>Wybierz punkt wyjścia</h2>
        </div>
        <a class="link-underline section__head-link" href="nowa-kolekcja.html">Zobacz wszystko</a>
      </div>
      <div class="cat-tiles">{tiles_html}</div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section__head">
        <div class="section__head-text">
          <span class="eyebrow">Nowa kolekcja</span>
          <h2>Wiosna – lato 2026</h2>
        </div>
        <a class="link-underline section__head-link" href="nowa-kolekcja.html">Wszystkie nowości</a>
      </div>
      <div class="products products--rail">{new_html}</div>
    </div>
  </section>

  <section class="section section--paper-deep">
    <div class="container">
      <div class="editorial">
        <div class="editorial__media reveal">
          <span class="imgframe"><img src="{cover(BY_KEY['standard-pique-polo'],'product_main')}" alt="Standard No. 1 Piqué Polo" loading="lazy" decoding="async"></span>
        </div>
        <div class="editorial__body reveal">
          <span class="eyebrow">O marce</span>
          <h2>Ubrania, które sprawdzają się na polu golfowym i poza nim</h2>
          <p class="lede">Tworzymy ubrania odpowiednie na pole golfowe i na co dzień. Stawiamy na jakość materiałów, dopracowane kroje i ponadczasowy charakter kolekcji.</p>
          <ul class="editorial__list">
            <li><span>01</span><span>Styl inspirowany golfem</span></li>
            <li><span>02</span><span>Ponadczasowe sylwetki</span></li>
            <li><span>03</span><span>Wysoka jakość wykonania</span></li>
            <li><span>04</span><span>Komfort i funkcjonalność</span></li>
          </ul>
          <div class="editorial__cta"><a class="btn btn--outline" href="o-nas.html">Poznaj markę</a></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section__head">
        <div class="section__head-text">
          <span class="eyebrow">Dodatki</span>
          <h2>Detale, które kończą stylizację</h2>
        </div>
        <a class="link-underline section__head-link" href="category-dodatki.html">Wszystkie dodatki</a>
      </div>
      <div class="products products--rail">{acc_html}</div>
    </div>
  </section>

  <section class="section section--tight">
    <div class="container"><div class="benefits">{ben}</div></div>
  </section>

</main>
""" + footer() + mobile_panel() + FOOT_JS


# ===========================================================================
# PRODUCT
# ===========================================================================
def build_product(p):
    out = p["stock"] == "out"
    parent = "Kobieta" if p["gender"] == "kobieta" else ("Mężczyzna" if p["gender"] == "mezczyzna" else "Dodatki")
    parent_file = {"Kobieta": "category.html", "Mężczyzna": "category-mezczyzna.html", "Dodatki": "category-dodatki.html"}[parent]
    crumbs = [("Strona główna", "index.html"), (parent, parent_file), (p["name"], "#")]

    slides = "".join(f"""<span class="imgframe"><img src="{img(g, p['slug'], 'product_main')}" alt="{p['full']} — zdjęcie {i+1}"{'' if i == 0 else ' loading="lazy"'} decoding="async"></span>""" for i, g in enumerate(p["gallery"]))

    dots = "".join(f'<button type="button" class="{"active" if i==0 else ""}" aria-label="Zdjęcie {i+1}"></button>' for i in range(len(p["gallery"])))

    colors_html = ""
    if p["colors"]:
        opts = "".join(f"""<span class="input-color">
  <input class="input-color__input js-variant-color" type="radio" name="color" id="c-{i}" data-name="{c}"{' checked' if i == 0 else ''}>
  <label class="input-color__label" for="c-{i}"><span class="color" style="--swatch:{COLOR_HEX.get(c,'#ccc')}"></span><span class="visually-hidden">{c}</span></label>
</span>""" for i, c in enumerate(p["colors"]))
        colors_html = f"""<div class="product-variant">
  <div class="product-variant__legend"><span>Kolor</span><span class="product-variant__selected" id="selected-color">{p['colors'][0]}</span></div>
  <div class="product-variant__colors">{opts}</div>
</div>"""

    size_opts = "".join(f"""<span class="product-variant__radio">
  <input type="radio" name="size" id="s-{i}" data-name="{s}" class="js-variant-size"{' disabled' if out else ''}>
  <label for="s-{i}">{s}</label></span>""" for i, s in enumerate(p["sizes"]))

    sizes_html = f"""<div class="product-variant">
  <div class="product-variant__legend"><span>Rozmiar</span><a class="product-variant__guide" href="#" data-modal="size-modal">Tabela rozmiarów</a></div>
  <div class="product-variant__radios">{size_opts}</div>
  <p class="form-error" id="size-error" hidden>Wybierz rozmiar, aby dodać produkt do koszyka.</p>
</div>"""

    if out:
        price_block = '<div class="product__prices"><span class="product__price product__price--unavailable">Obecnie brak na stanie</span></div>'
        avail = f'<p id="product-availability" class="is-out"><span class="dot"></span>Ten model jest chwilowo niedostępny</p>'
        cta = """<div class="product__actions-qty-add">
  <button type="button" class="btn btn--outline btn--lg" style="flex:1" data-modal="notify-modal">Powiadom o dostępności</button>
</div>"""
    else:
        price_block = f'<div class="product__prices"><span class="product__price num">{price_str(p["price"])}</span><span class="product__tax-label">Brutto</span></div>'
        if p["stock"] == "low":
            avail = '<p id="product-availability" class="is-low"><span class="dot"></span>Ostatnie sztuki w magazynie</p>'
        else:
            avail = '<p id="product-availability"><span class="dot"></span>Dostępny — wysyłka w 2–7 dni roboczych</p>'
        cta = f"""<div class="product__actions-qty-add">
  <div class="quantity-button js-qty">
    <button type="button" data-step="-1" aria-label="Zmniejsz ilość">–</button>
    <label class="visually-hidden" for="product-qty">Ilość</label>
    <input id="product-qty" type="number" value="1" min="1" inputmode="numeric">
    <button type="button" data-step="1" aria-label="Zwiększ ilość">+</button>
  </div>
  <button type="button" class="btn btn--primary btn--lg product__add-to-cart-button js-add-to-cart"
    data-key="{p['key']}" data-name="{p['name']}" data-sub="{p['sub']}" data-href="{p['file']}"
    data-img="{cover(p)}" data-price="{p['price']}">Dodaj do koszyka</button>
</div>"""

    desc_html = "".join(f"<p>{d}</p>" for d in p["desc"])
    details_html = "".join(f"<li>{d}</li>" for d in p["details"])

    related = [q for q in P if q["key"] != p["key"] and q["group"] == p["group"]][:4]
    if len(related) < 4:
        extra = [q for q in P if q["key"] != p["key"] and q not in related]
        related += extra[:4 - len(related)]
    rel_html = "".join(product_card(q) for q in related)

    buybar = "" if out else f"""
<div class="buybar" id="buybar">
  <div class="buybar__info">
    <div class="buybar__name">{p['name']}</div>
    <div class="buybar__price num">{price_str(p['price'])}</div>
  </div>
  <button type="button" class="btn btn--primary js-add-to-cart"
    data-key="{p['key']}" data-name="{p['name']}" data-sub="{p['sub']}" data-href="{p['file']}"
    data-img="{cover(p)}" data-price="{p['price']}">Dodaj do koszyka</button>
</div>"""

    notify_modal = """
<div class="modal" id="notify-modal" role="dialog" aria-modal="true" aria-labelledby="notify-title">
  <div class="modal__backdrop" data-modal-close></div>
  <div class="modal__dialog">
    <button type="button" class="btn-icon modal__close" data-modal-close aria-label="Zamknij">""" + ICON['close'] + """</button>
    <span class="eyebrow">Powiadomienie</span>
    <h2 id="notify-title" style="margin-top:var(--space-2xs)">Damy znać, gdy wróci</h2>
    <p class="lede" style="margin-top:var(--space-xs)">Zostaw adres e-mail — napiszemy w dniu, w którym model pojawi się ponownie w magazynie.</p>
    <form onsubmit="return false" style="margin-top:var(--space-md)">
      <div class="form-group">
        <label class="form-label" for="notify-mail">Adres e-mail</label>
        <input class="form-control" id="notify-mail" type="email" placeholder="jan.kowalski@example.com" autocomplete="email">
      </div>
      <button class="btn btn--primary btn--full" type="submit">Powiadom mnie</button>
    </form>
  </div>
</div>"""

    size_modal = f"""
<div class="modal" id="size-modal" role="dialog" aria-modal="true" aria-labelledby="size-title">
  <div class="modal__backdrop" data-modal-close></div>
  <div class="modal__dialog">
    <button type="button" class="btn-icon modal__close" data-modal-close aria-label="Zamknij">{ICON['close']}</button>
    <span class="eyebrow">Pomoc</span>
    <h2 id="size-title" style="margin-top:var(--space-2xs)">Tabela rozmiarów</h2>
    <p class="text-muted" style="font-size:var(--fs-sm);margin-top:var(--space-xs)">Dostępne rozmiary tego modelu: {', '.join(p['sizes'])}. W razie wątpliwości napisz do nas — pomożemy dobrać rozmiar.</p>
    <table class="size-table">
      <thead><tr><th>Rozmiar</th><th>Dostępność</th></tr></thead>
      <tbody>{''.join(f'<tr><td>{s}</td><td>{"Chwilowo brak" if out else "Dostępny"}</td></tr>' for s in p['sizes'])}</tbody>
    </table>
    <a class="btn btn--outline btn--full" href="kontakt.html" style="margin-top:var(--space-md)">Napisz do nas</a>
  </div>
</div>"""

    return head(f"{p['full']} — pic à bec", "page-product") + header(parent) + breadcrumb(crumbs) + f"""
<main id="main-content" class="wrapper">
  <div class="container">
    <div class="product__container">

      <div class="product__left">
        <div class="product__images js-images-container">
          <div style="position:relative">
            <span class="product__gallery-count" id="product-gallery-count">1 / {len(p['gallery'])}</span>
            <div class="product__carousel" id="product-carousel">{slides}</div>
            <div class="product__gallery-dots" id="product-dots">{dots}</div>
            {'<button type="button" class="btn btn--outline btn--sm product__gallery-more" id="gallery-more">Pokaż wszystkie zdjęcia (' + str(len(p['gallery'])) + ')</button>' if len(p['gallery']) > 3 else ''}
          </div>
        </div>
      </div>

      <div class="product__right">
        <div class="product__info-sticky">
          <div class="product__eyebrow"><span class="eyebrow">{p['group']}</span></div>
          <h1 class="product__title">{p['name'].replace('No. ', 'No.&nbsp;')}</h1>
          <p class="product__subtitle">{p['sub']}</p>
          {price_block}
          <hr class="rule product__divider">
          {colors_html}
          {sizes_html}
          <span id="product-buy-anchor"></span>
          {cta}
          {avail}
          <ul class="product__usp">
            <li>{ICON['truck']}<span>Darmowa wysyłka przy zamówieniach powyżej 125 USD</span></li>
            <li>{ICON['return']}<span>Bezpłatne zwroty i wymiany w ciągu 14 dni</span></li>
            <li>{ICON['shield']}<span>30-dniowa gwarancja satysfakcji</span></li>
          </ul>

          <div id="product_accordion" data-toggle-group>
            <div class="accordion-item">
              <button type="button" class="accordion-button" data-toggle aria-expanded="true">Opis<span class="sign" aria-hidden="true"></span></button>
              <div class="accordion-collapse"><div><div class="accordion-body rte">{desc_html}</div></div></div>
            </div>
            <div class="accordion-item">
              <button type="button" class="accordion-button" data-toggle aria-expanded="false">Szczegóły produktu<span class="sign" aria-hidden="true"></span></button>
              <div class="accordion-collapse"><div><div class="accordion-body rte"><ul>{details_html}</ul></div></div></div>
            </div>
            <div class="accordion-item">
              <button type="button" class="accordion-button" data-toggle aria-expanded="false">Wysyłka i zwroty<span class="sign" aria-hidden="true"></span></button>
              <div class="accordion-collapse"><div><div class="accordion-body rte">
                <p>Czas realizacji zamówień wynosi od 2 do 7 dni roboczych. Koszt standardowej przesyłki kurierskiej wynosi 18 zł, a do punktu odbioru lub automatu paczkowego 18,50 zł.</p>
                <p>Klient ma prawo odstąpić od umowy i zwrócić zakupiony produkt w terminie 14 dni od dnia otrzymania przesyłki bez podawania przyczyny. <a href="zwroty-i-wymiany.html">Zobacz pełne zasady zwrotów</a>.</p>
              </div></div></div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>

  <section class="section section--tight">
    <div class="container">
      <div class="section__head">
        <div class="section__head-text"><span class="eyebrow">Zobacz również</span><h2>Dobrane do tego modelu</h2></div>
        <a class="link-underline section__head-link" href="{parent_file}">Cała kategoria</a>
      </div>
      <div class="products products--rail">{rel_html}</div>
    </div>
  </section>
</main>
""" + footer() + mobile_panel() + buybar + size_modal + notify_modal + FOOT_JS


# ===========================================================================
# SEARCH
# ===========================================================================
def build_search():
    cards = "".join(product_card(p) for p in P)
    return head("Wyniki wyszukiwania — pic à bec", "page-search") + header() + breadcrumb(
        [("Strona główna", "index.html"), ("Wyszukiwanie", "#")]) + f"""
<main id="main-content" class="wrapper">
  <section class="search-head">
    <div class="container">
      <span class="eyebrow">Wyszukiwanie</span>
      <h1 class="visually-hidden">Wyniki wyszukiwania</h1>
      <form class="search-head__form js-search-form" role="search" style="margin-top:var(--space-2xs)">
        <label class="visually-hidden" for="search-page-input">Szukaj</label>
        <input id="search-page-input" type="search" name="q" value="polo" placeholder="Czego szukasz?" autocomplete="off">
        <button type="submit" class="btn-icon" aria-label="Szukaj">{ICON['search']}</button>
      </form>
      <p class="search-head__meta">Znaleziono <span id="search-result-count">6</span> wyników dla „<span id="search-query-out">polo</span>”</p>
      <div class="search-suggest">
        <span class="eyebrow">Może szukasz</span>
        <a class="chip" href="search.html?q=polo">polo</a>
        <a class="chip" href="search.html?q=czapka">czapka</a>
        <a class="chip" href="search.html?q=pasek">pasek</a>
        <a class="chip" href="search.html?q=spódnica">spódnica</a>
        <a class="chip" href="search.html?q=skarpetki">skarpetki</a>
      </div>
    </div>
  </section>

  <div id="js-product-list-top">
    <div class="container">
      <div class="products__selection">
        <button type="button" class="pic-filter-btn" data-open="filter-panel">
          <span class="pic-filter-btn__icon" aria-hidden="true">{ICON['filter']}</span>Filtruj i sortuj
          <span class="pic-filter-btn__count" id="filter-count" hidden>0</span>
        </button>
        <span class="products__count" id="products-count">{len(P)} {plural(len(P))}</span>
        <div class="sort-inline">
          <label for="sort-select">Sortuj wg</label>
          <select class="form-select js-sort" id="sort-select">{''.join(f'<option value="{v}">{l}</option>' for v, l in SORTS)}</select>
        </div>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="active-filters__list" id="active-filters"></div>
    <h2 class="visually-hidden">Produkty</h2>
    <div class="products products--wide" id="js-product-grid">{cards}</div>
    <div class="empty-state" id="grid-empty" hidden>
      <span class="empty-state__icon">{ICON['search']}</span>
      <h2 class="h3">Brak wyników</h2>
      <p>Nie znaleźliśmy produktów pasujących do tego zapytania. Spróbuj innej frazy albo przejrzyj kolekcję.</p>
      <a class="btn btn--outline" href="nowa-kolekcja.html">Zobacz kolekcję</a>
    </div>
  </div>
</main>
""" + footer() + mobile_panel() + filter_panel(P) + FOOT_JS


# ===========================================================================
# CART
# ===========================================================================
def build_cart():
    return head("Koszyk — pic à bec", "page-cart") + header() + breadcrumb(
        [("Strona główna", "index.html"), ("Koszyk", "#")]) + f"""
<main id="main-content" class="wrapper">
  <div class="container">
    <div style="padding-block:clamp(1.5rem,3vw,2.5rem) var(--space-md)">
      <span class="eyebrow">Zamówienie</span>
      <h1 class="page-title-section" style="margin-top:var(--space-2xs)">Koszyk</h1>
    </div>

    <div class="empty-state" id="cart-empty" hidden>
      <span class="empty-state__icon">{ICON['bag']}</span>
      <h2 class="h3">Twój koszyk jest pusty</h2>
      <p>Nie ma tu jeszcze żadnych produktów. Zacznij od nowej kolekcji albo zajrzyj do dodatków.</p>
      <div class="u-flex u-gap-sm u-wrap" style="justify-content:center">
        <a class="btn btn--primary" href="nowa-kolekcja.html">Nowa kolekcja</a>
        <a class="btn btn--outline" href="category-dodatki.html">Dodatki</a>
      </div>
    </div>

    <div class="cart-grid" id="cart-grid">
      <div class="cart-grid__content">
        <p class="eyebrow" style="padding-bottom:var(--space-xs);border-bottom:1px solid var(--color-line)"><span id="cart-count">0</span> <span id="cart-count-label">produktów</span> w koszyku</p>
        <div id="cart-lines"></div>
        <a class="cart__continue-shopping" href="nowa-kolekcja.html">{ICON['arrowl']} Kontynuuj zakupy</a>
      </div>

      <aside class="cart-grid__aside-wrapper">
        <div class="cart-summary">
          <div class="freeship">
            <p class="freeship__text" id="freeship-text">Do darmowej dostawy brakuje <strong>500,00 zł</strong>.</p>
            <span class="freeship__bar"><i id="freeship-bar" style="width:0%"></i></span>
          </div>

          <h2 class="cart-summary__title">Podsumowanie</h2>
          <div class="cart-summary__line"><span>Wartość produktów</span><span id="cart-subtotal">0,00 zł</span></div>
          <div class="cart-summary__line"><span>Dostawa</span><span id="cart-shipping">Gratis</span></div>
          <div class="cart-summary__line cart-summary__line--muted"><span>w tym VAT 23%</span><span id="cart-vat">0,00 zł</span></div>
          <div class="cart-summary__total"><span>Razem</span><strong id="cart-total">0,00 zł</strong></div>
          <p class="cart-summary__note">Ceny brutto. Koszt dostawy potwierdzimy w kasie.</p>

          <a class="btn btn--primary btn--full btn--lg" href="checkout.html">Przejdź do kasy</a>

          <div class="cart-promo">
            <span class="eyebrow">Kod rabatowy</span>
            <div class="cart-promo__row">
              <label class="visually-hidden" for="promo">Kod rabatowy</label>
              <input class="form-control" id="promo" type="text" placeholder="Wpisz kod">
              <button type="button" class="btn btn--outline">Zastosuj</button>
            </div>
          </div>

          <ul class="trust-row">
            <li>{ICON['truck']}Wysyłka 2–7 dni roboczych</li>
            <li>{ICON['return']}14 dni na zwrot</li>
            <li>{ICON['lock']}Bezpieczne płatności</li>
          </ul>
        </div>
      </aside>
    </div>
  </div>
</main>
""" + footer() + mobile_panel() + FOOT_JS


# ===========================================================================
# CHECKOUT
# ===========================================================================
def build_checkout():
    return head("Kasa — pic à bec", "page-checkout") + f"""
<div class="checkout-head">
  <div class="container">
    <div class="checkout-head__inner">
      <a class="checkout-head__back" href="cart.html">{ICON['arrowl']}<span>Wróć do koszyka</span></a>
      <a class="checkout-head__logo" href="index.html">pic à bec</a>
      <span class="checkout-head__secure">{ICON['lock']}<span>Bezpieczne zamówienie</span></span>
    </div>
  </div>
</div>

<main id="main-content" class="wrapper">
  <div class="container">
    <h1 class="visually-hidden">Kasa — dokończ zamówienie</h1>
    <div class="checkout-grid">
      <div>
        <nav class="checkout-steps" aria-label="Kroki zamówienia">
          <span class="checkout-steps__step checkout-steps__step--current" data-step="1"><span class="checkout-steps__number">1</span><span>Dane</span></span>
          <span class="checkout-steps__sep" aria-hidden="true"></span>
          <span class="checkout-steps__step" data-step="2"><span class="checkout-steps__number">2</span><span>Adres</span></span>
          <span class="checkout-steps__sep" aria-hidden="true"></span>
          <span class="checkout-steps__step" data-step="3"><span class="checkout-steps__number">3</span><span>Dostawa</span></span>
          <span class="checkout-steps__sep" aria-hidden="true"></span>
          <span class="checkout-steps__step" data-step="4"><span class="checkout-steps__number">4</span><span>Płatność</span></span>
        </nav>

        <section class="checkout-block" id="step-1">
          <div class="checkout-block__head">
            <span><span class="checkout-block__num">01</span><span class="checkout-block__title">Dane kontaktowe</span></span>
            <button type="button" class="checkout-block__edit js-checkout-edit">Zmień</button>
          </div>
          <p class="checkout-block__recap" data-live="1">Uzupełnione</p>
          <div class="checkout-block__body">
            <div class="form-row">
              <div class="form-group"><label class="form-label" for="fn">Imię <span class="req">*</span></label><input class="form-control" id="fn" type="text" autocomplete="given-name"></div>
              <div class="form-group"><label class="form-label" for="ln">Nazwisko <span class="req">*</span></label><input class="form-control" id="ln" type="text" autocomplete="family-name"></div>
            </div>
            <div class="form-group"><label class="form-label" for="em">Adres e-mail <span class="req">*</span></label><input class="form-control" id="em" type="email" autocomplete="email"><p class="form-hint">Na ten adres wyślemy potwierdzenie zamówienia.</p></div>
            <div class="form-check"><input class="form-check-input" type="checkbox" id="acc"><label class="form-check-label" for="acc">Załóż konto, aby szybciej składać kolejne zamówienia</label></div>
            <button type="button" class="btn btn--primary u-mt-md js-checkout-next" data-next="step-2" data-step="2">Dalej — adres dostawy</button>
          </div>
        </section>

        <section class="checkout-block checkout-block--pending" id="step-2">
          <div class="checkout-block__head">
            <span><span class="checkout-block__num">02</span><span class="checkout-block__title">Adres dostawy</span></span>
            <button type="button" class="checkout-block__edit js-checkout-edit">Zmień</button>
          </div>
          <p class="checkout-block__recap" data-live="1">Uzupełnione</p>
          <div class="checkout-block__body">
            <div class="form-group"><label class="form-label" for="st">Ulica i numer <span class="req">*</span></label><input class="form-control" id="st" type="text" autocomplete="street-address"></div>
            <div class="form-row">
              <div class="form-group"><label class="form-label" for="zp">Kod pocztowy <span class="req">*</span></label><input class="form-control" id="zp" type="text" inputmode="numeric" autocomplete="postal-code" placeholder="00-000"></div>
              <div class="form-group"><label class="form-label" for="ct">Miasto <span class="req">*</span></label><input class="form-control" id="ct" type="text" autocomplete="address-level2"></div>
            </div>
            <div class="form-row">
              <div class="form-group"><label class="form-label" for="cn">Kraj</label><select class="form-select" id="cn"><option>Polska</option><option>Niemcy</option><option>Czechy</option></select></div>
              <div class="form-group"><label class="form-label" for="ph">Telefon <span class="opt">(opcjonalne)</span></label><input class="form-control" id="ph" type="tel" autocomplete="tel"></div>
            </div>
            <div class="form-check"><input class="form-check-input" type="checkbox" id="inv"><label class="form-check-label" for="inv">Chcę fakturę VAT</label></div>
            <button type="button" class="btn btn--primary u-mt-md js-checkout-next" data-next="step-3" data-step="3">Dalej — dostawa</button>
          </div>
        </section>

        <section class="checkout-block checkout-block--pending" id="step-3">
          <div class="checkout-block__head">
            <span><span class="checkout-block__num">03</span><span class="checkout-block__title">Sposób dostawy</span></span>
            <button type="button" class="checkout-block__edit js-checkout-edit">Zmień</button>
          </div>
          <p class="checkout-block__recap" data-live="1">Wybrano</p>
          <div class="checkout-block__body">
            <label class="delivery-option__item">
              <input class="form-check-input" type="radio" name="ship" data-label="Kurier" checked>
              <span class="delivery-option__label">
                <span><span class="delivery-option__name">Przesyłka kurierska</span><span class="delivery-option__desc">Czas realizacji 2–7 dni roboczych</span></span>
                <span class="delivery-option__price num">18,00 zł</span>
              </span>
            </label>
            <label class="delivery-option__item">
              <input class="form-check-input" type="radio" name="ship" data-label="Punkt odbioru">
              <span class="delivery-option__label">
                <span><span class="delivery-option__name">Punkt odbioru / automat paczkowy</span><span class="delivery-option__desc">Czas realizacji 2–7 dni roboczych</span></span>
                <span class="delivery-option__price num">18,50 zł</span>
              </span>
            </label>
            <label class="delivery-option__item">
              <input class="form-check-input" type="radio" name="ship" data-label="UE">
              <span class="delivery-option__label">
                <span><span class="delivery-option__name">Wysyłka na terenie Unii Europejskiej</span><span class="delivery-option__desc">Czas realizacji do 14 dni roboczych</span></span>
                <span class="delivery-option__price num">—</span>
              </span>
            </label>
            <div class="form-group u-mt-md"><label class="form-label" for="note">Uwagi do zamówienia <span class="opt">(opcjonalne)</span></label><textarea class="form-control" id="note" rows="3"></textarea></div>
            <button type="button" class="btn btn--primary js-checkout-next" data-next="step-4" data-step="4">Dalej — płatność</button>
          </div>
        </section>

        <section class="checkout-block checkout-block--pending" id="step-4">
          <div class="checkout-block__head">
            <span><span class="checkout-block__num">04</span><span class="checkout-block__title">Płatność</span></span>
            <button type="button" class="checkout-block__edit js-checkout-edit">Zmień</button>
          </div>
          <div class="checkout-block__body">
            <label class="payment-option"><input class="form-check-input" type="radio" name="pay" checked><span>Szybki przelew online</span><span class="payment-option__logo"><i>Przelewy24</i><i>BLIK</i></span></label>
            <label class="payment-option"><input class="form-check-input" type="radio" name="pay"><span>Karta płatnicza</span><span class="payment-option__logo"><i>Visa</i><i>Mastercard</i></span></label>
            <label class="payment-option"><input class="form-check-input" type="radio" name="pay"><span>Płatność przy odbiorze</span><span class="payment-option__logo"><i>+ 5,00 zł</i></span></label>

            <div class="form-check u-mt-md"><input class="form-check-input" type="checkbox" id="terms"><label class="form-check-label" for="terms">Akceptuję <a href="regulamin.html">regulamin sklepu</a> i politykę prywatności <span class="req">*</span></label></div>
            <button type="button" class="btn btn--primary btn--lg btn--full u-mt-md" id="place-order">Zamawiam i płacę</button>
            <p class="form-hint" style="text-align:center">Prototyp — żadne dane nie są wysyłane ani zapisywane.</p>
          </div>
        </section>
      </div>

      <aside class="checkout-aside">
        <button type="button" class="checkout-aside__toggle" data-toggle aria-expanded="false">
          <span class="eyebrow">Podsumowanie zamówienia (<span id="checkout-count">0</span>)</span>
          <span id="checkout-total-mini" class="num" style="font-size:var(--fs-body)"></span>
        </button>
        <div class="checkout-aside__panel"><div>
          <div class="cart-summary">
            <div id="checkout-lines"></div>
            <div id="checkout-empty" class="blockcart-drawer__empty" style="padding-top:0" hidden>
              <p class="text-muted" style="font-size:var(--fs-sm)">Twój koszyk jest pusty — dodaj produkty, aby dokończyć zamówienie.</p>
              <a class="btn btn--outline btn--sm" href="nowa-kolekcja.html">Zobacz kolekcję</a>
            </div>
            <div class="cart-summary__line" style="margin-top:var(--space-sm)"><span>Wartość produktów</span><span id="checkout-subtotal">0,00 zł</span></div>
            <div class="cart-summary__line"><span>Dostawa</span><span id="checkout-shipping">Gratis</span></div>
            <div class="cart-summary__total"><span>Razem</span><strong id="checkout-total">0,00 zł</strong></div>
            <ul class="trust-row">
              <li>{ICON['lock']}Płatność szyfrowana SSL</li>
              <li>{ICON['return']}14 dni na zwrot</li>
            </ul>
          </div>
        </div></div>
      </aside>
    </div>
  </div>
</main>
<footer class="footer-min">
  <div class="container">
    <div class="footer-min__inner">
      <span>© 2026 — pic à bec · Peyote Sp. z o.o.</span>
      <nav class="footer-min__links" aria-label="Informacje">
        <a href="regulamin.html">Regulamin</a><a href="regulamin.html">Polityka prywatności</a>
        <a href="wysylka.html">Wysyłka</a><a href="zwroty-i-wymiany.html">Zwroty</a><a href="kontakt.html">Kontakt</a>
      </nav>
    </div>
  </div>
</footer>
""" + '<div id="overlay" class="overlay"></div><div class="toast" id="toast" role="status" aria-live="polite">' + ICON['check'] + '<span id="toast-text"></span></div>' + FOOT_JS


def build_confirmation():
    return head("Dziękujemy za zamówienie — pic à bec", "page-confirmation") + header() + f"""
<main id="main-content" class="wrapper">
  <div class="container container--narrow">
    <div style="padding-block:clamp(3rem,7vw,6rem);text-align:center;display:grid;gap:var(--space-sm);justify-items:center">
      <span class="btn-icon" style="width:56px;height:56px;border:1px solid var(--color-line-strong)">{ICON['check']}</span>
      <span class="eyebrow">Zamówienie przyjęte</span>
      <h1>Dziękujemy za zamówienie</h1>
      <p class="lede" style="text-align:center">Potwierdzenie wysłaliśmy na podany adres e-mail. Czas realizacji wynosi od 2 do 7 dni roboczych.</p>
      <p class="text-muted num" style="font-size:var(--fs-sm)">Numer zamówienia: PAB-2026-0417</p>
      <div class="u-flex u-gap-sm u-wrap" style="justify-content:center;margin-top:var(--space-sm)">
        <a class="btn btn--primary" href="account.html">Moje zamówienia</a>
        <a class="btn btn--outline" href="index.html">Wróć na stronę główną</a>
      </div>
    </div>
  </div>
</main>
""" + footer() + mobile_panel() + FOOT_JS


# ===========================================================================
# LOGIN / ACCOUNT
# ===========================================================================
def build_login():
    return head("Logowanie — pic à bec", "page-authentication") + header() + breadcrumb(
        [("Strona główna", "index.html"), ("Logowanie", "#")]) + f"""
<main id="main-content" class="wrapper">
  <div class="container">
    <div class="auth-grid login">
      <div class="auth-card">
        <span class="eyebrow">Klienci powracający</span>
        <h1 class="auth-card__title" style="margin-top:var(--space-2xs)">Zaloguj się</h1>
        <p class="auth-card__intro">Zaloguj się, aby zobaczyć historię zamówień, adresy i zapisane produkty.</p>
        <form onsubmit="return false">
          <div class="form-group">
            <label class="form-label" for="login-mail">Adres e-mail</label>
            <input class="form-control" id="login-mail" type="email" autocomplete="email" placeholder="jan.kowalski@example.com">
          </div>
          <div class="form-group">
            <label class="form-label" for="login-pass">Hasło</label>
            <span class="password-field">
              <input class="form-control" id="login-pass" type="password" autocomplete="current-password">
              <button type="button" class="toggle-pw" onclick="var i=document.getElementById('login-pass');i.type=i.type==='password'?'text':'password';this.textContent=i.type==='password'?'Pokaż':'Ukryj'">Pokaż</button>
            </span>
          </div>
          <div class="auth-card__row">
            <div class="form-check"><input class="form-check-input" type="checkbox" id="remember"><label class="form-check-label" for="remember">Zapamiętaj mnie</label></div>
            <a class="auth-card__forgot" href="#">Nie pamiętasz hasła?</a>
          </div>
          <a class="btn btn--primary btn--full btn--lg" href="account.html" id="submit-login">Zaloguj się</a>
        </form>
      </div>

      <div class="auth-card login__register-prompt">
        <span class="eyebrow">Nowy klient</span>
        <h2 style="margin-top:var(--space-2xs)">Załóż konto</h2>
        <p class="auth-card__intro">Szybsze zakupy, historia zamówień i zapisane adresy dostawy. Rejestracja zajmuje minutę.</p>
        <ul class="editorial__list" style="margin-top:0">
          <li><span>01</span><span>Historia i status zamówień</span></li>
          <li><span>02</span><span>Zapisane adresy dostawy</span></li>
          <li><span>03</span><span>Szybsza kasa przy kolejnych zakupach</span></li>
        </ul>
        <a class="btn btn--outline btn--lg u-mt-lg" href="account.html">Utwórz konto</a>
        <p class="form-hint u-mt-md">Kontynuując, akceptujesz <a href="regulamin.html" style="text-decoration:underline">regulamin sklepu</a>.</p>
      </div>
    </div>
  </div>
</main>
""" + footer() + mobile_panel() + FOOT_JS


def build_account():
    return head("Moje konto — pic à bec", "page-my-account") + header() + breadcrumb(
        [("Strona główna", "index.html"), ("Moje konto", "#")]) + f"""
<main id="main-content" class="wrapper">
  <div class="container">
    <div style="padding-block:clamp(1.5rem,3vw,2.5rem) 0">
      <span class="eyebrow">Konto</span>
      <h1 class="page-title-section" style="margin-top:var(--space-2xs)">Dzień dobry, Anno</h1>
    </div>

    <div class="account-grid">
      <nav class="account-menu" aria-label="Menu konta">
        <div class="account-menu__nav">
          <a href="account.html" class="account-menu__link--active">Pulpit</a>
          <a href="account.html">Zamówienia</a>
          <a href="account.html">Adresy</a>
          <a href="account.html">Dane osobowe</a>
          <a href="account.html">Ulubione</a>
          <a href="account.html">Zwroty</a>
          <a href="login.html">Wyloguj się</a>
        </div>
      </nav>

      <div>
        <div class="account-cards">
          <div class="account-card">
            <span class="account-card__title">Dane kontaktowe</span>
            <p>Anna Kowalska<br>anna.kowalska@example.com</p>
            <a class="link-underline" href="#">Edytuj dane</a>
          </div>
          <div class="account-card">
            <span class="account-card__title">Domyślny adres</span>
            <p>ul. Golfowa 1a<br>43-190 Mikołów, Polska</p>
            <a class="link-underline" href="#">Zarządzaj adresami</a>
          </div>
        </div>

        <h2 class="h3 u-mt-lg u-mb-md">Ostatnie zamówienia</h2>
        <div class="order-table-wrap"><table class="order-table">
          <thead><tr><th>Numer</th><th>Data</th><th>Status</th><th>Kwota</th><th></th></tr></thead>
          <tbody>
            <tr><td>PAB-2026-0417</td><td>12.08.2026</td><td><span class="order-status__badge">W realizacji</span></td><td>1 600,00 zł</td><td><a class="link-underline" href="#">Szczegóły</a></td></tr>
            <tr><td>PAB-2026-0388</td><td>28.07.2026</td><td><span class="order-status__badge">Dostarczone</span></td><td>460,00 zł</td><td><a class="link-underline" href="#">Szczegóły</a></td></tr>
            <tr><td>PAB-2026-0341</td><td>03.07.2026</td><td><span class="order-status__badge">Zwrócone</span></td><td>140,00 zł</td><td><a class="link-underline" href="#">Szczegóły</a></td></tr>
          </tbody>
        </table></div>
        <p class="form-hint u-mt-md">Prototyp — dane zamówień są przykładowe i służą wyłącznie prezentacji układu.</p>
      </div>
    </div>
  </div>
</main>
""" + footer() + mobile_panel() + FOOT_JS
