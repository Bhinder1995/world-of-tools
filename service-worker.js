const CACHE_NAME = 'world-of-tools-v22';
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
    '/base64-encoder-decoder',
    '/qr-code-generator',
    '/youtube-thumbnail-downloader',
    '/logo.svg',
    '/app-icon.png'
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

    const url = new URL(event.request.url);

    // Network-first strategy for HTML pages (navigations)
    // This ensures users always get the latest version of the site
    if (event.request.mode === 'navigate' || url.pathname.endsWith('.html') || url.pathname === '/') {
        event.respondWith(
            fetch(event.request)
                .then((response) => {
                    // Start caching a copy for offline use
                    const responseClone = response.clone();
                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(event.request, responseClone);
                    });
                    return response;
                })
                .catch(() => {
                    // If network fails, try cache
                    return caches.match(event.request);
                })
        );
        return;
    }

    // Cache-first strategy for static assets (CSS, JS, Images, Fonts)
    event.respondWith(
        caches.match(event.request)
            .then((response) => {
                if (response) {
                    return response;
                }

                // If not in cache, fetch from network
                return fetch(event.request).then((response) => {
                    // Cache the new resource
                    if (!response || response.status !== 200 || response.type !== 'basic') {
                        return response;
                    }

                    const responseClone = response.clone();
                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(event.request, responseClone);
                    });

                    return response;
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
