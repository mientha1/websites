/* PM Shooter — interactions. Vanilla, defensive, no dependencies. */
(() => {
  'use strict';
  const $ = (s, c = document) => c.querySelector(s);
  const $$ = (s, c = document) => [...c.querySelectorAll(s)];

  /* ---------------------------------------------- header ---- */
  const hd = $('.hd');
  const onScroll = () => hd && hd.classList.toggle('is-solid', window.scrollY > 12);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ----------------------------------------- mobile menu ---- */
  const menuBtn = $('[data-menu-btn]');
  const menu = $('#menu');
  let lastFocus = null;
  const setMenu = (open) => {
    if (!menu || !menuBtn) return;
    menuBtn.setAttribute('aria-expanded', String(open));
    menu.hidden = !open;
    document.body.classList.toggle('menu-open', open);
    if (open) { lastFocus = document.activeElement; ($('a', menu) || menu).focus({ preventScroll: true }); }
    else if (lastFocus) lastFocus.focus({ preventScroll: true });
  };
  menuBtn?.addEventListener('click', () => setMenu(menu.hidden));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && menu && !menu.hidden) setMenu(false);
  });
  $$('a', menu || document.createElement('div')).forEach(a => a.addEventListener('click', () => setMenu(false)));

  /* -------------------------------------------- reveals ----- */
  if (!matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window) {
    const io = new IntersectionObserver((es) => {
      es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('on'); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
    $$('.rv').forEach(el => io.observe(el));
  } else {
    $$('.rv').forEach(el => el.classList.add('on'));
  }

  /* ------------------------------------- package filters ---- */
  const tierBtns = $$('.pkg-tiers [data-tier]');
  if (tierBtns.length) {
    const rows = $$('[data-pkg-tier]');
    const counter = $('[data-pkg-count]');
    const apply = (tier) => {
      tierBtns.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.tier === tier)));
      let n = 0;
      rows.forEach(r => {
        const show = tier === 'wszystkie' || r.dataset.pkgTier === tier;
        r.hidden = !show;
        if (show) n++;
      });
      if (counter) counter.textContent = n;
    };
    tierBtns.forEach(b => b.addEventListener('click', () => apply(b.dataset.tier)));
    apply('wszystkie');
  }

  /* ------------------------------------- arsenal search ----- */
  const aSearch = $('[data-ars-search]');
  if (aSearch) {
    const cards = $$('[data-ars-item]');
    const secs = $$('[data-ars-sec]');
    const info = $('[data-ars-info]');
    const norm = (s) => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
    aSearch.addEventListener('input', () => {
      const q = norm(aSearch.value.trim());
      let n = 0;
      cards.forEach(c => {
        const hit = !q || norm(c.dataset.arsItem).includes(q);
        c.hidden = !hit;
        if (hit) n++;
      });
      secs.forEach(s => { s.hidden = q && !$$('[data-ars-item]:not([hidden])', s).length; });
      if (info) {
        info.hidden = !q;
        info.textContent = q ? `Znaleziono: ${n}` : '';
      }
    });
  }

  /* ------------------------------------------- lightbox ----- */
  const lbx = $('dialog.lbx');
  if (lbx && typeof lbx.showModal === 'function') {
    const items = $$('.gi');
    const im = $('.lbx__img', lbx);
    const cap = $('.lbx__cap', lbx);
    let i = 0;
    const show = (n) => {
      i = (n + items.length) % items.length;
      const src = items[i].dataset.full || $('img', items[i])?.src;
      const alt = $('img', items[i])?.alt || '';
      im.src = src; im.alt = alt; cap.textContent = alt;
    };
    items.forEach((el, n) => el.addEventListener('click', () => { show(n); lbx.showModal(); }));
    $('.lbx__prev', lbx)?.addEventListener('click', () => show(i - 1));
    $('.lbx__next', lbx)?.addEventListener('click', () => show(i + 1));
    $('.lbx__close', lbx)?.addEventListener('click', () => lbx.close());
    lbx.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') show(i - 1);
      if (e.key === 'ArrowRight') show(i + 1);
    });
    lbx.addEventListener('click', (e) => { if (e.target === lbx || e.target.classList.contains('lbx__in')) lbx.close(); });
  }

  /* -------------------------------- mobile bar vs footer ---- */
  const mbar = $('[data-mbar]');
  const ft = $('.ft');
  if (mbar && ft && 'IntersectionObserver' in window) {
    new IntersectionObserver((es) => {
      es.forEach(e => mbar.classList.toggle('is-hidden', e.isIntersecting));
    }, { threshold: 0.05 }).observe(ft);
  }
  menuBtn?.addEventListener('click', () => mbar?.classList.toggle('is-hidden', !menu.hidden === false && !menu.hidden));
})();
