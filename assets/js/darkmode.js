const userPref = window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark'
const currentTheme = localStorage.getItem('theme') ?? userPref

if (currentTheme) {
  document.documentElement.setAttribute('saved-theme', currentTheme);
}

const switchTheme = (e) => {
  if (e.target.checked) {
    localStorage.setItem('theme', 'dark')
    document.documentElement.setAttribute('saved-theme', 'dark')
  }
  else {
    localStorage.setItem('theme', 'light')
    document.documentElement.setAttribute('saved-theme', 'light')
  }
  GnuplotRenderer.renderPage();
}

window.addEventListener('DOMContentLoaded', () => {
  // Darkmode toggle
  const toggleSwitch = document.querySelector('#darkmode-toggle')

  // listen for toggle
  toggleSwitch.addEventListener('change', switchTheme, false)

  if (currentTheme === 'dark') {
    toggleSwitch.checked = true
  }
})
