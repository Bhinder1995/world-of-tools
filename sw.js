const CACHE_NAME = 'world-of-tools-v15';
const ASSETS_TO_CACHE = [
    '/',
    '/css/style.css?v=1.2',
    '/js/common.js?v=1.2',
    '/manifest.json',
    '/favicon.png',
    '/favicon.ico',
    '/age-calculator',
    '/percentage-calculator',
    '/word-counter',
    '/emi-calculator',
    '/password-generator',
    '/unit-converter',
    '/contact',
    '/privacy',
    '/terms',
    '/seo-meta-tag-generator',
    '/link-shortener',
    '/gst-calculator',
    '/json-formatter',
    '/text-compare-tool',
    '/css-minifier',
    '/image-compressor',
    '/base64-encoder-decoder'
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
    // Only handle GET requests
    if (event.request.method !== 'GET') return;

    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                // If we have a cached response, check if it's redirected
                // Service Workers cannot serve a Response with the .redirected property set to true for navigations
                if (response) {
                    if (response.redirected) {
                        // If it was redirected, don't use it, fetch fresh
                        return fetch(event.request);
                    }
                    return response;
                }

                // Fallback to network
                return fetch(event.request).then(fetchRes => {
                    // Optional: If we want to cache extension-less versions on the fly
                    return fetchRes;
                });
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
