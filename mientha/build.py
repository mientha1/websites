# -*- coding: utf-8 -*-
"""Mientha corporate site generator -> self-contained bilingual HTML pages."""
import os, pathlib

ROOT = pathlib.Path(__file__).parent
CSS = (ROOT/"assets"/"style.css").read_text(encoding="utf-8")
JS  = (ROOT/"assets"/"app.js").read_text(encoding="utf-8")

# ----------------------------------------------------------------- brand + icons
# Real Mientha logo extracted from the official vector files (RGB GRANAT).
import re as _re
_raw = (ROOT/"assets"/"logo_granat.svg").read_text(encoding="utf-8")
_inner = _re.sub(r'^.*?<svg[^>]*>', '', _raw, flags=_re.S).replace('</svg>', '').strip()
_VB = "84 234 676 128"   # tight crop of the logo artwork
_NAVY_FILL = "rgb(10.598755%, 0%, 41.598511%)"
def _logo(cls, wordmark=None, label="Mientha"):
    body = _inner if not wordmark else _inner.replace(_NAVY_FILL, wordmark)
    return (f'<svg class="{cls}" viewBox="{_VB}" role="img" aria-label="{label}" '
            f'preserveAspectRatio="xMinYMid meet">{body}</svg>')
LOGO       = _logo("brand__logo")                       # header: navy wordmark + mint mark
LOGO_LIGHT = _logo("brand__logo", "rgb(255,255,255)")   # footer: white wordmark on dark

I = {
 "automation":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="7" width="16" height="12" rx="2"/><path d="M9 7V5h6v2M9 12h.01M15 12h.01M12 3v2"/><path d="M8 16h8"/></svg>',
 "agent":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1"/></svg>',
 "bpo":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a9 9 0 1 1-3.5-7.1"/><path d="M21 4v5h-5"/><path d="M12 8v4l2.5 1.5"/></svg>',
 "ams":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/><path d="M7 9l2 2 3-4 2 3 3-2"/></svg>',
 "talent":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="8" r="3"/><path d="M4 20c0-3 2.5-5 5-5s5 2 5 5"/><path d="M17 8l2 2 3-3"/></svg>',
 "custom":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M14 4l6 6-9 9H5v-6z"/><path d="M12 6l6 6"/></svg>',
 "transport":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 6h11v10H3z"/><path d="M14 9h4l3 3v4h-7z"/><circle cx="7" cy="18" r="1.6"/><circle cx="17.5" cy="18" r="1.6"/></svg>',
 "factory":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 20V9l6 4V9l6 4V6l6 0v14z"/><path d="M3 20h18"/></svg>',
 "cart":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="20" r="1.5"/><circle cx="17" cy="20" r="1.5"/><path d="M3 4h2l2.4 12.3a1 1 0 0 0 1 .7h8.2a1 1 0 0 0 1-.8L21 8H6"/></svg>',
 "car":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M5 16l1.5-5A2 2 0 0 1 8.4 9.6h7.2a2 2 0 0 1 1.9 1.4L19 16"/><path d="M4 16h16v3h-3v-2H7v2H4z"/><circle cx="7.5" cy="16" r="0.5"/><circle cx="16.5" cy="16" r="0.5"/></svg>',
 "bank":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10l9-6 9 6"/><path d="M5 10v8M10 10v8M14 10v8M19 10v8M3 20h18"/></svg>',
 "telecom":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 18h.01"/><path d="M8.5 14.5a5 5 0 0 1 7 0M5.5 11.5a9 9 0 0 1 13 0"/></svg>',
 "health":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M20 8.5C20 5.5 17.8 4 15.8 4 14 4 12 5.5 12 5.5S10 4 8.2 4C6.2 4 4 5.5 4 8.5c0 5 8 11 8 11s8-6 8-11z"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M4 7l8 6 8-6"/></svg>',
 "tel":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h3l2 5-2.5 1.5a12 12 0 0 0 5 5L16 12l5 2v3a2 2 0 0 1-2 2A16 16 0 0 1 4 5a2 2 0 0 1 2-2z"/></svg>',
 "pin":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 21s7-6 7-11a7 7 0 1 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.4"/></svg>',
 "arrow":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "clock":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 "shield":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/></svg>',
 "chart":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M4 20V4M4 20h16"/><path d="M8 16l3-4 3 2 4-6"/></svg>',
 "globe":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18"/></svg>',
 "layers":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5M3 17l9 5 9-5"/></svg>',
 "plug":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3v6M15 3v6M6 9h12v3a6 6 0 0 1-12 0z"/><path d="M12 18v3"/></svg>',
 "doc":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 13h6M9 17h6"/></svg>',
 "spark":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/></svg>',
 "bubble":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12a8 8 0 0 1-8 8H5l-2 2V12a8 8 0 0 1 8-8h2a8 8 0 0 1 8 8z"/><path d="M8.5 12h.01M12 12h.01M15.5 12h.01"/></svg>',
}

DECO_TRI = '<svg class="deco" width="150" height="130" viewBox="0 0 150 130" fill="none"><path d="M75 12 L138 118 L12 118 Z" stroke="#18cf98" stroke-width="2" opacity=".55"/></svg>'
DECO_CHECK = '<svg class="deco" width="220" height="150" viewBox="0 0 220 150" fill="none"><path d="M20 70 L70 120 L200 20" stroke="#141436" stroke-width="2" opacity=".18" stroke-linecap="round" stroke-linejoin="round"/></svg>'

import base64 as _b64
def _datauri(fn):
    return "data:image/png;base64," + _b64.b64encode((ROOT/"assets"/fn).read_bytes()).decode()
UIPATH_LOCKUP   = _datauri("uipath-authorized-b.png")   # black lockup — light backgrounds
UIPATH_LOCKUP_W = _datauri("uipath-authorized-w.png")   # white lockup — dark backgrounds
try:
    import de_data
    DE_BY_EN = de_data.DE_BY_EN
    DE_TITLE_BY_EN = de_data.DE_TITLE_BY_EN
except Exception:
    DE_BY_EN = {}
    DE_TITLE_BY_EN = {}

_PL_SEEN = {}
def dual(pl, en, tag="span", cls=""):
    _PL_SEEN[pl] = en
    c = (" "+cls) if cls else ""
    de = DE_BY_EN.get(en, en)
    return (f'<{tag} class="pl{c}">{pl}</{tag}>'
            f'<{tag} class="en{c}">{en}</{tag}>'
            f'<{tag} class="de{c}">{de}</{tag}>')

def _checklist(items):
    return '<ul class="checklist">' + "".join(f'<li>{dual(a,b)}</li>' for a,b in items) + '</ul>'

def tri(pl, en, de, tag="span", cls=""):
    """Trilingual span with explicit German (used for chat mock copy)."""
    c = (" "+cls) if cls else ""
    return (f'<{tag} class="pl{c}">{pl}</{tag}>'
            f'<{tag} class="en{c}">{en}</{tag}>'
            f'<{tag} class="de{c}">{de}</{tag}>')

def chat(title, time, msgs, who=("Asystent Mienthy · Agent AI","Mientha Assistant · AI agent","Mientha-Assistent · KI-Agent")):
    """Teams-style conversation mock. msgs: list of (role, pl, en, de)."""
    body=""; shown=False
    for role,pl,en,de in msgs:
        if role=="agent" and not shown:
            body += f'<span class="msg__who">{tri(*who)}</span>'
            shown=True
        body += f'<div class="msg msg--{role}">{tri(pl,en,de)}</div>'
    return f'''<div class="chat" aria-label="Microsoft Teams">
      <div class="chat__bar"><span class="chat__dot"></span><b>{tri(*title)}</b><time>{time}</time></div>
      <div class="chat__body">{body}</div>
    </div>'''

# ----------------------------------------------------------------- nav / footer
# industries & services used both in the mega-menu and (optionally) on pages
INDUSTRIES = [
 ("transport","transport-spedycja.html","Transport i spedycja","Transport & logistics","Rozliczanie kierowców, integracja z TMS/ERP.","Driver settlement, TMS/ERP integration.",True),
 ("cart","fmcg.html","FMCG i retail","FMCG & retail","10+ wdrożonych automatyzacji — zobacz case studies.","10+ automations delivered — see case studies.",False),
 ("factory","branze.html#produkcja","Produkcja","Manufacturing","Procesy operacyjne i zakupowe, AMS.","Operations, procurement, AMS.",False),
 ("bank","branze.html#finanse","Finanse i BSS","Finance & shared services","P2P/O2C, zgodność, raporty KPI.","P2P/O2C, compliance, KPI reporting.",False),
 ("telecom","branze.html#telekomunikacja","Telekomunikacja","Telecom","Back-office, wsparcie aplikacji, zespoły IT.","Back-office, app support, IT teams.",False),
 ("car","branze.html#automotive","Automotive","Automotive","Łańcuch dostaw, finanse, eksperci IT.","Supply chain, finance, IT experts.",False),
]
SERVICES = [
 ("automation","uslugi.html#rpa","Automatyzacja RPA i Agentic AI","RPA & Agentic AI","Roboty i agenci AI dla powtarzalnych procesów.","Robots and AI agents for repetitive processes."),
 ("bpo","uslugi.html#bpo","Business Process Outsourcing","Business Process Outsourcing","Przejmujemy i optymalizujemy procesy.","We take over and optimise processes."),
 ("ams","wsparcie-247.html","Wsparcie 24/7 i AMS","24/7 support & AMS","Całodobowe wsparcie aplikacji krytycznych.","24/7 support for critical applications."),
 ("talent","uslugi.html#talent","Eksperci i rekrutacja IT","IT experts & talent","Zespoły i specjaliści IT oraz finansowi.","IT and finance teams and specialists."),
 ("custom","uslugi.html#custom","Rozwiązania szyte na miarę","Custom solutions","Dedykowane produkty i integracje.","Dedicated products and integrations."),
 ("bubble","agenty.html","Rozwiązania agentyczne","Agentic solutions","Asystent zarządu i agenci na Teams — case studies.","Executive assistant and agents on Teams — case studies."),
]

CARET = '<svg class="caret" viewBox="0 0 12 12" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2.5 4.5 6 8l3.5-3.5"/></svg>'

def _mega_item(icon,href,t_pl,t_en,d_pl,d_en):
    return (f'<a class="mega__item" href="{href}"><span class="mega__ico">{I[icon]}</span>'
            f'<span class="mega__tx"><b>{dual(t_pl,t_en)}</b>{dual(d_pl,d_en,cls="mega__d")}</span></a>')

def mega_branze():
    items = "".join(_mega_item(ic,hr,tp,te,dp,de) for ic,hr,tp,te,dp,de,_f in INDUSTRIES)
    return f'''<div class="megamenu" role="menu"><div class="megamenu__inner container">
      <div class="mega__feature">
        <span class="tag">{dual("Produkt flagowy","Flagship")}</span>
        <h4>{dual("Rozliczanie kierowców","Driver settlement")}</h4>
        <p>{dual("Automatyczne rozliczanie kierowców dla transportu i spedycji — od danych po listy płac.","Automated driver settlement for transport & logistics — from data to payroll.")}</p>
        <a href="transport-spedycja.html" class="btn btn--mint">{dual("Zobacz rozwiązanie","View solution")} {I["arrow"]}</a>
      </div>
      <div class="mega__grid">{items}</div>
    </div></div>'''

def mega_uslugi():
    items = "".join(_mega_item(ic,hr,tp,te,dp,de) for ic,hr,tp,te,dp,de in SERVICES)
    return f'''<div class="megamenu" role="menu"><div class="megamenu__inner container">
      <div class="mega__feature">
        <span class="tag">{dual("Usługi","Services")}</span>
        <h4>{dual("Kompleksowe wsparcie","End-to-end support")}</h4>
        <p>{dual("Od automatyzacji i outsourcingu po zespoły ekspertów IT — z gwarancją najlepszej oferty.","From automation and outsourcing to IT expert teams — with a best-offer guarantee.")}</p>
        <a href="uslugi.html" class="arrowlink">{dual("Wszystkie usługi","All services")} {I["arrow"]}</a>
      </div>
      <div class="mega__grid">{items}</div>
    </div></div>'''

NAV_ITEMS = [
    ("index.html","Start","Home",None),
    ("uslugi.html","Usługi","Services","uslugi"),
    ("branze.html","Branże","Industries","branze"),
    ("case-studies.html","Case studies","Case studies",None),
    ("o-nas.html","O nas","About",None),
    ("kontakt.html","Kontakt","Contact",None),
]

def nav(active):
    desk = ""
    mob = ""
    for href,pl,en,mega in NAV_ITEMS:
        act = " active" if href==active else ""
        if mega:
            panel = mega_branze() if mega=="branze" else mega_uslugi()
            src = INDUSTRIES if mega=="branze" else SERVICES
            desk += (f'<div class="nav__item"><a href="{href}" class="nav__link nav__link--top{act}" '
                     f'aria-haspopup="true">{dual(pl,en)}{CARET}</a>{panel}</div>')
            ch = f'<a class="m-all" href="{href}">{dual("Wszystkie","View all")} · {dual(pl,en)}</a>'
            for it in src:
                ch += f'<a href="{it[1]}">{dual(it[2],it[3])}</a>'
            mob += (f'<div class="m-group"><button class="m-group__t" type="button">'
                    f'{dual(pl,en)}{CARET}</button><div class="m-group__p">{ch}</div></div>')
        else:
            desk += f'<a href="{href}" class="nav__link{act}">{dual(pl,en)}</a>'
            mob  += f'<a class="m-link" href="{href}">{dual(pl,en)}</a>'
    cta = dual("Umów rozmowę","Book a call")
    return f'''<header class="site-header">
  <div class="container">
    <nav class="nav">
      <a href="index.html" class="brand" aria-label="Mientha">{LOGO}</a>
      <div class="nav__links">{desk}</div>
      <div class="nav__right">
        <div class="langtoggle" role="group" aria-label="Language">
          <button data-lang="pl" type="button">PL</button>
          <button data-lang="en" type="button">EN</button>
          <button data-lang="de" type="button">DE</button>
        </div>
        <a href="kontakt.html" class="btn btn--mint cta-btn">{cta}</a>
        <button class="nav__toggle" aria-label="Menu" aria-expanded="false" type="button">
          <span class="burger"><span></span><span></span><span></span></span>
        </button>
      </div>
    </nav>
    <div class="mobile-menu">{mob}<a class="m-cta btn btn--mint" href="kontakt.html">{cta}</a></div>
  </div>
</header>'''

def footer():
    col_serv = "".join(f'<li><a href="{href}">{dual(pl,en)}</a></li>' for href,pl,en in [
        ("agenty.html","Rozwiązania agentyczne","Agentic solutions"),
        ("uslugi.html","Automatyzacja RPA i Agentic AI","RPA & Agentic AI automation"),
        ("uslugi.html","Business Process Outsourcing","Business Process Outsourcing"),
        ("wsparcie-247.html","Wsparcie 24/7 i AMS","24/7 support & AMS"),
        ("uslugi.html","Rekrutacja i eksperci IT","Talent & IT experts"),
    ])
    col_ind = "".join(f'<li><a href="branze.html">{dual(pl,en)}</a></li>' for pl,en in [
        ("Transport i spedycja","Transport & logistics"),
        ("FMCG i retail","FMCG & retail"),
        ("Produkcja","Manufacturing"),
        ("Finanse i BSS","Finance & shared services"),
    ])
    col_comp = "".join(f'<li><a href="{href}">{dual(pl,en)}</a></li>' for href,pl,en in [
        ("o-nas.html","O nas","About us"),
        ("case-studies.html","Case studies","Case studies"),
        ("kontakt.html","Kontakt","Contact"),
    ])
    tagline = dual("Enabling Corporate Excellence","Enabling Corporate Excellence")
    desc = dual(
        "Międzynarodowy partner w automatyzacji procesów, outsourcingu i dostarczaniu ekspertów IT.",
        "An international partner in process automation, outsourcing and IT talent delivery.")
    return f'''<footer class="footer">
  <div class="container">
    <div class="footer__top">
      <div>
        <a href="index.html" class="brand brand--footer" aria-label="Mientha">{LOGO_LIGHT}</a>
        <p style="max-width:34ch;color:#aeb8bf;font-size:.95rem">{desc}</p>
        <img src="{UIPATH_LOCKUP_W}" alt="UiPath Authorized Partner" style="height:28px;width:auto;margin:6px 0 2px;display:block" width="640" height="121" loading="lazy" decoding="async">
        <div class="badge-row">
          <span class="fbadge">SAP Partner &middot; Open Ecosystem</span>
          <span class="fbadge">KYP.ai Partner</span>
          <span class="fbadge">Pipedrive Partner</span>
        </div>
      </div>
      <div><h5>{dual("Usługi","Services")}</h5><ul>{col_serv}</ul></div>
      <div><h5>{dual("Branże","Industries")}</h5><ul>{col_ind}</ul></div>
      <div><h5>{dual("Firma","Company")}</h5><ul>{col_comp}</ul></div>
    </div>
    <div class="footer__bottom">
      <span>&copy; 2026 Mientha. {dual("Wszelkie prawa zastrzeżone.","All rights reserved.")} &middot; {tagline}</span>
      <span>ul. Puławska 39/40, 02-508 Warszawa &middot; contact@mientha.com &middot; +48 22 290 27 27</span>
    </div>
  </div>
</footer>'''

# ----------------------------------------------------------------- page shell
def page(active, title_pl, title_en, body):
    html = """<!DOCTYPE html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TPL__</title>
<meta name="description" content="Mientha — Enabling Corporate Excellence. RPA, Agentic AI, BPO, AMS i eksperci IT.">
<meta name="theme-color" content="#ffffff">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
__CSS__
</style>
</head>
<body class="lang-pl" data-title-pl="__TPL__" data-title-en="__TEN__" data-title-de="__TDE__">
<a class="skiplink" href="#main"><span class="pl">Przejdź do treści</span><span class="en">Skip to content</span><span class="de">Zum Inhalt springen</span></a>
__NAV__
<main id="main">
__BODY__
</main>
__FOOTER__
<script>
__JS__
</script>
</body>
</html>"""
    html = html.replace("__CSS__", CSS).replace("__JS__", JS)
    html = html.replace("__NAV__", nav(active)).replace("__FOOTER__", footer())
    title_de = DE_TITLE_BY_EN.get(title_en, title_en)
    html = html.replace("__TPL__", title_pl).replace("__TEN__", title_en).replace("__TDE__", title_de)
    html = html.replace("__BODY__", body)
    return html

PAGES = {}

# ============================================================ reusable builders
def svc_card(icon, pl_t, en_t, pl_d, en_d):
    return f'''<div class="cap">
      <div class="card__ico">{I[icon]}</div>
      <h3>{dual(pl_t,en_t)}</h3>
      <p>{dual(pl_d,en_d)}</p>
    </div>'''

def stat(num_pl, num_en, lab_pl, lab_en):
    return f'<div class="stat reveal"><b>{dual(num_pl,num_en)}</b><span>{dual(lab_pl,en=lab_en)}</span></div>'

# ---- network / presence visual (stylised, not a literal map)
COUNTRY_NODES = [
    (150,60,"SE"),(300,175,"PL"),(215,205,"DE"),(120,255,"FR"),
    (255,250,"CZ"),(305,255,"SK"),(320,300,"HU"),(400,300,"RO"),
    (95,345,"ES"),(470,345,"TR"),
]
def presence_svg():
    hub = (250,230)
    lines = "".join(
        f'<line x1="{hub[0]}" y1="{hub[1]}" x2="{x}" y2="{y}" stroke="#18cf98" stroke-width="1.3" opacity=".55"/>'
        for x,y,_ in COUNTRY_NODES)
    dots = ""
    for x,y,code in COUNTRY_NODES:
        dots += (f'<circle cx="{x}" cy="{y}" r="5.5" fill="#141436"/>'
                 f'<circle cx="{x}" cy="{y}" r="11" fill="none" stroke="#141436" stroke-width="1" opacity=".2"/>'
                 f'<text x="{x+11}" y="{y+4}" font-family="Inter,sans-serif" font-size="12" font-weight="600" fill="#5c6771">{code}</text>')
    hubm = (f'<circle cx="{hub[0]}" cy="{hub[1]}" r="9" fill="#18cf98"/>'
            f'<circle cx="{hub[0]}" cy="{hub[1]}" r="17" fill="none" stroke="#18cf98" stroke-width="1.5" opacity=".5"/>'
            f'<text x="{hub[0]}" y="{hub[1]+30}" text-anchor="middle" font-family="Sora,sans-serif" font-size="13" font-weight="700" fill="#141436">HQ · Warszawa</text>')
    return f'''<div class="mapwrap"><svg viewBox="0 0 560 400" role="img" aria-label="Europe presence">
      <rect width="560" height="400" fill="#f6f7f6"/>
      {lines}{dots}{hubm}
    </svg></div>'''

# ============================================================ HOME
home = f'''
<section class="hero">
  <div class="container hero__inner">
    <div>
      <a class="notice" href="agent-asystent-zarzadu.html">
        <span class="notice__new">{dual("Nowość","New")}</span>
        {dual("Asystent zarządu na Teams — zobacz realne case study","Executive assistant on Teams — see the real case study")}
        {I["arrow"]}
      </a>
      <h1>{dual("Automatyzacja, która realnie zmienia sposób działania firm.","Automation that truly changes the way enterprises operate.")}</h1>
      <p class="lead">{dual(
        "Jesteśmy międzynarodowym partnerem technologicznym. Wdrażamy automatyzację RPA i rozwiązania agentowe (Agentic AI), przejmujemy procesy biznesowe i dostarczamy najlepszych specjalistów IT dla firm w całej Europie.",
        "We are an international technology partner. We deliver RPA automation and agentic AI solutions, take over business processes and provide top IT specialists for companies across Europe.")}</p>
      <div class="hero__cta">
        <a href="kontakt.html" class="btn btn--mint">{dual("Umów rozmowę","Book a call")} {I["arrow"]}</a>
        <a href="uslugi.html" class="btn btn--ghost">{dual("Poznaj usługi","Explore services")}</a>
      </div>
      <div class="chips" style="margin-top:34px">
        <span class="chip"><span class="dot"></span>UiPath Authorized Partner</span>
        <span class="chip"><span class="dot"></span>SAP Partner</span>
        <span class="chip"><span class="dot"></span>120+ {dual("ekspertów","experts")}</span>
      </div>
    </div>
    <div class="hero__panel">
      <div class="panel">
        <p class="eyebrow" style="margin-bottom:22px">{dual("Nasi klienci w liczbach","Our clients in numbers")}</p>
        <div class="stats" style="grid-template-columns:1fr 1fr">
          <div class="stat"><b>100 <span class="u">{dual("mld €","bn €")}</span></b><span>{dual("łączne przychody klientów (2023)","combined client revenue (2023)")}</span></div>
          <div class="stat"><b>90<span class="u">%+</span></b><span>{dual("utrzymanie kontraktów","contract retention")}</span></div>
          <div class="stat"><b>20<span class="u">+</span></b><span>{dual("lat doświadczenia w IT","years of IT experience")}</span></div>
          <div class="stat"><b>10<span class="u">+</span></b><span>{dual("krajów europejskich","European countries")}</span></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section--tight" style="border-block:1px solid var(--line)">
  <div class="container">
    <div style="display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:24px">
      <p class="muted" style="margin:0;font-weight:600;max-width:26ch">{dual("Zaufali nam liderzy europejskiego rynku — FMCG, consulting i produkcja.","Trusted by European market leaders — FMCG, consulting and manufacturing.")}</p>
      <div class="partners">
        <span class="partner"><img src="{UIPATH_LOCKUP}" alt="UiPath Authorized Partner" style="height:36px;width:auto" width="640" height="121"></span>
        <span class="partner"><span class="partner__badge" style="background:#0faaff">SAP</span><span>SAP Partner<small>Open Ecosystem</small></span></span>
        <span class="partner"><span class="partner__badge" style="background:#141436">KYP</span><span>KYP.ai<small>{dual("Partner Process Intelligence","Process Intelligence Partner")}</small></span></span>
        <span class="partner"><span class="partner__badge" style="background:#0a7d5a">P</span><span>Pipedrive<small>{dual("Partner CRM","CRM Partner")}</small></span></span>
      </div>
    </div>
  </div>
</section>

<section class="section" id="uipath">
  <div class="container split" style="align-items:center">
    <div class="reveal">
      <p class="eyebrow eyebrow--uipath">UiPath Authorized Partner</p>
      <h2>{dual("Automatyzacja klasy enterprise z liderem rynku","Enterprise-grade automation with a market leader")}</h2>
      <p class="lead" style="margin-bottom:24px">{dual("UiPath — lider w agentic business orchestration. Jako Autoryzowany Partner UiPath łączymy roboty programowe, agentów AI i ludzi w jeden, zgrany proces — na bezpiecznej i skalowalnej platformie.","UiPath — a leader in agentic business orchestration. As a UiPath Authorized Partner we bring software robots, AI agents and people together into one coordinated process — on a secure, scalable platform.")}</p>
      {_checklist([
        ("Agenci, roboty i ludzie w jednym rytmie","Agents, robots and people in one rhythm"),
        ("Platforma klasy enterprise — bezpieczna i skalowalna","An enterprise-grade platform — secure and scalable"),
        ("Od pilotażu do skalowania w całej organizacji","From piloting to scaling across the organisation")])}
      <div style="margin-top:26px;display:flex;align-items:center;gap:22px;flex-wrap:wrap">
        <a href="uslugi.html" class="btn btn--primary">{dual("Poznaj automatyzację","Explore automation")} {I["arrow"]}</a>
        <a href="agenty.html" class="arrowlink">{dual("Case studies rozwiązań agentycznych","Agentic solution case studies")} {I["arrow"]}</a>
      </div>
    </div>
    <div class="reveal">
      <div class="panel" style="background:linear-gradient(160deg,#fff6f2,#ffffff);border-color:#ffd9cc;text-align:center">
        <img src="{UIPATH_LOCKUP}" alt="UiPath Authorized Partner" style="height:54px;width:auto;margin:6px auto 22px;display:block">
        <p style="font-family:var(--font-display);font-weight:700;font-size:clamp(1.4rem,2.4vw,2rem);letter-spacing:-.03em;line-height:1.12;color:var(--ink);margin:0">Agents. Robots. People.<br><span style="color:#fa4616">All in sync.</span></p>
        <p class="muted" style="margin-top:14px;font-size:.92rem">{dual("Orkiestracja automatyzacji nowej generacji.","Next-generation automation orchestration.")}</p>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="max-width:60ch;margin-bottom:44px" class="reveal">
      <p class="eyebrow">{dual("Co robimy","What we do")}</p>
      <h2>{dual("Twoje procesy. Nasze rozwiązania. Realne rezultaty.","Your processes. Our solutions. Real results.")}</h2>
      <p class="lead">{dual("Łączymy technologię, doświadczenie i partnerskie podejście, aby dostarczać rozwiązania, które faktycznie robią różnicę.","We combine technology, experience and a partnership mindset to deliver solutions that make a real difference.")}</p>
    </div>
    <div class="capgrid reveal">
      {svc_card("automation","Automatyzacja RPA i Agentic AI","RPA & Agentic AI automation","Wirtualni pracownicy i agenci AI wykonują powtarzalne zadania, analizują dane i optymalizują procesy — bez udziału człowieka.","Virtual workers and AI agents perform repetitive tasks, analyse data and optimise processes — without human intervention.")}
      {svc_card("bpo","Business Process Outsourcing","Business Process Outsourcing","Przejmujemy pełną odpowiedzialność za wybrane procesy — zakupy, dane podstawowe, operacje — i stale je ulepszamy.","We take full ownership of selected processes — procurement, master data, operations — and continuously improve them.")}
      {svc_card("ams","Application Management Services","Application Management Services","Utrzymanie, wsparcie i rozwój aplikacji korporacyjnych z pełną transparentnością i raportowaniem.","Maintenance, support and enhancement of enterprise applications with full transparency and reporting.")}
      {svc_card("talent","Eksperci i rekrutacja IT","IT experts & talent acquisition","Kompletne zespoły projektowe i pojedynczy specjaliści IT oraz finansowi, dopasowani do potrzeb organizacji.","Complete project teams and individual IT and finance specialists, matched to your organisation.")}
      {svc_card("custom","Rozwiązania szyte na miarę","Custom-built solutions","Dedykowane produkty i integracje projektowane pod konkretną branżę i procesy klienta.","Dedicated products and integrations designed around your specific industry and processes.")}
      {svc_card("chart","Automatyczne raporty i KPI","Automated reporting & KPIs","Automatyzacja raportowania i analityki KPI — mniej pracy ręcznej, szybsze i lepsze decyzje.","Automated reporting and KPI analytics — less manual work, faster and better decisions.")}
    </div>
    <div style="margin-top:30px" class="reveal"><a href="uslugi.html" class="arrowlink">{dual("Zobacz wszystkie usługi","See all services")} {I["arrow"]}</a></div>
  </div>
</section>

<section class="section bg-paper">
  <div class="container">
    <div style="max-width:60ch;margin-bottom:40px" class="reveal">
      <p class="eyebrow">{dual("Branże","Industries")}</p>
      <h2>{dual("Gotowe produkty dla konkretnych branż","Ready-to-deploy products for specific industries")}</h2>
      <p class="lead">{dual("Nie zaczynamy od zera. Wdrażamy sprawdzone rozwiązania dopasowane do realiów Twojego sektora.","We don't start from scratch. We deploy proven solutions tailored to the reality of your sector.")}</p>
    </div>
    <div class="grid" style="gap:16px">
      <a href="transport-spedycja.html" class="rowcard reveal" style="border-color:var(--mint-100);background:linear-gradient(180deg,var(--mint-050),#fff)">
        <div class="rowcard__ico" style="background:var(--mint);color:#053d2c;border:0">{I["transport"]}</div>
        <div>
          <span class="tag">{dual("Produkt flagowy","Flagship product")}</span>
          <h3>{dual("Transport i spedycja — automatyczne rozliczanie kierowców","Transport & logistics — automated driver settlement")}</h3>
          <p>{dual("Kompletne rozwiązanie do sprawnego rozliczania kierowców: od zebrania danych po gotowe listy płac i raporty.","A complete solution for efficient driver settlement: from data capture to ready payroll and reports.")}</p>
        </div>
        <span class="btn btn--ghost">{dual("Zobacz","View")} {I["arrow"]}</span>
      </a>
      <div class="grid g-3" style="gap:16px">
        <a href="branze.html" class="rowcard reveal" style="grid-template-columns:auto 1fr"><div class="rowcard__ico">{I["cart"]}</div><div><h3>{dual("FMCG i retail","FMCG & retail")}</h3><p>{dual("Automatyzacja faktur, danych dostawców i raportowania.","Invoice, supplier-data and reporting automation.")}</p></div></a>
        <a href="branze.html" class="rowcard reveal" style="grid-template-columns:auto 1fr"><div class="rowcard__ico">{I["factory"]}</div><div><h3>{dual("Produkcja","Manufacturing")}</h3><p>{dual("Optymalizacja procesów operacyjnych i zakupowych.","Operational and procurement process optimisation.")}</p></div></a>
        <a href="branze.html" class="rowcard reveal" style="grid-template-columns:auto 1fr"><div class="rowcard__ico">{I["bank"]}</div><div><h3>{dual("Finanse i BSS","Finance & shared services")}</h3><p>{dual("Procesy P2P/O2C, dane podstawowe, zgodność.","P2P/O2C processes, master data, compliance.")}</p></div></a>
      </div>
    </div>
    <div style="margin-top:30px" class="reveal"><a href="branze.html" class="arrowlink">{dual("Wszystkie branże","All industries")} {I["arrow"]}</a></div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">{dual("Dlaczego Mientha","Why Mientha")}</p>
      <h2>{dual("Partner, nie tylko dostawca","A partner, not just a vendor")}</h2>
      <p class="lead" style="margin-bottom:26px">{dual("Ponad 120 ekspertów, doświadczenie z liderami rynku i model współpracy nastawiony na wynik.","Over 120 experts, experience with market leaders and a delivery model focused on outcomes.")}</p>
      <ul class="checklist">
        <li>{dual("Zwrot z inwestycji nawet w 3 miesiące od wdrożenia automatyzacji.","Return on investment in as little as 3 months from an automation rollout.")}</li>
        <li>{dual("Do 80% redukcji kosztów operacyjnych i czasu pracy ręcznej.","Up to 80% reduction in operational costs and manual work.")}</li>
        <li>{dual("Zespoły blended — juniorzy i seniorzy w najefektywniejszym układzie.","Blended teams — juniors and seniors combined in the most effective setup.")}</li>
        <li>{dual("Gwarancja najlepszej oferty — bardziej efektywnej kosztowo niż obecny dostawca.","Best-offer guarantee — more cost-effective than your current provider.")}</li>
      </ul>
      <div style="margin-top:28px"><a href="o-nas.html" class="btn btn--primary">{dual("Poznaj firmę","About the company")} {I["arrow"]}</a></div>
    </div>
    <div class="panel panel--ink reveal">
      {I["quote"] if "quote" in I else ""}
      <p style="font-family:var(--font-display);font-size:1.35rem;line-height:1.5;color:#fff;margin-bottom:24px">{dual(
        "„Konsultanci Mientha należą do absolutnie najlepszych — wysoko wykwalifikowani, profesjonalni i skuteczni od pierwszego dnia. Odegrali kluczową rolę w naszym sukcesie.”",
        "“Mientha’s consultants are among the very best — highly skilled, professional and immediately effective. They’ve played a key role in driving our success.”")}</p>
      <p style="margin:0;color:#9fa9b0;font-weight:600">IT &amp; Data Director<br><span style="font-weight:400">{dual("klient z sektora FMCG","FMCG-sector client")}</span></p>
    </div>
  </div>
</section>

<section class="section bg-paper">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">{dual("Zasięg międzynarodowy","International reach")}</p>
      <h2>{dual("Jeden partner. Cała Europa.","One partner. All of Europe.")}</h2>
      <p class="lead" style="margin-bottom:24px">{dual("Nasz międzynarodowy zespół działa w wielu krajach europejskich, dostarczając specjalistów IT z różnych dziedzin tam, gdzie są potrzebni.","Our international team operates across many European countries, delivering IT specialists from a wide range of fields wherever they're needed.")}</p>
      <div class="chips">
        {"".join(f'<span class="chip">{c}</span>' for c in ["Polska","Deutschland","France","España","Sweden","Česko","Slovensko","Magyarország","România","Türkiye"])}
      </div>
    </div>
    <div class="reveal">{presence_svg()}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta reveal">
      <p class="eyebrow" style="justify-content:center">{dual("Zacznijmy","Let's start")}</p>
      <h2 style="max-width:20ch;margin-inline:auto">{dual("Porozmawiajmy o Twoim najbliższym procesie do automatyzacji","Let's talk about your next process to automate")}</h2>
      <p class="lead" style="margin-inline:auto;color:#aeb8bf;margin-bottom:30px">{dual("Bezpłatna konsultacja i wstępna ocena potencjału oszczędności.","A free consultation and an initial assessment of savings potential.")}</p>
      <a href="kontakt.html" class="btn btn--mint">{dual("Umów rozmowę","Book a call")} {I["arrow"]}</a>
    </div>
  </div>
</section>
'''
PAGES["index.html"] = ("index.html","Mientha — Enabling Corporate Excellence","Mientha — Enabling Corporate Excellence", home)

# ============================================================ helpers for inner pages
def pagehero(crumb_pl, crumb_en, eyebrow_pl, eyebrow_en, h_pl, h_en, lead_pl, lead_en):
    return f'''<section class="pagehero">
  <div class="container">
    <p class="crumb"><a href="index.html">{dual("Start","Home")}</a> &middot; {dual(crumb_pl,crumb_en)}</p>
    <p class="eyebrow">{dual(eyebrow_pl,eyebrow_en)}</p>
    <h1 style="max-width:18ch">{dual(h_pl,h_en)}</h1>
    <p class="lead">{dual(lead_pl,lead_en)}</p>
  </div>
</section>'''

def service_block(icon, t_pl,t_en, d_pl,d_en, benefits, anchor=""):
    lis = "".join(f'<li>{dual(b[0],b[1])}</li>' for b in benefits)
    aid = f' id="{anchor}"' if anchor else ""
    return f'''<div class="card reveal"{aid} style="scroll-margin-top:100px">
      <div class="card__ico">{I[icon]}</div>
      <h3>{dual(t_pl,t_en)}</h3>
      <p>{dual(d_pl,d_en)}</p>
      <ul>{lis}</ul>
    </div>'''

# ============================================================ USŁUGI
uslugi = pagehero(
  "Usługi","Services","Nasze usługi","Our services",
  "Kompletne wsparcie — od automatyzacji po zespoły ekspertów",
  "End-to-end support — from automation to expert teams",
  "Specjalizujemy się w automatyzacji procesów (RPA), rozwiązaniach agentowych i wysokiej jakości outsourcingu. Dla każdej usługi zobowiązujemy się do oferty bardziej efektywnej kosztowo niż Twój obecny dostawca — bez kompromisów w jakości.",
  "We specialise in process automation (RPA), agentic solutions and high-quality outsourcing. For every service we commit to an offer more cost-effective than your current provider — with no compromise on quality.")
uslugi += f'''
<section class="section">
  <div class="container grid g-2">
    {service_block("automation","Automatyzacja RPA i Agentic AI","Process automation with RPA & Agentic AI",
      "Wdrażamy zaawansowaną automatyzację w oparciu o wiodące platformy (UiPath) i sztuczną inteligencję. Roboty i agenci AI samodzielnie wykonują powtarzalne zadania, analizują dane i optymalizują procesy operacyjne.",
      "We implement advanced automation on leading platforms (UiPath) and AI. Software robots and AI agents independently perform repetitive tasks, analyse data and optimise operational processes.",
      [("Zwrot z inwestycji nawet w 3 miesiące","Return on investment in as little as 3 months"),
       ("Do 80% redukcji kosztów operacyjnych i pracy ręcznej","Up to 80% reduction in operational costs and manual work"),
       ("Mniej błędów, większa kontrola i transparentność","Fewer errors, greater control and transparency"),
       ("Realizacja zadań dotąd odkładanych z braku zasobów","Execution of tasks previously delayed due to lack of resources")], anchor="rpa")}
    {service_block("bpo","Business Process Outsourcing (BPO)","Business Process Outsourcing (BPO)",
      "Przejmujemy pełną odpowiedzialność za wybrane procesy biznesowe, jednocześnie stale je optymalizując. Specjalizujemy się w procesach operacyjnych, zakupach i zarządzaniu danymi podstawowymi.",
      "We take full ownership of selected business processes while continuously optimising them. Our expertise lies in operational processes, procurement and master-data management.",
      [("Wsparcie procesu zakupowego end-to-end — od zamówienia do płatności","End-to-end procurement support — from order to payment"),
       ("Profesjonalne zarządzanie danymi dostawców i kont bankowych","Professional management of supplier data and bank-account records"),
       ("Istotna redukcja kosztów przy wyższej jakości usług","Significant cost reduction with improved service quality"),
       ("Regularne raportowanie i pełna transparentność działań","Regular reporting and full transparency of all activities")], anchor="bpo")}
    {service_block("ams","Application Management Services (AMS)","Application Management Services (AMS)",
      "Zapewniamy bieżące wsparcie, utrzymanie i optymalizację aplikacji korporacyjnych — dbając o wydajność, stabilność i zgodność ze zmieniającymi się potrzebami biznesu.",
      "We provide ongoing support, maintenance and optimisation of enterprise applications — ensuring performance, stability and alignment with evolving business needs.",
      [("Zarządzanie incydentami i zmianą, monitoring, wsparcie użytkowników","Incident & change management, monitoring, user support"),
       ("Uwalniamy Twój zespół IT do zadań strategicznych","We free your IT team to focus on strategic initiatives"),
       ("Regularne raportowanie i pełna transparentność współpracy","Regular reporting and full transparency of the collaboration")], anchor="ams")}
    {service_block("talent","Eksperci i rekrutacja IT","Expert support & talent acquisition",
      "Dostarczamy kompletne zespoły projektowe oraz pojedynczych specjalistów IT i finansowych — idealnie dopasowanych do potrzeb Twojej organizacji.",
      "We provide complete project teams and individual IT and finance specialists — perfectly matched to your organisation's needs.",
      [("Gwarancja jakości — 90% kandydatów zatrudnianych po pierwszej rozmowie","Quality guarantee — 90% of candidates hired after the first interview"),
       ("Zespoły blended — juniorzy i seniorzy w najefektywniejszym układzie","Blended teams — juniors and seniors in the most effective setup"),
       ("Niższe koszty — do 30% taniej niż standardowe stawki rynkowe","Lower costs — up to 30% below standard market rates")], anchor="talent")}
  </div>
  <div class="container" style="margin-top:22px">
    {service_block("custom","Rozwiązania szyte na miarę Twojego biznesu","Custom solutions built around your business",
      "Tworzymy dedykowane rozwiązania dopasowane do Twojej organizacji i branży — w tym automatyczne raporty i analitykę KPI, które oszczędzają czas i przyspieszają decyzje.",
      "We create dedicated solutions tailored to your organisation and industry — including automated reports and KPI analytics that save time and speed up decisions.",
      [("Automatyczne raporty i analityka KPI — szybsze decyzje","Automated reports and KPI analytics — faster decision-making"),
       ("Wyższa efektywność operacyjna i transparentność procesów","Improved operational efficiency and process transparency"),
       ("Łatwiejsze planowanie i lepsza kontrola","Easier planning and better control")], anchor="custom")}
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="container">
    <a href="wsparcie-247.html" class="rowcard reveal" style="border-color:var(--mint-100);background:linear-gradient(180deg,var(--mint-050),#fff)">
      <div class="rowcard__ico" style="background:var(--mint);color:#053d2c;border:0">{I["clock"]}</div>
      <div>
        <span class="tag">{dual("Wyróżniona usługa","Featured service")}</span>
        <h3>{dual("Wsparcie 24/7 dla aplikacji krytycznych","24/7 support for business-critical applications")}</h3>
        <p>{dual("Całodobowe wsparcie i dedykowane zespoły dla fabryk i firm z każdej branży — z zarządzanym transferem wiedzy i standardami światowej klasy (ITIL 4, ISO 20000/27001).","Round-the-clock support and dedicated teams for factories and companies of any industry — with managed knowledge transfer and world-class standards (ITIL 4, ISO 20000/27001).")}</p>
      </div>
      <span class="btn btn--ghost">{dual("Poznaj usługę","Explore the service")} {I["arrow"]}</span>
    </a>
  </div>
</section>

<section class="section bg-paper">
  <div class="container">
    <div style="max-width:60ch;margin-bottom:40px" class="reveal">
      <p class="eyebrow">{dual("Jak pracujemy","How we work")}</p>
      <h2>{dual("Od analizy do mierzalnego rezultatu","From analysis to measurable results")}</h2>
    </div>
    <div class="steps reveal">
      <div class="step"><div class="step__n"></div><div><h4>{dual("Analiza i ocena potencjału","Discovery & assessment")}</h4><p>{dual("Mapujemy proces, identyfikujemy wąskie gardła i szacujemy potencjał oszczędności.","We map the process, identify bottlenecks and estimate savings potential.")}</p></div></div>
      <div class="step"><div class="step__n"></div><div><h4>{dual("Projekt rozwiązania","Solution design")}</h4><p>{dual("Projektujemy architekturę automatyzacji lub model outsourcingu dopasowany do procesu.","We design the automation architecture or outsourcing model tailored to the process.")}</p></div></div>
      <div class="step"><div class="step__n"></div><div><h4>{dual("Wdrożenie","Implementation")}</h4><p>{dual("Budujemy, testujemy i uruchamiamy rozwiązanie w Twoim środowisku.","We build, test and deploy the solution in your environment.")}</p></div></div>
      <div class="step"><div class="step__n"></div><div><h4>{dual("Utrzymanie i rozwój","Run & optimise")}</h4><p>{dual("Monitorujemy, raportujemy i stale doskonalimy — z pełną transparentnością.","We monitor, report and continuously improve — with full transparency.")}</p></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="cta reveal" style="background:linear-gradient(120deg,#101018,#1c1c3a)">
      <p class="eyebrow" style="justify-content:center">{dual("Nasze zobowiązanie","Our commitment")}</p>
      <h2 style="max-width:22ch;margin-inline:auto">{dual("Najlepsza oferta — gwarantowana","The best offer — guaranteed")}</h2>
      <p class="lead" style="margin-inline:auto;color:#aeb8bf;margin-bottom:30px">{dual("Dla każdej z powyższych usług zobowiązujemy się zaproponować ofertę bardziej efektywną kosztowo niż Twój obecny dostawca — bez kompromisów w jakości.","For each of these services we commit to a more cost-effective offer than your current provider — with no compromise on quality.")}</p>
      <a href="kontakt.html" class="btn btn--mint">{dual("Poproś o wycenę","Request a quote")} {I["arrow"]}</a>
    </div>
  </div>
</section>
'''
PAGES["uslugi.html"] = ("uslugi.html","Usługi — Mientha","Services — Mientha", uslugi)

# ============================================================ BRANŻE
def ind_row(icon, t_pl,t_en, d_pl,d_en, prods, href="branze.html", flagship=False, anchor="",
            link_href="", link_pl="Zobacz rozwiązanie", link_en="View the solution"):
    tag = f'<span class="tag">{dual("Produkt flagowy","Flagship")}</span>' if flagship else ""
    prod_pills = "".join(f'<span class="chip"><span class="dot"></span>{dual(p[0],p[1])}</span>' for p in prods)
    style = 'style="border-color:var(--mint-100);background:linear-gradient(180deg,var(--mint-050),#fff)"' if flagship else ""
    icostyle = 'style="background:var(--mint);color:#053d2c;border:0"' if flagship else ""
    aid = f' id="{anchor}"' if anchor else ""
    inner_style = style[7:-1] if style else ""   # contents of style="..."
    card_style = f' style="scroll-margin-top:100px;{inner_style}"'
    lhref = href if flagship else link_href
    link = (f'<div style="margin-top:18px"><a href="{lhref}" class="arrowlink">'
            f'{dual(link_pl,link_en)} {I["arrow"]}</a></div>') if (flagship or link_href) else ""
    return f'''<div class="card reveal"{aid}{card_style}>
      <div style="display:flex;gap:20px;align-items:flex-start;flex-wrap:wrap">
        <div class="rowcard__ico" {icostyle}>{I[icon]}</div>
        <div style="flex:1;min-width:240px">
          {tag}
          <h3>{dual(t_pl,t_en)}</h3>
          <p style="margin-bottom:16px">{dual(d_pl,d_en)}</p>
          <div class="chips">{prod_pills}</div>
          {link}
        </div>
      </div>
    </div>'''

branze = pagehero(
  "Branże","Industries","Podział na branże","Industries",
  "Rozwiązania dopasowane do realiów Twojego sektora",
  "Solutions tailored to the reality of your sector",
  "Dla każdej branży łączymy gotowe produkty, które możemy szybko wdrożyć, z rozwiązaniami projektowanymi na miarę. Poniżej przykłady case studies i produktów gotowych do wdrożenia.",
  "For each industry we combine ready products we can deploy quickly with solutions built to measure. Below are examples of case studies and ready-to-deploy products.")
branze += f'''
<section class="section">
  <div class="container grid" style="gap:18px">
    {ind_row("transport","Transport i spedycja","Transport & logistics",
      "Flagowe rozwiązanie do sprawnego rozliczania kierowców — automatyczne zbieranie danych z tras, paliwa i delegacji, wyliczanie wynagrodzeń oraz generowanie gotowych raportów i list płac.",
      "Our flagship solution for efficient driver settlement — automated capture of route, fuel and per-diem data, pay calculation and ready-to-use reports and payroll.",
      [("Rozliczanie kierowców","Driver settlement"),("Delegacje i diety","Per-diems & allowances"),("Integracja z TMS/ERP","TMS/ERP integration")],
      href="transport-spedygja.html".replace("spedygja","spedycja"), flagship=True)}
    {ind_row("cart","FMCG i retail","FMCG & retail",
      "Automatyzacja procesów wysokiego wolumenu: obieg faktur, zarządzanie danymi dostawców, raportowanie sprzedaży i uzgodnienia.",
      "Automation of high-volume processes: invoice workflows, supplier-data management, sales reporting and reconciliations.",
      [("Automatyzacja faktur","Invoice automation"),("Dane dostawców","Supplier master data"),("Raporty sprzedaży","Sales reporting")], anchor="fmcg",
      link_href="fmcg.html", link_pl="Zobacz 10+ case studies FMCG", link_en="See 10+ FMCG case studies")}
    {ind_row("factory","Produkcja","Manufacturing",
      "Optymalizacja procesów operacyjnych, zakupowych i danych podstawowych oraz wsparcie AMS dla systemów produkcyjnych.",
      "Optimisation of operational, procurement and master-data processes, plus AMS support for production systems.",
      [("Procesy zakupowe P2P","P2P procurement"),("Dane podstawowe","Master data"),("AMS","AMS")], anchor="produkcja")}
    {ind_row("bank","Finanse i centra usług wspólnych (BSS)","Finance & shared services (BSS)",
      "Automatyzacja procesów P2P/O2C, zarządzanie danymi kont bankowych, zgodność i kontrola oraz automatyczne raportowanie KPI.",
      "Automation of P2P/O2C processes, bank-account data management, compliance and control, and automated KPI reporting.",
      [("P2P / O2C","P2P / O2C"),("Zgodność i kontrola","Compliance & control"),("Raporty KPI","KPI reporting")], anchor="finanse")}
    {ind_row("telecom","Telekomunikacja","Telecom",
      "Obsługa procesów wysokiego wolumenu, wsparcie aplikacji oraz dostarczanie wyspecjalizowanych zespołów IT.",
      "Handling high-volume processes, application support and delivery of specialised IT teams.",
      [("Automatyzacja back-office","Back-office automation"),("Wsparcie aplikacji","Application support"),("Zespoły IT","IT teams")], anchor="telekomunikacja")}
    {ind_row("car","Automotive","Automotive",
      "Rozwiązania automatyzujące procesy w łańcuchu dostaw i finansach oraz eksperci wspierający transformację cyfrową.",
      "Solutions that automate supply-chain and finance processes, plus experts supporting digital transformation.",
      [("Łańcuch dostaw","Supply chain"),("Finanse","Finance"),("Eksperci IT","IT experts")], anchor="automotive")}
  </div>
</section>

<section class="section bg-paper">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">{dual("Nie ma Twojej branży?","Don't see your industry?")}</p>
      <h2>{dual("Zbudujemy rozwiązanie od podstaw","We'll build a solution from the ground up")}</h2>
      <p class="lead">{dual("Tworzymy dedykowane rozwiązania dopasowane do Twojej organizacji i sektora. Zacznijmy od krótkiej rozmowy o procesie, który chcesz usprawnić.","We create dedicated solutions tailored to your organisation and sector. Let's start with a short conversation about the process you'd like to improve.")}</p>
      <div style="margin-top:24px"><a href="kontakt.html" class="btn btn--primary">{dual("Porozmawiajmy","Let's talk")} {I["arrow"]}</a></div>
    </div>
    <div class="panel reveal">
      <div class="grid g-2" style="gap:26px">
        <div class="stat"><b>90<span class="u">%+</span></b><span>{dual("utrzymanie kontraktów","contract retention")}</span></div>
        <div class="stat"><b>100 <span class="u">{dual("mld €","bn €")}</span></b><span>{dual("przychody klientów (2023)","client revenue (2023)")}</span></div>
        <div class="stat"><b>120<span class="u">+</span></b><span>{dual("ekspertów","experts")}</span></div>
        <div class="stat"><b>10<span class="u">+</span></b><span>{dual("krajów Europy","European countries")}</span></div>
      </div>
    </div>
  </div>
</section>
'''
PAGES["branze.html"] = ("branze.html","Branże — Mientha","Industries — Mientha", branze)

# ============================================================ TRANSPORT / SPEDYCJA (case study + product)
transport = f'''<section class="pagehero" style="background:linear-gradient(180deg,var(--mint-050),#fff)">
  <div class="container">
    <p class="crumb"><a href="index.html">{dual("Start","Home")}</a> &middot; <a href="branze.html">{dual("Branże","Industries")}</a> &middot; {dual("Transport i spedycja","Transport & logistics")}</p>
    <span class="tag">{dual("Produkt flagowy · Transport i spedycja","Flagship product · Transport & logistics")}</span>
    <h1 style="max-width:20ch">{dual("Automatyczne rozliczanie kierowców","Automated driver settlement")}</h1>
    <p class="lead">{dual("Koniec z ręcznym zbieraniem dokumentów i arkuszami kalkulacyjnymi. Nasze rozwiązanie automatyzuje cały proces rozliczania kierowców — od zebrania danych, przez wyliczenie wynagrodzeń i delegacji, po gotowe raporty i eksport do systemu płacowego.","No more manual document collection and spreadsheets. Our solution automates the entire driver-settlement process — from data capture, through pay and per-diem calculation, to ready reports and payroll export.")}</p>
    <div class="hero__cta" style="margin-top:26px">
      <a href="kontakt.html" class="btn btn--mint">{dual("Zamów demo","Request a demo")} {I["arrow"]}</a>
      <a href="case-studies.html" class="btn btn--ghost">{dual("Zobacz efekty","See the results")}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">{dual("Wyzwanie","The challenge")}</p>
      <h2>{dual("Rozliczanie kierowców pochłania czas i generuje błędy","Driver settlement eats time and generates errors")}</h2>
      <p class="lead measure">{dual("W firmach transportowych i spedycyjnych rozliczenie kierowców to comiesięczny wysiłek: dane z kart drogowych, tankowań, delegacji i systemów telematycznych trzeba ręcznie zebrać, uzgodnić i przeliczyć według złożonych zasad. To źródło opóźnień, pomyłek i frustracji.","In transport and forwarding companies, settling drivers is a monthly effort: data from route cards, fuel, per-diems and telematics has to be collected, reconciled and calculated by hand against complex rules. That means delays, mistakes and frustration.")}</p>
    </div>
    <div class="panel panel--ink reveal">
      <ul class="checklist">
        <li>{dual("Dane rozproszone w wielu systemach i dokumentach","Data scattered across many systems and documents")}</li>
        <li>{dual("Ręczne wyliczanie diet i delegacji krajowych oraz zagranicznych","Manual calculation of domestic and international per-diems")}</li>
        <li>{dual("Błędy i korekty obniżające zaufanie kierowców","Errors and corrections that undermine driver trust")}</li>
        <li>{dual("Brak przejrzystości i trudny audyt rozliczeń","No transparency and hard-to-audit settlements")}</li>
      </ul>
    </div>
  </div>
</section>

<section class="section bg-paper">
  <div class="container">
    <div style="max-width:60ch;margin-bottom:40px" class="reveal">
      <p class="eyebrow">{dual("Jak to działa","How it works")}</p>
      <h2>{dual("Cały proces rozliczenia — automatycznie","The whole settlement process — automated")}</h2>
    </div>
    <div class="steps reveal">
      <div class="step"><div class="step__n"></div><div><h4>{dual("Zbieranie danych","Data capture")}</h4><p>{dual("Robot pobiera dane z systemów telematycznych, kart paliwowych, TMS i dokumentów tras — automatycznie, o wyznaczonych porach.","A robot collects data from telematics, fuel cards, TMS and route documents — automatically, on schedule.")}</p></div></div>
      <div class="step"><div class="step__n"></div><div><h4>{dual("Walidacja i uzgodnienie","Validation & reconciliation")}</h4><p>{dual("System weryfikuje kompletność danych, wykrywa braki i uzgadnia trasy z tankowaniami oraz czasem pracy.","The system checks completeness, flags gaps and reconciles routes with fuel and working time.")}</p></div></div>
      <div class="step"><div class="step__n"></div><div><h4>{dual("Wyliczenie wynagrodzeń i diet","Pay & per-diem calculation")}</h4><p>{dual("Reguły płacowe, diety krajowe i zagraniczne oraz dodatki liczone są automatycznie, zgodnie z Twoją polityką.","Pay rules, domestic and foreign per-diems and bonuses are calculated automatically, per your policy.")}</p></div></div>
      <div class="step"><div class="step__n"></div><div><h4>{dual("Raporty i eksport","Reports & export")}</h4><p>{dual("Gotowe rozliczenia trafiają do raportów, paneli kierowców i eksportu do systemu płacowego/ERP.","Finished settlements flow into reports, driver panels and export to payroll/ERP.")}</p></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="grid g-3">
      <div class="card reveal"><div class="card__ico">{I["clock"]}</div><h3>{dual("Oszczędność czasu","Time savings")}</h3><p>{dual("Skrócenie miesięcznego rozliczenia z dni do godzin dzięki automatyzacji zbierania i przeliczania danych.","Monthly settlement cut from days to hours by automating data capture and calculation.")}</p></div>
      <div class="card reveal"><div class="card__ico">{I["shield"]}</div><h3>{dual("Mniej błędów","Fewer errors")}</h3><p>{dual("Spójne reguły i walidacja eliminują pomyłki oraz kosztowne korekty rozliczeń.","Consistent rules and validation eliminate mistakes and costly corrections.")}</p></div>
      <div class="card reveal"><div class="card__ico">{I["chart"]}</div><h3>{dual("Pełna transparentność","Full transparency")}</h3><p>{dual("Każde rozliczenie jest audytowalne, a kierowcy widzą swoje dane w przejrzystym panelu.","Every settlement is auditable and drivers see their data in a clear panel.")}</p></div>
      <div class="card reveal"><div class="card__ico">{I["plug"]}</div><h3>{dual("Integracje","Integrations")}</h3><p>{dual("Łączymy się z popularnymi systemami TMS, telematyką, kartami paliwowymi i systemami płacowymi/ERP.","We connect to popular TMS, telematics, fuel cards and payroll/ERP systems.")}</p></div>
      <div class="card reveal"><div class="card__ico">{I["doc"]}</div><h3>{dual("Zgodność","Compliance")}</h3><p>{dual("Reguły diet i czasu pracy zgodne z przepisami krajowymi i międzynarodowymi.","Per-diem and working-time rules aligned with national and international regulations.")}</p></div>
      <div class="card reveal"><div class="card__ico">{I["spark"]}</div><h3>{dual("Wdrożenie bez zera","No-cold-start rollout")}</h3><p>{dual("Startujemy z gotowego produktu i dostrajamy go do Twoich zasad — szybkie uruchomienie.","We start from a ready product and tune it to your rules — fast go-live.")}</p></div>
    </div>
  </div>
</section>

<section class="section bg-ink">
  <div class="container" style="text-align:center">
    <p class="eyebrow" style="justify-content:center">{dual("Potencjalne efekty","Potential impact")}</p>
    <h2 style="max-width:22ch;margin-inline:auto">{dual("Rezultaty, których możesz oczekiwać","Results you can expect")}</h2>
    <div class="stats" style="margin-top:20px">
      <div class="stat"><b>80<span class="u">%</span></b><span>{dual("mniej pracy ręcznej przy rozliczeniach","less manual settlement work")}</span></div>
      <div class="stat"><b>3<span class="u"> {dual("mies.","mo")}</span></b><span>{dual("typowy zwrot z inwestycji","typical return on investment")}</span></div>
      <div class="stat"><b>~0<span class="u"> {dual("błędów","errors")}</span></b><span>{dual("dzięki spójnym regułom","thanks to consistent rules")}</span></div>
      <div class="stat"><b>24/7</b><span>{dual("automatyczne zbieranie danych","automated data capture")}</span></div>
    </div>
    <p class="muted" style="color:#8a949c;margin-top:26px;font-size:.85rem">{dual("Wartości orientacyjne, zależne od skali floty i konfiguracji procesu.","Indicative figures, depending on fleet size and process configuration.")}</p>
    <div style="margin-top:30px"><a href="kontakt.html" class="btn btn--mint">{dual("Zamów demo rozliczania kierowców","Request a driver-settlement demo")} {I["arrow"]}</a></div>
  </div>
</section>
'''
PAGES["transport-spedycja.html"] = ("branze.html","Rozliczanie kierowców — Mientha","Driver settlement — Mientha", transport)

# ============================================================ CASE STUDIES
def cs_card(tag_pl,tag_en, t_pl,t_en, d_pl,d_en, metric_pl,metric_en, ml_pl,ml_en, href=None):
    link = f'<div style="margin-top:18px"><a href="{href}" class="arrowlink">{dual("Zobacz szczegóły","View details")} {I["arrow"]}</a></div>' if href else ""
    return f'''<div class="card reveal">
      <span class="tag">{dual(tag_pl,tag_en)}</span>
      <h3>{dual(t_pl,t_en)}</h3>
      <p>{dual(d_pl,d_en)}</p>
      <div style="margin-top:20px;padding-top:20px;border-top:1px solid var(--line);display:flex;align-items:baseline;gap:12px">
        <b style="font-family:var(--font-display);font-size:1.9rem;letter-spacing:-.03em;color:var(--ink)">{dual(metric_pl,metric_en)}</b>
        <span class="muted" style="font-size:.9rem">{dual(ml_pl,ml_en)}</span>
      </div>{link}
    </div>'''

cases = pagehero(
  "Case studies","Case studies","Case studies","Case studies",
  "Efekty, które dostarczamy klientom",
  "The results we deliver for clients",
  "Wybrane przykłady wdrożeń automatyzacji, outsourcingu i zespołów eksperckich. Ze względu na poufność część danych klientów została zanonimizowana.",
  "Selected examples of automation, outsourcing and expert-team engagements. For confidentiality, some client details have been anonymised.")
cases += f'''
<section class="section--tight">
  <div class="container">
    <a href="fmcg.html" class="rowcard reveal" style="border-color:var(--mint-100);background:linear-gradient(180deg,var(--mint-050),#fff)">
      <div class="rowcard__ico" style="background:var(--mint);color:#053d2c;border:0">{I["cart"]}</div>
      <div>
        <span class="tag">{dual("Kolekcja · FMCG","Collection · FMCG")}</span>
        <h3>{dual("10+ automatyzacji dla branży FMCG","10+ automations for the FMCG industry")}</h3>
        <p>{dual("Rozliczenia VAT, należności i kredyt, zapytania P2P, treasury i HR — zobacz komplet case studies opisanych krok po kroku.","VAT settlements, receivables and credit, P2P queries, treasury and HR — see the full set of case studies, explained step by step.")}</p>
      </div>
      <span class="btn btn--ghost">{dual("Zobacz kolekcję","View collection")} {I["arrow"]}</span>
    </a>
    <a href="agenty.html" class="rowcard reveal" style="margin-top:14px;border-color:#ffd9cc;background:linear-gradient(180deg,#fff6f2,#fff)">
      <div class="rowcard__ico" style="background:#fa4616;color:#fff;border:0">{I["bubble"]}</div>
      <div>
        <span class="tag" style="color:#c2410c;background:#fff1ea">{dual("Kolekcja · Agentic AI","Collection · Agentic AI")}</span>
        <h3>{dual("Rozwiązania agentyczne — agenci AI na Microsoft Teams","Agentic solutions — AI agents on Microsoft Teams")}</h3>
        <p>{dual("Asystent zarządu, poranny brief, zamknięcie miesiąca, należności — zobacz, jak rozmowa na Teams zamienia się w wykonaną pracę.","Executive assistant, morning brief, month-end close, receivables — see how a Teams conversation turns into finished work.")}</p>
      </div>
      <span class="btn btn--ghost">{dual("Zobacz kolekcję","View collection")} {I["arrow"]}</span>
    </a>
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="container grid g-2">
    {cs_card("Transport i spedycja","Transport & logistics",
      "Automatyczne rozliczanie kierowców","Automated driver settlement",
      "Wdrożenie gotowego produktu do rozliczania kierowców u operatora flotowego — automatyzacja zbierania danych, wyliczeń diet i eksportu do systemu płacowego.",
      "Deployment of our ready driver-settlement product at a fleet operator — automating data capture, per-diem calculation and payroll export.",
      "-80%","-80%","czasu rozliczeń","settlement time",
      href="transport-spedycja.html")}
    {cs_card("FMCG","FMCG",
      "Automatyzacja obiegu faktur","Invoice-processing automation",
      "Roboty RPA przejęły rejestrację i dekretację faktur zakupowych u producenta FMCG, integrując się z SAP i eliminując pracę ręczną.",
      "RPA robots took over purchase-invoice registration and coding at an FMCG manufacturer, integrating with SAP and removing manual work.",
      "3 mies.","3 mo","do zwrotu z inwestycji","to return on investment")}
    {cs_card("Produkcja · AMS","Manufacturing · AMS",
      "Utrzymanie aplikacji korporacyjnych","Enterprise application management",
      "Przejęliśmy AMS dla kluczowych aplikacji producenta, zapewniając monitoring, wsparcie użytkowników i proaktywne usprawnienia.",
      "We took over AMS for a manufacturer's core applications, providing monitoring, user support and proactive enhancements.",
      "90%+","90%+","utrzymanie współpracy","engagement retention")}
    {cs_card("Finanse · Talent","Finance · Talent",
      "Zespół ekspertów IT dla banku","IT expert team for a bank",
      "Dostarczyliśmy blended team specjalistów IT i finansowych do programu transformacji, dopasowany do potrzeb organizacji.",
      "We delivered a blended team of IT and finance specialists for a transformation programme, matched to the organisation's needs.",
      "90%","90%","kandydatów przyjętych po 1. rozmowie","candidates hired after 1st interview")}
    {cs_card("Zakupy · BPO","Procurement · BPO",
      "Outsourcing procesu zakupowego","Procurement process outsourcing",
      "Przejęliśmy proces zakupowy end-to-end oraz zarządzanie danymi dostawców i kont bankowych, obniżając koszty przy wyższej jakości.",
      "We took over the end-to-end procurement process and supplier/bank-account data management, lowering costs with higher quality.",
      "-30%","-30%","kosztów procesu","process cost")}
    {cs_card("Agentic AI","Agentic AI",
      "Agenci AI w obsłudze danych","AI agents in data operations",
      "Wdrożenie agentów AI do analizy i przetwarzania danych operacyjnych, realizujących zadania dotąd odkładane z braku zasobów.",
      "Deployment of AI agents for analysing and processing operational data, executing tasks previously delayed due to lack of resources.",
      "24/7","24/7","praca bez przerw","uninterrupted operation", href="agenty.html")}
  </div>
</section>

<section class="section bg-paper">
  <div class="container"><div class="cta reveal">
    <h2 style="max-width:22ch;margin-inline:auto">{dual("Twój proces może być następny","Your process could be next")}</h2>
    <p class="lead" style="margin-inline:auto;color:#aeb8bf;margin-bottom:30px">{dual("Opowiedz nam o procesie, który chcesz usprawnić — przygotujemy ocenę potencjału.","Tell us about a process you'd like to improve — we'll prepare a potential assessment.")}</p>
    <a href="kontakt.html" class="btn btn--mint">{dual("Umów rozmowę","Book a call")} {I["arrow"]}</a>
  </div></div>
</section>
'''
PAGES["case-studies.html"] = ("case-studies.html","Case studies — Mientha","Case studies — Mientha", cases)

# ============================================================ O NAS
onas = pagehero(
  "O nas","About","O firmie","About us",
  "Międzynarodowy partner w automatyzacji i IT",
  "An international partner in automation and IT",
  "Mientha powstała, aby realnie rozwiązywać problemy biznesowe, z którymi mierzą się duże organizacje. Dziś to zespół ponad 120 ekspertów działających w wielu krajach Europy.",
  "Mientha was founded to genuinely solve the business problems large organisations face. Today it is a team of over 120 experts operating across many European countries.")
onas += f'''
<section class="section">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">{dual("Nasza historia","Our story")}</p>
      <h2>{dual("Od doświadczenia w IT do partnera dla korporacji","From IT experience to a corporate partner")}</h2>
      <p class="lead measure">{dual("Firmę założył lider z ponad 20-letnim doświadczeniem w technologii i IT, który przeszedł drogę od roli technicznej do doradztwa biznesowego i IT. To połączenie perspektyw pozwoliło zbudować firmę skutecznie rozwiązującą realne problemy korporacyjnych klientów — dziś zatrudniającą ponad 120 ekspertów.","The company was founded by a leader with over 20 years of experience in technology and IT, who moved from a technical role into business and IT consulting. That blend of perspectives helped build a company that effectively solves the real problems of corporate clients — today employing over 120 experts.")}</p>
      <div class="chips" style="margin-top:22px">
        <span class="chip"><span class="dot"></span>UiPath Authorized Partner</span>
        <span class="chip"><span class="dot"></span>SAP Partner · Open Ecosystem</span>
      </div>
    </div>
    <div class="panel reveal">
      <div style="display:flex;gap:16px;align-items:center;margin-bottom:22px">
        <div style="width:64px;height:64px;border-radius:50%;background:var(--navy);color:#fff;display:grid;place-items:center;font-family:var(--font-display);font-weight:700;font-size:1.3rem">PK</div>
        <div><b style="font-family:var(--font-display);font-size:1.15rem;display:block">Paweł Kacprowicz</b><span class="muted">Chief Executive Officer</span></div>
      </div>
      <p style="font-family:var(--font-display);font-size:1.15rem;line-height:1.55;color:var(--ink);margin:0">{dual("„Łączymy technologię, doświadczenie i partnerskie podejście, aby dostarczać rozwiązania, które naprawdę robią różnicę.”","“We combine technology, experience and a partnership mindset to deliver solutions that truly make a difference.”")}</p>
    </div>
  </div>
</section>

<section class="section bg-ink">
  <div class="container">
    <p class="eyebrow" style="justify-content:flex-start">{dual("Nasi klienci","Our clients")}</p>
    <h2 style="max-width:24ch">{dual("Współpracujemy z liderami europejskiego rynku","We work with European market leaders")}</h2>
    <div class="stats" style="margin-top:36px">
      <div class="stat"><b>100 <span class="u">{dual("mld €","bn €")}</span></b><span>{dual("łączne przychody klientów w 2023","combined client revenue in 2023")}</span></div>
      <div class="stat"><b>90<span class="u">%+</span></b><span>{dual("utrzymanie kontraktów","contract retention rate")}</span></div>
      <div class="stat"><b>120<span class="u">+</span></b><span>{dual("ekspertów w zespole","experts in the team")}</span></div>
      <div class="stat"><b>10<span class="u">+</span></b><span>{dual("krajów europejskich","European countries")}</span></div>
    </div>
    <p style="margin-top:30px;max-width:60ch;color:#aeb8bf">{dual("Pracujemy z wiodącymi firmami w sektorach FMCG, consultingu i produkcji. Nasz międzynarodowy zespół dostarcza specjalistów IT z różnych dziedzin w całej Europie.","We work with leading companies across FMCG, consulting and manufacturing. Our international team delivers IT specialists from a wide range of fields across Europe.")}</p>
  </div>
</section>

<section class="section bg-paper">
  <div class="container">
    <div style="max-width:60ch;margin-bottom:40px" class="reveal">
      <p class="eyebrow">{dual("Partnerstwa technologiczne","Technology partnerships")}</p>
      <h2>{dual("Najlepsza technologia w rękach doświadczonego zespołu","The best technology in experienced hands")}</h2>
      <p class="lead">{dual("Łączymy wiodące platformy z wiedzą, jak je skutecznie wdrażać — aby automatyzacja przynosiła realny, mierzalny zwrot.","We combine leading platforms with the know-how to deploy them well — so automation delivers a real, measurable return.")}</p>
    </div>
    <div class="grid g-2">
      <div class="card reveal" style="border-color:#ffd9cc;background:linear-gradient(180deg,#fff6f2,#fff)">
        <img src="{UIPATH_LOCKUP}" alt="UiPath Authorized Partner" style="height:44px;width:auto;margin-bottom:20px">
        <h3>{dual("Autoryzowany Partner UiPath","UiPath Authorized Partner")}</h3>
        <p style="margin-bottom:12px">{dual("UiPath — lider w agentic business orchestration. Wdrażamy roboty programowe i agentów AI, którzy działają w synchronizacji z ludźmi i Twoimi systemami.","UiPath — a leader in agentic business orchestration. We build software robots and AI agents that work in sync with people and your systems.")}</p>
        <p class="eyebrow eyebrow--uipath" style="margin:14px 0 10px">{dual("Co to daje","What you gain")}</p>
        {_checklist([
          ("Automatyzacja na platformie klasy enterprise — bezpieczna i skalowalna","Automation on an enterprise-grade platform — secure and scalable"),
          ("Agenci, roboty i ludzie działający w jednym rytmie","Agents, robots and people working in one rhythm"),
          ("Sprawdzone wdrożenia — od pilotażu do skalowania","Proven rollouts — from piloting to scaling")])}
      </div>
      <div class="card reveal">
        <span class="partner__badge" style="background:#0faaff;margin-bottom:18px">SAP</span>
        <h3>SAP</h3>
        <p style="margin-bottom:12px"><strong>Partner · Open Ecosystem</strong></p>
        <p>{dual("Głęboka znajomość ekosystemu SAP pozwala nam automatyzować i wspierać procesy ściśle powiązane z Twoim systemem ERP.","Deep knowledge of the SAP ecosystem lets us automate and support processes tightly connected to your ERP.")}</p>
      </div>
      <div class="card reveal" style="border-color:var(--mint-100);background:linear-gradient(180deg,var(--mint-050),#fff)">
        <span class="partner__badge" style="background:var(--navy);margin-bottom:18px">KYP</span>
        <h3>KYP.ai</h3>
        <p style="margin-bottom:12px"><strong>{dual("Partner Process Intelligence","Process Intelligence Partner")}</strong></p>
        <p style="margin-bottom:12px">{dual("KYP.ai to platforma process & task mining, która pokazuje, jak naprawdę przebiegają procesy w organizacji. Dzięki partnerstwu nie zgadujemy, co automatyzować — wiemy to na podstawie danych.","KYP.ai is a process & task mining platform that reveals how processes really run in an organisation. Thanks to this partnership we don't guess what to automate — we know it from data.")}</p>
        <p class="eyebrow" style="margin:14px 0 10px">{dual("Co to daje","What you gain")}</p>
        {_checklist([
          ("Precyzyjne wskazanie procesów o największym potencjale","Pinpointing the processes with the biggest potential"),
          ("Pomiar realnego potencjału oszczędności przed wdrożeniem","Measuring real savings potential before we build"),
          ("Priorytetyzacja automatyzacji według ROI","Prioritising automations by ROI"),
          ("Ciągły pomiar efektów i produktywności","Continuous measurement of impact and productivity"),
          ("Szybszy i pewniejszy zwrot z inwestycji","A faster, more certain return on investment")])}
      </div>
      <div class="card reveal">
        <span class="partner__badge" style="background:#0a7d5a;margin-bottom:18px">P</span>
        <h3>Pipedrive</h3>
        <p style="margin-bottom:12px"><strong>{dual("Partner (Solution Provider)","Partner (Solution Provider)")}</strong></p>
        <p style="margin-bottom:12px">{dual("Pipedrive to sprzedażowy CRM. Jako partner wdrażamy, konfigurujemy i integrujemy Pipedrive oraz automatyzujemy procesy sprzedażowe — łącząc CRM z Twoimi systemami i robotami.","Pipedrive is a sales CRM. As a partner we implement, configure and integrate Pipedrive and automate sales processes — connecting the CRM with your systems and robots.")}</p>
        <p class="eyebrow" style="margin:14px 0 10px">{dual("Co to daje","What you gain")}</p>
        {_checklist([
          ("Wdrożenie i konfiguracja CRM pod Twój proces sprzedaży","CRM implementation and configuration for your sales process"),
          ("Integracje z SAP, innymi systemami i automatyzacją","Integrations with SAP, other systems and automation"),
          ("Szkolenia i wsparcie użytkowników","User training and support"),
          ("Szybszy i bardziej przewidywalny pipeline sprzedaży","A faster, more predictable sales pipeline")])}
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="max-width:56ch;margin-bottom:40px" class="reveal">
      <p class="eyebrow">{dual("Nasze wartości","Our values")}</p>
      <h2>{dual("Jak pracujemy","The way we work")}</h2>
    </div>
    <div class="grid g-3">
      <div class="card reveal"><div class="card__ico">{I["spark"]}</div><h3>{dual("Nastawienie na rezultat","Outcome-driven")}</h3><p>{dual("Mierzymy sukces oszczędnościami i realną poprawą procesów u klienta.","We measure success by savings and real process improvement for the client.")}</p></div>
      <div class="card reveal"><div class="card__ico">{I["shield"]}</div><h3>{dual("Partnerstwo i transparentność","Partnership & transparency")}</h3><p>{dual("Regularne raportowanie i pełna widoczność działań — działamy jak część Twojego zespołu.","Regular reporting and full visibility — we act as part of your team.")}</p></div>
      <div class="card reveal"><div class="card__ico">{I["globe"]}</div><h3>{dual("Zasięg międzynarodowy","International reach")}</h3><p>{dual("Dostarczamy ekspertów i rozwiązania w wielu krajach Europy.","We deliver experts and solutions across many European countries.")}</p></div>
    </div>
  </div>
</section>

<section class="section bg-paper">
  <div class="container"><div class="split" style="align-items:center">
    <div class="reveal">
      <p style="font-family:var(--font-display);font-size:clamp(1.3rem,2.2vw,1.8rem);line-height:1.45;color:var(--ink);margin-bottom:20px">{dual("„Konsultanci Mientha należą do absolutnie najlepszych — wysoko wykwalifikowani, profesjonalni i skuteczni od pierwszego dnia. Odegrali kluczową rolę w naszym sukcesie.”","“Mientha’s consultants are among the very best — highly skilled, professional and immediately effective. They’ve played a key role in driving our success.”")}</p>
      <p class="muted" style="margin:0;font-weight:600">IT &amp; Data Director · {dual("klient z sektora FMCG","FMCG-sector client")}</p>
    </div>
    <div class="reveal"><a href="kontakt.html" class="btn btn--primary">{dual("Poznajmy się","Let's get in touch")} {I["arrow"]}</a></div>
  </div></div>
</section>
'''
PAGES["o-nas.html"] = ("o-nas.html","O nas — Mientha","About — Mientha", onas)

# ============================================================ KONTAKT
def ci(icon, b_pl,b_en, span):
    return f'''<div class="contact-item"><div class="ci">{I[icon]}</div><div><b>{dual(b_pl,b_en)}</b><span>{span}</span></div></div>'''

kontakt = pagehero(
  "Kontakt","Contact","Kontakt","Contact",
  "Porozmawiajmy o Twoim procesie",
  "Let's talk about your process",
  "Umów bezpłatną konsultację. Odpowiemy na wiadomość w ciągu jednego dnia roboczego.",
  "Book a free consultation. We'll reply within one business day.")
kontakt += f'''
<section class="section">
  <div class="container split" style="align-items:flex-start">
    <div class="reveal">
      <p class="eyebrow">{dual("Dane kontaktowe","Contact details")}</p>
      <h2 style="margin-bottom:26px">Mientha</h2>
      {ci("mail","E-mail","E-mail","contact@mientha.com")}
      {ci("tel","Telefon","Phone","+48 22 290 27 27")}
      {ci("pin","Adres","Address","ul. Puławska 39 lok. 40, 02-508 Warszawa, Polska")}
      <div style="margin:30px 0;height:1px;background:var(--line)"></div>
      <p class="eyebrow">{dual("Kontakt bezpośredni","Direct contact")}</p>
      <div style="display:flex;gap:16px;align-items:center">
        <div style="width:56px;height:56px;border-radius:50%;background:var(--navy);color:#fff;display:grid;place-items:center;font-family:var(--font-display);font-weight:700">PK</div>
        <div>
          <b style="font-family:var(--font-display);font-size:1.05rem;display:block">Paweł Kacprowicz</b>
          <span class="muted" style="display:block;margin-bottom:4px">Chief Executive Officer</span>
          <a href="mailto:pawel.kacprowicz@mientha.com" class="arrowlink" style="font-size:.92rem">pawel.kacprowicz@mientha.com</a><br>
          <a href="tel:+48515515727" class="muted" style="font-size:.92rem">+48 515 515 727</a>
        </div>
      </div>
      <div class="badge-row" style="margin-top:30px;display:flex;gap:12px;flex-wrap:wrap">
        <span class="chip"><span class="dot"></span>UiPath Authorized Partner</span>
        <span class="chip"><span class="dot"></span>SAP Partner</span>
      </div>
    </div>

    <div class="panel reveal">
      <h3 style="margin-bottom:6px">{dual("Napisz do nas","Send us a message")}</h3>
      <p class="muted" style="font-size:.95rem;margin-bottom:22px">{dual("Wypełnij formularz — wrócimy z odpowiedzią najszybciej, jak to możliwe.","Fill in the form — we'll get back to you as soon as possible.")}</p>
      <form onsubmit="event.preventDefault(); this.style.display='none'; document.getElementById('thanks').style.display='block';">
        <div class="grid g-2" style="gap:16px">
          <div class="field"><label for="f-name">{dual("Imię i nazwisko","Full name")}</label><input id="f-name" required type="text" name="name" autocomplete="name"></div>
          <div class="field"><label for="f-company">{dual("Firma","Company")}</label><input id="f-company" type="text" name="company" autocomplete="organization"></div>
        </div>
        <div class="grid g-2" style="gap:16px">
          <div class="field"><label for="f-email">{dual("Służbowy e-mail","Work e-mail")}</label><input id="f-email" required type="email" name="email" autocomplete="email"></div>
          <div class="field"><label for="f-phone">{dual("Telefon","Phone")}</label><input id="f-phone" type="tel" name="phone" autocomplete="tel"></div>
        </div>
        <div class="field"><label for="f-topic">{dual("Czym jesteś zainteresowany?","What are you interested in?")}</label>
          <select id="f-topic" name="topic">
            <option>{dual("Automatyzacja RPA / Agentic AI","RPA / Agentic AI automation")}</option>
            <option>{dual("Rozliczanie kierowców (transport)","Driver settlement (transport)")}</option>
            <option>{dual("BPO / outsourcing procesów","BPO / process outsourcing")}</option>
            <option>{dual("AMS — utrzymanie aplikacji","AMS — application management")}</option>
            <option>{dual("Eksperci / rekrutacja IT","IT experts / talent")}</option>
            <option>{dual("Inne","Other")}</option>
          </select>
        </div>
        <div class="field"><label for="f-message">{dual("Wiadomość","Message")}</label><textarea id="f-message" rows="4" name="message"></textarea></div>
        <button class="btn btn--mint" type="submit" style="width:100%;justify-content:center">{dual("Wyślij wiadomość","Send message")} {I["arrow"]}</button>
        <p class="muted" style="font-size:.8rem;margin-top:14px">{dual("Wysyłając formularz akceptujesz przetwarzanie danych w celu kontaktu.","By submitting, you agree to your data being processed for contact purposes.")}</p>
      </form>
      <div id="thanks" style="display:none;text-align:center;padding:30px 0">
        <div class="card__ico" style="margin:0 auto 16px;width:56px;height:56px">{I["shield"]}</div>
        <h3>{dual("Dziękujemy!","Thank you!")}</h3>
        <p class="muted">{dual("Wiadomość została zapisana. Skontaktujemy się w ciągu jednego dnia roboczego.","Your message has been captured. We'll be in touch within one business day.")}</p>
        <p class="muted" style="font-size:.8rem">{dual("(To demo formularza — podłącz swój backend lub usługę e-mail.)","(This is a demo form — connect your backend or e-mail service.)")}</p>
      </div>
    </div>
  </div>
</section>
'''
PAGES["kontakt.html"] = ("kontakt.html","Kontakt — Mientha","Contact — Mientha", kontakt)

# ============================================================ FMCG CASE STUDIES
CASES_FMCG = [
 dict(slug="rozliczenia-vat", icon="doc",
   t_pl="Automatyczne rozliczenia VAT", t_en="Automated VAT settlements",
   lead_pl="Koniec z ręcznym przepisywaniem danych między systemami a formularzami VAT.",
   lead_en="No more manually re-typing data between systems and VAT forms.",
   prob_pl="Comiesięczne rozliczenia VAT w wielu krajach oznaczały godziny żmudnego kopiowania danych do arkuszy i formularzy. Przy takiej skali łatwo o pomyłkę i opóźnienie deklaracji.",
   prob_en="Monthly VAT settlements across many countries meant hours of tedious copying of data into spreadsheets and forms. At that scale, mistakes and late filings are almost inevitable.",
   did_pl="Uruchomiliśmy „cyfrowego pracownika”, który sam pobiera dane, przygotowuje kalkulacje według reguł klienta, wypełnia deklaracje VAT i weryfikuje numery kontrahentów, a na koniec archiwizuje dokumenty i przygotowuje płatności podatkowe do zatwierdzenia jednym kliknięciem.",
   did_en="We deployed a “digital worker” that pulls the data itself, prepares calculations per the client’s rules, fills in VAT returns and verifies counterparties, then archives the documents and prepares tax payments for one-click approval.",
   ben=[("Deklaracje gotowe do wysłania bez pracy ręcznej","Returns ready to file with no manual work"),
        ("Mniej błędów i kosztownych korekt","Fewer errors and costly corrections"),
        ("Terminowość i spokój podczas audytów","On-time filing and audit peace of mind"),
        ("Łatwe skalowanie na kolejne kraje i spółki","Easy to scale to more countries and entities")],
   res=[("Krótszy czas zamknięcia VAT","Shorter VAT close"),
        ("Niższe ryzyko kar podatkowych","Lower risk of tax penalties"),
        ("Odciążony zespół finansowy","A relieved finance team")]),
 dict(slug="przypisanie-windykatora", icon="chart",
   t_pl="Sprawy windykacyjne trafiają od razu do właściwej osoby", t_en="Collections cases routed to the right person instantly",
   lead_pl="Zgłoszenia dotyczące należności trafiają natychmiast do właściwego opiekuna — bez ręcznego sortowania.",
   lead_en="Receivables cases reach the right owner instantly — no manual sorting.",
   prob_pl="Zgłoszenia dotyczące należności trzeba było ręcznie przypisywać do odpowiednich osób w różnych regionach. To opóźniało start windykacji i rodziło błędy.",
   prob_en="Receivables cases had to be assigned by hand to the right people across regions. That delayed the start of collections and caused mistakes.",
   did_pl="Robot rozpoznaje, kogo dotyczy dana sprawa, i automatycznie kieruje ją do właściwego windykatora lub zespołu w danym regionie — natychmiast po zgłoszeniu i przez całą dobę.",
   did_en="A robot recognises who a case concerns and automatically routes it to the right collections owner or regional team — instantly and around the clock.",
   ben=[("Koniec ręcznego rozdzielania spraw","No more manual case sorting"),
        ("Szybszy start działań windykacyjnych","A faster start to collections"),
        ("Mniej błędnych przypisań i poprawek","Fewer misroutes and rework"),
        ("Jednolity proces we wszystkich krajach","One consistent process across countries")],
   res=[("Szybszy spływ należności (DSO)","Faster cash collection (DSO)"),
        ("Wyższa produktywność zespołu","Higher team productivity"),
        ("Krótszy czas obsługi sprawy","Shorter case handling time")]),
 dict(slug="zwalnianie-zamowien", icon="shield",
   t_pl="Szybsze zwalnianie zablokowanych zamówień", t_en="Faster release of blocked orders",
   lead_pl="Prawidłowe zamówienia ruszają szybciej — a firma szybciej zarabia.",
   lead_en="Valid orders move faster — so the company earns faster.",
   prob_pl="Zamówienia blokowane przez kontrolę kredytową czekały na ręczną weryfikację. Każda godzina zwłoki to opóźniona sprzedaż i przychód.",
   prob_en="Orders blocked by credit control waited for manual review. Every hour of delay meant postponed sales and revenue.",
   did_pl="Robot co kilka minut wykrywa zablokowane zamówienia, zbiera potrzebne informacje, wykonuje wstępne sprawdzenia i uruchamia proces akceptacji zgodnie z zasadami klienta — a po decyzji odblokowuje zamówienie.",
   did_en="Every few minutes a robot detects blocked orders, gathers the needed information, runs pre-checks and starts the approval process per the client’s rules — then releases the order once a decision is made.",
   ben=[("Szybsze zwalnianie prawidłowych zamówień","Faster release of valid orders"),
        ("Mniej ręcznej weryfikacji danych","Less manual data checking"),
        ("Ustandaryzowana ścieżka akceptacji","A standardised approval path"),
        ("Mniej utraconych przychodów przez opóźnienia","Fewer lost revenues from delays")],
   res=[("Szybsza realizacja przychodów","Faster revenue realisation"),
        ("Krótszy czas obsługi","Shorter cycle time"),
        ("Lepsza kontrola ryzyka kredytowego","Better credit-risk control")]),
 dict(slug="zmiana-terminu-platnosci", icon="clock",
   t_pl="Sprawna obsługa zmiany terminu płatności", t_en="Smooth payment-term changes",
   lead_pl="Wnioski klientów o nowy termin płatności obsłużone szybko i pod pełną kontrolą.",
   lead_en="Customer requests for new payment terms handled quickly and in full control.",
   prob_pl="Obsługa próśb o zmianę terminu płatności wymagała ręcznego zbierania danych i pilnowania kolejnych akceptacji.",
   prob_en="Handling requests to change payment terms required manual data gathering and chasing approvals.",
   did_pl="Robot uzupełnia zgłoszenie o wszystkie potrzebne dane i prowadzi je przez proces akceptacji zgodnie z zasadami klienta — aż do decyzji i zamknięcia sprawy.",
   did_en="A robot enriches the case with all the data needed and drives it through the approval process per the client’s rules — all the way to a decision and closure.",
   ben=[("Szybsza obsługa wniosków","Faster request handling"),
        ("Lepsze doświadczenie klienta i elastyczność","Better customer experience and flexibility"),
        ("Mniej pracy ręcznej","Less manual work"),
        ("Lepsza kontrola nad przepływem gotówki","Better control over cash flow")],
   res=[("Lepsze zarządzanie terminami (DSO)","Better terms management (DSO)"),
        ("Wyższa satysfakcja klienta","Higher customer satisfaction"),
        ("Przewidywalny cash flow","Predictable cash flow")]),
 dict(slug="limity-kredytowe", icon="bank",
   t_pl="Szybkie i spójne decyzje kredytowe", t_en="Fast, consistent credit decisions",
   lead_pl="Sprawne zarządzanie limitami kredytowymi — wsparcie sprzedaży bez wzrostu ryzyka.",
   lead_en="Streamlined credit-limit management — supporting sales without adding risk.",
   prob_pl="Zapytania o aktualny limit kredytowy oraz wnioski o jego zwiększenie lub zmniejszenie wymagały ręcznego zbierania danych finansowych i długo czekały na decyzję.",
   prob_en="Requests for a current credit limit and applications to increase or decrease it required manual gathering of financial data and waited a long time for a decision.",
   did_pl="Robot automatycznie pobiera aktualne dane o kliencie i jego historii, uzupełnia zgłoszenie i przekazuje sprawę do decyzji — obsługując zarówno proste zapytania, jak i wnioski o zmianę limitu.",
   did_en="A robot automatically retrieves up-to-date client and history data, enriches the case and passes it for decision — handling both simple enquiries and limit-change applications.",
   ben=[("Szybsze decyzje kredytowe","Faster credit decisions"),
        ("Skuteczniejsze wsparcie sprzedaży bez wzrostu ryzyka","Stronger sales support without added risk"),
        ("Automatyczne pobieranie danych finansowych","Automated financial-data retrieval"),
        ("Jednolite zasady na wszystkich rynkach","Uniform rules across all markets")],
   res=[("Szybszy onboarding klientów i przychody","Faster client onboarding and revenue"),
        ("Kontrola ryzyka złych długów","Bad-debt risk under control"),
        ("Krótszy czas decyzji kredytowej","Shorter credit-decision time")]),
 dict(slug="zapytania-p2p", icon="mail",
   t_pl="Automatyczna obsługa zapytań P2P", t_en="Automated P2P query handling",
   lead_pl="Kopie faktur, statusy i zestawienia dostarczane natychmiast — przez całą dobę.",
   lead_en="Invoice copies, statuses and statements delivered instantly — around the clock.",
   prob_pl="Zespoły i dostawcy zasypywali dział rozliczeń powtarzalnymi prośbami: kopia faktury, status płatności, zestawienie konta. To wiązało ludzi i tworzyło zaległości.",
   prob_en="Teams and suppliers flooded the finance team with repetitive requests: invoice copies, payment status, account statements. That tied up people and created backlogs.",
   did_pl="Robot odbiera zapytanie, znajduje potrzebny dokument lub informację i odsyła odpowiedź użytkownikowi — automatycznie i bez przerw, 24/7.",
   did_en="A robot receives the query, finds the needed document or information and sends the answer back to the user — automatically and without interruption, 24/7.",
   ben=[("Natychmiastowe odpowiedzi na typowe zapytania","Instant answers to common queries"),
        ("Koniec powtarzalnej pracy ręcznej","An end to repetitive manual work"),
        ("Dostępność usługi 24/7","A service available 24/7"),
        ("Mniejszy backlog w zespołach rozliczeń","Smaller backlog in finance teams")],
   res=[("Wyższa produktywność","Higher productivity"),
        ("Niższy koszt obsługi zapytania","Lower cost per query"),
        ("Zadowoleni użytkownicy i dostawcy","Happier users and suppliers")]),
 dict(slug="monitoring-wyciagow", icon="plug",
   t_pl="Monitoring wyciągów bankowych i księgowania wpłat", t_en="Bank-statement monitoring & cash application",
   lead_pl="Brakujące wyciągi wykrywane proaktywnie — płynne księgowanie wpłat.",
   lead_en="Missing statements caught proactively — smooth cash application.",
   prob_pl="Brakujące lub opóźnione wyciągi bankowe potrafiły zatrzymać księgowanie wpłat i psuć obraz płynności — a wykrywano je zwykle za późno.",
   prob_en="Missing or delayed bank statements could stall cash application and distort the liquidity picture — and were usually spotted too late.",
   did_pl="Robot analizuje raporty z systemu bankowego, sam odróżnia realne braki od dni wolnych i — gdy wyciąg powinien już być dostępny — automatycznie zakłada zgłoszenie i kieruje je do właściwej osoby.",
   did_en="A robot analyses reports from the banking system, tells real gaps from non-working days and — when a statement should already be available — automatically raises a ticket and routes it to the right person.",
   ben=[("Proaktywne wykrywanie braków","Proactive gap detection"),
        ("Szybsze rozwiązywanie problemów","Faster problem resolution"),
        ("Ciągłość procesu księgowania wpłat","Continuity of cash application"),
        ("Mniej przestojów w procesach finansowych","Fewer stoppages in finance processes")],
   res=[("Szybsze księgowanie wpłat (DSO)","Faster cash application (DSO)"),
        ("Lepsza widoczność przepływów","Better cash-flow visibility"),
        ("Niższe ryzyko operacyjne","Lower operational risk")]),
 dict(slug="uzgadnianie-sald", icon="layers",
   t_pl="Automatyczne uzgadnianie sald bankowych", t_en="Automated bank-balance reconciliation",
   lead_pl="Salda między systemami zawsze zgodne — rozbieżności wychwycone od razu.",
   lead_en="Balances always in sync between systems — discrepancies caught at once.",
   prob_pl="Ręczne porównywanie sald między dwoma systemami bankowymi było czasochłonne, a rozbieżności wychodziły na jaw za późno.",
   prob_en="Manually comparing balances between two banking systems was time-consuming, and discrepancies surfaced too late.",
   did_pl="Robot automatycznie porównuje salda dla każdego rachunku, a w razie różnicy zakłada zgłoszenie i wskazuje osobę lub zespół odpowiedzialny za wyjaśnienie.",
   did_en="A robot automatically compares balances for every account and, if there is a difference, raises a ticket and points to the person or team responsible for resolving it.",
   ben=[("Automatyczna kontrola zgodności sald","Automatic balance-consistency checks"),
        ("Wczesne wykrywanie różnic","Early detection of differences"),
        ("Mniej rozbieżności finansowych","Fewer financial discrepancies"),
        ("Gotowość do audytu","Audit readiness")],
   res=[("Wyższa dokładność danych finansowych","Higher financial-data accuracy"),
        ("Niższe ryzyko audytowe","Lower audit risk"),
        ("Krótszy czas uzgodnień","Shorter reconciliation time")]),
 dict(slug="hr-masowa-aktualizacja", icon="talent",
   t_pl="Masowa aktualizacja danych pracowniczych", t_en="Employee data mass update",
   lead_pl="Setki zmian danych wykonane szybko, bezpiecznie i bez błędów.",
   lead_en="Hundreds of data changes done quickly, safely and error-free.",
   prob_pl="Masowe zmiany danych pracowników w systemie HR to żmudne i wrażliwe zadanie, w którym łatwo o pomyłkę.",
   prob_en="Bulk changes to employee data in the HR system are a tedious, sensitive task where mistakes come easily.",
   did_pl="Robot pobiera zgłoszenie z plikiem zmian, weryfikuje jego zakres (z wykluczeniem kadry zarządzającej), przygotowuje dane i realizuje masową aktualizację, a na końcu raportuje wynik do zespołu HR.",
   did_en="A robot picks up the request with the change file, verifies its scope (excluding management), prepares the data and performs the bulk update, then reports the result back to HR.",
   ben=[("Szybka i bezpieczna aktualizacja masowa","Fast, safe bulk updates"),
        ("Eliminacja błędów ręcznego wprowadzania","No manual data-entry errors"),
        ("Kontrola nad wrażliwymi danymi","Control over sensitive data"),
        ("Pełny ślad i raport z operacji","Full audit trail and reporting")],
   res=[("Wyższa produktywność HR","Higher HR productivity"),
        ("Lepsza jakość danych","Better data quality"),
        ("Zgodność i mniej korekt","Compliance and fewer corrections")]),
 dict(slug="hr-onboarding", icon="spark",
   t_pl="Automatyczny onboarding nowego pracownika", t_en="Automated new-hire onboarding",
   lead_pl="Nowi pracownicy gotowi do pracy szybciej — mniej papierologii po stronie HR.",
   lead_en="New hires ready to work sooner — less paperwork for HR.",
   prob_pl="Zakładanie i aktualizacja danych nowych pracowników wymagało ręcznego przetwarzania plików i wielu kroków między systemami.",
   prob_en="Creating and updating new-hire records required manual file processing and many steps across systems.",
   did_pl="Robot pobiera i bezpiecznie przetwarza dane z systemu kadrowego, archiwizuje je i zakłada lub aktualizuje pracownika w systemie HR — od nowego zatrudnienia, przez zmiany, po zakończenie współpracy.",
   did_en="A robot retrieves and securely processes data from the payroll system, archives it and creates or updates the employee in the HR system — from new hire, through changes, to offboarding.",
   ben=[("Zautomatyzowany przepływ danych onboardingowych","Automated onboarding data flow"),
        ("Szybsza aktywacja pracowników w systemach","Faster activation of employees in systems"),
        ("Odciążenie HR z pracy administracyjnej","HR freed from admin work"),
        ("Bezpieczne przetwarzanie danych","Secure data processing")],
   res=[("Krótszy czas onboardingu","Shorter time-to-onboard"),
        ("Lepsze doświadczenie pracownika","Better employee experience"),
        ("Niższe koszty operacyjne HR","Lower HR operating costs")]),
]

def cs_slug(c): return "cs-"+c["slug"]+".html"

def _checklist(items):
    return '<ul class="checklist">' + "".join(f'<li>{dual(a,b)}</li>' for a,b in items) + '</ul>'

def cs_page(c):
    body = f'''<section class="pagehero" style="background:linear-gradient(180deg,var(--mint-050),#fff)">
  <div class="container">
    <p class="crumb"><a href="index.html">{dual("Start","Home")}</a> &middot; <a href="case-studies.html">Case studies</a> &middot; <a href="fmcg.html">FMCG</a> &middot; {dual(c["t_pl"],c["t_en"])}</p>
    <span class="tag">{dual("FMCG · Case study","FMCG · Case study")}</span>
    <h1 style="max-width:20ch">{dual(c["t_pl"],c["t_en"])}</h1>
    <p class="lead">{dual(c["lead_pl"],c["lead_en"])}</p>
    <div class="hero__cta" style="margin-top:24px">
      <a href="kontakt.html" class="btn btn--mint">{dual("Umów rozmowę","Book a call")} {I["arrow"]}</a>
      <a href="fmcg.html" class="btn btn--ghost">{dual("Wszystkie case studies FMCG","All FMCG case studies")}</a>
    </div>
  </div>
</section>

<section class="section--tight bg-paper">
  <div class="container" style="max-width:70ch">
    <p class="eyebrow">{dual("Wyzwanie","The challenge")}</p>
    <p class="lead" style="color:var(--ink-2)">{dual(c["prob_pl"],c["prob_en"])}</p>
  </div>
</section>

<section class="section">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">{dual("Co zrobiliśmy","What we did")}</p>
      <h2>{dual("Rozwiązanie w praktyce","The solution in practice")}</h2>
      <p class="lead measure" style="margin-bottom:26px">{dual(c["did_pl"],c["did_en"])}</p>
      <p class="eyebrow" style="margin-bottom:14px">{dual("Efekty biznesowe","Business benefits")}</p>
      {_checklist(c["ben"])}
    </div>
    <div class="panel panel--ink reveal">
      <p class="eyebrow" style="margin-bottom:18px">{dual("Wpływ na wyniki","Impact on results")}</p>
      {_checklist(c["res"])}
      <div class="chips" style="margin-top:26px">
        <span class="chip"><span class="dot"></span>UiPath</span>
        <span class="chip"><span class="dot"></span>{dual("Tryb 24/7","24/7 mode")}</span>
        <span class="chip"><span class="dot"></span>SAP · ServiceNow</span>
      </div>
    </div>
  </div>
</section>

<section class="section bg-paper">
  <div class="container"><div class="cta reveal">
    <h2 style="max-width:24ch;margin-inline:auto">{dual("Podobny proces spowalnia Twój zespół?","A similar process slowing your team down?")}</h2>
    <p class="lead" style="margin-inline:auto;color:#aeb8bf;margin-bottom:30px">{dual("Pokażemy, jak szybko możemy go zautomatyzować u Ciebie.","We'll show how quickly we can automate it for you.")}</p>
    <a href="kontakt.html" class="btn btn--mint">{dual("Umów rozmowę","Book a call")} {I["arrow"]}</a>
  </div></div>
</section>
'''
    PAGES[cs_slug(c)] = ("case-studies.html", c["t_pl"]+" — Mientha", c["t_en"]+" — Mientha", body)

for _c in CASES_FMCG:
    cs_page(_c)

# ---- FMCG hub page
def _fmcg_card(c):
    return f'''<a class="card card--link reveal" href="{cs_slug(c)}">
      <div class="card__ico">{I[c["icon"]]}</div>
      <h3>{dual(c["t_pl"],c["t_en"])}</h3>
      <p>{dual(c["lead_pl"],c["lead_en"])}</p>
      <div style="margin-top:16px"><span class="arrowlink">{dual("Zobacz case study","View case study")} {I["arrow"]}</span></div>
    </a>'''

fmcg = pagehero(
  "FMCG","FMCG","Branża · FMCG i retail","Industry · FMCG & retail",
  "Automatyzacja dla liderów FMCG",
  "Automation for FMCG leaders",
  "Dla firm z branży FMCG zautomatyzowaliśmy kilkanaście procesów finansowych, kredytowych i kadrowych — od rozliczeń VAT po onboarding pracowników. Poniżej realne przykłady wdrożeń wraz z korzyściami biznesowymi.",
  "For FMCG companies we have automated more than a dozen finance, credit and HR processes — from VAT settlements to employee onboarding. Below are real examples of our work and the business benefits they delivered.")
fmcg += f'''
<section class="section--tight" style="border-block:1px solid var(--line)">
  <div class="container" style="display:flex;flex-wrap:wrap;gap:24px;justify-content:space-between;align-items:center">
    <p class="muted" style="margin:0;font-weight:600;max-width:40ch">{dual("Procesy wysokiego wolumenu w finansach, obsłudze klienta i HR — obszary, w których automatyzacja daje najszybszy zwrot.","High-volume processes in finance, customer service and HR — where automation delivers the fastest return.")}</p>
    <div class="chips">
      <span class="chip"><span class="dot"></span>{dual("Finanse i należności","Finance & receivables")}</span>
      <span class="chip"><span class="dot"></span>{dual("Zakupy i płatności","Procurement & payments")}</span>
      <span class="chip"><span class="dot"></span>HR</span>
      <span class="chip"><span class="dot"></span>Treasury</span>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="max-width:58ch;margin-bottom:40px" class="reveal">
      <p class="eyebrow">{dual("Case studies","Case studies")}</p>
      <h2>{dual("Wybrane wdrożenia automatyzacji","Selected automation deliveries")}</h2>
      <p class="lead">{dual("Każdy przykład opisujemy prosto: jaki był problem, co zrobiliśmy i co zyskał klient.","We describe each example simply: what the problem was, what we did and what the client gained.")}</p>
    </div>
    <div class="grid g-3 reveal">
      {"".join(_fmcg_card(c) for c in CASES_FMCG)}
    </div>
    <p class="muted" style="font-size:.82rem;margin-top:26px">{dual("Ze względu na poufność dane klientów zostały zanonimizowane. Przykłady oparte na rzeczywistych wdrożeniach.","For confidentiality, client details have been anonymised. Examples based on real deployments.")}</p>
  </div>
</section>

<section class="section bg-paper">
  <div class="container"><div class="cta reveal">
    <h2 style="max-width:24ch;margin-inline:auto">{dual("Chcesz podobne efekty w swojej firmie FMCG?","Want similar results in your FMCG business?")}</h2>
    <p class="lead" style="margin-inline:auto;color:#aeb8bf;margin-bottom:30px">{dual("Zacznijmy od krótkiej rozmowy o procesie z największym potencjałem.","Let's start with a short talk about the process with the biggest potential.")}</p>
    <a href="kontakt.html" class="btn btn--mint">{dual("Umów rozmowę","Book a call")} {I["arrow"]}</a>
  </div></div>
</section>
'''
PAGES["fmcg.html"] = ("branze.html","FMCG — case studies automatyzacji — Mientha","FMCG — automation case studies — Mientha", fmcg)

# ============================================================ WSPARCIE 24/7
wsparcie = f'''<section class="hero" style="background:radial-gradient(120% 120% at 85% -10%, var(--mint-050) 0%, rgba(233,250,243,0) 45%), var(--white)">
  <div class="container" style="padding-block:clamp(56px,7vw,96px)">
    <p class="crumb"><a href="index.html">{dual("Start","Home")}</a> &middot; <a href="uslugi.html">{dual("Usługi","Services")}</a> &middot; {dual("Wsparcie 24/7","24/7 support")}</p>
    <p class="eyebrow">{dual("Usługa · Dedykowane zespoły","Service · Dedicated teams")}</p>
    <h1 style="max-width:22ch">{dual("Wsparcie 24/7 dla aplikacji krytycznych","24/7 support for business-critical applications")}</h1>
    <p class="lead" style="max-width:64ch">{dual(
      "Zapewniamy całodobowe wsparcie (24/7/365) dla każdej aplikacji krytycznej — w fabrykach i w firmach z dowolnej branży. Budujemy dedykowane zespoły dopasowane do Twoich technologii i przejmujemy odpowiedzialność za ciągłość działania.",
      "We provide round-the-clock support (24/7/365) for any business-critical application — in factories and companies of any industry. We build dedicated teams matched to your technologies and take ownership of keeping them running.")}</p>
    <div class="hero__cta" style="margin-top:26px">
      <a href="kontakt.html" class="btn btn--mint">{dual("Porozmawiajmy o wsparciu","Talk to us about support")} {I["arrow"]}</a>
      <a href="uslugi.html" class="btn btn--ghost">{dual("Wszystkie usługi","All services")}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="max-width:58ch;margin-bottom:40px" class="reveal">
      <p class="eyebrow">{dual("Co oferujemy","What we offer")}</p>
      <h2>{dual("Nieprzerwana opieka nad Twoimi systemami","Uninterrupted care for your systems")}</h2>
    </div>
    <div class="grid g-3">
      <div class="card reveal"><div class="card__ico">{I["clock"]}</div><h3>{dual("Dostępność 24/7/365","24/7/365 availability")}</h3><p>{dual("Wsparcie bez przerw — także w nocy, w weekendy i w święta, gdy przestój kosztuje najwięcej.","Support without breaks — nights, weekends and holidays, when downtime costs the most.")}</p></div>
      <div class="card reveal"><div class="card__ico">{I["talent"]}</div><h3>{dual("Dedykowane zespoły","Dedicated teams")}</h3><p>{dual("Stały zespół znający Twoje aplikacje i procesy, dopasowany do używanych technologii.","A stable team that knows your applications and processes, matched to your technology stack.")}</p></div>
      <div class="card reveal"><div class="card__ico">{I["layers"]}</div><h3>{dual("Poziomy wsparcia L1–L3","L1–L3 support tiers")}</h3><p>{dual("Od pierwszej linii i obsługi zgłoszeń po głęboką diagnostykę i rozwój — jedna, spójna usługa.","From first line and ticket handling to deep diagnostics and enhancements — one coherent service.")}</p></div>
      <div class="card reveal"><div class="card__ico">{I["chart"]}</div><h3>{dual("Proaktywny monitoring","Proactive monitoring")}</h3><p>{dual("Wykrywamy problemy, zanim zauważą je użytkownicy — i reagujemy, zanim urosną.","We catch problems before users do — and act before they grow.")}</p></div>
      <div class="card reveal"><div class="card__ico">{I["shield"]}</div><h3>{dual("Zarządzanie incydentami","Incident management")}</h3><p>{dual("Uporządkowana obsługa incydentów, problemów i zmian, z jasną komunikacją i eskalacją.","Structured incident, problem and change handling, with clear communication and escalation.")}</p></div>
      <div class="card reveal"><div class="card__ico">{I["doc"]}</div><h3>{dual("SLA i raportowanie","SLA & reporting")}</h3><p>{dual("Jasne zobowiązania SLA i regularne raporty — pełna transparentność jakości usługi.","Clear SLA commitments and regular reports — full transparency of service quality.")}</p></div>
    </div>
  </div>
</section>

<section class="section bg-paper">
  <div class="container">
    <div style="max-width:60ch;margin-bottom:40px" class="reveal">
      <p class="eyebrow">{dual("Transfer wiedzy","Knowledge transfer")}</p>
      <h2>{dual("Zarządzany transfer wiedzy — od zera do pełnej odpowiedzialności","Managed knowledge transfer — from zero to full ownership")}</h2>
      <p class="lead">{dual("Zanim przejmiemy wsparcie, przeprowadzamy ustrukturyzowany transfer wiedzy. Dzięki temu świadczymy usługę na najwyższym poziomie od pierwszego dnia steady state.","Before we take over support, we run a structured knowledge transfer. That lets us deliver at the highest level from day one of steady state.")}</p>
    </div>
    <div class="steps reveal">
      <div class="step"><div class="step__n"></div><div><h4>{dual("Discovery i dokumentacja","Discovery & documentation")}</h4><p>{dual("Poznajemy aplikacje, procesy i ryzyka; tworzymy lub uzupełniamy bazę wiedzy i procedury.","We learn the applications, processes and risks; we build or complete the knowledge base and runbooks.")}</p></div></div>
      <div class="step"><div class="step__n"></div><div><h4>{dual("Shadowing","Shadowing")}</h4><p>{dual("Nasz zespół uczy się od Twoich ekspertów, obserwując bieżącą pracę i realne zgłoszenia.","Our team learns from your experts by observing day-to-day work and real tickets.")}</p></div></div>
      <div class="step"><div class="step__n"></div><div><h4>{dual("Reverse shadowing","Reverse shadowing")}</h4><p>{dual("Przejmujemy zadania pod nadzorem Twoich ekspertów, potwierdzając gotowość zespołu.","We take over tasks under your experts' supervision, proving the team's readiness.")}</p></div></div>
      <div class="step"><div class="step__n"></div><div><h4>{dual("Steady state","Steady state")}</h4><p>{dual("Świadczymy usługę samodzielnie i z pełną odpowiedzialnością — z ciągłym doskonaleniem.","We run the service independently and with full ownership — with continuous improvement.")}</p></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="max-width:60ch;margin-bottom:40px" class="reveal">
      <p class="eyebrow">{dual("Standardy światowej klasy","World-class standards")}</p>
      <h2>{dual("Pracujemy według najlepszych standardów w branży","We work to the best standards in the industry")}</h2>
      <p class="lead">{dual("Nasze wsparcie opieramy na uznanych, międzynarodowych standardach zarządzania usługami, bezpieczeństwa i niezawodności.","Our support is built on recognised international standards for service management, security and reliability.")}</p>
    </div>
    <div class="grid g-3">
      <div class="card reveal"><span class="tag">ITIL 4</span><h3>{dual("Zarządzanie usługami IT","IT service management")}</h3><p>{dual("Najlepsze praktyki obsługi incydentów, problemów i zmian — uporządkowana, powtarzalna usługa.","Best practices for incident, problem and change management — an orderly, repeatable service.")}</p></div>
      <div class="card reveal"><span class="tag">ISO/IEC 20000</span><h3>{dual("Standard usług IT","IT service standard")}</h3><p>{dual("Międzynarodowy standard zarządzania usługami IT — gwarancja jakości i mierzalności.","The international standard for IT service management — assuring quality and measurability.")}</p></div>
      <div class="card reveal"><span class="tag">ISO/IEC 27001</span><h3>{dual("Bezpieczeństwo informacji","Information security")}</h3><p>{dual("Ochrona danych i systemów zgodnie z uznanym standardem bezpieczeństwa informacji.","Protecting data and systems in line with the recognised information-security standard.")}</p></div>
      <div class="card reveal"><span class="tag">SRE</span><h3>{dual("Niezawodność (Site Reliability)","Reliability (Site Reliability)")}</h3><p>{dual("Praktyki SRE: automatyzacja utrzymania, mierzalna niezawodność i minimalizacja przestojów.","SRE practices: automating operations, measurable reliability and minimising downtime.")}</p></div>
      <div class="card reveal"><span class="tag">Follow-the-sun</span><h3>{dual("Wsparcie w wielu strefach czasu","Multi-timezone support")}</h3><p>{dual("Zespoły w różnych strefach czasowych zapewniają płynne, całodobowe wsparcie bez nocnych dyżurów po Twojej stronie.","Teams across time zones deliver smooth, round-the-clock support without night shifts on your side.")}</p></div>
      <div class="card reveal"><span class="tag">KPI</span><h3>{dual("Mierzone efekty","Measured outcomes")}</h3><p>{dual("Dostępność, czas reakcji i naprawy (MTTR) oraz dotrzymanie SLA — wszystko raportowane.","Availability, response and repair time (MTTR) and SLA adherence — all reported.")}</p></div>
    </div>
  </div>
</section>

<section class="section bg-ink">
  <div class="container split" style="align-items:center">
    <div class="reveal">
      <p class="eyebrow">{dual("Korzyści","Benefits")}</p>
      <h2>{dual("Spokój o ciągłość działania","Peace of mind on continuity")}</h2>
      <p class="lead">{dual("Przejmujemy odpowiedzialność za utrzymanie, aby Twój zespół mógł skupić się na rozwoju, a nie na gaszeniu pożarów.","We take ownership of operations so your team can focus on growth, not firefighting.")}</p>
    </div>
    <div class="reveal">{_checklist([
      ("Krótszy czas reakcji i naprawy","Faster response and repair"),
      ("Wyższa dostępność aplikacji krytycznych","Higher availability of critical apps"),
      ("Odciążenie wewnętrznego zespołu IT","Your internal IT team relieved"),
      ("Przewidywalny koszt i jasne SLA","Predictable cost and clear SLAs"),
      ("Bezpieczeństwo i zgodność","Security and compliance")])}</div>
  </div>
</section>

<section class="section">
  <div class="container"><div class="cta reveal">
    <h2 style="max-width:24ch;margin-inline:auto">{dual("Masz aplikację, która nie może przestać działać?","Have an application that can't go down?")}</h2>
    <p class="lead" style="margin-inline:auto;color:#aeb8bf;margin-bottom:30px">{dual("Zbudujemy dla niej dedykowany zespół i wsparcie 24/7.","We'll build it a dedicated team and 24/7 support.")}</p>
    <a href="kontakt.html" class="btn btn--mint">{dual("Umów rozmowę","Book a call")} {I["arrow"]}</a>
  </div></div>
</section>
'''
PAGES["wsparcie-247.html"] = ("uslugi.html","Wsparcie 24/7 aplikacji — Mientha","24/7 application support — Mientha", wsparcie)

# ============================================================ AGENTIC SOLUTIONS
AGENT_HERO_BG = 'style="background:linear-gradient(180deg,#fff6f2,#fff)"'

def agent_stats_band(stats, note_pl, note_en):
    cells = "".join(f'<div class="stat"><b>{dual(a,b)}</b><span>{dual(c,d)}</span></div>' for a,b,c,d in stats)
    return f'''<section class="section bg-ink">
  <div class="container" style="text-align:center">
    <p class="eyebrow" style="justify-content:center">{dual("Efekty","Impact")}</p>
    <h2 style="max-width:24ch;margin-inline:auto">{dual("Co zyskuje zarząd","What the board gains")}</h2>
    <div class="stats" style="margin-top:24px">{cells}</div>
    <p class="muted" style="color:#8a949c;margin-top:26px;font-size:.85rem">{dual(note_pl,note_en)}</p>
  </div>
</section>'''

# ---------- Flagship article: Executive assistant on Teams
_CHAT_ZARZAD = chat(
  ("Microsoft Teams · kanał Zarząd","Microsoft Teams · Board channel","Microsoft Teams · Kanal Vorstand"), "07:58",
  [("user",
    "Jak wygląda cash flow na koniec tygodnia? Coś zagraża płynności w tym miesiącu?",
    "Where does cash flow stand as of this week? Anything threatening liquidity this month?",
    "Wie steht der Cashflow zum Wochenende? Gefährdet etwas die Liquidität in diesem Monat?"),
   ("agent",
    "Saldo gotówki: <b>18,4 mln zł</b> (+2,1 mln vs plan). Spływ należności: 94% planu. Ryzyko: dwie faktury kluczowego klienta po terminie (<b>1,8 mln zł</b>) — windykacja ruszyła wczoraj. Prognoza płynności na 30 dni: <b>bezpieczna</b>. Wysłać pełny raport czy brief na zarząd?",
    "Cash balance: <b>PLN 18.4M</b> (+2.1M vs plan). Collections: 94% of plan. Risk: two overdue invoices from a key client (<b>PLN 1.8M</b>) — dunning started yesterday. 30-day liquidity forecast: <b>safe</b>. Want the full report or a board brief?",
    "Kassenbestand: <b>18,4 Mio. PLN</b> (+2,1 Mio. vs. Plan). Zahlungseingänge: 94 % des Plans. Risiko: zwei überfällige Rechnungen eines Schlüsselkunden (<b>1,8 Mio. PLN</b>) — Mahnlauf gestern gestartet. 30-Tage-Liquiditätsprognose: <b>sicher</b>. Vollständigen Bericht oder Vorstands-Brief?"),
   ("user",
    "Przygotuj brief na jutrzejsze posiedzenie i dodaj marże wg rynków.",
    "Prepare a brief for tomorrow's meeting and add margins by market.",
    "Bereite einen Brief für die morgige Sitzung vor und ergänze Margen nach Märkten."),
   ("agent",
    "Gotowe — brief (PDF, 6 stron) jest w kanale Zarząd. Najważniejsze: marża brutto <b>31,2%</b> (+0,8 p.p. m/m), najmocniej rośnie rynek DE. Dwa tematy do decyzji oznaczyłem. Powiadomić CFO?",
    "Done — the brief (PDF, 6 pages) is in the Board channel. Highlights: gross margin <b>31.2%</b> (+0.8 pp MoM), the DE market is growing fastest. I flagged two items for decision. Notify the CFO?",
    "Fertig — der Brief (PDF, 6 Seiten) liegt im Kanal Vorstand. Wichtigste Punkte: Bruttomarge <b>31,2 %</b> (+0,8 PP m/m), der DE-Markt wächst am stärksten. Zwei Entscheidungsthemen habe ich markiert. CFO benachrichtigen?")])

asystent = f'''<section class="pagehero" {AGENT_HERO_BG}>
  <div class="container">
    <p class="crumb"><a href="index.html">{dual("Start","Home")}</a> &middot; <a href="agenty.html">{dual("Rozwiązania agentyczne","Agentic solutions")}</a> &middot; {dual("Asystent zarządu","Executive assistant")}</p>
    <span class="tag" style="color:#c2410c;background:#fff1ea">{dual("Agentic AI · Case study","Agentic AI · Case study")}</span>
    <h1 style="max-width:21ch">{dual("Asystent zarządu: rozmawiaj z danymi firmy tak, jak rozmawiasz z ludźmi","The executive assistant: talk to your company's data the way you talk to people")}</h1>
    <p class="lead">{dual("Agent AI dostępny na Microsoft Teams odpowiada na pytania zarządu o finanse, sprzedaż i operacje w kilka sekund. Przygotowuje brief przed posiedzeniem, tłumaczy „dlaczego”, a na Twoje polecenie uruchamia działania — z pełną kontrolą i śladem audytowym.","An AI agent available on Microsoft Teams answers board questions about finance, sales and operations in seconds. It prepares the pre-meeting brief, explains the “why”, and on your instruction triggers actions — with full control and an audit trail.")}</p>
    <div class="hero__cta" style="margin-top:26px">
      <a href="kontakt.html" class="btn btn--mint">{dual("Zamów demo","Request a demo")} {I["arrow"]}</a>
      <a href="agenty.html" class="btn btn--ghost">{dual("Wszystkie rozwiązania agentyczne","All agentic solutions")}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split" style="align-items:center">
    <div class="reveal">
      <p class="eyebrow eyebrow--uipath">{dual("Poniedziałek, 7:58","Monday, 7:58 am")}</p>
      <h2>{dual("Posiedzenie za dwie godziny. Ty już wiesz wszystko.","The board meets in two hours. You already know everything.")}</h2>
      <p class="lead measure" style="margin-bottom:18px">{dual("Zamiast prosić zespół o „szybkie wyciągnięcie liczb” i czekać do środy, zadajesz pytanie na Teams — z laptopa albo z telefonu w drodze na spotkanie.","Instead of asking the team to “quickly pull the numbers” and waiting until Wednesday, you ask the question on Teams — from your laptop, or your phone on the way to the meeting.")}</p>
      <p class="measure" style="color:var(--muted)">{dual("Asystent rozumie pytanie, sięga do SAP, hurtowni danych i systemów operacyjnych, a odpowiada jak najlepszy analityk: liczbą, kontekstem i rekomendacją. To nie wizja — to wdrożenie, które nasi klienci znają z codziennej pracy.","The assistant understands the question, reaches into SAP, the data warehouse and operational systems, and answers like your best analyst: with the number, the context and a recommendation. This isn't a vision — it's a deployment our clients use every day.")}</p>
    </div>
    <div class="reveal">{_CHAT_ZARZAD}</div>
  </div>
</section>

<section class="section bg-paper">
  <div class="container">
    <div style="max-width:60ch;margin-bottom:40px" class="reveal">
      <p class="eyebrow">{dual("Co potrafi","What it can do")}</p>
      <h2>{dual("Jeden asystent. Cała firma w zasięgu pytania.","One assistant. The whole company within a question's reach.")}</h2>
    </div>
    <div class="capgrid reveal">
      <div class="cap"><div class="card__ico">{I["chart"]}</div><h3>{dual("Odpowiedzi w sekundy","Answers in seconds")}</h3><p>{dual("P&L, cash flow, marże, DSO, sprzedaż vs plan — bez czekania na raport i bez wersji „prawie aktualnej”.","P&L, cash flow, margins, DSO, sales vs plan — no waiting for a report, no “almost current” version.")}</p></div>
      <div class="cap"><div class="card__ico">{I["doc"]}</div><h3>{dual("Brief przed posiedzeniem","The pre-meeting brief")}</h3><p>{dual("Liczby, trendy i tematy do decyzji — gotowe w kanale zarządu na godzinę przed spotkaniem.","Numbers, trends and items for decision — ready in the board channel an hour before the meeting.")}</p></div>
      <div class="cap"><div class="card__ico">{I["spark"]}</div><h3>{dual("Drill-down „dlaczego”","The “why” drill-down")}</h3><p>{dual("Od liczby do przyczyny: który rynek, który klient, które SKU. Bez przeklikiwania dashboardów.","From the number to the cause: which market, which client, which SKU. No dashboard spelunking.")}</p></div>
      <div class="cap"><div class="card__ico">{I["clock"]}</div><h3>{dual("Alerty, zanim urośnie problem","Alerts before problems grow")}</h3><p>{dual("Pilnuje KPI i sam odzywa się, gdy coś schodzi z kursu — z gotową diagnozą.","Watches your KPIs and speaks up when something drifts off course — diagnosis included.")}</p></div>
      <div class="cap"><div class="card__ico">{I["automation"]}</div><h3>{dual("Od słów do działania","From words to action")}</h3><p>{dual("Na Twoje OK uruchamia roboty UiPath: raport, windykację, blokadę zamówień. Ty decydujesz — on wykonuje.","On your OK it triggers UiPath robots: a report, dunning, an order block. You decide — it executes.")}</p></div>
      <div class="cap"><div class="card__ico">{I["globe"]}</div><h3>{dual("Mówi Twoim językiem","Speaks your language")}</h3><p>{dual("Po polsku, angielsku i niemiecku. Na laptopie, tablecie i telefonie — wszędzie tam, gdzie Teams.","In Polish, English and German. On laptop, tablet and phone — wherever Teams is.")}</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="max-width:60ch;margin-bottom:40px" class="reveal">
      <p class="eyebrow">{dual("Jak to działa","How it works")}</p>
      <h2>{dual("Agenci myślą. Roboty wykonują. Ty prowadzisz.","Agents think. Robots do. You lead.")}</h2>
    </div>
    <div class="steps reveal">
      <div class="step"><div class="step__n"></div><div><h4>{dual("Pytasz na Teams","You ask on Teams")}</h4><p>{dual("Normalnym językiem, jak człowieka. Bez formularzy, bez SQL, bez szkolenia.","In plain language, like you'd ask a person. No forms, no SQL, no training.")}</p></div></div>
      <div class="step"><div class="step__n"></div><div><h4>{dual("Agent rozumie i sprawdza uprawnienia","The agent understands and checks permissions")}</h4><p>{dual("Interpretuje intencję i widzi wyłącznie te dane, do których dana osoba ma prawo.","It interprets the intent and sees only the data that person is entitled to.")}</p></div></div>
      <div class="step"><div class="step__n"></div><div><h4>{dual("Sięga do danych i orkiestruje roboty","It reaches the data and orchestrates robots")}</h4><p>{dual("SAP, hurtownia, BI, systemy operacyjne — a rutynowe czynności wykonują roboty UiPath.","SAP, the data warehouse, BI, operational systems — with UiPath robots handling the routine work.")}</p></div></div>
      <div class="step"><div class="step__n"></div><div><h4>{dual("Odpowiada — a działa tylko za Twoją zgodą","It answers — and acts only with your approval")}</h4><p>{dual("Każda odpowiedź i akcja zostawia pełny ślad audytowy. Human-in-the-loop nie jest opcją — jest zasadą.","Every answer and action leaves a full audit trail. Human-in-the-loop isn't an option — it's the rule.")}</p></div></div>
    </div>
  </div>
</section>

<section class="section bg-paper">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">{dual("Bezpieczeństwo i kontrola","Security and control")}</p>
      <h2>{dual("Bezpieczny z założenia, nie z deklaracji","Secure by design, not by declaration")}</h2>
      <p class="lead">{dual("Zarząd dostaje szybkość — dział bezpieczeństwa dostaje kontrolę. Rozwiązanie działa w ramach orkiestracji agentowej UiPath: z guardrailami, obserwowalnością i nadzorem człowieka.","The board gets speed — security gets control. The solution runs within UiPath agentic orchestration: with guardrails, observability and human oversight.")}</p>
    </div>
    <div class="panel panel--ink reveal">{_checklist([
      ("Dostęp według ról — każdy widzi tylko swoje dane","Role-based access — everyone sees only their data"),
      ("Dane pozostają w Twoim środowisku","Data stays inside your environment"),
      ("Pełny ślad audytowy każdej odpowiedzi i akcji","A full audit trail of every answer and action"),
      ("Działania wymagają ludzkiej akceptacji","Actions require human approval"),
      ("Zgodność z politykami IT i compliance","Aligned with IT and compliance policies")])}</div>
  </div>
</section>

{agent_stats_band([
  ("~10 s","~10 s","średni czas odpowiedzi na pytanie zarządu","average time to answer a board question"),
  ("24/7","24/7","dostępny także z telefonu, w podróży","available 24/7, phone included"),
  ("1","1","wersja prawdy — wszyscy patrzą na te same liczby","version of the truth — everyone sees the same numbers"),
  ("−70%","−70%","zapytań ad hoc do zespołu FP&A","ad-hoc requests to the FP&A team")],
  "Wartości orientacyjne z wdrożeń pilotażowych; zależą od zakresu danych i konfiguracji.",
  "Indicative values from pilot deployments; they depend on data scope and configuration.")}

<section class="section">
  <div class="container"><div class="cta reveal">
    <h2 style="max-width:24ch;margin-inline:auto">{dual("Chcesz takiego asystenta dla swojego zarządu?","Want an assistant like this for your board?")}</h2>
    <p class="lead" style="margin-inline:auto;color:#aeb8bf;margin-bottom:30px">{dual("Pokażemy go na żywo, na realistycznych danych demo — 30 minut, bez zobowiązań.","We'll show it live on realistic demo data — 30 minutes, no strings attached.")}</p>
    <a href="kontakt.html" class="btn btn--mint">{dual("Zamów demo","Request a demo")} {I["arrow"]}</a>
  </div></div>
</section>
'''
PAGES["agent-asystent-zarzadu.html"] = ("uslugi.html","Asystent zarządu na Teams — Mientha","Executive assistant on Teams — Mientha", asystent)

# ---------- Satellite agentic cases
AGENT_CASES = [
 dict(slug="agent-poranny-brief", icon="clock",
   t=("Poranny brief zarządu, codziennie o 7:00","The morning executive brief, daily at 7:00"),
   lead=("Zarząd zaczyna dzień z pełnym obrazem firmy — zanim ktokolwiek zdąży o niego poprosić.","The board starts the day with the full picture — before anyone has to ask for it."),
   prob=("Poniedziałkowe raporty opisują zeszły tydzień, dashboardy wymagają szukania, a najważniejsze sygnały i tak przychodzą za późno.","Monday reports describe last week, dashboards require digging, and the signals that matter still arrive too late."),
   did=("Codziennie rano agent publikuje w kanale zarządu zwięzły brief: wczorajsza sprzedaż, produkcja, gotówka i wyjątki wymagające uwagi. A potem odpowiada na pytania — jak człowiek, tylko szybciej.","Every morning the agent posts a concise brief in the board channel: yesterday's sales, production, cash and the exceptions that need attention. Then it answers follow-ups — like a person, only faster."),
   ch=chat(("Microsoft Teams · Poranny brief","Microsoft Teams · Morning brief","Microsoft Teams · Morgen-Brief"),"07:00",
    [("agent",
      "Dzień dobry! Wczoraj: sprzedaż <b>4,2 mln zł</b> (102% planu), produkcja bez przestojów, 3 nowe zamówienia &gt; 100 tys. zł. Uwaga: rotacja magazynu w PL spada 4. dzień z rzędu — szczegóły w załączniku.",
      "Good morning! Yesterday: sales <b>PLN 4.2M</b> (102% of plan), production with zero downtime, 3 new orders &gt; PLN 100k. Heads-up: PL warehouse rotation down for the 4th day running — details attached.",
      "Guten Morgen! Gestern: Umsatz <b>4,2 Mio. PLN</b> (102 % des Plans), Produktion ohne Stillstände, 3 neue Aufträge &gt; 100 Tsd. PLN. Achtung: Lagerumschlag in PL sinkt den 4. Tag in Folge — Details im Anhang."),
     ("user",
      "Pokaż trend rotacji i główną przyczynę.",
      "Show me the rotation trend and the main cause.",
      "Zeig mir den Umschlagstrend und die Hauptursache."),
     ("agent",
      "Trend 30 dni w załączniku. Główna przyczyna: opóźnione wysyłki do dwóch klientów. Plan naprawczy uzgodniony z logistyką — ETA piątek. Chcesz, żebym pilnował i dał znać w czwartek?",
      "30-day trend attached. Main cause: delayed shipments to two clients. Recovery plan agreed with logistics — ETA Friday. Want me to track it and check in on Thursday?",
      "30-Tage-Trend im Anhang. Hauptursache: verspätete Lieferungen an zwei Kunden. Maßnahmenplan mit der Logistik vereinbart — ETA Freitag. Soll ich es verfolgen und mich am Donnerstag melden?")]),
   ben=[("Pełny obraz dnia w 90 sekund czytania","The full day's picture in a 90-second read"),
        ("Pytania follow-up od ręki, bez angażowania analityków","Follow-up questions answered instantly, no analysts involved"),
        ("Wyjątki i ryzyka podane, zanim urosną","Exceptions and risks surfaced before they grow"),
        ("Ten sam brief dla całego zarządu — jedna wersja prawdy","One brief for the whole board — a single version of the truth")],
   res=[("Godzina dziennie odzyskana na członka zarządu","An hour a day back per board member"),
        ("Decyzje szybsze o dni, nie godziny","Decisions faster by days, not hours"),
        ("Koniec z „nie wiedzieliśmy”","The end of “we didn't know”")]),
 dict(slug="agent-zamkniecie-miesiaca", icon="doc",
   t=("Agent zamknięcia miesiąca","The month-end close agent"),
   lead=("Zamknięcie krótsze o dni — bo ktoś w końcu pilnuje go bez przerwy.","A close that's days shorter — because someone finally watches it around the clock."),
   prob=("Zamknięcie miesiąca to dziesiątki zadań, zależności i ponagleń. CFO widzi status dopiero wtedy, gdy ktoś zdąży go zebrać — a opóźnienia wychodzą na jaw ostatniego dnia.","Month-end close is dozens of tasks, dependencies and reminders. The CFO sees status only when someone compiles it — and slippage surfaces on the last day."),
   did=("Agent prowadzi checklistę zamknięcia 24/7: pilnuje terminów, ponagla właścicieli zadań na Teams, uzgadnia pozycje i proponuje księgowania, a odchylenia opisuje pierwszą wersją komentarza zarządczego.","The agent runs the close checklist 24/7: watches deadlines, nudges task owners on Teams, reconciles items and proposes postings, and drafts the first version of the management commentary on variances."),
   ch=chat(("Microsoft Teams · Zamknięcie miesiąca","Microsoft Teams · Month-end close","Microsoft Teams · Monatsabschluss"),"14:32",
    [("agent",
      "Status zamknięcia: <b>92% zadań gotowych</b>. Blokery: 3 brakujące faktury kosztowe (przypomnienia wysłane), 1 niezgodność międzyfirmowa 42 tys. zł — proponuję księgowanie korygujące, czekam na akcept.",
      "Close status: <b>92% of tasks done</b>. Blockers: 3 missing cost invoices (reminders sent), 1 intercompany mismatch of PLN 42k — I propose a correcting entry, awaiting approval.",
      "Abschluss-Status: <b>92 % der Aufgaben erledigt</b>. Blocker: 3 fehlende Kostenrechnungen (Erinnerungen versandt), 1 Intercompany-Differenz von 42 Tsd. PLN — ich schlage eine Korrekturbuchung vor, warte auf Freigabe."),
     ("user",
      "Akceptuję. Kiedy wstępny P&L?",
      "Approved. When is the preliminary P&L?",
      "Freigegeben. Wann kommt die vorläufige GuV?"),
     ("agent",
      "Dziś o 16:00. Komentarz do odchyleń &gt; 5% przygotuję do 17:00 — z przyczynami i rekomendacjami.",
      "Today at 4:00 pm. Commentary on variances &gt; 5% by 5:00 pm — with causes and recommendations.",
      "Heute um 16:00. Kommentar zu Abweichungen &gt; 5 % bis 17:00 — mit Ursachen und Empfehlungen.")]),
   ben=[("Checklista zamknięcia pilnowana 24/7","The close checklist watched 24/7"),
        ("Automatyczne ponaglenia właścicieli zadań na Teams","Automatic Teams nudges to task owners"),
        ("Uzgodnienia i propozycje księgowań z audytowalnym śladem","Reconciliations and posting proposals with an audit trail"),
        ("Pierwsza wersja komentarza zarządczego pisze się sama","The first draft of management commentary writes itself")],
   res=[("Zamknięcie krótsze o 2–4 dni","A close 2–4 days shorter"),
        ("Mniej nadgodzin w zespole finansów","Fewer overtime hours in finance"),
        ("CFO widzi status w każdej chwili","The CFO sees status at any moment")]),
 dict(slug="agent-naleznosci", icon="bank",
   t=("Agent należności: gotówka wraca szybciej","The receivables agent: cash comes back sooner"),
   lead=("Priorytetyzuje, pisze, eskaluje i proponuje decyzje — a Ty tylko zatwierdzasz.","It prioritises, writes, escalates and proposes decisions — you just approve."),
   prob=("Windykacja rządzi się kalendarzem ludzi: przypomnienia idą seriami, eskalacje giną w mailach, a najwięksi dłużnicy czekają w kolejce razem z najmniejszymi.","Collections runs on people's calendars: reminders go out in batches, escalations get lost in email, and the biggest debtors queue up with the smallest."),
   did=("Agent na bieżąco analizuje należności, pisze spersonalizowane przypomnienia dopasowane do klienta i historii, eskaluje na Teams do właściwych osób, a decyzje — jak blokada zamówień — proponuje i wykonuje po akceptacji.","The agent analyses receivables continuously, writes personalised reminders tuned to the client and history, escalates on Teams to the right people, and proposes decisions — like order blocks — executing them once approved."),
   ch=chat(("Microsoft Teams · Należności","Microsoft Teams · Receivables","Microsoft Teams · Forderungen"),"11:15",
    [("agent",
      "Klient X: 3 faktury po terminie 14+ dni, łącznie <b>640 tys. zł</b>. Wysłałem spersonalizowane przypomnienie do ich działu płatności; kopia u opiekuna. Proponuję wstrzymać nowe zamówienia powyżej limitu — decyzja?",
      "Client X: 3 invoices 14+ days overdue, <b>PLN 640k</b> in total. I've sent a personalised reminder to their payables team; account owner in copy. I propose holding new orders above the limit — your call?",
      "Kunde X: 3 Rechnungen 14+ Tage überfällig, insgesamt <b>640 Tsd. PLN</b>. Ich habe eine personalisierte Erinnerung an deren Kreditorenteam gesendet; Betreuer in Kopie. Ich schlage vor, neue Aufträge über dem Limit anzuhalten — Ihre Entscheidung?"),
     ("user",
      "Wstrzymaj i umów opiekunowi telefon na jutro rano.",
      "Hold the orders and book a call for the account owner tomorrow morning.",
      "Aufträge anhalten und für den Betreuer morgen früh einen Anruf einplanen."),
     ("agent",
      "Zrobione. Zamówienia powyżej limitu wstrzymane, zaproszenie na 10:00 w kalendarzu, brief o kliencie w opisie spotkania.",
      "Done. Orders above the limit are on hold, a 10:00 invite is in the calendar, and a client brief is in the meeting notes.",
      "Erledigt. Aufträge über dem Limit angehalten, Einladung für 10:00 im Kalender, Kunden-Brief in der Besprechungsnotiz.")]),
   ben=[("Priorytety według ryzyka i wartości, nie kolejności na liście","Priorities by risk and value, not list order"),
        ("Korespondencja pisana kontekstowo, nie z szablonu","Correspondence written in context, not from a template"),
        ("Eskalacje na Teams do właściwych osób, od razu","Teams escalations to the right people, instantly"),
        ("Działa 24/7 — także wtedy, gdy zespół śpi","Works 24/7 — including while the team sleeps")],
   res=[("Niższe DSO i mniej przeterminowań","Lower DSO and fewer overdues"),
        ("Opiekunowie dostają gotowy kontekst, nie zadanie","Account owners get context, not homework"),
        ("Każda akcja z pełnym śladem audytowym","Every action fully auditable")]),
]

def agent_case_page(c):
    body = f'''<section class="pagehero" {AGENT_HERO_BG}>
  <div class="container">
    <p class="crumb"><a href="index.html">{dual("Start","Home")}</a> &middot; <a href="agenty.html">{dual("Rozwiązania agentyczne","Agentic solutions")}</a> &middot; {dual(c["t"][0],c["t"][1])}</p>
    <span class="tag" style="color:#c2410c;background:#fff1ea">{dual("Agentic AI · Case study","Agentic AI · Case study")}</span>
    <h1 style="max-width:22ch">{dual(c["t"][0],c["t"][1])}</h1>
    <p class="lead">{dual(c["lead"][0],c["lead"][1])}</p>
    <div class="hero__cta" style="margin-top:24px">
      <a href="kontakt.html" class="btn btn--mint">{dual("Zamów demo","Request a demo")} {I["arrow"]}</a>
      <a href="agenty.html" class="btn btn--ghost">{dual("Wszystkie rozwiązania agentyczne","All agentic solutions")}</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container split" style="align-items:center">
    <div class="reveal">
      <p class="eyebrow">{dual("Wyzwanie","The challenge")}</p>
      <p class="lead measure" style="margin-bottom:22px">{dual(c["prob"][0],c["prob"][1])}</p>
      <p class="eyebrow">{dual("Co robi agent","What the agent does")}</p>
      <p class="measure" style="color:var(--muted)">{dual(c["did"][0],c["did"][1])}</p>
    </div>
    <div class="reveal">{c["ch"]}</div>
  </div>
</section>

<section class="section bg-paper">
  <div class="container split">
    <div class="reveal">
      <p class="eyebrow">{dual("Efekty biznesowe","Business benefits")}</p>
      <h2 style="margin-bottom:24px">{dual("Dlaczego zarządy to kupują","Why boards buy this")}</h2>
      {_checklist(c["ben"])}
    </div>
    <div class="panel panel--ink reveal">
      <p class="eyebrow" style="margin-bottom:18px">{dual("Wpływ na wyniki","Impact on results")}</p>
      {_checklist(c["res"])}
      <div class="chips" style="margin-top:26px">
        <span class="chip"><span class="dot"></span>UiPath</span>
        <span class="chip"><span class="dot"></span>Microsoft Teams</span>
        <span class="chip"><span class="dot"></span>{dual("Human-in-the-loop","Human-in-the-loop")}</span>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container"><div class="cta reveal">
    <h2 style="max-width:24ch;margin-inline:auto">{dual("Zobacz tego agenta na żywo","See this agent live")}</h2>
    <p class="lead" style="margin-inline:auto;color:#aeb8bf;margin-bottom:30px">{dual("30-minutowe demo na realistycznych danych — bez zobowiązań.","A 30-minute demo on realistic data — no strings attached.")}</p>
    <a href="kontakt.html" class="btn btn--mint">{dual("Zamów demo","Request a demo")} {I["arrow"]}</a>
  </div></div>
</section>
'''
    PAGES[c["slug"]+".html"] = ("uslugi.html", c["t"][0]+" — Mientha", c["t"][1]+" — Mientha", body)

for _a in AGENT_CASES:
    agent_case_page(_a)

# ---------- Agentic hub
def _agent_card(c):
    return f'''<a class="card card--link reveal" href="{c["slug"]}.html">
      <div class="card__ico">{I[c["icon"]]}</div>
      <h3>{dual(c["t"][0],c["t"][1])}</h3>
      <p>{dual(c["lead"][0],c["lead"][1])}</p>
      <div style="margin-top:16px"><span class="arrowlink">{dual("Zobacz case study","View case study")} {I["arrow"]}</span></div>
    </a>'''

agenty = f'''<section class="pagehero" {AGENT_HERO_BG}>
  <div class="container">
    <p class="crumb"><a href="index.html">{dual("Start","Home")}</a> &middot; {dual("Rozwiązania agentyczne","Agentic solutions")}</p>
    <p class="eyebrow eyebrow--uipath">Agentic AI · UiPath</p>
    <h1 style="max-width:20ch">{dual("Agenci AI, którzy pracują jak Twój najlepszy zespół","AI agents that work like your best team")}</h1>
    <p class="lead">{dual("Zadajesz pytanie na Microsoft Teams. Agent rozumie, sięga do danych i uruchamia roboty UiPath — a Ty dostajesz odpowiedź i wykonaną pracę. Z uprawnieniami, guardrailami i pełnym śladem audytowym.","You ask a question on Microsoft Teams. The agent understands, reaches the data and triggers UiPath robots — and you get the answer and the finished work. With permissions, guardrails and a full audit trail.")}</p>
    <div class="hero__cta" style="margin-top:26px">
      <a href="kontakt.html" class="btn btn--mint">{dual("Zamów demo","Request a demo")} {I["arrow"]}</a>
      <a href="agent-asystent-zarzadu.html" class="btn btn--ghost">{dual("Case study: asystent zarządu","Case study: the executive assistant")}</a>
    </div>
  </div>
</section>

<section class="section--tight" style="border-block:1px solid var(--line)">
  <div class="container" style="display:flex;flex-wrap:wrap;gap:24px;justify-content:space-between;align-items:center">
    <p class="muted" style="margin:0;font-weight:600;max-width:44ch">{dual("88% firm pilotuje lub już wdrożyło agentów AI (KPMG Quarterly Pulse, 4Q 2025). Pytanie nie brzmi „czy”, tylko „jak” — bezpiecznie i z realnym zwrotem.","88% of companies are piloting or have deployed AI agents (KPMG Quarterly Pulse, 4Q 2025). The question isn't “whether” — it's “how”: safely, and with a real return.")}</p>
    <img src="{UIPATH_LOCKUP}" alt="UiPath Authorized Partner" style="height:34px;width:auto" width="640" height="121" loading="lazy" decoding="async">
  </div>
</section>

<section class="section">
  <div class="container">
    <div style="max-width:60ch;margin-bottom:40px" class="reveal">
      <p class="eyebrow">{dual("Podejście agentowe","The agentic approach")}</p>
      <h2>{dual("Agenci myślą. Roboty wykonują. Ludzie prowadzą.","Agents think. Robots do. People lead.")}</h2>
      <p class="lead">{dual("Orkiestracja agentowa spina agentów, roboty, systemy i ludzi w jeden bezpieczny, audytowalny proces — zamiast kolekcji niepołączonych eksperymentów z AI.","Agentic orchestration binds agents, robots, systems and people into one safe, auditable process — instead of a collection of disconnected AI experiments.")}</p>
    </div>
    <div class="capgrid reveal">
      <div class="cap"><div class="card__ico">{I["agent"]}</div><h3>{dual("Agenci myślą","Agents think")}</h3><p>{dual("Rozumieją kontekst i nieustrukturyzowane dane, planują kolejne kroki i wiedzą, kiedy zapytać człowieka.","They understand context and unstructured data, plan next steps and know when to ask a human.")}</p></div>
      <div class="cap"><div class="card__ico">{I["automation"]}</div><h3>{dual("Roboty wykonują","Robots do")}</h3><p>{dual("Precyzyjnie realizują zadania w SAP i pozostałych systemach — powtarzalnie, szybko i 24/7.","They execute tasks in SAP and other systems precisely — repeatably, fast and 24/7.")}</p></div>
      <div class="cap"><div class="card__ico">{I["talent"]}</div><h3>{dual("Ludzie prowadzą","People lead")}</h3><p>{dual("Decydują tam, gdzie potrzebny jest osąd. Każde działanie agenta czeka na ich zgodę.","They decide wherever judgement is needed. Every agent action waits for their approval.")}</p></div>
    </div>
  </div>
</section>

<section class="section bg-paper">
  <div class="container">
    <div style="max-width:60ch;margin-bottom:34px" class="reveal">
      <p class="eyebrow">{dual("Case studies","Case studies")}</p>
      <h2>{dual("Zobacz, jak to wygląda w praktyce","See what it looks like in practice")}</h2>
    </div>
    <a href="agent-asystent-zarzadu.html" class="rowcard reveal" style="border-color:#ffd9cc;background:linear-gradient(180deg,#fff6f2,#fff);margin-bottom:16px">
      <div class="rowcard__ico" style="background:#fa4616;color:#fff;border:0">{I["bubble"]}</div>
      <div>
        <span class="tag" style="color:#c2410c;background:#fff1ea">{dual("Case study flagowe","Flagship case study")}</span>
        <h3>{dual("Asystent zarządu na Microsoft Teams","The executive assistant on Microsoft Teams")}</h3>
        <p>{dual("Rozmawiasz z danymi firmy jak z najlepszym analitykiem: odpowiedź w sekundy, brief przed posiedzeniem, działania po Twoim OK.","Talk to your company's data like your best analyst: answers in seconds, a pre-meeting brief, actions on your OK.")}</p>
      </div>
      <span class="btn btn--ghost">{dual("Przeczytaj","Read it")} {I["arrow"]}</span>
    </a>
    <div class="grid g-3">
      {"".join(_agent_card(c) for c in AGENT_CASES)}
    </div>
    <p class="muted" style="font-size:.82rem;margin-top:24px">{dual("Przykłady oparte na rzeczywistych wdrożeniach i pilotażach; dane klientów zanonimizowane.","Examples based on real deployments and pilots; client details anonymised.")}</p>
  </div>
</section>

<section class="section bg-ink">
  <div class="container split" style="align-items:center">
    <div class="reveal">
      <p class="eyebrow">{dual("Pełna kontrola","Full control")}</p>
      <h2>{dual("Żadnej czarnej skrzynki","No black box")}</h2>
      <p class="lead">{dual("Wdrażamy agentów w ramach orkiestracji UiPath — z tymi samymi standardami bezpieczeństwa, które stosujemy w automatyzacjach dla liderów rynku.","We deploy agents within UiPath orchestration — with the same security standards we apply in automations for market leaders.")}</p>
    </div>
    <div class="reveal">{_checklist([
      ("Guardraile: agent robi dokładnie to, co powinien","Guardrails: the agent does exactly what it should"),
      ("Obserwowalność: każdy krok widoczny i mierzalny","Observability: every step visible and measurable"),
      ("Human-in-the-loop: działania za zgodą człowieka","Human-in-the-loop: actions with human approval"),
      ("Uprawnienia i dane pod kontrolą Twojego IT","Permissions and data controlled by your IT"),
      ("Pełny ślad audytowy od pytania do akcji","A full audit trail from question to action")])}</div>
  </div>
</section>

<section class="section">
  <div class="container"><div class="cta reveal">
    <h2 style="max-width:22ch;margin-inline:auto">{dual("Zobacz agentów w akcji","See the agents in action")}</h2>
    <p class="lead" style="margin-inline:auto;color:#aeb8bf;margin-bottom:30px">{dual("30-minutowe demo na Twoich przykładach — pokażemy, od czego zacząć, żeby zwrot był szybki i mierzalny.","A 30-minute demo on your examples — we'll show where to start so the return is fast and measurable.")}</p>
    <a href="kontakt.html" class="btn btn--mint">{dual("Umów demo","Book a demo")} {I["arrow"]}</a>
  </div></div>
</section>
'''
PAGES["agenty.html"] = ("uslugi.html","Rozwiązania agentyczne — Mientha","Agentic solutions — Mientha", agenty)

# ============================================================ WRITE OUT
for fname,(active,tpl,ten,body) in PAGES.items():
    (ROOT/fname).write_text(page(active,tpl,ten,body), encoding="utf-8")
    print("wrote", fname, len((ROOT/fname).read_text(encoding='utf-8')), "bytes")
print("done")


