import os
import json
from bs4 import BeautifulSoup

def process_i18n(base_dir):
    data = {
        "age-calculator.html": {
            "slug": "age-calculator",
            "en": { "title": "Age Calculator | Free Online Tool", "h1": "Age Calculator", "desc": "Calculate your exact age online." },
            "es": { "title": "Calculadora de edad | Herramienta online gratuita", "h1": "Calculadora de edad", "desc": "Calcula tu edad exacta con precisión con esta herramienta gratuita." },
            "pt": { "title": "Calculadora de idade | Ferramenta online gratuita", "h1": "Calculadora de idade", "desc": "Calcule sua idade exata rapidamente com nossa ferramenta gratuita." }
        },
        "word-counter.html": {
            "slug": "word-counter",
            "en": { "title": "Word Counter | Free Online Tool", "h1": "Word Counter", "desc": "Count words and characters online." },
            "es": { "title": "Contador de palabras | Gratuito", "h1": "Contador de palabras", "desc": "Cuenta palabras y caracteres en línea de forma rápida y segura." },
            "pt": { "title": "Contador de palavras | Gratuito", "h1": "Contador de palavras", "desc": "Conte palavras e caracteres online com total privacidade." }
        },
        "percentage-calculator.html": {
            "slug": "percentage-calculator",
            "en": { "title": "Percentage Calculator", "h1": "Percentage Calculator", "desc": "Fast percentage calculator." },
            "es": { "title": "Calculadora de porcentajes", "h1": "Calculadora de porcentajes", "desc": "Calculadora rápida de porcentajes y descuentos." },
            "pt": { "title": "Calculadora de porcentagem", "h1": "Calculadora de porcentagem", "desc": "Calcule porcentagens e descontos facilmente." }
        },
        "bmi-calculator.html": {
            "slug": "bmi-calculator",
            "en": { "title": "BMI Calculator", "h1": "BMI Calculator", "desc": "Calculate Body Mass Index online." },
            "es": { "title": "Calculadora de IMC | Gratuito", "h1": "Calculadora de IMC", "desc": "Calcula tu Índice de Masa Corporal (IMC) fácilmente." },
            "pt": { "title": "Calculadora de IMC | Gratuito", "h1": "Calculadora de IMC", "desc": "Calcule seu Índice de Massa Corporal (IMC) rapidamente." }
        },
        "password-generator.html": {
            "slug": "password-generator",
            "en": { "title": "Password Generator", "h1": "Password Generator", "desc": "Create highly secure passwords natively in browser." },
            "es": { "title": "Generador de contraseñas seguras", "h1": "Generador de contraseñas", "desc": "Crea contraseñas altamente seguras y aleatorias en tu navegador." },
            "pt": { "title": "Gerador de senhas seguras", "h1": "Gerador de senhas", "desc": "Crie senhas fortes e seguras rapidamente no seu navegador." }
        },
        "image-compressor.html": {
            "slug": "image-compressor",
            "en": { "title": "Image Compressor", "h1": "Image Compressor", "desc": "Compress JPG/PNG offline without uploads." },
            "es": { "title": "Compresor de imágenes", "h1": "Compresor de imágenes", "desc": "Comprime imágenes JPG/PNG de forma privada sin subirlas a la red." },
            "pt": { "title": "Compressor de imagens", "h1": "Compressor de imagens", "desc": "Comprima imagens JPG/PNG offline com segurança." }
        },
        "video-compressor.html": {
            "slug": "video-compressor",
            "en": { "title": "Video Compressor", "h1": "Video Compressor", "desc": "Reduce video file sizes privately." },
            "es": { "title": "Compresor de video", "h1": "Compresor de video", "desc": "Reduce el tamaño de tus archivos de video rápidamente y sin conexión." },
            "pt": { "title": "Compressor de vídeo", "h1": "Compressor de vídeo", "desc": "Reduza o tamanho dos seus vídeos de forma privada e rápida." }
        },
        "qr-code-generator.html": {
            "slug": "qr-code-generator",
            "en": { "title": "QR Code Generator", "h1": "QR Code Generator", "desc": "Create free QR codes instantly." },
            "es": { "title": "Generador de códigos QR", "h1": "Generador de códigos QR", "desc": "Crea códigos QR personalizados para URLs y textos." },
            "pt": { "title": "Gerador de QR Code", "h1": "Gerador de QR Code", "desc": "Crie QR codes personalizados de forma rápida e gratuita." }
        },
        "unit-converter.html": {
            "slug": "unit-converter",
            "en": { "title": "Unit Converter", "h1": "Unit Converter", "desc": "Convert lengths, weights and sizes easily." },
            "es": { "title": "Conversor de unidades", "h1": "Conversor de unidades", "desc": "Convierte longitudes, pesos y más dimensiones fácilmente." },
            "pt": { "title": "Conversor de unidades", "h1": "Conversor de unidades", "desc": "Converta comprimentos, pesos e várias medidas com precisão." }
        },
        "aspect-ratio-calculator.html": {
            "slug": "aspect-ratio-calculator",
            "en": { "title": "Aspect Ratio Calculator", "h1": "Aspect Ratio Calculator", "desc": "Calculate image and video aspect dimensions." },
            "es": { "title": "Calculadora de relación de aspecto", "h1": "Calculadora de relación de aspecto", "desc": "Calcula dimensiones exactas para video e imagen (16:9, 4:3, etc)." },
            "pt": { "title": "Calculadora de proporção de tela", "h1": "Calculadora de proporção de tela", "desc": "Calcule dimensões exatas de proporção de tela para imagens e vídeos." }
        }
    }

    es_dir = os.path.join(base_dir, 'es')
    pt_dir = os.path.join(base_dir, 'pt')
    os.makedirs(es_dir, exist_ok=True)
    os.makedirs(pt_dir, exist_ok=True)

    base_site = "https://worldoftools.in"

    success_count = 0

    for filename, translations in data.items():
        filepath = os.path.join(base_dir, filename)
        if not os.path.exists(filepath):
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            base_html = f.read()

        # Build English Base Soup to inject hreflang tags
        soup_en = BeautifulSoup(base_html, 'html.parser')
        slug = translations['slug']

        # Clear existing hreflangs if any to avoid duplication
        for hr in soup_en.find_all('link', attrs={'rel': 'alternate'}):
            if 'hreflang' in hr.attrs:
                hr.decompose()

        hreflang_tags = [
            f'<link rel="alternate" hreflang="x-default" href="{base_site}/{slug}" />',
            f'<link rel="alternate" hreflang="en" href="{base_site}/{slug}" />',
            f'<link rel="alternate" hreflang="es" href="{base_site}/es/{slug}" />',
            f'<link rel="alternate" hreflang="pt" href="{base_site}/pt/{slug}" />'
        ]
        
        # Append to head
        if soup_en.head:
            soup_en.head.append(BeautifulSoup(''.join(hreflang_tags), 'html.parser'))
        
        # Write modified english file permanently
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup_en))

        # Now Create the Foreign Versions
        for lang_code in ['es', 'pt']:
            soup = BeautifulSoup(str(soup_en), 'html.parser') # Start fresh from the modified english base
            
            # 1. Update Lang attribute
            html_tag = soup.find('html')
            if html_tag:
                html_tag['lang'] = lang_code
                
            # 2. Canonical and OG URLs
            target_url = f"{base_site}/{lang_code}/{slug}"
            can_tag = soup.find('link', rel='canonical')
            if can_tag:
                can_tag['href'] = target_url
                
            og_url = soup.find('meta', property='og:url')
            if og_url:
                og_url['content'] = target_url
                
            tw_url = soup.find('meta', attrs={'name': 'twitter:url'})
            if tw_url:
                tw_url['content'] = target_url

            # 3. Titles and Descriptions
            tr = translations[lang_code]
            
            title_tag = soup.find('title')
            if title_tag: title_tag.string = tr['title']
            
            og_title = soup.find('meta', property='og:title')
            if og_title: og_title['content'] = tr['title']
            
            tw_title = soup.find('meta', attrs={'name': 'twitter:title'})
            if tw_title: tw_title['content'] = tr['title']

            desc_tag = soup.find('meta', attrs={'name': 'description'})
            if desc_tag: desc_tag['content'] = tr['desc']
            
            og_desc = soup.find('meta', property='og:description')
            if og_desc: og_desc['content'] = tr['desc']
            
            tw_desc = soup.find('meta', attrs={'name': 'twitter:description'})
            if tw_desc: tw_desc['content'] = tr['desc']
            
            # 4. H1
            h1 = soup.find('h1')
            if h1:
                # keep inside tags if exist, simplistic replacement
                h1.string = tr['h1']

            # 5. Asset routing fixes. 
            # Because the file is now in /es/, relative links like `js/script.js` will break. 
            # We MUST fix CSS and JS imports. 
            for link in soup.find_all('link', href=True):
                if link['href'].startswith(('css/', 'js/', 'icon', 'logo')):
                    link['href'] = '/' + link['href']
            
            for script in soup.find_all('script', src=True):
                if script['src'].startswith('js/'):
                    script['src'] = '/' + script['src']
                    
            for img in soup.find_all('img', src=True):
                if img['src'].startswith('img/'):
                    img['src'] = '/' + img['src']

            # Make link to home absolute
            for a in soup.find_all('a', href=True):
                if a['href'] == 'index.html' or a['href'] == '':
                    a['href'] = '/'

            # 6. Save
            out_path = os.path.join(base_dir, lang_code, filename)
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(str(soup))
                
        success_count += 1
        print(f"Propagated {slug} to EN, ES, and PT successfully.")

    print(f"Total universal tools fully internationalized: {success_count}")

if __name__ == "__main__":
    process_i18n(r"c:\Users\HP\Desktop\Projects Folder\world_of_tools")
