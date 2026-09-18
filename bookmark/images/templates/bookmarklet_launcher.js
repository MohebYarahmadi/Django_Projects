(function () {
  if (window.bookmarkletLaunch) {
    window.bookmarkletLaunch();
    return;
  }
  var s = document.createElement('script');
  s.src = 'https://mysite.com:8000/static/js/bookmarklet.js?r=' + Date.now();
  s.onload = function () {
    if (window.bookmarkletLaunch) window.bookmarkletLaunch();
  };
  s.onerror = function () {
    console.error('[bookmarklet] failed to load from mysite.com:8000');
  };
  document.body.appendChild(s);
})();
