#!/usr/bin/env python3
"""
patch_h1_inline.py
Patches the inline <style> block inside each tool HTML to shrink the .tool-hero h1
and remove text-transform:uppercase from h1 elements.
"""
import os, re, glob

ROOT = r"C:\Users\HP\Desktop\Projects Folder\world_of_tools"

def patch_file(path):
    with open(path, encoding='utf-8', errors='replace') as f:
        html = f.read()
    orig = html

    # Fix 1: .tool-hero h1 font-size (inline style block)
    # Pattern: .tool-hero h1 { ... font-size:clamp(...); ... }
    def fix_h1_style(m):
        s = m.group(0)
        # Replace font-size clamp
        s = re.sub(r'font-size\s*:\s*clamp\([^)]+\)', 'font-size:clamp(1.2rem,2.8vw,1.75rem)', s)
        # Replace font-weight 900 -> 800
        s = re.sub(r'(font-weight\s*:\s*)950|900', r'\g<1>800', s)
        # Fix letter-spacing
        s = re.sub(r'letter-spacing\s*:\s*-0\.[0-9]+em', 'letter-spacing:-0.01em', s)
        # Remove text-transform from h1 blocks
        s = re.sub(r'text-transform\s*:\s*uppercase\s*;?\s*', '', s, flags=re.IGNORECASE)
        return s

    # Match the .tool-hero h1 rule inside <style> block
    html = re.sub(r'\.tool-hero h1\s*\{[^}]+\}', fix_h1_style, html, flags=re.DOTALL)

    # Fix 2: Remove any standalone text-transform:uppercase from h1 CSS rules
    html = re.sub(r'(h1[^{]*\{[^}]*?)text-transform\s*:\s*uppercase\s*;?\s*', r'\1', html, flags=re.DOTALL|re.IGNORECASE)

    # Fix 3: Fix seo-section h2 sizes (also often too big)
    def fix_seo_h2(m):
        s = m.group(0)
        s = re.sub(r'font-size\s*:\s*\d+\.?\d*rem', 'font-size:1.25rem', s)
        s = re.sub(r'(font-weight\s*:\s*)950', r'\g<1>800', s)
        return s

    html = re.sub(r'\.seo-section h2\s*\{[^}]+\}', fix_seo_h2, html, flags=re.DOTALL)

    # Fix 4: Do NOT override font via Syne for h1 on tools — switch to Space Grotesk in inline style
    # Replace font-family:'Syne'... in .tool-hero h1 rule
    html = re.sub(
        r"(\.tool-hero h1\s*\{[^}]*font-family\s*:\s*)'Syne'",
        r"\g<1>'Space Grotesk'",
        html, flags=re.DOTALL
    )

    # Fix 5: Remove duplicate "More Free Tools" section IF we have wot-post-rec div
    # Actually just shrink the duplicate tools-grid h2 label
    def fix_h2_size(m):
        tag = m.group(0)
        # Replace font-size if it's in an inline style on h2/h3
        tag = re.sub(r'font-size:\s*\d+\.?\d*rem', 'font-size:1.1rem', tag)
        return tag
    # Shrink h2/h3 with inline styles that have large font-size
    html = re.sub(r'<h[23][^>]*style="[^"]*font-size:\s*[23]\.[0-9]+rem[^"]*"[^>]*>', fix_h2_size, html)

    if html != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)
        return True
    return False

def main():
    files = glob.glob(os.path.join(ROOT, '*.html'))
    fixed = 0
    for f in sorted(files):
        fn = os.path.basename(f)
        if fn in ('index.html', 'about-us.html', 'contact-us.html', 'privacy.html', 'terms.html'):
            continue
        if patch_file(f):
            print(f'  PATCHED: {fn}')
            fixed += 1
    print(f'\nDone: {fixed} files patched')

if __name__ == '__main__':
    main()
