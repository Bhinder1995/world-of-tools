import os
import glob
import re

files = glob.glob('*.html')
sanitized_count = 0

for f in files:
    if f in ['calculators-online.html', 'developer-tools-online.html', 'text-tools-online.html', 'seo-tools-free.html', 'india-tools.html', 'image-tools.html', 'design-tools.html', 'security-tools.html']:
        continue
        
    with open(f, 'r', encoding='utf-8') as content:
        html = content.read()
    
    # Check for the injected block
    if '<!-- SEO Optimization Meta Tags -->' in html:
        # We have the injected block. Let's see if we have duplicates outside of it.
        
        # 1. Remove canonical tags outside the block
        # Find the block start
        block_start = html.find('<!-- SEO Optimization Meta Tags -->')
        
        # Content before the block
        head_before = html[:block_start]
        # Content of the block and after
        rest = html[block_start:]
        
        # Check if head_before has canonical
        if 'rel="canonical"' in head_before or 'rel=\'canonical\'' in head_before:
            # Remove canonical from head_before
            head_before = re.sub(r'<link.*?rel=["\']canonical["\'].*?>', '', head_before, flags=re.IGNORECASE)
            head_before = re.sub(r'<link.*?href=.*?rel=["\']canonical["\'].*?>', '', head_before, flags=re.IGNORECASE)
            
            new_html = head_before + rest
            html = new_html
            sanitized_count += 1
            
        # 2. Remove duplicate OG tags in head_before
        og_tags = ['og:type', 'og:url', 'og:title', 'og:description', 'og:image', 'og:site_name', 'twitter:card', 'twitter:title', 'twitter:description', 'twitter:image']
        for og in og_tags:
            if og in head_before:
                head_before = re.sub(f'<meta.*?property=["\']{og}["\'].*?>', '', head_before, flags=re.IGNORECASE)
                head_before = re.sub(f'<meta.*?name=["\']{og}["\'].*?>', '', head_before, flags=re.IGNORECASE)
        
        html = head_before + rest

    with open(f, 'w', encoding='utf-8') as content:
        content.write(html)

print(f"Sanitized {sanitized_count} files by removing duplicate tags outside the primary SEO block.")
