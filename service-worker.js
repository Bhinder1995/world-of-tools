const CACHE_NAME = 'world-of-tools-v115';

const ASSETS_TO_CACHE = [
    '/',
    '/index.html',
    '/css/style.css',
    '/js/common.js',
    '/logo.svg',
    '/manifest.json',
    '/guides/',
    '/guides/index.html',
    '/app-icon.png',
    '/favicon.png',
    '/favicon.ico',
    '/apple-touch-icon.png',
    '/hash-generator',
    '/jwt-decoder',
    '/sql-formatter',
    '/cron-expression-generator',
    '/url-encoder-decoder',
    '/age-calculator',
    '/percentage-calculator',
    '/word-counter',
    '/emi-calculator',
    '/password-generator',
    '/unit-converter',
    '/about-us',
    '/contact-us',
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
    '/color-converter',
    '/regex-tester',
    '/uuid-generator',
    '/case-converter',
    '/csv-to-json',
    '/xml-formatter',
    '/markdown-to-html',
    '/keyword-density-checker',
    '/scientific-calculator',
    '/time-zone-converter',
    '/lorem-ipsum-generator',
    '/barcode-generator',
    '/linkedin-creator-suite',
    '/number-to-words-converter',
    '/random-number-generator',
    '/roman-numerals-converter',
    '/text-to-binary-converter',
    '/calculators-online',
    '/developer-tools-online',
    '/seo-tools-free',
    '/text-tools-online',
    '/web-utilities-free',
    '/background-remover',
    '/image-upscaler',
    '/image-converter',
    '/bmi-calculator',
    '/sip-calculator',
    '/loan-eligibility-calculator',
    '/ppf-calculator',
    '/aspect-ratio-calculator',
    '/serp-preview',
    '/invoice-generator',
    '/typing-speed-test',
    '/css-gradient-generator',
    '/email-signature-generator',
    '/favicon-generator',
    '/ip-address-lookup',
    '/guides/age-calculator-guide',
    '/guides/background-remover-guide',
    '/guides/barcode-generator-guide',
    '/guides/base64-encoder-decoder-guide',
    '/guides/case-converter-guide',
    '/guides/color-converter-guide',
    '/guides/cron-expression-generator-guide',
    '/guides/css-minifier-guide',
    '/guides/csv-to-json-guide',
    '/guides/emi-calculator-guide',
    '/guides/gst-calculator-guide',
    '/guides/hash-generator-guide',
    '/guides/image-compressor-guide',
    '/guides/image-converter-guide',
    '/guides/image-upscaler-guide',
    '/guides/json-formatter-guide',
    '/guides/jwt-decoder-guide',
    '/guides/keyword-density-checker-guide',
    '/guides/link-shortener-guide',
    '/guides/linkedin-creator-suite-guide',
    '/guides/lorem-ipsum-generator-guide',
    '/guides/markdown-to-html-guide',
    '/guides/number-to-words-converter-guide',
    '/guides/password-generator-guide',
    '/guides/percentage-calculator-guide',
    '/guides/qr-code-generator-guide',
    '/guides/random-number-generator-guide',
    '/guides/regex-tester-guide',
    '/guides/roman-numerals-converter-guide',
    '/guides/scientific-calculator-guide',
    '/guides/seo-meta-tag-generator-guide',
    '/guides/sql-formatter-guide',
    '/guides/text-compare-tool-guide',
    '/guides/text-to-binary-converter-guide',
    '/guides/time-zone-converter-guide',
    '/guides/unit-converter-guide',
    '/guides/url-encoder-decoder-guide',
    '/guides/uuid-generator-guide',
    '/guides/xml-formatter-guide',
    '/guides/youtube-thumbnail-downloader-guide',
    '/guides/word-counter-guide',
    '/guides/bmi-calculator-guide',
    '/guides/sip-calculator-guide',
    '/guides/loan-eligibility-calculator-guide',
    '/guides/ppf-calculator-guide',
    '/guides/aspect-ratio-calculator-guide',
    '/guides/serp-preview-guide',
    '/guides/invoice-generator-guide',
    '/guides/typing-speed-test-guide',
    '/guides/css-gradient-generator-guide',
    '/guides/email-signature-generator-guide',
    '/guides/favicon-generator-guide',
    '/guides/ip-address-lookup-guide',
    '/guides/video-compressor-guide',
    '/guides/emi-sip-gst-financial-planning',
    '/guides/how-to-start-sip-investment',
    '/guides/compress-convert-background-images',
    '/guides/jwt-base64-hash-developer-guide',
    '/guides/compress-2gb-video',
    '/guides/veed-clideo-alternatives',
    '/video-compressor',
    '/compress-video-online-free',
    '/compress-video-for-whatsapp',
    '/compress-video-for-instagram',
    '/compress-video-for-discord',
    '/free-url-shortener-online',
    '/secure-password-generator-online',
    '/transcribe-audio-online',
    '/voice-to-text-converter',
    '/cgpa-to-percentage',
    '/gpa-to-cgpa-calculator',
    '/compare-loan-offers',
    '/bank-loan-comparison',
    '/watermark-remover-online',
    '/erase-logo-from-photo',
    '/guides/remove-watermark-from-image-guide',
    '/guides/age-calculator-hindi-guide',
    '/guides/cgpa-calculator-bengali-guide',
    '/guides/emi-calculator-marathi-guide',
    '/guides/gst-calculator-telugu-guide',
    '/guides/remove-watermark-tamil-guide'
];


self.addEventListener('install', (event) => {
    self.skipWaiting();
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                // Add assets individually so a single local 404 doesn't crash the entire worker
                return Promise.all(
                    ASSETS_TO_CACHE.map(url => 
                        cache.add(url).catch(err => console.warn('Failed to cache:', url, err))
                    )
                );
            })
    );
});

self.addEventListener('fetch', (event) => {
    // Only handle GET requests
    if (event.request.method !== 'GET') return;

    const url = new URL(event.request.url);
    
    // Ignore non-HTTP(s) requests (like chrome-extension://)
    if (!url.protocol.startsWith('http')) {
        return;
    }

    // Network-first strategy for HTML pages (navigations)
    // This ensures users always get the latest version of the site
    if (event.request.mode === 'navigate' || url.pathname.endsWith('.html') || url.pathname === '/') {
        event.respondWith(
            fetch(event.request)
                .then((response) => {
                    // Start caching a copy for offline use
                    const responseClone = response.clone();
                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(event.request, responseClone).catch(() => {});
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
                        cache.put(event.request, responseClone).catch(() => {});
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
