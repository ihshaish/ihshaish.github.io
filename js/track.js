/* Photo-section tracking, wired into the existing Birzeit visitor system.
 * Reuses the gate's stored Birzeit ID (localStorage 'birzeit_visitor_id') and the
 * same Apps Script endpoint, so photo activity lands in your existing Sheet
 * (a separate 'photos' tab). Events fired on the homepage photo wall:
 *   - 'pictures_view'  when the photo section scrolls into view
 *   - 'photo_enlarge'  (with the caption) each time a photo is shown in the
 *                      lightbox, i.e. on open AND on every prev/next slide
 *   - 'video_play'     when the clip is played
 * If a visitor never passed a gate, id is 'anon'.
 */
(function () {
  var ENDPOINT = "https://script.google.com/macros/s/AKfycbxoJo0jG7fu2ccTBQj_FmdCxaEm9zdi7je1LvF9XB1C_ndWrHbaH5MCcCEqY8ZrRuHKYA/exec";

  function vid() {
    try { return localStorage.getItem('birzeit_visitor_id') || 'anon'; }
    catch (e) { return 'anon'; }
  }

  function send(ev, detail) {
    var data = {
      id: vid(), event: ev, detail: detail || '',
      page: location.pathname + location.hash,
      ref: document.referrer || '',
      ts: new Date().toISOString()
    };
    try {
      var body = JSON.stringify(data);
      if (navigator.sendBeacon) navigator.sendBeacon(ENDPOINT, body);
      else fetch(ENDPOINT, {
        method: 'POST', mode: 'no-cors',
        headers: { 'Content-Type': 'text/plain;charset=utf-8' },
        body: body, keepalive: true
      });
    } catch (e) {}
  }
  window.vtrack = send;

  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }
  ready(function () {
    // photo section scrolled into view
    var sec = document.getElementById('personal') || document.querySelector('.rg-track');
    if (sec && 'IntersectionObserver' in window) {
      var seen = false;
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting && !seen) { seen = true; send('pictures_view'); io.disconnect(); }
        });
      }, { threshold: 0.25 });
      io.observe(sec);
    }

    // every photo shown in the lightbox: open + each prev/next slide
    var im = document.getElementById('rg-lb-img'), cap = document.getElementById('rg-lb-cap');
    if (im && 'MutationObserver' in window) {
      new MutationObserver(function () {
        if (im.getAttribute('src')) send('photo_enlarge', (cap && cap.textContent) || '');
      }).observe(im, { attributes: true, attributeFilter: ['src'] });
    }

    // video played
    var v = document.querySelector('.rg-video video');
    if (v) {
      var fired = false;
      v.addEventListener('play', function () {
        if (!fired) { fired = true; send('video_play', 'Atef teaching me English (video)'); }
      });
    }
  });
})();
