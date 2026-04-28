import os
import re

def fix_seo_links(root_dir):
    # Regex to find href="/something.html"
    # Group 1 captures the path without .html
    href_regex = re.compile(r'href="/([^"]+)\.html"')
    
    # Regex to find canonical link with .html in guides
    # Specifically targeting worldoftools.in/guides/...html
    canonical_regex = re.compile(r'(<link rel="canonical" href="https://worldoftools\.in/guides/[^"]+)\.html"')

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                print(f"Processing {file_path}...")
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 1. Replace internal hrefs
                new_content = href_regex.sub(r'href="/\1"', content)
                
                # 2. Replace canonicals in guides
                # (Note: This is mostly for files in guides/ directory)
                new_content = canonical_regex.sub(r'\1"', new_content)
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"  Fixed links/canonicals in {file}")

if __name__ == "__main__":
    base_path = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    fix_seo_links(base_path)
