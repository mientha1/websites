/* Mientha site — language toggle, nav, reveal */
(function(){
  var VALID = ["pl","en","de"];

  function getLang(){
    var p = new URLSearchParams(location.search).get("lang");
    if(VALID.indexOf(p) > -1) return p;
    return "pl";
  }

  function applyLang(lang){
    document.body.classList.remove("lang-pl","lang-en","lang-de");
    document.body.classList.add("lang-"+lang);
    document.documentElement.setAttribute("lang", lang);
    // toggle buttons
    document.querySelectorAll(".langtoggle button").forEach(function(b){
      b.classList.toggle("on", b.dataset.lang === lang);
    });
    // rewrite internal links to carry ?lang
    document.querySelectorAll('a[href]').forEach(function(a){
      var href = a.getAttribute("href");
      if(!href || href.charAt(0)==="#" || /^(https?:|mailto:|tel:)/i.test(href)) return;
      var base = href.split("#")[0].split("?")[0];
      var hash = href.indexOf("#") > -1 ? href.slice(href.indexOf("#")) : "";
      if(base.indexOf(".html") > -1 || base === "" ){
        a.setAttribute("href", base + "?lang=" + lang + hash);
      }
    });
    // swap document title if data provided
    var t = document.body.getAttribute("data-title-"+lang);
    if(t) document.title = t;
  }

  function setLang(lang){
    if(VALID.indexOf(lang) < 0) lang = "pl";
    var url = new URL(location.href);
    url.searchParams.set("lang", lang);
    history.replaceState(null,"",url);
    applyLang(lang);
  }

  document.addEventListener("DOMContentLoaded", function(){
    applyLang(getLang());

    document.querySelectorAll(".langtoggle button").forEach(function(b){
      b.addEventListener("click", function(){ setLang(b.dataset.lang); });
    });

    // mobile menu
    var nav = document.querySelector(".nav");
    var toggle = document.querySelector(".nav__toggle");
    var menu = document.querySelector(".mobile-menu");
    function closeMenu(){
      if(!menu) return;
      menu.classList.remove("show");
      if(nav) nav.classList.remove("open");
      if(toggle) toggle.setAttribute("aria-expanded","false");
    }
    if(toggle && menu && nav){
      toggle.addEventListener("click", function(){
        var open = menu.classList.toggle("show");
        nav.classList.toggle("open", open);
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
      });
      menu.addEventListener("click", function(e){
        if(e.target.closest("a")) closeMenu();
      });
      document.addEventListener("keydown", function(e){
        if(e.key === "Escape" && menu.classList.contains("show")){ closeMenu(); toggle.focus(); }
      });
    }
    // mobile accordion groups
    document.querySelectorAll(".m-group__t").forEach(function(btn){
      btn.addEventListener("click", function(){
        btn.parentElement.classList.toggle("open");
      });
    });

    // ROI calculators (illustrative estimates)
    function fmt(n){ return Math.round(n).toString().replace(/\B(?=(\d{3})+(?!\d))/g, " "); }
    document.querySelectorAll(".calc").forEach(function(c){
      var vol = c.querySelector('input[data-k="vol"]');
      var min = c.querySelector('input[data-k="min"]');
      var rate = c.querySelector('input[data-k="rate"]');
      var oh = c.querySelector('[data-o="hours"] b');
      var oy = c.querySelector('[data-o="annual"] b');
      if(!vol || !min || !rate || !oh || !oy) return;
      function recalc(){
        var v = Math.max(0, parseFloat(vol.value) || 0);
        var m = Math.max(0, parseFloat(min.value) || 0);
        var r = Math.max(0, parseFloat(rate.value) || 0);
        var hours = v * m / 60;
        var annual = hours * r * 12;
        oh.textContent = fmt(hours) + " h";
        oy.textContent = "≈ " + fmt(annual) + " €";
      }
      [vol, min, rate].forEach(function(i){ i.addEventListener("input", recalc); });
      recalc();
    });

    // case-study index filter
    var fbar = document.querySelector(".fbar");
    if(fbar){
      var cards = document.querySelectorAll(".idxcard");
      fbar.addEventListener("click", function(e){
        var btn = e.target.closest("button[data-f]");
        if(!btn) return;
        fbar.querySelectorAll("button").forEach(function(b){ b.classList.toggle("on", b === btn); });
        var f = btn.getAttribute("data-f");
        cards.forEach(function(card){
          var tags = " " + (card.getAttribute("data-f") || "") + " ";
          card.classList.toggle("hide", f !== "all" && tags.indexOf(" " + f + " ") === -1);
        });
      });
    }

    // reveal on scroll
    var els = document.querySelectorAll(".reveal");
    if("IntersectionObserver" in window){
      var io = new IntersectionObserver(function(entries){
        entries.forEach(function(e){
          if(e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target); }
        });
      },{threshold:.12, rootMargin:"0px 0px -40px 0px"});
      els.forEach(function(el){ io.observe(el); });
    } else {
      els.forEach(function(el){ el.classList.add("in"); });
    }
  });
})();
