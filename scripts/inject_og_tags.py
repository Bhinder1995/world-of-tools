import os
from bs4 import BeautifulSoup

def update_og_tags(filepath, base_url="https://worldoftools.in"):
    if not os.path.exists(filepath):
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    filename = os.path.basename(filepath)
    url_slug = filename.replace('.html', '')
    if filename == 'index.html':
        url_slug = ''
        
    full_url = f"{base_url}/{url_slug}".rstrip('/')

    head = soup.head
    if not head:
        return False

    # Add geo meta tags if missing
    add_geo_meta(soup, head)

    # Add og:locale if missing
    if not soup.find('meta', property='og:locale'):
        locale_tag = soup.new_tag('meta', property='og:locale', content='en_IN')
        head.append(locale_tag)

    # Check if OG tags already exist, if so only save geo/locale changes
    if soup.find('meta', property='og:title'):
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        return True

    # Extract existing title and description
    title_element = soup.find('title')
    title_text = title_element.string if title_element else "Free Online Tools - WorldOfTools"
    
    desc_element = soup.find('meta', attrs={'name': 'description'})
    desc_text = desc_element['content'] if desc_element else title_text

    # Default image (use banner for all pages)
    og_image = f"{base_url}/og/worldoftools-banner.png"

    tags_to_inject = [
        # Open Graph
        soup.new_tag('meta', property='og:type', content='website'),
        soup.new_tag('meta', property='og:url', content=full_url),
        soup.new_tag('meta', property='og:title', content=title_text),
        soup.new_tag('meta', property='og:description', content=desc_text),
        soup.new_tag('meta', property='og:image', content=og_image),
        soup.new_tag('meta', property='og:image:width', content='1200'),
        soup.new_tag('meta', property='og:image:height', content='630'),
        soup.new_tag('meta', property='og:site_name', content='WorldOfTools'),
        
        # Twitter
        soup.new_tag('meta', attrs={'name': 'twitter:card', 'content': 'summary_large_image'}),
        soup.new_tag('meta', attrs={'name': 'twitter:url', 'content': full_url}),
        soup.new_tag('meta', attrs={'name': 'twitter:title', 'content': title_text}),
        soup.new_tag('meta', attrs={'name': 'twitter:description', 'content': desc_text}),
        soup.new_tag('meta', attrs={'name': 'twitter:image', 'content': og_image})
    ]

    # Just append to head
    for tag in tags_to_inject:
         head.append(tag)

    with open(filepath, 'w', encoding='utf-8') as f:
        # using str(soup) over prettify so inline structural elements aren't ruined
        f.write(str(soup))
        
    return True

def add_geo_meta(soup, head):
    geo_tags = {
        'geo.region': 'IN',
        'geo.placename': 'India',
        'geo.position': '20.593684;78.96288',
        'ICBM': '20.593684, 78.96288'
    }
    for name, content in geo_tags.items():
        existing = soup.find('meta', attrs={'name': name})
        if not existing:
            tag = soup.new_tag('meta', attrs={'name': name, 'content': content})
            head.append(tag)

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    count = 0
    
    for root, dirs, files in os.walk(base_dir):
        # Ignore deep node modules or git folders
        if 'node_modules' in root or '.git' in root:
            continue
            
        for f in files:
            if f.endswith('.html'):
                abs_path = os.path.join(root, f)
                if update_og_tags(abs_path):
                    count += 1
                    print(f"Injected Social SEO Tags: {f}")
                    
    print(f"Total HTML files supercharged with Open Graph tags: {count}")

if __name__ == "__main__":
    main()
