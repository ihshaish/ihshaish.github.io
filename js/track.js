/* Anonymous, per-session journey tracking.
 * Privacy: a random id kept only in sessionStorage (gone when the tab closes).
 * No student id, no name, no cookies, no fingerprinting. Inert until ENDPOINT is set.
 * Logs: every page view (path + referrer), a "pictures_view" when the photo
 * section is scrolled into view, and "photo_enlarge" (with the caption) when a
 * photo is opened in the lightbox. Same session id ties the journey together,
 * so you can see if a session that opened a course page also reached the photos.
 */
(function () {
  var ENDPOINT = ""; // <-- paste your Google Apps Script /exec URL here to switch it on
  if (!ENDPOINT) return;

  function sid() {
    try {
      var s = sessionStorage.getItem("vsid");
      if (!s) {
        s = Date.now().toString(36) + "-" + Math.random().toString(36).slice(2, 9);
        sessionStorage.setItem("vsid", s);
      }
      return s;
    } catch (e) { return "nostore"; }
  }

  function send(ev, detail) {
    var data = {
      sid: sid(), ev: ev, detail: detail || "",
      path: location.pathname + location.hash,
      ref: document.referrer || "",
      t: new Date().toISOString()
    };
    try {
      var body = JSON.stringify(data);
      if (navigator.sendBeacon) navigator.sendBeacon(ENDPOINT, body);
      else fetch(ENDPOINT, { method: "POST", body: body, mode: "no-cors", keepalive: true });
    } catch (e) {}
  }
  window.vtrack = send;

  send("view"); // page view (includes the path, so course pages are distinguishable)

  function ready(fn) {
    if (document.readyState !== "loading") fn();
    else document.addEventListener("DOMContentLoaded", fn);
  }
  ready(function () {
    // photo section came into view
    var sec = document.getElementById("personal") || document.querySelector(".rg-track");
    if (sec && "IntersectionObserver" in window) {
      var seen = false;
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (en) {
          if (en.isIntersecting && !seen) { seen = true; send("pictures_view"); io.disconnect(); }
        });
      }, { threshold: 0.25 });
      io.observe(sec);
    }
    // a photo was enlarged in the lightbox
    var lb = document.getElementById("rg-lb"), cap = document.getElementById("rg-lb-cap");
    if (lb && "MutationObserver" in window) {
      var was = false;
      new MutationObserver(function () {
        var open = lb.classList.contains("open");
        if (open && !was) send("photo_enlarge", (cap && cap.textContent) || "");
        was = open;
      }).observe(lb, { attributes: true, attributeFilter: ["class"] });
    }
  });
})();
