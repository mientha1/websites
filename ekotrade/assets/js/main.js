/* EKOTRADE — warstwa interakcji (vanilla, bez zależności) */
(function () {
  'use strict';

  /* Nagłówek: stan po przewinięciu */
  var header = document.querySelector('.header');
  function onScroll() {
    if (!header) return;
    header.classList.toggle('scrolled', window.scrollY > 8);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* Menu mobilne */
  var burger = document.querySelector('.burger');
  var menu = document.getElementById('mobile-menu');
  if (burger && menu) {
    burger.addEventListener('click', function () {
      var open = burger.getAttribute('aria-expanded') === 'true';
      burger.setAttribute('aria-expanded', String(!open));
      menu.classList.toggle('open', !open);
      document.body.classList.toggle('menu-open', !open);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && menu.classList.contains('open')) {
        burger.setAttribute('aria-expanded', 'false');
        menu.classList.remove('open');
        document.body.classList.remove('menu-open');
        burger.focus();
      }
    });
  }

  /* Rozwijane „Usługi" w nawigacji */
  var drop = document.querySelector('.nav-drop');
  if (drop) {
    var btn = drop.querySelector('button');
    var panel = drop.querySelector('.drop-panel');
    function setDrop(open) {
      drop.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', String(open));
    }
    btn.addEventListener('click', function () { setDrop(!drop.classList.contains('open')); });
    document.addEventListener('click', function (e) {
      if (!drop.contains(e.target) && drop.classList.contains('open')) setDrop(false);
    });
    drop.addEventListener('focusout', function (e) {
      if (!drop.contains(e.relatedTarget)) setDrop(false);
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drop.classList.contains('open')) { setDrop(false); btn.focus(); }
    });
    if (panel) panel.addEventListener('click', function (e) { e.stopPropagation(); });
  }

  /* Odsłanianie sekcji */
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && revealEls.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }

  /* Wyszukiwarka lokalizacji (sieć oddziałów, kariera) */
  document.querySelectorAll('[data-loc-search]').forEach(function (input) {
    var scope = document.querySelector(input.getAttribute('data-loc-search'));
    if (!scope) return;
    var empty = scope.querySelector('.loc-empty');
    var counter = document.querySelector('[data-loc-count]');
    var total = scope.querySelectorAll('.loc').length;
    function norm(s) {
      return (s || '').toLowerCase()
        .replace(/ą/g, 'a').replace(/ć/g, 'c').replace(/ę/g, 'e').replace(/ł/g, 'l')
        .replace(/ń/g, 'n').replace(/ó/g, 'o').replace(/ś/g, 's').replace(/ż/g, 'z').replace(/ź/g, 'z');
    }
    input.addEventListener('input', function () {
      var q = norm(input.value.trim());
      var shown = 0;
      scope.querySelectorAll('.loc').forEach(function (card) {
        var hit = !q || norm(card.getAttribute('data-search')).indexOf(q) !== -1;
        card.classList.toggle('hidden', !hit);
        if (hit) shown++;
      });
      scope.querySelectorAll('.loc-group').forEach(function (group) {
        var any = group.querySelectorAll('.loc:not(.hidden)').length > 0;
        group.style.display = any ? '' : 'none';
      });
      if (empty) empty.style.display = shown ? 'none' : 'block';
      if (counter) counter.textContent = q ? (shown + ' z ' + total) : String(total);
    });
  });

  /* Filtr regionu (kariera) */
  document.querySelectorAll('[data-region-filter]').forEach(function (select) {
    var scope = document.querySelector(select.getAttribute('data-region-filter'));
    if (!scope) return;
    select.addEventListener('change', function () {
      var v = select.value;
      scope.querySelectorAll('[data-region]').forEach(function (el) {
        el.style.display = (v === 'all' || el.getAttribute('data-region') === v) ? '' : 'none';
      });
    });
  });

  /* Formularze: walidacja po stronie klienta + stan demonstracyjny.
     Uwaga wdrożeniowa: endpoint POST + ochrona antyspamowa po stronie serwera
     zostają podpięte na etapie integracji (patrz docs/wdrozenie.md). */
  document.querySelectorAll('form[data-demo-form]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var valid = true;
      /* pole-pułapka (honeypot) */
      var hp = form.querySelector('.hp-field input');
      if (hp && hp.value) return;
      form.querySelectorAll('[required]').forEach(function (field) {
        var wrap = field.closest('.field') || field.closest('.check');
        var ok = field.type === 'checkbox' ? field.checked : field.value.trim().length > 0;
        if (ok && field.type === 'email') ok = /.+@.+\..+/.test(field.value.trim());
        if (wrap && wrap.classList.contains('field')) wrap.classList.toggle('invalid', !ok);
        if (!ok) valid = false;
      });
      if (!valid) {
        var firstInvalid = form.querySelector('.field.invalid input, .field.invalid textarea');
        if (firstInvalid) firstInvalid.focus();
        return;
      }
      var status = form.querySelector('.form-status');
      if (status) {
        status.classList.add('show');
        status.setAttribute('tabindex', '-1');
        status.focus();
      }
      form.querySelectorAll('input, textarea, select, button').forEach(function (el) {
        if (!status || !status.contains(el)) el.disabled = true;
      });
    });
    form.querySelectorAll('input, textarea').forEach(function (field) {
      field.addEventListener('input', function () {
        var wrap = field.closest('.field');
        if (wrap) wrap.classList.remove('invalid');
      });
    });
  });
})();
