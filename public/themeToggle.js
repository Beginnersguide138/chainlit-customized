// Minimal light/dark-theme switcher for Chainlit UI
//
// This file purposefully strips away all heavy visual effects present in
// public/script.js and keeps ONLY the logic that updates colors when the
// `<html>` element gains / loses the `dark` class.
//
// 1. On load it checks the current theme and applies the matching palette.
// 2. It observes class changes on <html> so manual or system-driven toggles
//    are picked up instantly.
// 3. Only two CSS custom properties are updated here to demonstrate the
//    concept:  --cl-bg  (background) and  --cl-fg  (foreground / text).
//    You can extend `applyTheme()` with more variables if needed.
//
// NOTE • Include this file in Chainlit’s template (e.g. public/index.html)
//       after the built-in bundle so it can run immediately.

document.addEventListener('DOMContentLoaded', () => {
  // utility – set the two CSS variables depending on dark / light
  function applyTheme(isDark) {
    const root = document.documentElement;
    if (isDark) {
      root.style.setProperty('--cl-bg', '#111827'); // near-black
      root.style.setProperty('--cl-fg', '#F9FAFB'); // light text
    } else {
      root.style.setProperty('--cl-bg', '#FFFFFF'); // white
      root.style.setProperty('--cl-fg', '#1F2937'); // dark text
    }

    // Immediately update the landing-page hero section so theme switching
    // is visually obvious without relying on CSS variables elsewhere.
    const hero = document.querySelector('.compact-hero');
    if (hero) {
      hero.style.background = isDark
        ? 'linear-gradient(135deg, #1e3a8a 0%, #312e81 100%)'
        : 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)';
    }
  }

  // initial application
  const htmlEl = document.documentElement;
  // unified dark-mode checker (data-theme or .dark class)
  function isDark() {
    return (
      htmlEl.getAttribute('data-theme') === 'dark' ||
      htmlEl.classList.contains('dark')
    );
  }
  applyTheme(isDark());

  // watch for future changes
  const obs = new MutationObserver((muts) => {
    muts.forEach((m) => {
      if (m.attributeName === 'class') {
        applyTheme(isDark());
      }
    });
  });
  obs.observe(htmlEl, {
    attributes: true,
    attributeFilter: ['class', 'data-theme']
  });
});
