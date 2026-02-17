// Legacy Service Worker - Unregister self to allow new worker to take over
self.addEventListener('install', () => {
    self.skipWaiting();
});

self.addEventListener('activate', () => {
    self.registration.unregister()
        .then(() => {
            return self.clients.matchAll();
        })
        .then((clients) => {
            clients.forEach(client => client.navigate(client.url));
        });
});
