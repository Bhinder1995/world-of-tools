import re
from bs4 import BeautifulSoup

def extract_guides():
    with open('WorldOfTools_Guides_and_InterLink_Report.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    guides = soup.find_all('div', class_='guide-card')
    
    print(f"Found {len(guides)} guides.")
    for g in guides[:2]:
        slug_div = g.find('div', class_='guide-slug')
        if not slug_div:
            continue
        slug_text = slug_div.text
        slug = re.search(r'worldoftools\.in/(.*?) ·', slug_text).group(1).strip()
        print(f"--- Guide for {slug} ---")
        body = g.find('div', class_='guide-body')
        # Print first 200 chars of text
        print(body.text[:200].replace('\n', ' '))

if __name__ == '__main__':
    extract_guides()
