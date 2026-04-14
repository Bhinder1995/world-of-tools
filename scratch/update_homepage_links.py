#!/usr/bin/env python3
"""
update_homepage_links.py
- Replaces all .html href references in index.html with clean URLs
- Updates JS/CSS version references to v6.0
- Ensures all internal links use /tool-slug (no .html)
"""
import re, os

ROOT = r"C:\Users\HP\Desktop\Projects Folder\world_of_tools"
INDEX_PATH = os.path.join(ROOT, "index.html")

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    html = f.read()

original = html

# 1. Fix href="tool-name.html" -> href="/tool-name" (for all tool cards on homepage)
# Pattern: href="some-tool-name.html" where it's a relative href (no /)
html = re.sub(r'href="([a-z][a-z0-9-]+)\.html"', r'href="/\1"', html)

# 2. Fix guide links: href="/guides/some-guide.html" - keep .html for guides since they're files
# (guides still need .html extension, so revert those)
# Actually clean URLs work for guides too due to cleanUrls:true in vercel, so leave them

# 3. Update JS version
html = html.replace('common.js?v=5.3', 'common.js?v=6.0')
html = html.replace('common.js?v=4.0', 'common.js?v=6.0')
html = html.replace('style.css?v=5.3', 'style.css?v=6.0')
html = html.replace('style.css?v=4.0', 'style.css?v=6.0')
html = html.replace('neo-brutalism.css?v=5.3', 'neo-brutalism.css?v=6.0')

# 4. Add Vercel speed insights script if missing
if '_vercel/speed-insights' not in html and '_vercel/insights' in html:
    html = html.replace(
        '<script defer src="/_vercel/insights/script.js"></script>',
        '<script defer src="/_vercel/insights/script.js"></script>\n<script defer src="/_vercel/speed-insights/script.js"></script>'
    )

# 5. Fix quick-chip hrefs to use clean URLs
html = re.sub(r'href="(/)?([a-z][a-z0-9-]+)\.html"', lambda m: f'href="/{m.group(2)}"', html)

changes = sum(1 for a, b in zip(original, html) if a != b)
print(f"Changes detected: {changes} characters changed")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("index.html updated successfully")

# Also update all guide files to use common.js v6.0
GUIDES_DIR = os.path.join(ROOT, "guides")
guide_updates = 0
for fname in os.listdir(GUIDES_DIR):
    if not fname.endswith(".html"):
        continue
    fpath = os.path.join(GUIDES_DIR, fname)
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    new_content = content
    new_content = new_content.replace('common.js?v=5.3', 'common.js?v=6.0')
    new_content = new_content.replace('common.js?v=4.0', 'common.js?v=6.0')
    new_content = new_content.replace('common.js?v=3', 'common.js?v=6.0')
    new_content = new_content.replace('style.css?v=5.3', 'style.css?v=6.0')
    new_content = new_content.replace('style.css?v=4.0', 'style.css?v=6.0')
    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        guide_updates += 1

print(f"Updated {guide_updates} guide files to v6.0")

# Update other key pages
OTHER_PAGES = ["about-us.html", "contact-us.html", "privacy.html", "terms.html",
               "calculators-online.html", "developer-tools-online.html",
               "seo-tools-free.html", "text-tools-online.html", "web-utilities-free.html"]

page_updates = 0
for fname in OTHER_PAGES:
    fpath = os.path.join(ROOT, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    new_content = content
    new_content = new_content.replace('common.js?v=5.3', 'common.js?v=6.0')
    new_content = new_content.replace('common.js?v=4.0', 'common.js?v=6.0')
    new_content = new_content.replace('style.css?v=5.3', 'style.css?v=6.0')
    new_content = new_content.replace('style.css?v=4.0', 'style.css?v=6.0')
    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        page_updates += 1

print(f"Updated {page_updates} other pages to v6.0")
print("All done!")
