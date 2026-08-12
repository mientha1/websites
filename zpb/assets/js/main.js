/* ZPB Kaczmarek — interactions. Vanilla, dependency-free, engineered to be quiet. */
(function () {
  "use strict";
  var d = document;

  /* ---------- mega panel ---------- */
  var megaBtn = d.querySelector("[data-mega-toggle]");
  var mega = d.getElementById("panel-produkty");
  function closeMega() {
    if (!mega || mega.hidden) return;
    mega.hidden = true;
    megaBtn.setAttribute("aria-expanded", "false");
  }
  if (megaBtn && mega) {
    megaBtn.addEventListener("click", function () {
      var open = mega.hidden;
      mega.hidden = !open;
      megaBtn.setAttribute("aria-expanded", String(open));
    });
    d.addEventListener("click", function (e) {
      if (!mega.hidden && !mega.contains(e.target) && !megaBtn.contains(e.target)) closeMega();
    });
    d.addEventListener("keydown", function (e) {
      if (e.key === "Escape") { closeMega(); closeMenu(); closeSearch(); }
    });
  }

  /* ---------- mobile menu ---------- */
  var menuBtn = d.querySelector("[data-menu-toggle]");
  var menu = d.getElementById("menu-mobile");
  function closeMenu() {
    if (!menu || menu.hidden) return;
    menu.hidden = true;
    menuBtn.setAttribute("aria-expanded", "false");
    d.body.style.overflow = "";
  }
  if (menuBtn && menu) {
    menuBtn.addEventListener("click", function () {
      var open = menu.hidden;
      menu.hidden = !open;
      menuBtn.setAttribute("aria-expanded", String(open));
      d.body.style.overflow = open ? "hidden" : "";
    });
  }

  /* ---------- search ---------- */
  var searchEl = d.getElementById("search-dialog");
  var searchInput = d.querySelector("[data-search-input]");
  var searchResults = d.querySelector("[data-search-results]");
  var searchData = null;
  function openSearch() {
    if (!searchEl) return;
    closeMega(); closeMenu();
    searchEl.hidden = false;
    d.body.style.overflow = "hidden";
    if (!searchData) {
      try { searchData = JSON.parse(d.getElementById("search-data").textContent); } catch (e) { searchData = []; }
    }
    setTimeout(function () { searchInput.focus(); }, 30);
  }
  function closeSearch() {
    if (!searchEl || searchEl.hidden) return;
    searchEl.hidden = true;
    d.body.style.overflow = "";
  }
  d.querySelectorAll("[data-search-open]").forEach(function (b) { b.addEventListener("click", openSearch); });
  d.querySelectorAll("[data-search-close]").forEach(function (b) { b.addEventListener("click", closeSearch); });
  if (searchEl) {
    searchEl.addEventListener("click", function (e) { if (e.target === searchEl) closeSearch(); });
    d.addEventListener("keydown", function (e) {
      if ((e.key === "k" || e.key === "K") && (e.metaKey || e.ctrlKey)) { e.preventDefault(); openSearch(); }
    });
    var form = d.querySelector("[data-search-form]");
    if (form) form.addEventListener("submit", function (e) { e.preventDefault(); });
  }
  function norm(s) {
    return (s || "").toLowerCase()
      .replace(/ą/g, "a").replace(/ć/g, "c").replace(/ę/g, "e").replace(/ł/g, "l")
      .replace(/ń/g, "n").replace(/ó/g, "o").replace(/ś/g, "s").replace(/[żź]/g, "z");
  }
  var KIND_LABEL = { produkt: "Produkty", kategoria: "Kategorie", dokument: "Dokumenty", katalog: "Katalogi i cenniki" };
  if (searchInput) {
    searchInput.addEventListener("input", function () {
      var q = norm(searchInput.value.trim());
      if (q.length < 2) { searchResults.innerHTML = ""; return; }
      var hits = [];
      for (var i = 0; i < searchData.length; i++) {
        var it = searchData[i];
        var t = norm(it.t), x = norm(it.x || "") + " " + norm(it.c || "");
        var score = -1;
        if (t.indexOf(q) === 0) score = 0;
        else if (t.indexOf(q) > -1) score = 1;
        else if (x.indexOf(q) > -1) score = 2;
        if (score >= 0) hits.push([score, it]);
      }
      hits.sort(function (a, b) { return a[0] - b[0]; });
      hits = hits.slice(0, 24);
      if (!hits.length) {
        searchResults.innerHTML = '<p class="search-empty">Brak wyników dla „' + searchInput.value.replace(/[<>&]/g, "") + '”. Sprawdź pisownię albo zadzwoń: +48 65 546 12 55.</p>';
        return;
      }
      var groups = {};
      hits.forEach(function (h) { (groups[h[1].k] = groups[h[1].k] || []).push(h[1]); });
      var html = "";
      Object.keys(groups).forEach(function (k) {
        html += '<div class="search-group"><span class="eyebrow">' + (KIND_LABEL[k] || k) + "</span>";
        groups[k].forEach(function (it) {
          var ext = /^https?:/.test(it.u);
          html += '<a class="search-hit" href="' + it.u + '"' + (ext ? ' rel="noopener"' : "") + ">" +
            "<span>" + it.t + "</span>" + (it.c ? '<span class="ctx">' + it.c + "</span>" : "") + "</a>";
        });
        html += "</div>";
      });
      searchResults.innerHTML = html;
    });
  }

  /* ---------- scroll reveal ---------- */
  if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches && "IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-in"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
    d.querySelectorAll(".reveal").forEach(function (el) { io.observe(el); });
  } else {
    d.querySelectorAll(".reveal").forEach(function (el) { el.classList.add("is-in"); });
  }

  /* ---------- product filters (listing page) ---------- */
  var filterRoot = d.querySelector("[data-filters]");
  if (filterRoot) {
    var cards = Array.prototype.slice.call(d.querySelectorAll("[data-p]"));
    var countEl = d.querySelector("[data-filter-count]");
    var clearBtn = d.querySelector("[data-filter-clear]");
    var emptyEl = d.querySelector("[data-filter-empty]");
    // presets from URL, e.g. ?kol=barwy zimy&usz=płukane
    try {
      var params = new URLSearchParams(location.search);
      ["zast", "kol", "gr", "usz"].forEach(function (k) {
        var v = params.get(k);
        if (!v) return;
        v.split(",").forEach(function (val) {
          var inp = filterRoot.querySelector('input[name="' + k + '"][value="' + val.trim() + '"]');
          if (inp) inp.checked = true;
        });
      });
    } catch (e) {}
    function apply() {
      var active = {};
      filterRoot.querySelectorAll("input:checked").forEach(function (i) {
        (active[i.name] = active[i.name] || []).push(i.value);
      });
      var shown = 0;
      cards.forEach(function (c) {
        var ok = Object.keys(active).every(function (k) {
          var have = (c.getAttribute("data-" + k) || "").split("|");
          return active[k].some(function (v) { return have.indexOf(v) > -1; });
        });
        c.hidden = !ok;
        if (ok) shown++;
      });
      if (countEl) countEl.textContent = shown;
      if (clearBtn) clearBtn.hidden = Object.keys(active).length === 0;
      if (emptyEl) emptyEl.hidden = shown > 0;
      d.querySelectorAll("[data-filter-group]").forEach(function (g) {
        var n = g.querySelectorAll("input:checked").length;
        var b = g.querySelector("[data-badge]");
        if (b) { b.textContent = n || ""; }
      });
    }
    filterRoot.addEventListener("change", apply);
    if (clearBtn) clearBtn.addEventListener("click", function () {
      filterRoot.querySelectorAll("input:checked").forEach(function (i) { i.checked = false; });
      apply();
    });
    var fToggle = d.querySelector("[data-filters-toggle]");
    if (fToggle) {
      fToggle.addEventListener("click", function () {
        var open = filterRoot.classList.toggle("is-open");
        fToggle.setAttribute("aria-expanded", String(open));
        d.body.style.overflow = open && window.innerWidth < 981 ? "hidden" : "";
      });
    }
    var fClose = d.querySelector("[data-filters-close]");
    if (fClose) fClose.addEventListener("click", function () {
      filterRoot.classList.remove("is-open");
      var t = d.querySelector("[data-filters-toggle]");
      if (t) t.setAttribute("aria-expanded", "false");
      d.body.style.overflow = "";
    });
    apply();
  }

  /* ---------- dealer search ---------- */
  var dealerRoot = d.querySelector("[data-dealers]");
  if (dealerRoot) {
    var q = d.querySelector("[data-dealer-q]");
    var expo = d.querySelector("[data-dealer-expo]");
    var rows = Array.prototype.slice.call(dealerRoot.querySelectorAll("[data-dealer]"));
    var dCount = d.querySelector("[data-dealer-count]");
    var dEmpty = d.querySelector("[data-dealer-empty]");
    function dApply() {
      var term = norm(q ? q.value.trim() : "");
      var onlyExpo = expo && expo.checked;
      var n = 0;
      rows.forEach(function (r) {
        var hay = norm(r.getAttribute("data-hay"));
        var ok = (!term || hay.indexOf(term) > -1) && (!onlyExpo || r.hasAttribute("data-expo"));
        r.hidden = !ok;
        if (ok) n++;
      });
      if (dCount) dCount.textContent = n;
      if (dEmpty) dEmpty.hidden = n > 0;
    }
    if (q) q.addEventListener("input", dApply);
    if (expo) expo.addEventListener("change", dApply);
    dApply();
  }

  /* ---------- gallery (product page) ---------- */
  var gal = d.querySelector("[data-gallery]");
  if (gal) {
    var main = gal.querySelector("[data-gallery-main] img");
    gal.querySelectorAll("[data-gallery-thumb]").forEach(function (t) {
      t.addEventListener("click", function () {
        var img = t.querySelector("img");
        if (main && img) {
          main.src = img.getAttribute("data-full") || img.src;
          main.alt = img.alt;
          gal.querySelectorAll("[data-gallery-thumb]").forEach(function (x) { x.classList.remove("is-cur"); });
          t.classList.add("is-cur");
        }
      });
    });
  }

  /* ---------- doc library filter ---------- */
  var docsRoot = d.querySelector("[data-docs]");
  if (docsRoot) {
    var dq = d.querySelector("[data-docs-q]");
    var chips = d.querySelectorAll("[data-docs-chip]");
    var docRows = Array.prototype.slice.call(docsRoot.querySelectorAll("[data-doc]"));
    var docsCount = d.querySelector("[data-docs-count]");
    var activeKind = "";
    function docsApply() {
      var term = norm(dq ? dq.value.trim() : "");
      var n = 0;
      docRows.forEach(function (r) {
        var ok = (!term || norm(r.getAttribute("data-hay")).indexOf(term) > -1) &&
                 (!activeKind || r.getAttribute("data-kind") === activeKind);
        r.hidden = !ok;
        if (ok) n++;
      });
      if (docsCount) docsCount.textContent = n;
      d.querySelectorAll("[data-docs-sect]").forEach(function (s) {
        var any = s.querySelector("[data-doc]:not([hidden])");
        s.hidden = !any;
      });
    }
    if (dq) dq.addEventListener("input", docsApply);
    chips.forEach(function (c) {
      c.addEventListener("click", function () {
        var k = c.getAttribute("data-docs-chip");
        activeKind = activeKind === k ? "" : k;
        chips.forEach(function (x) { x.setAttribute("aria-pressed", String(x.getAttribute("data-docs-chip") === activeKind)); });
        docsApply();
      });
    });
    docsApply();
  }
})();
