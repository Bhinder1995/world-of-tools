const CACHE_NAME = 'world-of-tools-v4';
const ASSETS_TO_CACHE = [
    '/',
    '/index.html',
    '/css/style.css?v=1.2',
    '/js/common.js?v=1.2',
    '/age-calculator.html',
    '/percentage-calculator.html',
    '/word-counter.html',
    '/emi-calculator.html',
    '/password-generator.html',
    '/unit-converter.html',
    '/contact.html',
    '/privacy.html',
    '/terms.html',
    '/seo-meta-tag-generator.html',
    '/link-shortener.html',
    '/gst-calculator.html'
];

self.addEventListener('install', (event) => {
    self.skipWaiting();
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                return cache.addAll(ASSETS_TO_CACHE);
            })
    );
});

self.addEventListener('fetch', (event) => {
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                return response || fetch(event.request);
            })
    );
});

self.addEventListener('activate', (event) => {
    const cacheWhitelist = [CACHE_NAME];
    event.waitUntil(
        Promise.all([
            caches.keys().then((cacheNames) => {
                return Promise.all(
                    cacheNames.map((cacheName) => {
                        if (cacheWhitelist.indexOf(cacheName) === -1) {
                            return caches.delete(cacheName);
                        }
                    })
                );
            }),
            self.clients.claim()
        ])
    );
});
