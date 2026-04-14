import os
import json

history_dir = os.path.expandvars(r'%APPDATA%\Code\User\History')
print(f"Searching in {history_dir}")

common_js_candidates = []
style_css_candidates = []

for root, dirs, files in os.walk(history_dir):
    for file in files:
        if file.endswith('.json') or file == 'entries.json':
            continue # skip metadata files
        filepath = os.path.join(root, file)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                if 'Vintage Notebook' in content or 'Retro Neo-Brutalist' in content or '--shadow:' in content:
                    # Is it style.css?
                    if '--shadow:' in content and 'var(--border-color)' not in content and 'neo-brutalist' in content.lower():
                        style_css_candidates.append(filepath)
                    elif '--shadow:' in content and '--bg-color' in content: 
                        style_css_candidates.append(filepath)

                    # Is it common.js?
                    if 'injectHeader' in content and 'injectFooter' in content and 'Retro Neo-Brutalist' in content:
                        common_js_candidates.append(filepath)
        except Exception:
            pass

print("common.js candidates:", common_js_candidates)
print("style.css candidates:", style_css_candidates)
