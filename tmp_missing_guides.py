import os
import re
import json

base_dir = 'guides'
index_file = os.path.join(base_dir, 'index.html')

with open(index_file, 'r', encoding='utf-8') as f:
    index_content = f.read()

missing_guides = []
for filename in os.listdir(base_dir):
    if filename.endswith('.html') and filename not in ['index.html', 'guide-template.html']:
        slug = filename[:-5]
        if slug not in index_content:
            file_path = os.path.join(base_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
                title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
                title = title_match.group(1).strip() if title_match else slug
                
                desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE | re.DOTALL)
                desc = desc_match.group(1).strip() if desc_match else ""
                
                missing_guides.append({
                    "slug": slug,
                    "title": title,
                    "desc": desc
                })

print(json.dumps(missing_guides, indent=2))
