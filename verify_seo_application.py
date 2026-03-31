import os
import json
from bs4 import BeautifulSoup

def verify_seo():
    with open('seo_mapping.json', 'r', encoding='utf-8') as f:
        mapping = json.load(f)

    base_path = r'c:\Users\HP\Desktop\Projects Folder\world_of_tools'
    results = {'matched': 0, 'mismatched': 0, 'missing_file': 0}

    for url, expected in mapping.items():
        if url == '/':
            filename = 'index.html'
        else:
            filename = url.lstrip('/') + '.html'
        
        filepath = os.path.join(base_path, filename)
        
        if not os.path.exists(filepath):
            # Try guides directory if it's a guide URL (though mapping is mainly root tools)
            if 'guide' in url:
                filepath = os.path.join(base_path, 'guides', filename)
            
        if not os.path.exists(filepath):
            print(f"❌ Missing File: {filename} (URL: {url})")
            results['missing_file'] += 1
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'html.parser')
            
        actual_title = soup.title.string.strip() if soup.title else ""
        # Handle &amp; and other entities in soup
        expected_title = expected['title'].strip()
        
        # Simple comparison, might need to handle entities but let's see
        if actual_title == expected_title or actual_title.replace('&', '&amp;') == expected_title or actual_title == expected_title.replace('&amp;', '&'):
            results['matched'] += 1
        else:
            print(f"⚠️ Mismatch in {filename}:")
            print(f"  Expected: {expected_title}")
            print(f"  Actual:   {actual_title}")
            results['mismatched'] += 1

    print("\n--- Verification Stats ---")
    print(f"Matched: {results['matched']}")
    print(f"Mismatched: {results['mismatched']}")
    print(f"Missing Files: {results['missing_file']}")

if __name__ == "__main__":
    verify_seo()
