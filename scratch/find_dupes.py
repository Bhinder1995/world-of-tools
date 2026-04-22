import os
import glob

files = glob.glob('*.html')
dupes = []
for f in files:
    if f in ['calculators-online.html', 'developer-tools-online.html', 'text-tools-online.html', 'seo-tools-free.html', 'india-tools.html', 'image-tools.html', 'design-tools.html', 'security-tools.html']:
        continue # Hubs might have different patterns
    with open(f, 'r', encoding='utf-8') as content:
        c = content.read()
        if c.count('rel="canonical"') > 1 or c.count('"@type": "SoftwareApplication"') > 1:
            dupes.append(f)

print(f"Found {len(dupes)} files with duplicate SEO tags.")
for d in dupes[:10]:
    print(d)
