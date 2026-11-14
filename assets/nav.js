/* Adds a small "Home | Privacy Policy" bar to the top of any page.
   Added to every game automatically by add-nav.py. */
(function () {
  if (document.getElementById('site-nav')) return;
  var src = document.currentScript && document.currentScript.src;
  var root = src ? new URL('../', src) : new URL('./', location.href);

  var css = document.createElement('style');
  css.textContent =
    '#site-nav{position:fixed;top:0;left:0;z-index:2147483647;display:flex;gap:14px;' +
    'padding:6px 12px;background:rgba(20,20,22,.88);border-bottom-right-radius:8px;' +
    'font:14px system-ui,-apple-system,"Segoe UI",sans-serif}' +
    '#site-nav a{color:#3ea6ff;text-decoration:underline}' +
    '#site-nav a:hover{color:#8fcbff}';
  document.head.appendChild(css);

  var nav = document.createElement('nav');
  nav.id = 'site-nav';
  nav.setAttribute('aria-label', 'Site');
  [['Home', 'index.html'], ['Privacy Policy', 'privacy.html']].forEach(function (l) {
    var a = document.createElement('a');
    a.textContent = l[0];
    a.href = new URL(l[1], root).href;
    nav.appendChild(a);
  });
  document.body.appendChild(nav);
})();
