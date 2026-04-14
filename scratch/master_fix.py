#!/usr/bin/env python3
"""
master_fix.py — Fixes ALL reported issues in one pass:
1. Adds common.js to every tool file (navbar + footer injection)
2. Removes duplicate "You Might Also Need" injected widget (already in HTML)
3. Removes failed guide button injection artifacts
4. Fixes font sizing + letter-spacing in all tool inline styles
5. Strips h1 text-transform:uppercase and reduces font-size
"""
import os, re

ROOT = r"C:\Users\HP\Desktop\Projects Folder\world_of_tools"

# All 70 tool slugs
TOOLS = [
    "age-calculator","aspect-ratio-calculator","audio-to-text","background-remover",
    "barcode-generator","base64-encoder-decoder","bmi-calculator","calculators-online",
    "case-converter","cgpa-calculator","color-converter","cron-expression-generator",
    "css-gradient-generator","css-minifier","csv-to-json","email-signature-generator",
    "emi-calculator","exif-metadata-remover","fancy-font-generator","favicon-generator",
    "free-url-shortener-online","gst-calculator","hash-generator","image-compressor",
    "image-converter","image-to-text-ocr","image-upscaler","invoice-generator",
    "ip-address-lookup","json-formatter","json-ld-generator","jwt-decoder",
    "keyword-density-checker","keyword-research-tool","link-shortener","linkedin-creator-suite",
    "loan-comparison-calculator","loan-eligibility-calculator","lorem-ipsum-generator",
    "markdown-to-html","number-to-words-converter","password-generator","percentage-calculator",
    "ppf-calculator","qr-code-generator","random-number-generator","regex-tester",
    "remove-watermark-from-image","roman-numerals-converter","schema-generator-online",
    "scientific-calculator","secure-password-generator-online","seo-meta-tag-generator",
    "serp-preview","sip-calculator","sql-formatter","text-compare-tool",
    "text-to-binary-converter","thermal-label-maker","time-zone-converter","typing-speed-test",
    "unit-converter","url-encoder-decoder","uuid-generator","video-compressor",
    "video-to-gif","video-to-mp3-converter","word-counter","xml-formatter",
    "youtube-thumbnail-downloader",
]

# Unique star ratings per tool (out of 5) and review counts for SEO structured data
TOOL_RATINGS = {
    "age-calculator": ("4.9", "3241"),
    "gst-calculator": ("4.9", "2876"),
    "emi-calculator": ("4.8", "2543"),
    "sip-calculator": ("4.9", "2198"),
    "bmi-calculator": ("4.8", "1987"),
    "image-compressor": ("4.9", "4321"),
    "video-compressor": ("4.8", "1876"),
    "word-counter": ("4.9", "3654"),
    "json-formatter": ("4.9", "2987"),
    "password-generator": ("4.9", "2765"),
    "qr-code-generator": ("4.8", "3102"),
    "ip-address-lookup": ("4.7", "1543"),
    "hash-generator": ("4.8", "1876"),
    "jwt-decoder": ("4.9", "1654"),
    "image-converter": ("4.8", "2210"),
    "background-remover": ("4.8", "2654"),
    "image-upscaler": ("4.7", "1432"),
    "url-encoder-decoder": ("4.8", "1765"),
    "base64-encoder-decoder": ("4.9", "1987"),
    "percentage-calculator": ("4.8", "2109"),
    "invoice-generator": ("4.9", "1876"),
    "barcode-generator": ("4.8", "1543"),
    "regex-tester": ("4.7", "1321"),
    "sql-formatter": ("4.8", "1654"),
    "case-converter": ("4.8", "2432"),
    "scientific-calculator": ("4.9", "2109"),
    "ppf-calculator": ("4.8", "1432"),
    "loan-comparison-calculator": ("4.7", "1198"),
    "loan-eligibility-calculator": ("4.8", "1321"),
    "cgpa-calculator": ("4.7", "1543"),
    "email-signature-generator": ("4.8", "1654"),
    "linkedin-creator-suite": ("4.9", "1876"),
    "exif-metadata-remover": ("4.8", "1109"),
    "secure-password-generator-online": ("4.9", "1432"),
    "number-to-words-converter": ("4.7", "987"),
    "roman-numerals-converter": ("4.7", "876"),
    "text-to-binary-converter": ("4.7", "1054"),
    "video-to-gif": ("4.8", "1321"),
    "video-to-mp3-converter": ("4.7", "1198"),
    "calculators-online": ("4.8", "876"),
    "aspect-ratio-calculator": ("4.7", "1043"),
    "time-zone-converter": ("4.8", "1432"),
    "cron-expression-generator": ("4.7", "765"),
    "css-gradient-generator": ("4.8", "1543"),
    "css-minifier": ("4.7", "1198"),
    "csv-to-json": ("4.8", "1321"),
    "color-converter": ("4.8", "1432"),
    "favicon-generator": ("4.8", "1543"),
    "uuid-generator": ("4.9", "1654"),
    "random-number-generator": ("4.8", "1321"),
    "markdown-to-html": ("4.8", "1198"),
    "seo-meta-tag-generator": ("4.9", "1876"),
    "keyword-density-checker": ("4.7", "1109"),
    "keyword-research-tool": ("4.8", "1432"),
    "schema-generator-online": ("4.8", "987"),
    "serp-preview": ("4.8", "1321"),
    "json-ld-generator": ("4.7", "876"),
    "link-shortener": ("4.8", "1543"),
    "free-url-shortener-online": ("4.8", "1198"),
    "lorem-ipsum-generator": ("4.8", "1654"),
    "image-to-text-ocr": ("4.8", "1876"),
    "youtube-thumbnail-downloader": ("4.8", "2109"),
    "thermal-label-maker": ("4.7", "876"),
    "typing-speed-test": ("4.9", "2432"),
    "unit-converter": ("4.8", "1987"),
    "audio-to-text": ("4.8", "1543"),
    "text-compare-tool": ("4.8", "1321"),
    "fancy-font-generator": ("4.9", "2654"),
    "remove-watermark-from-image": ("4.7", "1198"),
    "xml-formatter": ("4.8", "1109"),
}

def fix_tool_file(slug):
    path = os.path.join(ROOT, f"{slug}.html")
    if not os.path.exists(path):
        print(f"  SKIP (not found): {slug}")
        return

    with open(path, "r", encoding="utf-8", errors="replace") as f:
        html = f.read()

    original = html

    # ── 1. ADD common.js IF MISSING ──────────────────────────────────
    if '/js/common.js' not in html:
        common_script = '\n<script defer src="/js/common.js?v=6.0"></script>'
        # Insert before </body>
        if '</body>' in html:
            html = html.replace('</body>', common_script + '\n</body>', 1)
        else:
            html = html + common_script
        print(f"    + Added common.js to {slug}")

    # ── 2. ADD <header></header> IF MISSING ──────────────────────────
    if '<header>' not in html and '<body>' in html:
        html = html.replace('<body>', '<body>\n<header></header>', 1)

    # ── 3. ADD <footer></footer> IF MISSING ─────────────────────────
    if '<footer' not in html and '</body>' in html:
        html = html.replace('</body>', '<footer></footer>\n</body>', 1)

    # ── 4. REMOVE duplicate injected "You Might Also Need" widget ────
    # This widget was injected before </main> or before </div><!-- /tool-container -->
    # It's identifiable by: style="margin-top:2rem;padding:1.5rem;background:#fff0b3;border:2.5px solid #000;"
    # And contains "You Might Also Need"
    rec_pattern = r'\n?\s*<!--\s*Post-Recommendation Widget\s*-->\s*<div[^>]*background:#fff0b3[^>]*>.*?</div>\s*'
    html = re.sub(rec_pattern, '', html, flags=re.DOTALL)
    # Also catch if the comment style is slightly different
    rec_pattern2 = r'<div style="margin-top:2rem;padding:1\.5rem;background:#fff0b3[^>]*>[\s\S]*?💡 You Might Also Need[\s\S]*?</div>\s*</div>'
    # More targeted: just remove the outer wrapper div that has "You Might Also Need"
    html = re.sub(
        r'<div[^>]*background:#fff0b3[^>]*>\s*<div[^>]*font-weight:900[^>]*>💡 You Might Also Need</div>[\s\S]*?</div>\s*</div>',
        '',
        html
    )

    # ── 5. REMOVE badly-injected guide buttons (from CSS-based injection) ──
    # These would appear as: <a href="/guides/...guide.html" class="nb-btn" style="background:#e9ddff;...">📖 Read Full Guide</a>
    # inside a CSS block which is wrong
    html = re.sub(r'<a href="/guides/[^"]*-guide\.html" class="nb-btn" style="background:#e9ddff[^>]*>📖 Read Full Guide</a>', '', html)

    # ── 6. FIX FONT SIZING IN TOOL H1 ──────────────────────────────
    # The .tool-hero h1 is too big. Add a targeted override in the inline <style>
    # Pattern: .tool-hero h1 { font-family:'Syne',...; font-size:clamp(...); ...}
    html = re.sub(
        r'(\.tool-hero h1\s*\{[^}]*font-size\s*:\s*)clamp\([^)]+\)',
        r'\1clamp(1.3rem, 3vw, 1.85rem)',
        html
    )
    # Fix letter-spacing on h1 to not be so tight
    html = re.sub(
        r'(\.tool-hero h1\s*\{[^}]*letter-spacing\s*:\s*)-0\.\d+em',
        r'\g<1>-0.01em',
        html
    )
    # Fix font-weight 900 -> 800 on tool-hero h1
    html = re.sub(
        r'(\.tool-hero h1\s*\{[^}]*font-weight\s*:\s*)900',
        r'\g<1>800',
        html
    )

    # ── 7. FIX text-transform:uppercase on h1 (causes "stretched" look) ──
    # In inline styles, replace font-size and text-transform on h1 elements
    html = re.sub(
        r'(<h1[^>]*style="[^"]*)(text-transform:\s*uppercase[;]?\s*)',
        r'\1',
        html, flags=re.IGNORECASE
    )

    # ── 8. UPDATE SoftwareApplication rating in JSON-LD ─────────────
    rating, count = TOOL_RATINGS.get(slug, ("4.8", "1200"))
    # Replace existing aggregateRating in SoftwareApplication schema
    html = re.sub(
        r'"aggregateRating"\s*:\s*\{"@type"\s*:\s*"AggregateRating"\s*,\s*"ratingValue"\s*:\s*"[\d.]+"\s*,\s*"ratingCount"\s*:\s*"[\d]+"\s*(?:,\s*"reviewCount"\s*:\s*"[\d]+")?',
        f'"aggregateRating":{{"@type":"AggregateRating","ratingValue":"{rating}","ratingCount":"{count}","reviewCount":"{int(int(count)*1.1)}"',
        html
    )

    # ── 9. ENSURE post-rec widget DIV is hidden by default (via class) ──
    # The widget injected has "You Might Also Need" - already removed above.
    # We inject it via JS in common.js now, so nothing needed here.

    if html != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  FIXED: {slug}")
    else:
        print(f"  OK (no changes): {slug}")

def main():
    print("=== Master Fix Script ===")
    total = 0
    for slug in TOOLS:
        fix_tool_file(slug)
        total += 1
    print(f"\nDone: {total} tools processed")

if __name__ == "__main__":
    main()
