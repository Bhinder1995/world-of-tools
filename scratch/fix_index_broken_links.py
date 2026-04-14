import os
import re

def fix_broken_links_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    # Look for href="/es/guides/.html" or href="/hi/guides/.html" 
    # Or generically anything like href="/([^/]+)/guides/.html" and change it to href="/guides/"
    
    # 1. Fix the "Browse All Guides" links
    content = re.sub(r'href="/(es|hi|des)/guides/\.html"', r'href="/guides/"', content)
    
    # 2. Fix localized guide cards if any became like href="/es/guides/some-guide.html"
    content = re.sub(r'href="/(es|hi|des)/guides/([^"]+)"', r'href="/guides/\2"', content)
    
    # 3. Strip ?lang=x from any guide links
    content = re.sub(r'href="(/guides/[^"?]+)\?lang=(es|hi)"', r'href="\1"', content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed broken links in {filepath}")

def process_all():
    directories = ['es', 'hi']
    for base_path in directories:
        if not os.path.exists(base_path): continue
        for file in os.listdir(base_path):
            if file.endswith('.html'):
                filepath = os.path.join(base_path, file)
                fix_broken_links_in_file(filepath)

if __name__ == "__main__":
    process_all()
