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
            return new Response("URL Shortener API Running", { headers: corsHeaders });
        }

        // CREATE SHORT LINK
        if (request.method === "POST" && url.pathname === "/go") {
            const { url: longUrl } = await request.json();

            if (!longUrl || !longUrl.startsWith("http")) {
                return new Response(JSON.stringify({ error: "Invalid URL" }), {
                    status: 400,
                    headers: { "Content-Type": "application/json", ...corsHeaders }
                });
            }

            const key = Math.random().toString(36).substring(2, 8);

            try {
                // Store in Cloudflare KV
                await env.LINKS_DB.put(key, longUrl);

                return new Response(JSON.stringify({
                    shortUrl: `${url.origin}/go/${key}`
                }), {
                    headers: { "Content-Type": "application/json", ...corsHeaders }
                });
            } catch (e) {
                return new Response(JSON.stringify({ error: "Database error" }), {
                    status: 500,
                    headers: { "Content-Type": "application/json", ...corsHeaders }
                });
            }
        }

        // REDIRECT
        // Handle /go/key or /key
        let key = url.pathname.substring(1);
        if (key.startsWith("go/")) {
            key = key.substring(3);
        }

        if (key) {
            const longUrl = await env.LINKS_DB.get(key);
            if (longUrl) {
                return Response.redirect(longUrl, 301);
            }
        }

        return new Response("Link not found", { status: 404, headers: corsHeaders });
    }
};
