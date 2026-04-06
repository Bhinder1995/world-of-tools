import os
from bs4 import BeautifulSoup

def build_home(base_dir):
    index_path = os.path.join(base_dir, 'index.html')
    if not os.path.exists(index_path):
        print("index.html not found!")
        return

    with open(index_path, 'r', encoding='utf-8') as f:
        base_html = f.read()

    soup_en = BeautifulSoup(base_html, 'html.parser')
    base_site = "https://worldoftools.in"

    # Add hreflangs to English index if not present
    for hr in soup_en.find_all('link', attrs={'rel': 'alternate'}):
        if 'hreflang' in hr.attrs:
            hr.decompose()

    hreflang_tags = [
        f'<link rel="alternate" hreflang="x-default" href="{base_site}/" />',
        f'<link rel="alternate" hreflang="en" href="{base_site}/" />',
        f'<link rel="alternate" hreflang="es" href="{base_site}/es/" />',
        f'<link rel="alternate" hreflang="pt" href="{base_site}/pt/" />'
    ]
    if soup_en.head:
        soup_en.head.append(BeautifulSoup(''.join(hreflang_tags), 'html.parser'))
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(str(soup_en))

    # Translations
    translations = {
        'es': {
            'title': 'Herramientas Online Gratuitas — 100% Privado | WorldOfTools',
            'desc': '60+ herramientas gratuitas online — calculadoras, utilidades para desarrolladores y SEO. Privado, sin registro y seguro.',
            'h1': '60+ Herramientas Online Gratuitas — Sin Registro y Privado'
        },
        'pt': {
            'title': 'Ferramentas Online Gratuitas — 100% Privado | WorldOfTools',
            'desc': 'Mais de 60 ferramentas online gratuitas — calculadoras, ferramentas de desenvolvedor e SEO. 100% privado.',
            'h1': '60+ Ferramentas Online Gratuitas — Sem Registro, 100% Privado'
        }
    }

    for lang_code in ['es', 'pt']:
        soup = BeautifulSoup(str(soup_en), 'html.parser')
        
        html_tag = soup.find('html')
        if html_tag: html_tag['lang'] = lang_code
            
        target_url = f"{base_site}/{lang_code}/"
        can_tag = soup.find('link', rel='canonical')
        if can_tag: can_tag['href'] = target_url
            
        # Meta updating
        tr = translations[lang_code]
        
        title_tag = soup.find('title')
        if title_tag: title_tag.string = tr['title']
        
        desc_tag = soup.find('meta', attrs={'name': 'description'})
        if desc_tag: desc_tag['content'] = tr['desc']
        
        og_title = soup.find('meta', property='og:title')
        if og_title: og_title['content'] = tr['title']
        
        og_desc = soup.find('meta', property='og:description')
        if og_desc: og_desc['content'] = tr['desc']

        # H1 updating
        h1 = soup.find('h1', class_='hero-title')
        if h1: h1.string = tr['h1']

        # Fix relative assets because file is in /es/ directory
        for link in soup.find_all('link', href=True):
            if link['href'].startswith(('css/', 'js/', 'img/', 'icon', 'logo')):
                if not link['href'].startswith('/'):
                    link['href'] = '/' + link['href']
        
        for script in soup.find_all('script', src=True):
            if script['src'].startswith('js/'):
                if not script['src'].startswith('/'):
                    script['src'] = '/' + script['src']

        # Write out
        out_path = os.path.join(base_dir, lang_code, 'index.html')
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))
            
        print(f"Generated {lang_code}/index.html")

if __name__ == "__main__":
    build_home(r"c:\Users\HP\Desktop\Projects Folder\world_of_tools")
