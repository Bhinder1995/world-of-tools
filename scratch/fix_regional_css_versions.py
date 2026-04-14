"""
Fix regional (hi/ and es/) HTML files:
1. Update common.js version from v=5.0 to v=6.1 (critical — old version has no guide injection)
2. Add neo-brutalism.css if missing
3. Update style.css version to v=6.1 if lower
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = [
    os.path.join(ROOT, 'hi'),
    os.path.join(ROOT, 'es'),
]

updated = 0
skipped = 0

for d in DIRS:
    if not os.path.isdir(d):
        print(f"Skipping missing dir: {d}")
        continue
    for fname in os.listdir(d):
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(d, fname)
        with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        original = content

        # 1. Update common.js version reference (any old version -> v=6.1)
        content = re.sub(
            r'(/js/common\.js\?v=)[0-9.]+',
            r'\g<1>6.1',
            content
        )
        # Also catch defer version (some have defer)
        content = re.sub(
            r'(src="/js/common\.js)[^"]*(")',
            r'\g<1>?v=6.1\2',
            content
        )

        # 2. Update style.css version
        content = re.sub(
            r'(/css/style\.css\?v=)[0-9.]+',
            r'\g<1>6.1',
            content
        )

        # 3. Add neo-brutalism.css if not already there
        if 'neo-brutalism.css' not in content:
            content = content.replace(
                '<link href="/css/style.css?v=6.1" rel="stylesheet"/>',
                '<link href="/css/style.css?v=6.1" rel="stylesheet"/>\n<link href="/css/neo-brutalism.css?v=6.1" rel="stylesheet"/>'
            )
            # also handle alternate format
            content = content.replace(
                '<link rel="stylesheet" href="/css/style.css?v=6.1"/>',
                '<link rel="stylesheet" href="/css/style.css?v=6.1"/>\n<link href="/css/neo-brutalism.css?v=6.1" rel="stylesheet"/>'
            )

        if content != original:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            updated += 1
            print(f"  Updated: {os.path.relpath(fpath, ROOT)}")
        else:
            skipped += 1

print(f"\nDone! Updated {updated} files, {skipped} already current.")
