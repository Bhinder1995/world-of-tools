export default {
    async fetch(request, env) {
        const url = new URL(request.url);

        // Health check
        if (url.pathname === "/") {
            return new Response("URL Shortener API Running");
        }

        // CREATE SHORT LINK
        if (request.method === "POST" && url.pathname === "/create") {
            const { longUrl } = await request.json();

            if (!longUrl || !longUrl.startsWith("http")) {
                return new Response("Invalid URL", { status: 400 });
            }

            const key = Math.random().toString(36).substring(2, 8);

            await env.LINKS_DB.put(key, longUrl);

            return new Response(JSON.stringify({
                shortUrl: `https://go.worldoftools.in/${key}`
            }), {
                headers: { "Content-Type": "application/json" }
            });
        }

        // REDIRECT
        const key = url.pathname.substring(1);
        const longUrl = await env.LINKS_DB.get(key);

        if (longUrl) {
            return Response.redirect(longUrl, 301);
        }

        return new Response("Link not found", { status: 404 });
    }
};
