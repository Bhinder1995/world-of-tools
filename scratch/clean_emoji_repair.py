"""
clean_emoji_repair.py
Reads each file as latin-1 (so the bytes map 1:1 to chars),
then decodes the "double-encoded" sequences back to their original emoji,
then saves as proper UTF-8.
"""
import os, re

ROOT = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"

# The key insight: these files were UTF-8 bytes, but then MISTAKENLY decoded
# as latin-1 a second time.  So to recover:
# - read the file as a STRING (utf-8 with errors=surrogateescape or latin-1)
# - encode back to bytes as latin-1
# - decode those bytes as utf-8

def fix_file(path):
    try:
        with open(path, 'r', encoding='utf-8', errors='surrogateescape') as f:
            raw = f.read()
        
        # Check if there's mojibake we need to fix
        if 'Ã' not in raw and 'Å¸' not in raw:
            return  # Already clean
        
        # Encode as latin-1 to get the original bytes, then decode as utf-8
        try:
            fixed_bytes = raw.encode('latin-1', errors='ignore')
            fixed = fixed_bytes.decode('utf-8', errors='ignore')
        except Exception:
            return

        # Also collapse multiple blank lines
        fixed = re.sub(r'(\r?\n\s*){3,}', '\n\n', fixed)
        
        # Fix the CSS link versioning (no more triple ?v=)
        fixed = re.sub(r'(style\.css)(\?v=[0-9.]+)+', r'\1?v=5.0', fixed)
        fixed = re.sub(r'(common\.js)(\?v=[0-9.]+)+', r'\1?v=5.0', fixed)
        
        # Ensure common.js link exists in head
        js_tag = '<script src="/js/common.js?v=5.0" defer></script>'
        if '/js/common.js' not in fixed:
            fixed = fixed.replace('</head>', f'  {js_tag}\n</head>')
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(fixed)
        print(f'Fixed: {os.path.basename(path)}')
    except Exception as e:
        print(f'SKIP {os.path.basename(path)}: {e}')

fixed_count = 0
for root, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in ('node_modules', '.git', 'scratch', '__pycache__')]
    for fn in files:
        if fn.endswith('.html'):
            fix_file(os.path.join(root, fn))
            fixed_count += 1

print(f'\nDone. Processed {fixed_count} HTML files.')
