/*
 * Birzeit course-material visitor gate.
 *
 * What it does:
 *   - Asks first-time visitors for their Birzeit ID or email before revealing
 *     the page.
 *   - Stores the ID in localStorage so they are only prompted once per browser.
 *   - Posts the ID + page URL + timestamp to a Google Apps Script endpoint,
 *     which writes a row to a private Google Sheet you own. Name lookup
 *     happens server-side, so no roster data is exposed in this file.
 *   - Does NOT restrict access. Anyone with a valid-format ID gets in.
 *
 * Accepted inputs:
 *   - 7-digit Birzeit student ID (e.g. 1220063)
 *   - Birzeit email (e.g. 1220063@stbzu.birzeit.edu or 1220063@birzeit.edu)
 *   - Instructor bypass token: HI-2386
 */

(function () {
  'use strict';

  // -------- configuration --------
  var STORAGE_KEY = 'birzeit_visitor_id';
  var INSTRUCTOR_TOKEN = 'HI-2386';
  // PASTE the deployed Apps Script /exec URL between the quotes.
  // Until this is filled in, the gate still works locally; logging is skipped.
  var APPS_SCRIPT_URL = 'https://script.google.com/macros/s/AKfycbxoJo0jG7fu2ccTBQj_FmdCxaEm9zdi7je1LvF9XB1C_ndWrHbaH5MCcCEqY8ZrRuHKYA/exec';
  // --------------------------------

  var stored = null;
  try { stored = localStorage.getItem(STORAGE_KEY); } catch (e) { /* private mode */ }

  // If no ID is stored yet, hide page content immediately so it does not
  // flash before the modal appears.
  if (!stored) {
    var hide = document.createElement('style');
    hide.id = 'bz-gate-hide';
    hide.textContent =
      'body > *:not(.bz-gate-overlay) { visibility: hidden !important; }';
    (document.head || document.documentElement).appendChild(hide);
  }

  function validate(raw) {
    var v = (raw || '').trim();
    var m = v.match(/^(\d{7})@(stbzu\.)?birzeit\.edu$/i);
    if (m) return m[1];
    if (/^\d{7}$/.test(v)) return v;
    if (v.toUpperCase() === INSTRUCTOR_TOKEN) return INSTRUCTOR_TOKEN;
    return null;
  }

  // Best-effort public-IP lookup (Apps Script cannot read the client IP itself).
  // Used mainly to attach an IP to visitors whose ID is not on the roster.
  function getIp(cb) {
    var done = false;
    function fin(v) { if (!done) { done = true; cb(v || ''); } }
    try {
      var x = new XMLHttpRequest();
      x.open('GET', 'https://api.ipify.org?format=json', true);
      x.timeout = 3000;
      x.onreadystatechange = function () {
        if (x.readyState === 4) { var ip = ''; try { ip = JSON.parse(x.responseText).ip || ''; } catch (e) {} fin(ip); }
      };
      x.onerror = function () { fin(''); };
      x.ontimeout = function () { fin(''); };
      x.send();
    } catch (e) { fin(''); }
    setTimeout(function () { fin(''); }, 3500);
  }

  function logVisit(id) {
    if (!APPS_SCRIPT_URL || APPS_SCRIPT_URL.indexOf('PASTE_') === 0) return;
    getIp(function (ip) {
      try {
        fetch(APPS_SCRIPT_URL, {
          method: 'POST',
          mode: 'no-cors',
          headers: { 'Content-Type': 'text/plain;charset=utf-8' },
          body: JSON.stringify({
            id: id,
            ip: ip,
            page: location.pathname,
            ts: new Date().toISOString(),
            ua: navigator.userAgent,
            ref: document.referrer || ''
          }),
          keepalive: true
        });
      } catch (e) { /* silent: gate must not block the page if logging fails */ }
    });
  }

  function reveal() {
    var el = document.getElementById('bz-gate-hide');
    if (el) el.remove();
  }

  function showGate() {
    var overlay = document.createElement('div');
    overlay.className = 'bz-gate-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.innerHTML = [
      '<style>',
      '.bz-gate-overlay {',
      '  position: fixed; inset: 0; z-index: 2147483647;',
      '  background: rgba(20, 30, 40, 0.92);',
      '  display: flex; align-items: center; justify-content: center;',
      '  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;',
      '  backdrop-filter: blur(8px);',
      '  -webkit-backdrop-filter: blur(8px);',
      '  visibility: visible !important;',
      '  padding: 20px;',
      '}',
      '.bz-gate-card {',
      '  background: #faf6ee; color: #1a2332;',
      '  width: 100%; max-width: 460px;',
      '  padding: 36px 36px 28px;',
      '  border-radius: 8px;',
      '  box-shadow: 0 20px 60px rgba(0,0,0,0.4);',
      '  border-top: 4px solid #004B23;',
      '  box-sizing: border-box;',
      '}',
      '.bz-gate-card .bz-eyebrow {',
      '  font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase;',
      '  color: #004B23; font-weight: 600; margin: 0 0 10px;',
      '}',
      '.bz-gate-card h2 {',
      '  font-family: "Cormorant Garamond", Georgia, "Times New Roman", serif;',
      '  font-size: 28px; font-weight: 500;',
      '  margin: 0 0 12px; color: #1a2332; letter-spacing: -0.01em;',
      '  line-height: 1.15;',
      '}',
      '.bz-gate-card .bz-lede {',
      '  font-size: 14px; line-height: 1.55;',
      '  color: #4a5468; margin: 0 0 22px;',
      '}',
      '.bz-gate-card label {',
      '  display: block; font-size: 11px; letter-spacing: 0.1em;',
      '  text-transform: uppercase; font-weight: 600;',
      '  color: #1a2332; margin-bottom: 6px;',
      '}',
      '.bz-gate-card input {',
      '  width: 100%; padding: 11px 14px;',
      '  border: 1px solid #c9bfa8; border-radius: 4px;',
      '  background: white; font-size: 15px;',
      '  font-family: inherit; color: #1a2332;',
      '  box-sizing: border-box;',
      '}',
      '.bz-gate-card input:focus {',
      '  outline: none; border-color: #004B23;',
      '  box-shadow: 0 0 0 3px rgba(0, 75, 35, 0.15);',
      '}',
      '.bz-gate-card .bz-error {',
      '  color: #a83232; font-size: 13px; min-height: 18px;',
      '  margin-top: 8px;',
      '}',
      '.bz-gate-card button {',
      '  margin-top: 14px; width: 100%; padding: 12px;',
      '  background: #004B23; color: white;',
      '  border: none; border-radius: 4px;',
      '  font-size: 13px; font-weight: 600; letter-spacing: 0.06em;',
      '  text-transform: uppercase; cursor: pointer;',
      '  font-family: inherit;',
      '  transition: background 0.15s;',
      '}',
      '.bz-gate-card button:hover { background: #006030; }',
      '.bz-gate-card button:active { background: #003a1a; }',
      '.bz-gate-card .bz-note {',
      '  margin-top: 20px; font-size: 12px; color: #7a7466;',
      '  line-height: 1.5; border-top: 1px solid #e6dec7; padding-top: 14px;',
      '}',
      '</style>',
      '<div class="bz-gate-card">',
      '  <div class="bz-eyebrow">Birzeit University &middot; Course Material</div>',
      '  <h2>Sign in to continue</h2>',
      '  <p class="bz-lede">Please log in with your Birzeit ID or university email.</p>',
      '  <label for="bz-gate-input">Birzeit ID or email</label>',
      '  <input id="bz-gate-input" type="text" autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" placeholder="1220063  or  1220063@stbzu.birzeit.edu">',
      '  <div class="bz-error" id="bz-gate-error" aria-live="polite"></div>',
      '  <button id="bz-gate-submit" type="button">Continue</button>',
      '</div>'
    ].join('\n');

    document.body.appendChild(overlay);

    var input  = overlay.querySelector('#bz-gate-input');
    var submit = overlay.querySelector('#bz-gate-submit');
    var errEl  = overlay.querySelector('#bz-gate-error');

    function attempt() {
      var id = validate(input.value);
      if (!id) {
        errEl.textContent =
          'Please enter a valid 7-digit Birzeit ID or university email.';
        input.focus();
        input.select();
        return;
      }
      try { localStorage.setItem(STORAGE_KEY, id); } catch (e) { /* ignore */ }
      logVisit(id);
      overlay.remove();
      reveal();
    }

    submit.addEventListener('click', attempt);
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter') { e.preventDefault(); attempt(); }
    });
    input.addEventListener('input', function () { errEl.textContent = ''; });

    // Focus a moment after insertion so screen-readers announce the modal first.
    setTimeout(function () { try { input.focus(); } catch (e) {} }, 60);
  }

  function init() {
    if (stored) {
      logVisit(stored);
      return;
    }
    showGate();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
