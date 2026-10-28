/* Offline support for the reading app. Scope is the /books/ mount; everything the
   reader loads is cached so a started book keeps working without a connection, and
   repeat visits paint from cache. No analytics, no cross-origin caching. */
const VERSION = "v1";
const CACHE = "reader-" + VERSION;
const SCOPE = new URL(self.registration.scope).pathname;        // "/books/"
const shellURL = path => new URL(path, self.registration.scope).toString();

// Stable (non-hashed) shell URLs worth having before the first offline load.
// Content-hashed JS is picked up at runtime on first visit.
const CORE = ["", "read.html", "manifest.json", "app.webmanifest",
  "book-view.css", "book-pages.css", "visual-polish.css", "reference-reader.css",
  "fonts/fonts.css", "favicon.svg", "icon-192.png", "icon-512.png"];

self.addEventListener("install", e => {
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(c =>
    Promise.allSettled(CORE.map(u => c.add(shellURL(u))))));
});

self.addEventListener("activate", e => {
  e.waitUntil((async () => {
    for (const k of await caches.keys()) if (k !== CACHE) await caches.delete(k);
    await self.clients.claim();
  })());
});

function store(req, res) {
  if (res && res.ok && res.type === "basic") caches.open(CACHE).then(c => c.put(req, res)).catch(() => {});
  return res;
}

self.addEventListener("fetch", e => {
  const req = e.request;
  if (req.method !== "GET") return;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin || !url.pathname.startsWith(SCOPE)) return;   // leave cross-origin & off-scope alone

  // HTML pages and content JSON (episodes, dict, gist, manifest): fresh when online,
  // cache when offline; a navigation offline falls back to the reader shell.
  if (req.mode === "navigate" || url.pathname.endsWith(".json")) {
    e.respondWith(
      fetch(req).then(r => store(req, r.clone()) && r)
        .catch(() => caches.match(req).then(m => m || caches.match(shellURL("read.html")))));
    return;
  }
  // Static assets (hashed JS, CSS, fonts, SVG, PNG): cache-first, refresh in the background.
  e.respondWith(caches.match(req).then(hit => {
    const net = fetch(req).then(r => store(req, r.clone()) && r).catch(() => hit);
    return hit || net;
  }));
});
