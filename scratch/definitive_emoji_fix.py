"""
definitive_emoji_fix.py
Uses ftfy to fix encoding mess, plus direct fallback replacements.
"""
import os
import re

try:
    import ftfy
    HAS_FTFY = True
    print("ftfy available - using it for encoding repair")
except ImportError:
    HAS_FTFY = False
    print("ftfy not available - using direct fallbacks")

ROOT = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"

# Final fallback direct replacements for patterns ftfy might miss
# These are the EXACT broken strings we confirmed are in the files
DIRECT_FIXES = {
    # Still-broken 4-byte emoji remnants (ðŸ patterns)
    "ðŸ\x94\x8d": "🔍",   # 🔍
    "ðŸ\x94\xa0": "🔠",   # 🔠
    "ðŸ\x93\x8d": "📍",   # 📍
    "ðŸ\x95\x92": "🕒",   # 🕒
    "ðŸ\x9a\x80": "🚀",   # 🚀
    "ðŸ\x8e\x82": "🎂",   # 🎂
    "ðŸ\x93\xb9": "📹",   # 📹
    "ðŸ\x91\x94": "👔",   # 👔
    "ðŸ\x94\xa5": "🔥",   # 🔥
    "ðŸ\x93\xa6": "📦",   # 📦
    "ðŸ\x9b\xa1": "🛡️",  # 🛡️
    "ðŸ\x9b\xa0": "🛠️",  # 🛠️
    "ðŸ\x8e\x9e": "🎞️",  # 🎞️
    "ðŸ\x96\xa8": "🏷️",  # 🏷️
    "ðŸ\xa7\xae": "🧪",   # 🧪
    "ðŸ\x93\x88": "📈",   # 📈
    "ðŸ\xa7\xae": "🧮",   # 🧮
    "ðŸ\x94\x96": "🔖",   # 🔖
    "ðŸ\x94\x9b": "🔛",   # 🔛
    
    # Also handle the ðŸ without following control chars (partially broken)
    # These appear as just "ðŸ" without recoverable following bytes
}

# Text patterns that are consistently broken and can be matched as plain text
TEXT_FIXES = {
    "ðŸ": "",  # Remove unresolvable ðŸ remnants as LAST resort
}

def fix_html_file(path):
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        
        original = content
        
        # Step 1: Try ftfy if available
        if HAS_FTFY:
            content = ftfy.fix_text(content, fix_encoding=True, normalization='NFC')
        
        # Step 2: Direct byte-level fixes
        for bad, good in DIRECT_FIXES.items():
            if bad in content:
                content = content.replace(bad, good)
        
        # Step 3: Remove any remaining unrecoverable ðŸ sequences
        # (these are the ones where the neighboring bytes were lost)
        # Replace ðŸ + up to 3 non-alphanumeric chars with empty
        content = re.sub(r'ðŸ[^\w<>\s"]{0,4}', '', content)
        
        # Step 4: Fix the version string doubling in links
        content = re.sub(r'(\.css|\.js)(\?v=[\d.]+)+', r'\1?v=5.0', content)
        
        # Step 5: Collapse multiple blank lines
        content = re.sub(r'\n(\s*\n){2,}', '\n\n', content)
        
        if content != original:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"  ERROR {os.path.basename(path)}: {e}")
        return False

count = 0
fixed = 0
for root, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in ('node_modules', '.git', 'scratch', '__pycache__')]
    for fn in files:
        if fn.endswith('.html'):
            count += 1
            if fix_html_file(os.path.join(root, fn)):
                fixed += 1
                print(f"  Fixed: {fn}")

print(f"\nProcessed {count} files, fixed {fixed}.")
