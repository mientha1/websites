# Mientha — nowy serwis korporacyjny

Nowoczesny, dwujęzyczny (PL/EN) serwis wielostronicowy. Czysta paleta (biel, złamana biel,
szarości) z miętowymi akcentami i granatem w logo. Odświeżony obecny brand.

## Struktura

| Plik | Strona |
|------|--------|
| `index.html` | Start / Home |
| `uslugi.html` | Usługi / Services |
| `branze.html` | Branże / Industries |
| `transport-spedycja.html` | Produkt flagowy: rozliczanie kierowców |
| `case-studies.html` | Case studies |
| `o-nas.html` | O nas / About (z sekcją Partnerstwa: UiPath, SAP, KYP.ai) |
| `kontakt.html` | Kontakt / Contact |
| `fmcg.html` | Branża FMCG — hub z 10 case studies automatyzacji |
| `cs-*.html` | 10 osobnych case studies FMCG (VAT, windykacja, kredyt, P2P, treasury, HR…) |
| `wsparcie-247.html` | Usługa: dedykowane zespoły i wsparcie 24/7 aplikacji krytycznych |

Każda strona jest **samodzielna** (CSS i JS wbudowane) — wystarczy otworzyć plik w przeglądarce
lub wgrać cały folder na dowolny hosting statyczny (Netlify, Vercel, S3, zwykły serwer WWW).

## Wersje językowe (PL / EN / DE)

Przełącznik **PL / EN / DE** w nagłówku. Wybór języka przenosi się między podstronami przez
parametr `?lang=pl` / `?lang=en` / `?lang=de`. Domyślny język to polski. Tłumaczenia
niemieckie znajdują się w `de_data.py` (kluczowane po tekście angielskim; brakujący klucz =
fallback do angielskiego).

## Partnerstwa

- **UiPath Authorized Partner** — użyto oficjalnego lockupu (assets/uipath-authorized-b/w.png,
  źródłowy SVG w assets/uipath-authorized-b.svg). Sekcja na stronie głównej i karta na „O nas"
  używają zatwierdzonej frazeologii („UiPath — a leader in agentic business orchestration").
  Uwaga: wg wytycznych UiPath wszelkie **press release** wzmiankujące UiPath wymagają ich
  akceptacji — treści na stronie są opisowe i zachowawcze (bez wyolbrzymiania relacji).
- **SAP Partner** (Open Ecosystem), **KYP.ai** (Process Intelligence), **Pipedrive** (CRM,
  Solution Provider) — badge'e tekstowe; można podmienić na oficjalne assety.

## Do podmiany / dokończenia

- **Logo** — w serwisie użyto odtworzonej wersji znaku (SVG) w kolorach marki. Podmień na
  oryginalny plik logo (SVG/PNG), jeśli chcesz 1:1 z materiałami firmowymi.
- **Formularz kontaktowy** — działa jako demo (pokazuje podziękowanie). Podłącz backend lub
  usługę e-mail (np. Formspree, własny endpoint) w `kontakt.html`.
- **Dane liczbowe w case studies / transport** — część wskaźników ma charakter orientacyjny
  (spójny z materiałami „About"). Zastąp realnymi danymi klientów, gdy będą dostępne.
- **Czcionki** — Sora (nagłówki) + Inter (tekst) z Google Fonts.

## Źródła treści

Materiały „About" (PDF) oraz obecna strona mientha.com: usługi (RPA/Agentic AI, BPO, AMS,
eksperci IT, rozwiązania custom), partnerstwa (UiPath Authorized Partner, SAP Partner),
statystyki (120+ ekspertów, 100 mld € przychodów klientów, 90%+ retencji), zasięg europejski.

## Ponowne generowanie

Serwis powstaje z generatora `build.py` (źródła stylu w `assets/style.css`, logika w
`assets/app.js`). Aby przebudować: `python3 build.py`.
