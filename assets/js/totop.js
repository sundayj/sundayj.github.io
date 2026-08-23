(() => {
  const upperLimit = 1000;
  const scrollElem = document.getElementById('totop');

  if (!scrollElem) {
    return;
  }

  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  const updateVisibility = () => {
    const shouldShow = window.scrollY > upperLimit;
    scrollElem.style.opacity = shouldShow ? '1' : '0';
    scrollElem.style.pointerEvents = shouldShow ? 'auto' : 'none';
    scrollElem.setAttribute('aria-hidden', shouldShow ? 'false' : 'true');
    scrollElem.tabIndex = shouldShow ? 0 : -1;
  };

  scrollElem.style.opacity = '0';
  scrollElem.style.pointerEvents = 'none';
  scrollElem.style.transition = reducedMotion.matches ? 'none' : 'opacity 300ms ease';

  window.addEventListener('scroll', updateVisibility, { passive: true });
  reducedMotion.addEventListener?.('change', (event) => {
    scrollElem.style.transition = event.matches ? 'none' : 'opacity 300ms ease';
  });

  scrollElem.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: reducedMotion.matches ? 'auto' : 'smooth',
    });
  });

  updateVisibility();
})();
