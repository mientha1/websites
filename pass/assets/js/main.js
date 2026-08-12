/* Pałac Pass — interface (no dependencies) */
(function () {
  'use strict';
  var d = document, w = window;
  var head = d.querySelector('.site-head');
  var reduced = w.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* header state */
  var lastY = 0;
  function onScroll() {
    var y = w.scrollY || 0;
    if (head) head.classList.toggle('is-scrolled', y > 24);
    lastY = y;
  }
  w.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  /* mobile menu */
  var btn = d.querySelector('.menu-btn');
  var menu = d.getElementById('site-menu');
  function setMenu(open) {
    d.body.classList.toggle('menu-open', open);
    if (btn) btn.setAttribute('aria-expanded', String(open));
    if (menu) menu.setAttribute('aria-hidden', String(!open));
    if (open && menu) {
      var first = menu.querySelector('a');
      if (first) first.focus({ preventScroll: true });
    }
  }
  if (btn && menu) {
    btn.addEventListener('click', function () {
      setMenu(!d.body.classList.contains('menu-open'));
    });
    menu.addEventListener('click', function (e) {
      if (e.target.closest('a')) setMenu(false);
    });
    d.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && d.body.classList.contains('menu-open')) { setMenu(false); btn.focus(); }
    });
  }

  /* reveals */
  var items = [].slice.call(d.querySelectorAll('[data-reveal]'));
  if (!reduced && 'IntersectionObserver' in w) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
    items.forEach(function (el) { io.observe(el); });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  /* lightbox */
  var lbox = d.getElementById('lbox');
  if (lbox) {
    var stageImg = lbox.querySelector('.lbox__stage img');
    var capEl = lbox.querySelector('.lbox__cap');
    var countEl = lbox.querySelector('.lbox__count');
    var triggers = [].slice.call(d.querySelectorAll('.gitem'));
    var idx = 0;
    function show(i) {
      idx = (i + triggers.length) % triggers.length;
      var t = triggers[idx];
      var full = t.getAttribute('data-full') || t.querySelector('img').currentSrc;
      var alt = t.querySelector('img').getAttribute('alt') || '';
      stageImg.src = full;
      stageImg.alt = alt;
      capEl.textContent = t.getAttribute('data-cap') || alt;
      countEl.textContent = (idx + 1) + ' / ' + triggers.length;
    }
    triggers.forEach(function (t, i) {
      t.addEventListener('click', function () { show(i); if (!lbox.open) lbox.showModal(); });
    });
    lbox.addEventListener('click', function (e) {
      var a = e.target.closest('[data-lb]');
      if (!a) { if (e.target === lbox) lbox.close(); return; }
      var k = a.getAttribute('data-lb');
      if (k === 'close') lbox.close();
      if (k === 'prev') show(idx - 1);
      if (k === 'next') show(idx + 1);
    });
    lbox.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') show(idx - 1);
      if (e.key === 'ArrowRight') show(idx + 1);
    });
    lbox.addEventListener('close', function () { stageImg.src = ''; });
  }

  /* click-to-load embeds (film · map · tour) — nothing loads before consent-by-click */
  [].slice.call(d.querySelectorAll('[data-embed]')).forEach(function (box) {
    var activate = function () {
      if (box.classList.contains('is-live')) return;
      var kind = box.getAttribute('data-embed');
      if (kind === 'video') {
        var v = d.createElement('video');
        v.src = box.getAttribute('data-src');
        v.controls = true; v.autoplay = true; v.playsInline = true;
        v.setAttribute('preload', 'metadata');
        box.appendChild(v);
        box.querySelector('img') && box.querySelector('img').remove();
        var tag = box.querySelector('.filmstill__tag'); if (tag) tag.remove();
      } else {
        var f = d.createElement('iframe');
        f.src = box.getAttribute('data-src');
        f.loading = 'lazy';
        f.setAttribute('allowfullscreen', '');
        f.setAttribute('allow', 'accelerometer; encrypted-media; gyroscope; picture-in-picture; fullscreen');
        f.title = box.getAttribute('data-title') || '';
        box.appendChild(f);
      }
      box.classList.add('is-live');
    };
    box.addEventListener('click', activate);
    box.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); activate(); } });
  });
})();
