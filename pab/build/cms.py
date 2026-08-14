# -*- coding: utf-8 -*-
"""CMS + contact pages. All copy verbatim from the live store."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import BASE, BY_KEY
from build import head, header, footer, mobile_panel, breadcrumb, ICON, FOOT_JS, cover, BENEFITS

ABOUT_IMG = BASE + "/img/cms/2026_03_16_pica_bec5649.jpg"


def cms_page(fname, title, eyebrow, lede, toc, body, crumb_label):
    toc_html = "".join(f'<a href="#{i}">{l}</a>' for i, l in toc)
    return head(f"{title} — pic à bec", "page-cms") + header() + breadcrumb(
        [("Strona główna", "index.html"), (crumb_label, "#")]) + f"""
<main id="main-content" class="wrapper">
  <section class="page-hero">
    <div class="container">
      <div class="page-hero__grid">
        <div><span class="eyebrow">{eyebrow}</span><h1 style="margin-top:var(--space-2xs)">{title}</h1></div>
        <div><p class="lede">{lede}</p></div>
      </div>
    </div>
  </section>
  <div class="container">
    <div class="cms-layout">
      <nav class="cms-toc" aria-label="Spis treści"><span class="eyebrow" style="margin-bottom:var(--space-2xs);display:block">Na tej stronie</span>{toc_html}</nav>
      <div class="rte">{body}</div>
    </div>
  </div>
</main>
""" + footer() + mobile_panel() + FOOT_JS


def build_about():
    body = f"""
<h2 id="marka">O marce</h2>
<p>pic a bec to marka odzieżowa inspirowana światem golfa, łącząca elegancję, funkcjonalność i nowoczesny minimalizm.</p>
<p>Tworzymy ubrania, które sprawdzają się zarówno na polu golfowym, jak i na co dzień. Stawiamy na jakość materiałów, dopracowane kroje i ponadczasowy charakter kolekcji — dla osób, które cenią komfort i estetykę.</p>

<figure style="margin:var(--space-lg) 0">
  <span class="imgframe imgframe--wide"><img src="{ABOUT_IMG}" alt="pic à bec — kampania marki" loading="lazy" decoding="async"></span>
</figure>

<h2 id="wyroznia">Co nas wyróżnia</h2>
<ul>
  <li>Styl inspirowany golfem</li>
  <li>Ponadczasowe sylwetki</li>
  <li>Wysoka jakość wykonania</li>
  <li>Komfort i funkcjonalność</li>
</ul>

<h2 id="dla-kogo">Dla kogo</h2>
<p>Dla osób, które chcą wyglądać dobrze bez przesady – na polu golfowym i poza nim.</p>

<h2 id="kolekcja">Kolekcja</h2>
<p>Każdego sezonu kolekcja pic a bec czerpie z klasycznych elementów garderoby, właśnie takich jak koszule damskie. Ich fundamentem są wysokiej jakości materiały – między innymi bawełna, jedwab czy len – a także podkreślające atuty sylwetki kroje w różnych wydaniach: od bardziej luźnych modeli do podkreślających talię eleganckich koszul. Nasza kolekcja to zbiór nigdy niewychodzących z mody neutralnych odcieni bieli, czerni i beżu, a także sezonowych, intensywnych kolorów, które przypieczętują adekwatnie skomponowaną garderobę.</p>
<p style="margin-top:var(--space-lg)"><a class="btn btn--outline" href="nowa-kolekcja.html">Zobacz nową kolekcję</a></p>
"""
    return cms_page("o-nas.html", "O nas", "Marka",
                    "pic a bec to marka odzieżowa inspirowana światem golfa, łącząca elegancję, funkcjonalność i nowoczesny minimalizm.",
                    [("marka", "O marce"), ("wyroznia", "Co nas wyróżnia"), ("dla-kogo", "Dla kogo"), ("kolekcja", "Kolekcja")],
                    body, "O nas")


def build_shipping():
    body = """
<h2 id="kurier">Przesyłka kurierska</h2>
<p>Przesyłki na terenie RP realizowane są za pośrednictwem przykładowej firmy kurierskiej.</p>
<p>Czas realizacji zamówień wynosi od 2 do 7 dni roboczych.</p>
<p>Koszt standardowej przesyłki kurierskiej wynosi 18 zł.</p>

<h2 id="punkt">Punkt odbioru i automat paczkowy</h2>
<p>Przesyłki na terenie RP realizowane są również za pośrednictwem przykładowej firmy kurierskiej.</p>
<p>Czas realizacji zamówień wynosi od 2 do 7 dni roboczych.</p>
<p>Koszt standardowej przesyłki do punktu odbioru lub automatu paczkowego wynosi 18,50 zł.</p>

<h2 id="ue">Przesyłki międzynarodowe</h2>
<p>Przesyłki międzynarodowe na terenie krajów Unii Europejskiej realizowane są za pośrednictwem przykładowej firmy kurierskiej.</p>
<p>Czas realizacji zamówień wynosi do 14 dni roboczych.</p>
<p style="margin-top:var(--space-lg)"><a class="btn btn--outline" href="zwroty-i-wymiany.html">Zwroty i wymiany</a></p>
"""
    return cms_page("wysylka.html", "Wysyłka", "Obsługa klienta",
                    "Czas realizacji zamówień wynosi od 2 do 7 dni roboczych. Przesyłki międzynarodowe na terenie Unii Europejskiej — do 14 dni roboczych.",
                    [("kurier", "Przesyłka kurierska"), ("punkt", "Punkt odbioru"), ("ue", "Przesyłki międzynarodowe")],
                    body, "Wysyłka")


def build_returns():
    body = """
<p class="lede" style="margin-bottom:var(--space-lg)">W pic a bec zależy nam, aby każdy zakup spełniał oczekiwania naszych klientów. Jeżeli zamówiony produkt nie odpowiada pod względem rozmiaru, fasonu lub koloru, możesz skorzystać z możliwości zwrotu lub wymiany.</p>

<h2 id="zwrot">1. Zwrot produktów</h2>
<p>Klient ma prawo odstąpić od umowy i zwrócić zakupiony produkt w terminie 14 dni od dnia otrzymania przesyłki bez podawania przyczyny.</p>
<p>Aby dokonać zwrotu:</p>
<ul>
  <li>wypełnij formularz zwrotu lub prześlij informację drogą e-mail,</li>
  <li>zapakuj produkt w bezpieczny sposób,</li>
  <li>odeślij przesyłkę na adres wskazany przez sklep.</li>
</ul>
<p>Zwrot środków zostanie wykonany w terminie do 14 dni od momentu otrzymania i zaakceptowania zwrotu.</p>

<h2 id="warunki">2. Warunki zwrotu</h2>
<p>Zwracany produkt powinien:</p>
<ul>
  <li>być nieużywany,</li>
  <li>nie posiadać śladów użytkowania,</li>
  <li>posiadać oryginalne metki i oznaczenia,</li>
  <li>zostać odesłany w możliwie oryginalnym opakowaniu.</li>
</ul>
<p>Sklep zastrzega sobie możliwość odmowy przyjęcia zwrotu w przypadku produktów noszących ślady użytkowania lub uszkodzeń powstałych po stronie klienta.</p>

<h2 id="wymiana">3. Wymiana produktów</h2>
<p>Istnieje możliwość wymiany produktu na inny rozmiar lub kolor, jeżeli wybrany wariant jest dostępny w magazynie. W celu dokonania wymiany prosimy o wcześniejszy kontakt ze sklepem drogą e-mail.</p>
<ul>
  <li>wymiana realizowana jest po otrzymaniu zwracanego produktu,</li>
  <li>czas realizacji wymiany zależy od dostępności produktów,</li>
  <li>w przypadku braku dostępności możliwy jest zwrot środków.</li>
</ul>

<h2 id="koszty">4. Koszty przesyłki</h2>
<p>Koszt odesłania produktu do sklepu pokrywa klient, chyba że zwrot lub reklamacja wynika z błędu po stronie sklepu. Koszt ponownej wysyłki przy wymianie może zostać naliczony zgodnie z aktualnym cennikiem dostawy.</p>

<h2 id="reklamacje">5. Produkty uszkodzone lub niezgodne z zamówieniem</h2>
<p>Jeżeli otrzymany produkt posiada wadę lub jest niezgodny z zamówieniem, prosimy o kontakt ze sklepem w celu zgłoszenia reklamacji. W zgłoszeniu warto podać:</p>
<ul>
  <li>numer zamówienia,</li>
  <li>opis problemu,</li>
  <li>zdjęcia produktu, jeśli to możliwe.</li>
</ul>
<p>Każda reklamacja rozpatrywana jest indywidualnie zgodnie z obowiązującymi przepisami prawa.</p>

<h2 id="kontakt">6. Kontakt</h2>
<p>W sprawach dotyczących zwrotów, wymian i reklamacji prosimy o kontakt przez <a href="kontakt.html">formularz kontaktowy</a>.</p>
"""
    return cms_page("zwroty-i-wymiany.html", "Zwroty i wymiany", "Obsługa klienta",
                    "Masz 14 dni na odstąpienie od umowy bez podawania przyczyny. Wymiana na inny rozmiar lub kolor jest możliwa, jeśli wariant jest dostępny w magazynie.",
                    [("zwrot", "Zwrot produktów"), ("warunki", "Warunki zwrotu"), ("wymiana", "Wymiana produktów"),
                     ("koszty", "Koszty przesyłki"), ("reklamacje", "Produkty uszkodzone"), ("kontakt", "Kontakt")],
                    body, "Zwroty i wymiany")


def build_terms():
    body = """
<h2 id="regulamin">Regulamin Sklepu Internetowego Pic à Bec</h2>
<p>Regulamin określa warunki i zasady sprzedaży prowadzonej za pośrednictwem sklepu internetowego www.picabec.com oraz zasady świadczenia usług nieodpłatnych drogą elektroniczną.</p>
<p>Sklep prowadzi Peyote Sp. z o.o. z siedzibą w Jankach, ul. Mszczonowska 48, 05-090 Raszyn, Polska, wpisana do rejestru przedsiębiorców KRS pod numerem 0001010721, NIP 5342658923, właściciel marki Pic à Bec.</p>

<h2 id="spis">Spis treści</h2>
<ul>
  <li>§ 1 Definicje</li>
  <li>§ 2 Zasady korzystania ze Sklepu</li>
  <li>§ 3 Rejestracja Konta</li>
  <li>§ 4 Zamówienia</li>
  <li>§ 5 Płatność i Dostawa</li>
  <li>§ 6 Reklamacje</li>
  <li>§ 7 Odstąpienie od Umowy</li>
  <li>§ 8 Newsletter</li>
  <li>§ 9 Dane osobowe</li>
  <li>§ 10 Postanowienia końcowe</li>
</ul>

<h2 id="prywatnosc">Polityka prywatności</h2>
<p>Administratorem danych osobowych jest Peyote Sp. z o.o., ul. Mszczonowska 48, 05-090 Raszyn, Polska, KRS 0001010721, NIP 5342658923, e-mail customercare@picabec.com.</p>
<h3>Cele i podstawa prawna przetwarzania danych osobowych</h3>
<h3>Zakupy i usługi online</h3>

<h2 id="cookies">Polityka cookies</h2>
<ul>
  <li>Czym są pliki cookies</li>
  <li>Rodzaje cookies — niezbędne, funkcjonalne, personalizacyjne, analityczne, marketingowe</li>
  <li>Zarządzanie cookies</li>
  <li>Usuwanie plików cookies</li>
  <li>Cookies dostawców zewnętrznych</li>
  <li>Użytkownicy z innych państw</li>
  <li>Postanowienia końcowe</li>
</ul>
"""
    return cms_page("regulamin.html", "Regulamin i polityki", "Informacje prawne",
                    "Regulamin określa warunki i zasady sprzedaży prowadzonej za pośrednictwem sklepu internetowego oraz zasady świadczenia usług nieodpłatnych drogą elektroniczną.",
                    [("regulamin", "Regulamin"), ("spis", "Spis treści"), ("prywatnosc", "Polityka prywatności"), ("cookies", "Polityka cookies")],
                    body, "Regulamin")


def build_contact():
    return head("Kontakt z nami — pic à bec", "page-contact") + header() + breadcrumb(
        [("Strona główna", "index.html"), ("Kontakt", "#")]) + f"""
<main id="main-content" class="wrapper">
  <section class="page-hero">
    <div class="container">
      <div class="page-hero__grid">
        <div><span class="eyebrow">Obsługa klienta</span><h1 style="margin-top:var(--space-2xs)">Kontakt z nami</h1></div>
        <div><p class="lede">Odpowiadamy od poniedziałku do piątku, w godzinach 09:00–17:00. Zwykle w ciągu jednego dnia roboczego.</p></div>
      </div>
    </div>
  </section>

  <div class="container">
    <div class="contact-pic">
      <div class="contact-pic__info">
        <div class="contact-pic__info-col">
          <span class="eyebrow">Adres</span>
          <p class="contact-pic__info-text">Pic à bec<br>Ulica Golfowa 1a<br>43-190 Mikołów<br>Polska</p>
        </div>
        <div class="contact-pic__info-col">
          <span class="eyebrow">Infolinia</span>
          <p class="contact-pic__info-text"><a href="tel:123432555">123-432-555</a><br>Pon. – pt. 09:00 – 17:00</p>
        </div>
        <div class="contact-pic__info-col">
          <span class="eyebrow">E-mail</span>
          <p class="contact-pic__info-text"><a href="mailto:customerservice.eu@picabec.com">customerservice.eu@picabec.com</a></p>
        </div>
        <div class="contact-pic__info-col">
          <span class="eyebrow">Dane rejestrowe</span>
          <p class="contact-pic__info-text">Peyote Sp. z o.o.<br>ul. Mszczonowska 48, 05-090 Raszyn<br>KRS 0001010721 · NIP 5342658923</p>
        </div>
        <div class="contact-pic__info-col">
          <span class="eyebrow">Pomoc</span>
          <p class="contact-pic__info-text"><a href="wysylka.html" class="link-underline" style="letter-spacing:0;text-transform:none;font-size:var(--fs-sm)">Wysyłka</a> · <a href="zwroty-i-wymiany.html" class="link-underline" style="letter-spacing:0;text-transform:none;font-size:var(--fs-sm)">Zwroty i wymiany</a></p>
        </div>
      </div>

      <div class="contact-pic__form-col">
        <h2 class="contact-pic__form-title">Formularz kontaktowy</h2>
        <form onsubmit="return false">
          <div class="form-group">
            <label class="form-label" for="topic">Temat <span class="req">*</span></label>
            <select class="form-select" id="topic"><option>Biuro Obsługi Klienta</option><option>Webmaster</option></select>
          </div>
          <div class="form-group">
            <label class="form-label" for="cmail">Adres e-mail <span class="req">*</span></label>
            <input class="form-control" id="cmail" type="email" autocomplete="email">
          </div>
          <div class="form-group">
            <label class="form-label" for="corder">Numer zamówienia <span class="opt">(opcjonalne)</span></label>
            <input class="form-control" id="corder" type="text" placeholder="PAB-2026-0000">
          </div>
          <div class="form-group">
            <label class="form-label" for="cmsg">Wiadomość <span class="req">*</span></label>
            <textarea class="form-control" id="cmsg" rows="6"></textarea>
          </div>
          <div class="form-check u-mb-md">
            <input class="form-check-input" type="checkbox" id="cconsent">
            <label class="form-check-label" for="cconsent">Zapoznałam/em się z <a href="regulamin.html">polityką prywatności</a>. <span class="req">*</span></label>
          </div>
          <button class="btn btn--primary btn--lg" type="submit">Wyślij wiadomość</button>
        </form>
      </div>
    </div>
  </div>
</main>
""" + footer() + mobile_panel() + FOOT_JS
