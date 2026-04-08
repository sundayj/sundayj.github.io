(() => {
  const upperLimit = 1000;
  const scrollElem = document.getElementById("totop");
  const scrollButton = document.getElementById("totop-button");

  if (!scrollElem || !scrollButton) {
    return;
  }

  const updateVisibility = () => {
    if (window.scrollY > upperLimit) {
      scrollElem.classList.add("is-visible");
    } else {
      scrollElem.classList.remove("is-visible");
    }
  };

  scrollButton.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  updateVisibility();
  window.addEventListener("scroll", updateVisibility, { passive: true });
})();
