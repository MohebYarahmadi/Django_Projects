(function () {
  var siteUrl = 'https://mysite.com:8000/';   // or http:// if running plain runserver
  var styleUrl = siteUrl + 'static/css/bookmarklet.css';
  var minWidth = 250;
  var minHeight = 250;

  // ---- Load CSS once ----
  if (!document.getElementById('bookmarklet-css')) {
    var link = document.createElement('link');
    link.id = 'bookmarklet-css';
    link.rel = 'stylesheet';
    link.type = 'text/css';
    link.href = styleUrl + '?r=' + Date.now();
    document.head.appendChild(link);
  }

  // ---- Inject box once ----
  if (!document.getElementById('bookmarklet')) {
    var wrapper = document.createElement('div');
    wrapper.innerHTML = `
      <div id="bookmarklet">
        <a href="#" id="close">&times;</a>
        <h1>Select an image to bookmark:</h1>
        <div class="images"></div>
      </div>`;
    document.body.appendChild(wrapper.firstElementChild);

    // close handler — attached ONCE
    document.querySelector('#bookmarklet #close')
      .addEventListener('click', function (e) {
        e.preventDefault();
        document.getElementById('bookmarklet').style.display = 'none';
      });
  }

  function bookmarkletLaunch() {
    var panel = document.getElementById('bookmarklet');
    var imagesFound = panel.querySelector('.images');
    imagesFound.innerHTML = '';
    panel.style.display = 'block';

    var imgs = document.querySelectorAll(
      'img[src$=".jpg"], img[src$=".jpeg"], img[src$=".png"], img[src$=".webp"], img[src$=".gif"]'
    );

    imgs.forEach(function (image) {
      if (image.naturalWidth >= minWidth && image.naturalHeight >= minHeight) {
        var found = document.createElement('img');
        found.src = image.currentSrc || image.src;
        imagesFound.appendChild(found);
      }
    });

    imagesFound.querySelectorAll('img').forEach(function (image) {
      image.addEventListener('click', function (event) {
        var selected = event.target;
        panel.style.display = 'none';
        window.open(
          siteUrl + 'images/create/?url=' +
            encodeURIComponent(selected.src) +
            '&title=' +
            encodeURIComponent(document.title),
          '_blank'
        );
      });
    });
  }

  // Expose globally so the loader can call it on later clicks
  window.bookmarkletLaunch = bookmarkletLaunch;
  bookmarkletLaunch();
})();
