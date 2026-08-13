/* mClinic — minimal behaviour layer (no dependencies) */
(function () {
  'use strict';
  var d = document;

  /* offer panel (desktop) */
  var panelBtn = d.querySelector('[data-panel-btn]');
  var panel = d.querySelector('[data-panel]');
  if (panelBtn && panel) {
    var closePanel = function () { panel.classList.remove('is-open'); panelBtn.setAttribute('aria-expanded', 'false'); };
    panelBtn.addEventListener('click', function (e) {
      e.preventDefault();
      var open = panel.classList.toggle('is-open');
      panelBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape') closePanel(); });
    d.addEventListener('click', function (e) {
      if (panel.classList.contains('is-open') && !panel.contains(e.target) && e.target !== panelBtn && !panelBtn.contains(e.target)) closePanel();
    });
  }

  /* mobile menu */
  var mBtn = d.querySelector('[data-menu-btn]');
  var mMenu = d.querySelector('[data-menu]');
  if (mBtn && mMenu) {
    var setMenu = function (open) {
      mMenu.classList.toggle('is-open', open);
      mBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
      d.documentElement.style.overflow = open ? 'hidden' : '';
    };
    mBtn.addEventListener('click', function () { setMenu(!mMenu.classList.contains('is-open')); });
    mMenu.querySelectorAll('[data-menu-close]').forEach(function (el) {
      el.addEventListener('click', function () { setMenu(false); });
    });
    d.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
  }

  /* reveal on scroll */
  var revealEls = d.querySelectorAll('.reveal, .reveal-group');
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* progressive image upgrade: placeholder -> real clinic photo when reachable */
  d.querySelectorAll('img[data-remote]').forEach(function (img) {
    var probe = new Image();
    probe.onload = function () {
      img.style.transition = 'opacity .45s ease';
      img.style.opacity = '0.25';
      requestAnimationFrame(function () {
        img.src = img.getAttribute('data-remote');
        img.style.opacity = '1';
      });
    };
    probe.src = img.getAttribute('data-remote');
  });

  /* price list filter */
  var pInput = d.querySelector('[data-price-filter]');
  if (pInput) {
    var rows = Array.prototype.slice.call(d.querySelectorAll('.ptable tbody tr'));
    var groups = Array.prototype.slice.call(d.querySelectorAll('[data-pgroup]'));
    var secs = Array.prototype.slice.call(d.querySelectorAll('[data-psec]'));
    var norm = function (s) { return s.toLowerCase().normalize('NFD').replace(/[̀-̧]/g, ''); };
    var apply = function () {
      var q = norm(pInput.value.trim());
      rows.forEach(function (tr) {
        tr.hidden = q !== '' && norm(tr.textContent).indexOf(q) === -1;
      });
      groups.forEach(function (g) {
        var any = g.querySelector('tbody tr:not([hidden])');
        g.hidden = !any;
      });
      secs.forEach(function (s) {
        var any = s.querySelector('[data-pgroup]:not([hidden])');
        s.hidden = !any;
      });
    };
    pInput.addEventListener('input', apply);
  }

  /* sticky CTA on treatment pages (mobile) — appears after the protokół scrolls past */
  var sticky = d.querySelector('.sticky-cta');
  var trigger = d.querySelector('[data-cta-trigger]');
  if (sticky && trigger && 'IntersectionObserver' in window) {
    var io2 = new IntersectionObserver(function (entries) {
      sticky.classList.toggle('is-visible', !entries[0].isIntersecting && entries[0].boundingClientRect.top < 0);
    }, { threshold: 0 });
    io2.observe(trigger);
  }
})();
