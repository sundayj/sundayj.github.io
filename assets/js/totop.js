(() => {
  const upperLimit = 1000;
  const scrollElem = document.getElementById('totop');

  if (!scrollElem) {
    return;
  }

  const updateVisibility = () => {
    const shouldShow = window.scrollY > upperLimit;
    scrollElem.hidden = !shouldShow;
    scrollElem.style.opacity = shouldShow ? '1' : '0';
  };

  scrollElem.hidden = true;
  scrollElem.style.transition = 'opacity 300ms ease';

  window.addEventListener('scroll', updateVisibility, { passive: true });
  scrollElem.addEventListener('click', (event) => {
    event.preventDefault();
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  updateVisibility();
})();
