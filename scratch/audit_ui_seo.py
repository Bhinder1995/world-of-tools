import os
import glob
import re
import json

def audit():
    files = glob.glob('c:/Users/HP/Desktop/Projects Folder/world_of_tools/*.html')
    issues = {
        'duplicate_guide_buttons': [],
        'wrong_theme_color': [],
        'missing_canonical': [],
        'js_version_mismatch': [],
        'missing_schema_rating': [],
    }

    for f in files:
        if 'worldoftools' in f or 'index.html' in f or 'calculators-online' in f or 'developer-tools' in f or 'seo-tools' in f or 'text-tools' in f or 'web-utilities' in f:
            continue
            
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Duplicate guide buttons
            guide_btn_pattern = r'<div style="margin-bottom:1\.75rem;"><a class="btn" href="/guides/[^"]+"[^>]*>.*?Read Tool Guide</a></div>'
            matches = re.findall(guide_btn_pattern, content)
            if len(matches) > 1:
                issues['duplicate_guide_buttons'].append((os.path.basename(f), len(matches)))
                
            # Theme color
            theme_color = re.search(r'<meta[^>]*name="theme-color"[^>]*content="([^"]+)"', content)
            if theme_color and theme_color.group(1).lower() != '#ffe066':
                issues['wrong_theme_color'].append((os.path.basename(f), theme_color.group(1)))
            elif not theme_color:
                issues['wrong_theme_color'].append((os.path.basename(f), "MISSING"))
                
            # Canonical
            if 'rel="canonical"' not in content:
                issues['missing_canonical'].append(os.path.basename(f))
                
            # JS version
            js_version = re.search(r' src="/js/common\.js\?v=([^"]+)"', content)
            if js_version and js_version.group(1) != '2.6':
                issues['js_version_mismatch'].append((os.path.basename(f), js_version.group(1)))
                
            # Schema
            if '"@type": "SoftwareApplication"' in content and '"AggregateRating"' in content and '"reviewCount"' not in content:
                issues['missing_schema_rating'].append(os.path.basename(f))

    with open('c:/tmp/ui_seo_audit_results.json', 'w', encoding='utf-8') as outfile:
        json.dump(issues, outfile, indent=2)

audit()
