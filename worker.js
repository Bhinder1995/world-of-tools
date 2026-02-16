export default {
    async fetch(request, env) {
        const corsHeaders = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type"
        };

        if (request.method === "OPTIONS") {
            return new Response(null, { headers: corsHeaders });
        }

        const url = new URL(request.url);

        // Health check
        if (url.pathname === "/") {
            return new Response("URL Shortener API (TinyURL Masking Mode) Running", { headers: corsHeaders });
        }

        // CREATE SHORT LINK
        if (request.method === "POST" && url.pathname === "/create") {
            const { longUrl } = await request.json();

            if (!longUrl || !longUrl.startsWith("http")) {
                return new Response("Invalid URL", { status: 400, headers: corsHeaders });
            }

            // 1. Get TinyURL code (optional, we can just use our own random code for masking)
            // For maximum reliability, we'll use our own random code and store the redirect.
            const key = Math.random().toString(36).substring(2, 8);

            try {
                // Store in Cloudflare KV
                await env.LINKS_DB.put(key, longUrl);

                return new Response(JSON.stringify({
                    shortUrl: `https://go.worldoftools.in/${key}`
                }), {
                    headers: { "Content-Type": "application/json", ...corsHeaders }
                });
            } catch (e) {
                return new Response(JSON.stringify({ error: "KV Storage failed. Ensure LINKS_DB is bound." }), {
                    status: 500,
                    headers: corsHeaders
                });
            }
        }

        // REDIRECT
        const key = url.pathname.substring(1);
        const longUrl = await env.LINKS_DB.get(key);

        if (longUrl) {
            return Response.redirect(longUrl, 301);
        }

        // FALLBACK: If not found, it might be a direct TinyURL redirect if we implemented that flow
        return new Response("Link not found on WorldOfTools Hub", { status: 404 });
    }
};
