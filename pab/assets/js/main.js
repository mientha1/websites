/* =============================================================================
   pic à bec — prototype interactions
   -----------------------------------------------------------------------------
   Deliberately small. Everything visual (hover, reveal, open/close animation,
   layout, sticky behaviour) is done in CSS; JS only holds state that a real
   PrestaShop front-end would hold too: panel open/closed, selected variant,
   cart contents, gallery index.
   ========================================================================== */
(function () {
  'use strict';

  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ---------------------------------------------------------------- storage */
  var mem = {};
  var store = {
    get: function (k) {
      try { var v = window.localStorage.getItem(k); return v === null ? mem[k] : v; }
      catch (e) { return mem[k]; }
    },
    set: function (k, v) {
      mem[k] = v;
      try { window.localStorage.setItem(k, v); } catch (e) {}
    }
  };

  /* ----------------------------------------------------------- pluralisation */
  function plProducts(n) {
    if (n === 1) return 'produkt';
    var d = n % 10, h = n % 100;
    return (d >= 2 && d <= 4 && (h < 12 || h > 14)) ? 'produkty' : 'produktów';
  }

  /* ------------------------------------------------------------------ money */
  function money(v) {
    return v.toFixed(2).replace('.', ',').replace(/\B(?=(\d{3})+(?!\d))/g, ' ') + ' zł';
  }

  /* ------------------------------------------------------------------- cart */
  var FREE_FROM = 500; // free delivery threshold used by the prototype summary
  var SHIPPING  = 18;

  function readCart() {
    try { return JSON.parse(store.get('pab_cart') || '[]'); } catch (e) { return []; }
  }
  function writeCart(items) { store.set('pab_cart', JSON.stringify(items)); paint(); }

  function cartCount() { return readCart().reduce(function (n, i) { return n + i.qty; }, 0); }
  function cartTotal() { return readCart().reduce(function (n, i) { return n + i.price * i.qty; }, 0); }

  function addToCart(item) {
    var items = readCart();
    var id = [item.key, item.color, item.size].join('|');
    var found = null;
    items.forEach(function (i) { if (i.id === id) found = i; });
    if (found) { found.qty += item.qty; }
    else { items.push({ id: id, key: item.key, name: item.name, sub: item.sub, href: item.href,
                        img: item.img, price: item.price, color: item.color, size: item.size, qty: item.qty }); }
    writeCart(items);
  }

  function setQty(id, delta) {
    var items = readCart().map(function (i) {
      if (i.id === id) { i.qty = Math.max(0, i.qty + delta); }
      return i;
    }).filter(function (i) { return i.qty > 0; });
    writeCart(items);
  }
  function removeLine(id) { writeCart(readCart().filter(function (i) { return i.id !== id; })); }

  /* -------------------------------------------------------------- rendering */
  function lineHTML(i, opts) {
    opts = opts || {};
    var attrs = [i.color, i.size].filter(Boolean).join(' · ');
    return '' +
      '<article class="product-line" data-line="' + i.id + '">' +
        '<a class="product-line__img" href="' + i.href + '">' +
          '<span class="imgframe imgframe--tall"><img src="' + i.img + '" alt="" loading="lazy"></span>' +
        '</a>' +
        '<div class="product-line__content">' +
          '<a class="product-line__title" href="' + i.href + '">' + i.name + '</a>' +
          (i.sub ? '<span class="product-line__attrs">' + i.sub + '</span>' : '') +
          (attrs ? '<span class="product-line__attrs">' + attrs + '</span>' : '') +
          '<div class="product-line__bottom">' +
            '<span class="product-line__qty">' +
              '<button type="button" data-qty="-1" aria-label="Zmniejsz ilość">–</button>' +
              '<span>' + i.qty + '</span>' +
              '<button type="button" data-qty="1" aria-label="Zwiększ ilość">+</button>' +
            '</span>' +
            '<span class="product-line__price num">' + money(i.price * i.qty) + '</span>' +
          '</div>' +
          (opts.remove !== false
            ? '<div style="margin-top:6px"><button type="button" class="js-remove-from-cart">Usuń</button></div>' : '') +
        '</div>' +
      '</article>';
  }

  function paint() {
    var items = readCart();
    var count = cartCount();
    var total = cartTotal();

    /* header badge */
    $$('.header-pic__cart-badge').forEach(function (b) {
      b.textContent = count;
      b.classList.toggle('is-visible', count > 0);
    });

    /* drawer */
    var body = $('#blockcart-body');
    if (body) {
      if (!items.length) {
        body.innerHTML =
          '<div class="blockcart-drawer__empty">' +
            '<p class="lede">Twój koszyk jest pusty.</p>' +
            '<p class="text-muted" style="font-size:var(--fs-sm)">Zacznij od nowej kolekcji albo wróć do ostatnio oglądanych modeli.</p>' +
            '<a class="btn btn--outline" href="category.html">Zobacz kolekcję</a>' +
          '</div>';
      } else {
        body.innerHTML = items.map(function (i) { return lineHTML(i); }).join('');
      }
      var foot = $('#blockcart-foot');
      if (foot) foot.style.display = items.length ? '' : 'none';
      var t = $('#blockcart-total'); if (t) t.textContent = money(total);
      var ship = $('#blockcart-ship');
      if (ship) {
        ship.textContent = total >= FREE_FROM
          ? 'Dostawa gratis — próg spełniony.'
          : 'Do darmowej dostawy brakuje ' + money(FREE_FROM - total) + '.';
      }
    }

    /* cart page */
    var list = $('#cart-lines');
    if (list) {
      var empty = $('#cart-empty'), grid = $('#cart-grid');
      if (!items.length) {
        if (empty) empty.hidden = false;
        if (grid) grid.hidden = true;
      } else {
        if (empty) empty.hidden = true;
        if (grid) grid.hidden = false;
        list.innerHTML = items.map(function (i) { return lineHTML(i); }).join('');
      }
      var sub = $('#cart-subtotal'); if (sub) sub.textContent = money(total);
      var shipEl = $('#cart-shipping');
      var shipCost = (total >= FREE_FROM || total === 0) ? 0 : SHIPPING;
      if (shipEl) shipEl.textContent = shipCost === 0 ? 'Gratis' : money(shipCost);
      var tot = $('#cart-total'); if (tot) tot.textContent = money(total + shipCost);
      var vat = $('#cart-vat'); if (vat) vat.textContent = money((total + shipCost) * 23 / 123);
      var n = $('#cart-count'); if (n) n.textContent = count;
      var nl = $('#cart-count-label'); if (nl) nl.textContent = plProducts(count);

      var bar = $('#freeship-bar');
      if (bar) {
        var pct = Math.min(100, Math.round(total / FREE_FROM * 100));
        bar.style.width = pct + '%';
        var box = bar.closest('.freeship');
        if (box) box.classList.toggle('is-complete', total >= FREE_FROM);
        var txt = $('#freeship-text');
        if (txt) txt.innerHTML = total >= FREE_FROM
          ? 'Dostawa <strong>gratis</strong> — próg spełniony.'
          : 'Do darmowej dostawy brakuje <strong>' + money(FREE_FROM - total) + '</strong>.';
      }
    }

    /* checkout recap */
    var recap = $('#checkout-lines');
    if (recap) {
      recap.innerHTML = items.map(function (i) { return lineHTML(i, { remove: false }); }).join('');
      var cs = $('#checkout-subtotal'); if (cs) cs.textContent = money(total);
      var shipCost2 = (total >= FREE_FROM || total === 0) ? 0 : SHIPPING;
      var ch = $('#checkout-shipping'); if (ch) ch.textContent = shipCost2 === 0 ? 'Gratis' : money(shipCost2);
      var ct = $('#checkout-total'); if (ct) ct.textContent = money(total + shipCost2);
      var cn = $('#checkout-count'); if (cn) cn.textContent = count;
      var ce = $('#checkout-empty'); if (ce) ce.hidden = items.length > 0;
      var ctm = $('#checkout-total-mini'); if (ctm) ctm.textContent = money(total);
    }
  }

  /* ------------------------------------------------------------- overlays */
  /* Closed panels must leave the tab order — they are only moved offscreen. */
  function setInert(el, on) {
    if (!el) return;
    if (on) { el.setAttribute('inert', ''); el.setAttribute('aria-hidden', 'true'); }
    else { el.removeAttribute('inert'); el.removeAttribute('aria-hidden'); }
  }
  $$('.js-panel, .header-pic__search-bar').forEach(function (el) {
    if (!el.classList.contains('is-open')) setInert(el, true);
  });

  var openPanel = null;
  function setOpen(el, on) {
    if (!el) return;
    el.classList.toggle('is-open', on);
    setInert(el, !on);
    var ov = $('#overlay');
    if (ov) ov.classList.toggle('is-open', on);
    document.body.classList.toggle('is-locked', on);
    openPanel = on ? el : null;
    if (on) {
      var f = el.querySelector('button, a, input');
      if (f) { try { f.focus({ preventScroll: true }); } catch (e) { f.focus(); } }
    }
  }
  function closeAll() {
    $$('.js-panel').forEach(function (p) { p.classList.remove('is-open'); setInert(p, true); });
    var ov = $('#overlay'); if (ov) ov.classList.remove('is-open');
    document.body.classList.remove('is-locked');
    openPanel = null;
  }

  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-open]');
    if (t) {
      e.preventDefault();
      var el = $('#' + t.getAttribute('data-open'));
      var isOpen = el && el.classList.contains('is-open');
      closeAll();
      if (!isOpen) setOpen(el, true);
      return;
    }
    if (e.target.closest('[data-close]') || e.target.id === 'overlay') { closeAll(); }
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      if (openPanel) { closeAll(); }
      var s = $('#header-search');
      if (s) { s.classList.remove('is-open'); setInert(s, true);
               $$('[data-search-toggle]').forEach(function (b) { b.setAttribute('aria-expanded', 'false'); }); }
      var m = $('.modal.is-open'); if (m) { m.classList.remove('is-open'); document.body.classList.remove('is-locked'); }
    }
  });

  /* --------------------------------------------------------------- search */
  var searchBar = $('#header-search');
  $$('[data-search-toggle]').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      if (!searchBar) return;
      var on = !searchBar.classList.contains('is-open');
      searchBar.classList.toggle('is-open', on);
      setInert(searchBar, !on);
      $$('[data-search-toggle]').forEach(function (b) { b.setAttribute('aria-expanded', String(on)); });
      if (on) { var i = $('#search-input'); if (i) i.focus(); }
    });
  });
  $$('.js-search-form').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var q = (f.querySelector('input') || {}).value || '';
      window.location.href = 'search.html?q=' + encodeURIComponent(q.trim());
    });
  });

  /* ------------------------------------------------------- generic toggles */
  document.addEventListener('click', function (e) {
    var t = e.target.closest('[data-toggle]');
    if (!t) return;
    var expanded = t.getAttribute('aria-expanded') === 'true';
    if (t.hasAttribute('data-toggle-exclusive')) {
      var scope = t.closest('[data-toggle-group]');
      if (scope) {
        $$('[data-toggle]', scope).forEach(function (o) { if (o !== t) o.setAttribute('aria-expanded', 'false'); });
      }
    }
    t.setAttribute('aria-expanded', String(!expanded));
  });

  /* ------------------------------------------------------------ modals */
  document.addEventListener('click', function (e) {
    var open = e.target.closest('[data-modal]');
    if (open) {
      e.preventDefault();
      var m = $('#' + open.getAttribute('data-modal'));
      if (m) { m.classList.add('is-open'); document.body.classList.add('is-locked'); }
      return;
    }
    if (e.target.closest('[data-modal-close]') || e.target.classList.contains('modal__backdrop')) {
      var mm = e.target.closest('.modal');
      if (mm) { mm.classList.remove('is-open'); document.body.classList.remove('is-locked'); }
    }
  });

  /* ---------------------------------------------------------- header state */
  var header = $('#header');
  if (header && header.classList.contains('header--transparent')) {
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 40); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* -------------------------------------------------------------- gallery */
  var carousel = $('#product-carousel');
  if (carousel) {
    var slides = $$('.imgframe', carousel);
    var dots   = $$('#product-dots button');
    var counter = $('#product-gallery-count');

    var sync = function () {
      var idx = Math.round(carousel.scrollLeft / Math.max(1, carousel.clientWidth));
      dots.forEach(function (d, i) { d.classList.toggle('active', i === idx); });
      if (counter) counter.textContent = (idx + 1) + ' / ' + slides.length;
    };
    carousel.addEventListener('scroll', function () { window.requestAnimationFrame(sync); }, { passive: true });
    dots.forEach(function (d, i) {
      d.addEventListener('click', function () { carousel.scrollTo({ left: i * carousel.clientWidth, behavior: 'smooth' }); });
    });
    sync();

    $$('.product__thumbnail').forEach(function (th, i) {
      th.addEventListener('click', function (e) {
        e.preventDefault();
        $$('.product__thumbnail').forEach(function (o) { o.classList.remove('active'); });
        th.classList.add('active');
        if (window.matchMedia('(min-width: 1000px)').matches) {
          carousel.classList.add('is-expanded');
          if (slides[i]) slides[i].scrollIntoView({ behavior: 'smooth', block: 'center' });
        } else {
          carousel.scrollTo({ left: i * carousel.clientWidth, behavior: 'smooth' });
        }
      });
    });

    var more = $('#gallery-more');
    if (more) {
      more.addEventListener('click', function () {
        carousel.classList.add('is-expanded');
        more.style.display = 'none';
      });
    }
  }

  /* ------------------------------------------------------------- variants */
  $$('.js-variant-color').forEach(function (input) {
    input.addEventListener('change', function () {
      var out = $('#selected-color');
      if (out) out.textContent = input.getAttribute('data-name');
    });
  });
  $$('.js-variant-size').forEach(function (input) {
    input.addEventListener('change', function () {
      var out = $('#selected-size');
      if (out) out.textContent = input.getAttribute('data-name');
      var err = $('#size-error'); if (err) err.hidden = true;
    });
  });

  /* ------------------------------------------------------------- quantity */
  $$('.js-qty').forEach(function (wrap) {
    var input = wrap.querySelector('input');
    wrap.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      var d = parseInt(b.getAttribute('data-step'), 10) || 0;
      input.value = Math.max(1, (parseInt(input.value, 10) || 1) + d);
    });
  });

  /* ----------------------------------------------------------- add to cart */
  function toast(msg) {
    var t = $('#toast'); if (!t) return;
    $('#toast-text').textContent = msg;
    t.classList.add('is-visible');
    clearTimeout(toast._t);
    toast._t = setTimeout(function () { t.classList.remove('is-visible'); }, 2600);
  }

  $$('.js-add-to-cart').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var d = btn.dataset;
      var size = d.size;
      if (!size) {
        var checked = $('.js-variant-size:checked');
        if (!checked) {
          var err = $('#size-error');
          if (err) { err.hidden = false; }
          var first = $('.product-variant__radios');
          if (first) first.scrollIntoView({ behavior: 'smooth', block: 'center' });
          return;
        }
        size = checked.getAttribute('data-name');
      }
      var color = d.color;
      if (!color) { var c = $('.js-variant-color:checked'); color = c ? c.getAttribute('data-name') : ''; }
      var qtyInput = $('#product-qty');
      addToCart({
        key: d.key, name: d.name, sub: d.sub || '', href: d.href, img: d.img,
        price: parseFloat(d.price), color: color, size: size,
        qty: qtyInput ? (parseInt(qtyInput.value, 10) || 1) : 1
      });
      closeAll();
      setOpen($('#blockcart-drawer'), true);
      toast('Dodano do koszyka: ' + d.name);
    });
  });

  /* ----------------------------------------------- cart line interactions */
  document.addEventListener('click', function (e) {
    var line = e.target.closest('[data-line]');
    if (!line) return;
    var id = line.getAttribute('data-line');
    var q = e.target.closest('[data-qty]');
    if (q) { setQty(id, parseInt(q.getAttribute('data-qty'), 10)); return; }
    if (e.target.closest('.js-remove-from-cart')) { removeLine(id); }
  });

  /* ------------------------------------------------------------ buy bar */
  var buybar = $('#buybar');
  if (buybar) {
    var anchor = $('#product-buy-anchor');
    if (anchor) {
      var ticking = false;
      var syncBar = function () {
        buybar.classList.toggle('is-visible', anchor.getBoundingClientRect().bottom < 0);
        ticking = false;
      };
      window.addEventListener('scroll', function () {
        if (!ticking) { ticking = true; window.requestAnimationFrame(syncBar); }
      }, { passive: true });
      window.addEventListener('resize', syncBar, { passive: true });
      syncBar();
    }
  }

  /* ------------------------------------------------- listing: sort + filter */
  var grid = $('#js-product-grid');
  if (grid) {
    var cards = $$('.product-miniature', grid);

    var applySort = function (mode) {
      var sorted = cards.slice();
      var val = function (c) { return parseFloat(c.getAttribute('data-price')) || 0; };
      if (mode === 'price-asc')  sorted.sort(function (a, b) { return val(a) - val(b); });
      if (mode === 'price-desc') sorted.sort(function (a, b) { return val(b) - val(a); });
      if (mode === 'name-asc')   sorted.sort(function (a, b) { return a.getAttribute('data-name').localeCompare(b.getAttribute('data-name'), 'pl'); });
      if (mode === 'name-desc')  sorted.sort(function (a, b) { return b.getAttribute('data-name').localeCompare(a.getAttribute('data-name'), 'pl'); });
      sorted.forEach(function (c) { grid.appendChild(c); });
    };

    var chips = $('#active-filters');
    var applyFilters = function () {
      var colors = $$('.js-filter[data-facet="color"]:checked').map(function (i) { return i.value; });
      var sizes  = $$('.js-filter[data-facet="size"]:checked').map(function (i) { return i.value; });
      var groups = $$('.js-filter[data-facet="group"]:checked').map(function (i) { return i.value; });
      var maxPrice = parseFloat(($('#filter-price') || {}).value || '99999');
      var shown = 0;

      cards.forEach(function (c) {
        var cColors = (c.getAttribute('data-colors') || '').split('|');
        var cSizes  = (c.getAttribute('data-sizes') || '').split('|');
        var cGroup  = c.getAttribute('data-group') || '';
        var price   = parseFloat(c.getAttribute('data-price')) || 0;
        var ok =
          (!colors.length || colors.some(function (v) { return cColors.indexOf(v) > -1; })) &&
          (!sizes.length  || sizes.some(function (v) { return cSizes.indexOf(v) > -1; })) &&
          (!groups.length || groups.indexOf(cGroup) > -1) &&
          (price === 0 || price <= maxPrice);
        c.hidden = !ok;
        if (ok) shown++;
      });

      var count = $('#filter-count');
      var active = colors.length + sizes.length + groups.length;
      if (count) { count.textContent = active; count.hidden = active === 0; }
      var res = $('#products-count');
      if (res) res.textContent = shown + ' ' + plProducts(shown);
      var empty = $('#grid-empty'); if (empty) empty.hidden = shown !== 0;

      if (chips) {
        chips.innerHTML = colors.concat(sizes, groups).map(function (v) {
          return '<button type="button" class="chip js-chip" data-value="' + v + '">' + v + '<span class="chip__x" aria-hidden="true">×</span><span class="visually-hidden">Usuń filtr</span></button>';
        }).join('');
      }
    };

    $$('.js-filter').forEach(function (i) { i.addEventListener('change', applyFilters); });
    var priceInput = $('#filter-price');
    if (priceInput) {
      priceInput.addEventListener('input', function () {
        var out = $('#filter-price-out');
        if (out) out.textContent = money(parseFloat(priceInput.value));
        applyFilters();
      });
    }
    document.addEventListener('click', function (e) {
      var chip = e.target.closest('.js-chip');
      if (chip) {
        var v = chip.getAttribute('data-value');
        $$('.js-filter').forEach(function (i) { if (i.value === v) i.checked = false; });
        applyFilters();
      }
      if (e.target.closest('#filter-clear')) {
        $$('.js-filter').forEach(function (i) { i.checked = false; });
        if (priceInput) { priceInput.value = priceInput.max; var o = $('#filter-price-out'); if (o) o.textContent = money(parseFloat(priceInput.max)); }
        applyFilters();
      }
    });
    $$('.js-sort').forEach(function (s) {
      s.addEventListener('change', function () {
        applySort(s.value);
        $$('.js-sort').forEach(function (o) { if (o !== s) o.value = s.value; });
      });
    });
    applyFilters();
  }

  /* ------------------------------------------------------- search results */
  var searchTitle = $('#search-query-out');
  if (searchTitle) {
    var input = $('#search-page-input');
    var q = new URLSearchParams(window.location.search).get('q') || (input ? input.value : '');
    q = (q || '').trim();
    if (input) input.value = q;
    searchTitle.textContent = q;

    // crude but effective PL stem: drop the last character on longer words so
    // "czapka" also matches "czapki", "spodnie" matches "spodni…"
    var needle = q.toLowerCase();
    if (needle.length > 4) needle = needle.slice(0, -1);

    var g = $('#js-product-grid');
    if (g) {
      var visible = 0;
      $$('.product-miniature', g).forEach(function (c) {
        var hay = ((c.getAttribute('data-search') || c.getAttribute('data-name')) || '').toLowerCase();
        var ok = !needle || hay.indexOf(needle) > -1;
        c.hidden = !ok; if (ok) visible++;
      });
      var e2 = $('#grid-empty'); if (e2) e2.hidden = visible !== 0;
      var c2 = $('#search-result-count'); if (c2) c2.textContent = visible;
      var c3 = $('#products-count');
      if (c3) c3.textContent = visible + ' ' + plProducts(visible);
    }
  }

  /* ------------------------------------------------------------- checkout */
  $$('.js-checkout-next').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var block = btn.closest('.checkout-block');
      var next  = $('#' + btn.getAttribute('data-next'));
      if (block) {
        block.classList.add('checkout-block--done');
        var recap = block.querySelector('.checkout-block__recap');
        if (recap && recap.getAttribute('data-live')) {
          var vals = $$('input:checked, input[type="text"], input[type="email"]', block)
            .map(function (i) { return i.type === 'radio' ? (i.getAttribute('data-label') || '') : i.value; })
            .filter(Boolean);
          if (vals.length) recap.textContent = vals.slice(0, 3).join(' · ');
        }
      }
      if (next) {
        next.classList.remove('checkout-block--done', 'checkout-block--pending');
        next.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
      var step = btn.getAttribute('data-step');
      if (step) {
        $$('.checkout-steps__step').forEach(function (s) {
          var n = s.getAttribute('data-step');
          s.classList.remove('checkout-steps__step--current');
          if (parseInt(n, 10) < parseInt(step, 10)) s.classList.add('checkout-steps__step--done');
          if (n === step) { s.classList.add('checkout-steps__step--current'); s.classList.remove('checkout-steps__step--done'); }
        });
      }
    });
  });
  $$('.js-checkout-edit').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      var b = btn.closest('.checkout-block');
      if (b) b.classList.remove('checkout-block--done');
    });
  });
  var placeOrder = $('#place-order');
  if (placeOrder) {
    placeOrder.addEventListener('click', function (e) {
      e.preventDefault();
      writeCart([]);
      window.location.href = 'order-confirmation.html';
    });
  }

  /* ------------------------------------------------- category description */
  $$('[data-desc-toggle]').forEach(function (btn) {
    var desc = $('#' + btn.getAttribute('aria-controls'));
    if (!desc) return;
    var needed = function () { return desc.scrollHeight - desc.clientHeight > 2 || btn.getAttribute('aria-expanded') === 'true'; };
    var sync = function () { btn.style.display = needed() ? '' : 'none'; };
    btn.addEventListener('click', function () {
      var on = btn.getAttribute('aria-expanded') === 'true';
      btn.setAttribute('aria-expanded', String(!on));
      desc.classList.toggle('is-open', !on);
    });
    window.addEventListener('resize', sync, { passive: true });
    sync();
  });

  /* --------------------------------------------------------------- reveal */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    $$('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    $$('.reveal').forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ------------------------------------------- graceful image degradation */
  $$('img').forEach(function (img) {
    img.addEventListener('error', function () { img.setAttribute('data-broken', ''); }, { once: true });
  });

  /* ------------------------------------------------------------ wishlist */
  document.addEventListener('click', function (e) {
    var w = e.target.closest('.product-miniature__wish');
    if (!w) return;
    e.preventDefault();
    var on = w.classList.toggle('is-active');
    w.setAttribute('aria-pressed', String(on));
    toast(on ? 'Dodano do ulubionych' : 'Usunięto z ulubionych');
  });

  paint();
})();
