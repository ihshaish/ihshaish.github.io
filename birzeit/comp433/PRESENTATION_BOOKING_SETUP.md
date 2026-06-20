# COMP433 Presentation Booking — setup & operation

A shared, live-synced presentation slot calendar for **both Section 5 and Section 6**,
embedded behind the existing password in each section's protected page
(Project → **Presentation Booking** tab).

## What it does
- Shows 22 slots: **Wed 24 Jun 15:00–17:30** (7 × 20 min) and **Thu 25 Jun 12:00–17:00** (15 × 20 min).
- A group picks a free slot → chooses **Section (5 or 6)** and **Group letter** → member **names and student IDs prefill from the roster** and are **editable** → confirms.
- Bookings sync in **real time across both sections** (a taken slot vanishes for everyone instantly).
- A group can **edit or cancel** its own booking; booking a second slot automatically frees the first (one slot per group).
- Race-safe: claiming a slot uses a Realtime Database transaction, so two groups can't grab the same slot.

## Capacity note
22 slots vs **26 groups** (S5: A–N = 14, S6: A–L = 12). If every group presents, you are **~4 slots short** —
either extend a window (e.g. Wed to 18:40 gives 26), switch to 15-minute slots (fits 26 exactly), or handle
the overflow manually. Edit the `SLOTS` array in the booking block (in both `protected-content-s5.html`
and `protected-content-s6.html`), then re-run `node encrypt.js`.

## Go live (one-time, ~5 min)
1. **Firebase project** — https://console.firebase.google.com → create a project,
   *or reuse the existing* `comp322-live` project (booking data lives under its own `comp433/` path).
2. Enable **Authentication → Anonymous**.
3. Create a **Realtime Database**.
4. Paste **`firebase-rules.json`** into Realtime Database → Rules → Publish.
5. Copy the web app's `firebaseConfig` into **`firebase-config.js`** (replace every `PASTE_…`).
6. Commit & push. The calendar goes live automatically; until then it shows a "not live yet" preview.

## Files
- `firebase-config.js` — paste credentials here (read by both sections).
- `firebase-rules.json` — Realtime Database security rules (authed read; create-if-empty / owner-only edit).
- Booking widget markup + logic lives inside `protected-content-s5.html` and `protected-content-s6.html`
  (identical block, self-scoping). After editing either, re-run `node encrypt.js` to repackage `index.html`.

## Viewing / exporting bookings
Firebase console → Realtime Database → `comp433/presentations/v1/bookings`. Each node is a slot id
(`w-1500`, `ta-1200`, `tp-1640`, …) holding `{section, letter, biz, members[], owner, at}`.
