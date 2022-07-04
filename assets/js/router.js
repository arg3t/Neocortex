import {
  apply,
  navigate,
  prefetch,
  router,
} from "https://unpkg.com/million@1.11.5-0/dist/router.mjs"

export const attachSPARouting = (init, rerender) => {
  // Attach SPA functions to the global Million namespace
  window.Million = {
    apply,
    navigate,
    prefetch,
    router,
  }

  const render = () => {
    requestAnimationFrame(rerender);
    mermaid.initialize({ startOnLoad: true, theme: ((currentTheme == "dark") ? "dark" : "default")});
    GnuplotRenderer.renderPage();
  };

  window.addEventListener("DOMContentLoaded", () => {
    apply((doc) => init(doc))
    init()
    router(".singlePage")
    render()
  })
  window.addEventListener("million:navigate", render)
}
