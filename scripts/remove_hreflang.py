import os
from bs4 import BeautifulSoup

def remove_hreflangs(base_dir):
    for f in os.listdir(base_dir):
        if not f.endswith('.html'):
            continue
            
        filepath = os.path.join(base_dir, f)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            
        soup = BeautifulSoup(content, 'html.parser')
        modified = False
        
        for hr in soup.find_all('link', attrs={'rel': 'alternate'}):
            if 'hreflang' in hr.attrs:
                hr.decompose()
                modified = True
                
        if modified:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(str(soup))
            print(f"Cleaned hreflang from {f}")

if __name__ == "__main__":
    remove_hreflangs(r"c:\Users\HP\Desktop\Projects Folder\world_of_tools")
