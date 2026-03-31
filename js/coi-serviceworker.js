/* 
  COI Service Worker (coi-serviceworker.js)
  This script enables SharedArrayBuffer in the browser for FFmpeg.wasm 
  by setting COOP and COEP headers on the fly.
  MIT Licensed by Kagami Sasakure
*/
if (typeof window === "undefined") {
    self.addEventListener("install", () => self.skipWaiting());
    self.addEventListener("activate", (event) => event.waitUntil(self.clients.claim()));

    self.addEventListener("fetch", (event) => {
        if (event.request.cache === "only-if-cached" && event.request.mode !== "same-origin") {
            return;
        }

        event.respondWith(
            fetch(event.request)
                .then((response) => {
                    if (response.status === 0) {
                        return response;
                    }

                    const newHeaders = new Headers(response.headers);
                    newHeaders.set("Cross-Origin-Embedder-Policy", "require-corp");
                    newHeaders.set("Cross-Origin-Opener-Policy", "same-origin");

                    return new Response(response.body, {
                        status: response.status,
                        statusText: response.statusText,
                        headers: newHeaders,
                    });
                })
                .catch((e) => console.error(e))
        );
    });
} else {
    (() => {
        const sc = document.createElement("script");
        sc.src = "js/coi-serviceworker.js";
        // To avoid infinite loop, we only register if not already managed
        if ("serviceWorker" in navigator && !navigator.serviceWorker.controller) {
            navigator.serviceWorker.register(window.document.currentScript.src);
        }
    })();
}
