"""
restore_hero_emojis.py
Directly restores the known emojis for specific tool chips and badges in index.html
by targeting the surrounding text context.
"""
import re

PATH = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools\index.html"

with open(PATH, 'r', encoding='utf-8') as f:
    html = f.read()

# ── Hero badge (45+ Professional Tools) ─────────────────────
html = html.replace(
    '<span style="font-size: 1.1rem;">\n\n</span>\n\n45+ Professional Tools',
    '<span style="font-size: 1.1rem;">✨</span>\n\n45+ Professional Tools'
)

# ── Tool chips (Top Rated row) ───────────────────────────────
# Case Converter
html = re.sub(
    r'(<span class="ico">\n\n</span>\n\nCase Converter)',
    '<span class="ico">🔠</span>\n\nCase Converter',
    html
)
# IP Lookup
html = re.sub(
    r'(<span class="ico">\n\n</span>\n\nIP Lookup)',
    '<span class="ico">📍</span>\n\nIP Lookup',
    html
)
# Age Calculator
html = re.sub(
    r'(<span class="ico">\n\n</span>\n\nAge Calculator)',
    '<span class="ico">🎂</span>\n\nAge Calculator',
    html
)
# Video Compressor
html = re.sub(
    r'(<span class="ico">\n\n</span>\n\nVideo Compressor)',
    '<span class="ico">📹</span>\n\nVideo Compressor',
    html
)
# LinkedIn Suite
html = re.sub(
    r'(<span class="ico">\n\n</span>\n\nLinkedIn Suite)',
    '<span class="ico">👔</span>\n\nLinkedIn Suite',
    html
)

# ── Recent Tools row ─────────────────────────────────────────
# Fix the "Top Rated:" and "Recent Tools:" labels
html = html.replace(
    '\n\nTop Rated:\n\n</span>',
    '\n\n🚀 Top Rated:\n\n</span>'
)
html = html.replace(
    '\n\nRecent Tools:\n\n</span>',
    '\n\n🕒 Recent Tools:\n\n</span>'
)

# ── "Most Popular" badge ─────────────────────────────────────
html = re.sub(
    r'(<div style="display:inline-flex;[^"]*">\n\n)(Most Popular)',
    r'\1🔥 Most Popular',
    html
)

# Fallback for the Most Popular badge with slightly different formatting
html = html.replace(
    'Most Popular\n\n</div>',
    '🔥 Most Popular\n\n</div>'
)

# ── Category chips ────────────────────────────────────────────
html = re.sub(r'(<a class="btn btn-secondary"[^>]*>\n\n)(Calculators)', r'\1🧮 Calculators', html)
html = re.sub(r'(<a class="btn btn-secondary"[^>]*>\n\n)(Developer Tools)', r'\1🛠️ Developer Tools', html)
html = re.sub(r'(<a class="btn btn-secondary"[^>]*>\n\n)(SEO Tools)', r'\1📈 SEO Tools', html)
html = re.sub(r'(<a class="btn btn-secondary"[^>]*>\n\n)(Text Tools)', r'\1✍️ Text Tools', html)
html = re.sub(r'(<a class="btn btn-secondary"[^>]*>\n\n)(Web Utilities)', r'\1🌐 Web Utilities', html)

# ── Trust badges (add checkmarks back) ───────────────────────
# They lost their ✓ checkmarks
html = re.sub(
    r'(border-radius: 4px; padding: 0\.4rem 1rem; font-size: 0\.82rem; font-weight: 700;">\n\n)(\w)',
    r'\1✓ \2',
    html
)

with open(PATH, 'w', encoding='utf-8') as f:
    f.write(html)

print("Hero emojis restored in index.html.")
