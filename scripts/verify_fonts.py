"""Verify font loading fix"""
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(base_dir)

fixed_count = 0
unfixed_count = 0

amp = chr(38)
exact_fixed = '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700;800' + amp + 'family=Syne:wght@700;800;900' + amp + 'display=swap" rel="stylesheet" media="print" onload="this.media=\'all\'"/>'

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
        if exact_fixed in content:
            fixed_count += 1
        else:
            unfixed_count += 1
            print(f'NOT FIXED: {f}')
            idx = content.find('Space+Grotesk')
            if idx >= 0:
                start = content.rfind('<link', 0, idx)
                end = content.find('>', idx) + 1
                print(f'  Current: {repr(content[start:end])}')

print(f'\nFixed: {fixed_count}, Unfixed: {unfixed_count}')
