# -*- coding: utf-8 -*-
"""Screenshot QA harness.

The live store's photos cannot be fetched from this sandbox, so during QA we
intercept requests to pic.designpartners.pl and serve deterministic tonal
stand-ins at a realistic 3:4 portrait ratio. Layout, spacing, typography and
overflow are therefore judged exactly as they will behave with real photos.
"""
import os, sys, hashlib, io
from playwright.sync_api import sync_playwright
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHOTS = os.path.join(ROOT, "..", "qa-shots")
os.makedirs(SHOTS, exist_ok=True)

TONES = [(205,196,176),(186,180,161),(160,158,141),(214,203,182),(139,143,130),
         (176,166,148),(196,186,166),(151,152,138),(120,126,114),(224,215,196)]

_cache = {}
def placeholder(url, w=900, h=1200):
    key = hashlib.md5(url.encode()).hexdigest()
    if key in _cache: return _cache[key]
    idx = int(key[:2], 16) % len(TONES)
    base = TONES[idx]
    im = Image.new("RGB", (w, h), base)
    d = ImageDraw.Draw(im)
    # soft vertical gradient
    for y in range(h):
        f = 1 - (y / h) * 0.18
        d.line([(0, y), (w, y)], fill=tuple(int(c * f) for c in base))
    # abstract garment shape so crops are judgeable
    d.rounded_rectangle([w*0.22, h*0.14, w*0.78, h*0.86], radius=int(w*0.06),
                        fill=tuple(min(255, int(c*1.10)) for c in base))
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=72)
    _cache[key] = buf.getvalue()
    return _cache[key]


def run(pages, widths, tag="", actions=None, full=True):
    with sync_playwright() as pw:
        b = pw.chromium.launch(args=["--force-color-profile=srgb"])
        for w, h in widths:
            ctx = b.new_context(viewport={"width": w, "height": h}, device_scale_factor=1,
                                locale="pl-PL", reduced_motion="reduce")
            ctx.route("**pic.designpartners.pl/**", lambda route: route.fulfill(
                status=200, content_type="image/jpeg", body=placeholder(route.request.url)))
            pg = ctx.new_page()
            for name, fname in pages:
                pg.goto("file://" + os.path.join(ROOT, fname), wait_until="load")
                pg.evaluate("""async () => {
                  const H = document.body.scrollHeight;
                  for (let y = 0; y < H; y += window.innerHeight * 0.8) {
                    window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60));
                  }
                  window.scrollTo(0, 0); await new Promise(r => setTimeout(r, 120));
                }""")
                pg.wait_for_timeout(500)
                if actions:
                    actions(pg, name, w)
                out = os.path.join(SHOTS, "%s%s-%d.png" % (name, tag, w))
                pg.screenshot(path=out, full_page=full)
            ctx.close()
        b.close()


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    PAGES = [("home", "index.html"), ("category", "category.html"), ("product", "product.html"),
             ("cart", "cart.html"), ("checkout", "checkout.html"), ("search", "search.html"),
             ("login", "login.html"), ("account", "account.html"), ("about", "o-nas.html"),
             ("contact", "kontakt.html"), ("empty", "category-buty.html"),
             ("nowa", "nowa-kolekcja.html"), ("returns", "zwroty-i-wymiany.html")]
    if which == "desktop":
        run(PAGES, [(1440, 900)])
    elif which == "mobile":
        run(PAGES, [(390, 844)])
    elif which == "wide":
        run([("home", "index.html"), ("category", "category.html"), ("product", "product.html")],
            [(1280, 800), (1536, 900), (1920, 1080), (2560, 1400)])
    elif which == "small":
        run(PAGES, [(320, 700), (360, 780), (768, 1024)])
    else:
        run(PAGES, [(1440, 900), (390, 844)])
