/* Service worker dell'app Flotta.
   L'applicazione è un file solo: la si tiene in cache e si apre anche senza
   rete. I dati non passano di qui: stanno nell'archivio del telefono e,
   quando parte la coda, su SharePoint. */
const VER = 'flotta-app-1.0.0';
const GUSCIO = ['./', './index.html', './manifest.webmanifest',
  './icons/icon-192.png', './icons/icon-512.png', './icons/apple-touch-icon.png', './icons/favicon-32.png'];

self.addEventListener('install', e => {
  e.waitUntil((async () => {
    const c = await caches.open(VER);
    await Promise.allSettled(GUSCIO.map(u => c.add(new Request(u, { cache: 'reload' }))));
    self.skipWaiting();
  })());
});
self.addEventListener('activate', e => {
  e.waitUntil((async () => {
    for (const k of await caches.keys()) if (k !== VER) await caches.delete(k);
    await self.clients.claim();
  })());
});
self.addEventListener('message', e => { if (e.data === 'aggiorna') self.skipWaiting(); });

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;            // Graph e Microsoft passano diretti
  if (url.pathname.endsWith('/config.json')) return;      // mai dalla cache

  e.respondWith((async () => {
    try {
      const res = await fetch(req);
      if (res.ok) (await caches.open(VER)).put(req, res.clone());
      return res;
    } catch (err) {
      const hit = await caches.match(req) || await caches.match('./index.html');
      if (hit) return hit;
      throw err;
    }
  })());
});
