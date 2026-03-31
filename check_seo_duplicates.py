import os
from bs4 import BeautifulSoup
from collections import defaultdict

def check_duplicates():
    base_path = r'c:\Users\HP\Desktop\Projects Folder\world_of_tools'
    titles = defaultdict(list)
    descriptions = defaultdict(list)

    # Walk through root and guides
    for root_dir, dirs, files in os.walk(base_path):
        if '.git' in root_dir or 'node_modules' in root_dir:
            continue
            
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root_dir, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        soup = BeautifulSoup(f.read(), 'html.parser')
                    
                    title = soup.title.string.strip() if soup.title else "MISSING TITLE"
                    desc_tag = soup.find('meta', attrs={'name': 'description'})
                    desc = desc_tag['content'].strip() if desc_tag and desc_tag.has_attr('content') else "MISSING DESC"
                    
                    titles[title].append(file)
                    descriptions[desc].append(file)
                except Exception as e:
                    print(f"Error reading {file}: {e}")

    print("--- DUPLICATE TITLES ---")
    for title, files in titles.items():
        if len(files) > 1 and title != "MISSING TITLE":
            print(f"Duplicate Title: '{title}' in {files}")
            
    print("\n--- DUPLICATE DESCRIPTIONS ---")
    for desc, files in descriptions.items():
        if len(files) > 1 and desc != "MISSING DESC":
            # Some guides might share descriptions with tools if not updated, let's check
            print(f"Duplicate Desc: '{desc[:50]}...' in {files}")

if __name__ == "__main__":
    check_duplicates()
