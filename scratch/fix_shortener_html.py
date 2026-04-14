import re

def fix_shortener():
    filepath = 'free-url-shortener-online.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove the text below the button
    content = re.sub(
        r'<p[^>]*>⚡ Links are created using TinyURL\'s free API[^<]*</p>',
        '<p style="text-align:center;font-size:0.82rem;color:#888;font-weight:600;">⚡ Fast and secure. No data stored on WorldOfTools servers.</p>',
        content
    )

    # 2. Fix the FAQ references
    content = content.replace("This tool uses TinyURL's free API", "This tool uses our robust shortening infrastructure")
    content = content.replace("Links shortened via TinyURL do not expire.", "Your short links are permanent redirects.")
    content = content.replace("TinyURL short links are permanent and do not expire.", "Our short links are permanent and do not expire.")

    # 3. Update the JavaScript function
    js_replacement = """
    try {
      let shortUrl = null;
      try {
        const workerResp = await fetch('https://steep-glade-3331.bhindersingh199529.workers.dev/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ url: url })
        });
        if (workerResp.ok) {
            const data = await workerResp.json();
            if (data && data.shortUrl) {
                shortUrl = data.shortUrl;
            }
        }
      } catch (workerErr) {
        console.warn('Worker fallback:', workerErr);
      }

      if (!shortUrl) {
          const response = await fetch(`https://tinyurl.com/api-create.php?url=${encodeURIComponent(url)}`);
          if (!response.ok) throw new Error('Service unavailable');
          shortUrl = await response.text();
          if (!shortUrl.startsWith('http')) throw new Error('Invalid response');
      }

      currentShortUrl = shortUrl;
      displayResult(url, shortUrl);
    } catch (err) {"""

    # Find the try block inside shortenUrl()
    content = re.sub(
        r'try\s*\{\s*const\s*response\s*=\s*await\s*fetch\(`https://tinyurl\.com.*?\s*displayResult\(url,\s*shortUrl\);\s*\}\s*catch\s*\(err\)\s*\{',
        js_replacement,
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    fix_shortener()
