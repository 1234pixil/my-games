# My Games

Browser games and tools. Everything runs in the browser.

## Structure

```
index.html        Home page (game list is generated)
privacy.html      Privacy Policy
assets/nav.js     The "Home | Privacy Policy" bar shown on every page
games/            One .html file per game or tool
add-nav.py        Adds the bar to every game and rebuilds the home page list
```

## Adding games

1. Save each game as an `.html` file in `games/` (for example `games/gulp-pond.html`).
2. Run `python add-nav.py`.
3. Open `index.html` to check it.

## Putting it on GitHub

```
git init
git add .
git commit -m "Add my games"
git branch -M main
git remote add origin https://github.com/YOUR-NAME/YOUR-REPO.git
git push -u origin main
```

To get a live link, turn on **GitHub Pages** in the repo's Settings (Pages, then deploy from the `main` branch).

Before publishing, add your contact details to `privacy.html` (search for `TODO`).
