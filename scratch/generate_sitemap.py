import os
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = "https://www.worldoftools.in"

# Ignore these
IGNORE = ['404.html', '500.html']
IGNORE_DIRS = ['css', 'js', 'files', 'scratch', 'scripts', '.git', 'hi', 'es']

urls = []

def add_url(path, priority):
    # Convert path to clean URL
    path = path.replace('\\', '/')
    if path.endswith('/index.html'):
        path = path[:-10]
    elif path.endswith('.html'):
        path = path[:-5]
    if path == "":
        url = BASE_URL + "/"
    else:
        url = f"{BASE_URL}/{path}"
    
    urls.append(f"""  <url>
    <loc>{url}</loc>
    <lastmod>{datetime.today().strftime('%Y-%m-%d')}</lastmod>
    <changefreq>daily</changefreq>
    <priority>{priority}</priority>
  </url>""")

# 1. Add index
add_url("", "1.0")

# 2. Add main categories
categories = [
    'calculators-online.html',
    'image-tools-online.html',
    'developer-tools-online.html',
    'text-content-tools-online.html',
    'web-utilities-free.html',
    'seo-tools-free.html',
]
for cat in categories:
    add_url(cat, "0.9")

# 3. Add tools and guides
for root, dirs, files in os.walk(ROOT):
    # Filter ignored dirs
    dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
    
    for file in files:
        if file.endswith('.html') and file not in IGNORE and file not in categories and file != 'index.html':
            rel_path = os.path.relpath(os.path.join(root, file), ROOT)
            
            if 'guides' in root:
                add_url(rel_path, "0.8")
            else:
                add_url(rel_path, "0.9")

sitemap = f"""<?xml version="1.0" ?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>"""

with open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write(sitemap)

print(f"Generated sitemap with {len(urls)} URLs")
