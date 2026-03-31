/*
  COI Service Worker (coi-serviceworker.js)
  Enables SharedArrayBuffer for FFmpeg.wasm by injecting COOP/COEP headers.
  Uses 'credentialless' COEP so CDN resources (jsdelivr) load without issues.
*/
if (typeof window === "undefined") {
    // ── Service Worker context ──────────────────────────────────────────────
    self.addEventListener("install", () => self.skipWaiting());
    self.addEventListener("activate", (event) => event.waitUntil(self.clients.claim()));

    self.addEventListener("fetch", (event) => {
        if (event.request.cache === "only-if-cached" && event.request.mode !== "same-origin") {
            return;
        }
        event.respondWith(
            fetch(event.request)
                .then((response) => {
                    if (response.status === 0) return response;
                    const newHeaders = new Headers(response.headers);
                    // 'credentialless' allows cross-origin resources (CDNs) without CORP
                    newHeaders.set("Cross-Origin-Embedder-Policy", "credentialless");
                    newHeaders.set("Cross-Origin-Opener-Policy", "same-origin");
                    return new Response(response.body, {
                        status: response.status,
                        statusText: response.statusText,
                        headers: newHeaders,
                    });
                })
                .catch((e) => console.error("[COI-SW] fetch error:", e))
        );
    });

} else {
    // ── Main (window) context ───────────────────────────────────────────────
    if ("serviceWorker" in navigator) {
        // If we're already cross-origin isolated, nothing to do
        if (window.crossOriginIsolated) {
            console.log("[COI-SW] Already cross-origin isolated ✓");
        } else {
            // Check if we've already tried reloading to avoid infinite loops
            const reloaded = sessionStorage.getItem("coi_reloaded");
            sessionStorage.removeItem("coi_reloaded");

            navigator.serviceWorker
                .register(document.currentScript.src)
                .then((reg) => {
                    // SW is being installed or is waiting – reload once to activate it
                    if ((reg.installing || reg.waiting) && !reloaded) {
                        sessionStorage.setItem("coi_reloaded", "1");
                        window.location.reload();
                    }
                    // Also reload if a new worker just took control
                    navigator.serviceWorker.addEventListener("controllerchange", () => {
                        if (!reloaded) {
                            sessionStorage.setItem("coi_reloaded", "1");
                            window.location.reload();
                        }
                    });
                })
                .catch((err) => console.warn("[COI-SW] Registration failed:", err));
        }
    }
}

