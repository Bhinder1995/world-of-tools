"""Inject missing SEO meta tags into all HTML pages"""
import os
import re

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
site_url = "https://worldoftools.in"
today = "2026-05-28"

def fix_page(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    filename = os.path.basename(filepath)
    slug = filename.replace('.html', '')
    is_home = filename == 'index.html'

    # 1. Add robots meta if missing
    if 'name="robots"' not in content and 'name=robots' not in content:
        robots_tag = '<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large"/>'
        content = content.replace('<meta charset="utf-8"/>', f'<meta charset="utf-8"/>\n{robots_tag}')

    # 2. Add og:image:width and og:image:height if missing
    if 'og:image:width' not in content:
        content = content.replace(
            '<meta property="og:image"',
            '<meta property="og:image:width" content="1200"/>\n    <meta property="og:image:height" content="630"/>\n    <meta property="og:image"'
        )

    # 3. Add article:published_time if missing (freshness signal)
    if 'article:published_time' not in content and not is_home:
        pub_tag = f'<meta property="article:published_time" content="{today}T00:00:00+05:30"/>'
        content = content.replace('</title>', f'</title>\n    {pub_tag}')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

count = 0
for root, dirs, files in os.walk(base_dir):
    if '.git' in root or '__pycache__' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            path = os.path.join(root, f)
            if fix_page(path):
                count += 1
                print(f"Fixed: {f}")

print(f"\nFixed {count} HTML pages with missing meta tags.")
