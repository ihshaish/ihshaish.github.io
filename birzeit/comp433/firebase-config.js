// ---------------------------------------------------------------------------
// COMP433 — shared Firebase config for the Presentation Booking calendar.
//
// The booking widget (in both Section 5 and Section 6 protected pages) reads
// this single file, so you paste your Firebase web config ONCE here and both
// sections stay in sync.
//
// HOW TO GO LIVE (one-time, ~5 minutes):
//   1. Go to https://console.firebase.google.com  →  create a project
//      (or reuse the existing "comp322-live" project — both are fine; the
//      booking data lives under its own path "comp433/presentations").
//   2. In the project, enable:
//        • Build → Authentication → Sign-in method → Anonymous  (Enable)
//        • Build → Realtime Database → Create database  (start in locked mode)
//   3. Paste the security rules from firebase-rules.json (same folder) into
//      Realtime Database → Rules → Publish.
//   4. Project settings → "Your apps" → Web app → copy the firebaseConfig
//      object and paste its values below (replace every PASTE_… placeholder).
//   5. Commit & push. The booking calendar goes live automatically.
//
// Until the placeholders are filled in, the widget shows a friendly
// "booking not live yet" notice and a preview of the slot grid.
// ---------------------------------------------------------------------------
window.COMP433_FIREBASE_CONFIG = {
  apiKey: "PASTE_YOUR_API_KEY_HERE",
  authDomain: "PASTE_PROJECT.firebaseapp.com",
  databaseURL: "https://PASTE_PROJECT-default-rtdb.firebaseio.com",
  projectId: "PASTE_PROJECT",
  storageBucket: "PASTE_PROJECT.appspot.com",
  messagingSenderId: "PASTE_YOUR_SENDER_ID",
  appId: "PASTE_YOUR_APP_ID"
};
