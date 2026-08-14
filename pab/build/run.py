# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import P, BY_KEY, in_cat
from build import listing_page, write, build_css
import pages, cms

HOME = ("Strona główna", "index.html")

W = [p for p in P if p["gender"] == "kobieta"]
M = [p for p in P if p["gender"] == "mezczyzna"]
A = [p for p in P if "dodatki" in p["cats"]]

WOMEN_DESC = ("Każdego sezonu kolekcja pic a bec czerpie z klasycznych elementów garderoby, właśnie takich jak koszule damskie. "
              "Ich fundamentem są wysokiej jakości materiały – między innymi bawełna, jedwab czy len – a także podkreślające atuty "
              "sylwetki kroje w różnych wydaniach: od bardziej luźnych modeli do podkreślających talię eleganckich koszul.")
MEN_DESC = ("Męska część kolekcji pic a bec opiera się na klasycznych elementach garderoby inspirowanych elegancją klubów golfowych "
            "i tenisowych: dopracowanych krojach, naturalnych materiałach i stonowanej kolorystyce.")
ACC_DESC = ("Dodatki pic a bec dopełniają stylizacje na pole golfowe i kort tenisowy – od nakryć głowy, przez skórzane paski "
            "plecione we Włoszech, po jedwabne apaszki z ręcznie rolowanymi brzegami.")

W_SUBS = [("Sukienki i spódnice", "category-sukienki.html"),
          ("Koszulki polo i topy", "category-kobieta-polo.html"),
          ("Spodnie", "category-kobieta-spodnie.html")]
M_SUBS = [("Koszulki polo i topy", "category-mezczyzna-polo.html"),
          ("Spodnie", "category-mezczyzna-spodnie.html")]
A_SUBS = [("Czapki", "category-czapki.html"), ("Skarpetki", "category-skarpetki.html"),
          ("Paski", "category-paski.html"), ("Buty", "category-buty.html")]

LISTINGS = [
 ("category.html", "Kobieta", WOMEN_DESC, W, [HOME, ("Kobieta", "#")], W_SUBS, "Kobieta", "Kolekcja"),
 ("category-sukienki.html", "Sukienki i spódnice", "Sukienki polo i spódnice plisowane o klasycznym, sportowym kroju – wpisujące się w minimalistyczną elegancję pic à bec inspirowaną golfem i tenisem.",
    [p for p in P if "sukienki" in p["cats"]], [HOME, ("Kobieta", "category.html"), ("Sukienki i spódnice", "#")], W_SUBS, "Kobieta", "Kobieta"),
 ("category-kobieta-polo.html", "Koszulki polo i topy", "Damskie koszulki polo o ponadczasowym kroju – z krótkim i długim rękawem oraz w wersji bez rękawów, z tkanin z certyfikatem OEKO-TEX®.",
    [p for p in P if "kobieta-polo" in p["cats"]], [HOME, ("Kobieta", "category.html"), ("Koszulki polo i topy", "#")], W_SUBS, "Kobieta", "Kobieta"),
 ("category-kobieta-spodnie.html", "Spodnie", "Kolarki i spodnie damskie o dopasowanym kroju, zaprojektowane do noszenia pod spódnicą, sukienką polo lub samodzielnie.",
    [p for p in P if "kobieta-spodnie" in p["cats"]], [HOME, ("Kobieta", "category.html"), ("Spodnie", "#")], W_SUBS, "Kobieta", "Kobieta"),

 ("category-mezczyzna.html", "Mężczyzna", MEN_DESC, M, [HOME, ("Mężczyzna", "#")], M_SUBS, "Mężczyzna", "Kolekcja"),
 ("category-mezczyzna-polo.html", "Koszulki polo i topy", "Męskie koszulki polo o klasycznej sylwetce – dzianina piqué, rogowe guziki i wersje z długim rękawem.",
    [p for p in P if "mezczyzna-polo" in p["cats"]], [HOME, ("Mężczyzna", "category-mezczyzna.html"), ("Koszulki polo i topy", "#")], M_SUBS, "Mężczyzna", "Mężczyzna"),
 ("category-mezczyzna-spodnie.html", "Spodnie", "Spodnie męskie o klasycznym kroju, inspirowane elegancją klubów golfowych i tenisowych.",
    [p for p in P if "mezczyzna-spodnie" in p["cats"]], [HOME, ("Mężczyzna", "category-mezczyzna.html"), ("Spodnie", "#")], M_SUBS, "Mężczyzna", "Mężczyzna"),

 ("category-dodatki.html", "Dodatki", ACC_DESC, A, [HOME, ("Dodatki", "#")], A_SUBS, "Dodatki", "Kolekcja"),
 ("category-czapki.html", "Czapki", "Daszki, czapki z daszkiem i kapelusze bucket hat z bawełny z dodatkiem poliamidu – lekkie, z szerokim rondem chroniącym przed słońcem.",
    [p for p in P if "czapki" in p["cats"]], [HOME, ("Dodatki", "category-dodatki.html"), ("Czapki", "#")], A_SUBS, "Dodatki", "Dodatki"),
 ("category-skarpetki.html", "Skarpetki", "Bawełniane skarpetki golfowe i tenisowe o klasycznym, uniwersalnym kroju.",
    [p for p in P if "skarpetki" in p["cats"]], [HOME, ("Dodatki", "category-dodatki.html"), ("Skarpetki", "#")], A_SUBS, "Dodatki", "Dodatki"),
 ("category-paski.html", "Paski", "Plecione, skórzane paski o ponadczasowym designie, wykonane we Włoszech w oparciu o tradycyjne rzemiosło skórzane.",
    [p for p in P if "paski" in p["cats"]], [HOME, ("Dodatki", "category-dodatki.html"), ("Paski", "#")], A_SUBS, "Dodatki", "Dodatki"),
 ("category-buty.html", "Buty", "Obuwie pic à bec pojawi się w kolejnej odsłonie kolekcji.",
    [], [HOME, ("Dodatki", "category-dodatki.html"), ("Buty", "#")], A_SUBS, "Dodatki", "Dodatki"),

 ("nowa-kolekcja.html", "Nowa kolekcja", "Pełna kolekcja wiosna – lato 2026: koszulki polo, sukienki, spódnice, spodnie i dodatki inspirowane światem golfa i tenisa.",
    P, [HOME, ("Nowa kolekcja", "#")], None, "Nowa kolekcja", "Wiosna – lato 2026"),
]


def main():
    n = build_css()
    write("index.html", pages.build_home())
    for fname, title, desc, prods, crumbs, subs, nav, eyebrow in LISTINGS:
        write(fname, listing_page(fname, title, desc, prods, crumbs, subs, nav, eyebrow))
    for p in P:
        write(p["file"], pages.build_product(p))
    write("search.html", pages.build_search())
    write("cart.html", pages.build_cart())
    write("checkout.html", pages.build_checkout())
    write("order-confirmation.html", pages.build_confirmation())
    write("login.html", pages.build_login())
    write("account.html", pages.build_account())
    write("o-nas.html", cms.build_about())
    write("kontakt.html", cms.build_contact())
    write("wysylka.html", cms.build_shipping())
    write("zwroty-i-wymiany.html", cms.build_returns())
    write("regulamin.html", cms.build_terms())
    print("css bytes:", n)


if __name__ == "__main__":
    main()
