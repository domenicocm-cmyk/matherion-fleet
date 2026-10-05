/* Service worker del Gestionale flotta.
   Strategia: rete prima per le pagine (così un aggiornamento pubblicato arriva
   subito), cache come riserva quando non c'è connessione; cache prima per icone
   e manifest, che cambiano di rado.
   I dati NON passano di qui: restano nel registro .xlsx della cartella di lavoro. */

const VER = 'flotta-2026.10.05d';
const SHELL = [
  '/',
  '/burago',
  '/manifest.webmanifest',
  '/manifest-burago.webmanifest',
  '/icons/icon-192.png',
  '/icons/icon-512.png',
  '/icons/maskable-192.png',
  '/icons/maskable-512.png',
  '/icons/apple-touch-icon.png',
  '/icons/favicon-32.png',
  '/icons/icon-192-burago.png',
  '/icons/icon-512-burago.png',
  '/icons/maskable-192-burago.png',
  '/icons/maskable-512-burago.png',
  '/icons/apple-touch-icon-burago.png',
  '/icons/favicon-32-burago.png'
];

self.addEventListener('install', e => {
  e.waitUntil((async () => {
    const c = await caches.open(VER);
    await Promise.allSettled(SHELL.map(u => c.add(new Request(u, { cache: 'reload' }))));
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

const isIcona = u => u.pathname.startsWith('/icons/') || u.pathname.endsWith('.webmanifest');
// la configurazione degli accessi non va mai tenuta in cache: deve poter cambiare subito
const isConfig = u => u.pathname === '/config.json';

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);
  if (url.origin !== location.origin) return;
  if (url.pathname.startsWith('/app')) return;   // l'app dei telefoni ha il suo

  if (isConfig(url)) return;                // sempre dalla rete, mai dalla cache

  if (isIcona(url)) {                       // cache prima
    e.respondWith((async () => {
      const hit = await caches.match(req);
      if (hit) return hit;
      const res = await fetch(req);
      if (res.ok) (await caches.open(VER)).put(req, res.clone());
      return res;
    })());
    return;
  }

  e.respondWith((async () => {              // rete prima
    try {
      const res = await fetch(req);
      if (res.ok) (await caches.open(VER)).put(req, res.clone());
      return res;
    } catch (err) {
      const hit = await caches.match(req) || await caches.match(new URL(req.url).pathname);
      if (hit) return hit;
      if (req.mode === 'navigate') {
        const home = await caches.match('/');
        if (home) return home;
      }
      throw err;
    }
  })());
});
