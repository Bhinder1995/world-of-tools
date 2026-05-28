"""Add non-render-blocking font loading to all HTML pages"""
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(base_dir)

count = 0

# Generate font URLs to match
amp = chr(38)
font_variants = [
    '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700;800' + amp + 'family=Syne:wght@700;800;900' + amp + 'display=swap" rel="stylesheet"/>',
    '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700;800' + amp + 'family=Syne:wght@700;800;900' + amp + 'display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700;800' + amp + 'family=Syne:wght@700;800;900' + amp + 'display=swap" rel="stylesheet" />',
]
fixed = '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700;800' + amp + 'family=Syne:wght@700;800;900' + amp + 'display=swap" rel="stylesheet" media="print" onload="this.media=\'all\'"/>'

excludes = ['.git', '__pycache__', 'node_modules']

for root, dirs, files in os.walk('.'):
    if any(e in root for e in excludes):
        continue
    for f in files:
        if not f.endswith('.html'):
            continue
        path = os.path.join(root, f)
        with open(path, 'r', encoding='utf-8') as fh:
            content = fh.read()

        if 'Space+Grotesk' not in content:
            continue
        if 'media="print"' in content:
            continue  # already fixed

        changed = False
        for variant in font_variants:
            if variant in content:
                content = content.replace(variant, fixed)
                changed = True
                break

        if changed:
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(content)
            count += 1
            print(f'Fixed: {f}')

print(f'\nFixed font loading in {count} files.')
