import os
import re

# We will scan the 'guides' directory to find out which slug has which guide
# But it's easier to use a static map since some guides have special names
GUIDE_MAP = {
    "age-calculator": "age-calculator-guide",
    "bmi-calculator": "bmi-calculator-guide",
    "sip-calculator": "sip-calculator-guide",
    "loan-eligibility-calculator": "loan-eligibility-calculator-guide",
    "ppf-calculator": "ppf-calculator-guide",
    "emi-calculator": "emi-calculator-guide",
    "gst-calculator": "gst-calculator-guide",
    "scientific-calculator": "scientific-calculator-guide",
    "percentage-calculator": "percentage-calculator-guide",
    "aspect-ratio-calculator": "aspect-ratio-calculator-guide",
    "number-to-words-converter": "number-to-words-converter-guide",
    "roman-numerals-converter": "roman-numerals-converter-guide",
    "random-number-generator": "random-number-generator-guide",
    "unit-converter": "unit-converter-guide",

    # Developer Tools
    "json-formatter": "json-formatter-guide",
    "css-gradient-generator": "css-gradient-generator-guide",
    "hash-generator": "hash-generator-guide",
    "jwt-decoder": "jwt-decoder-guide",
    "sql-formatter": "sql-formatter-guide",
    "regex-tester": "regex-tester-guide",
    "base64-encoder-decoder": "base64-encoder-decoder-guide",
    "url-encoder-decoder": "url-encoder-decoder-guide",

    # Text & Content Tools
    "word-counter": "word-counter-guide",
    "case-converter": "case-converter-guide",
    "lorem-ipsum-generator": "lorem-ipsum-generator-guide",
    "markdown-to-html": "markdown-to-html-guide",
    "typing-speed-test": "typing-speed-test-guide",
    "text-compare-tool": "text-compare-tool-guide",
    "text-to-binary-converter": "text-to-binary-converter-guide",

    # Image Tools
    "image-compressor": "image-compressor-guide",
    "background-remover": "background-remover-guide",
    "qr-code-generator": "qr-code-generator-guide",
    "image-to-text-ocr": "image-to-text-ocr-guide",
    "image-converter": "image-converter-guide",
    "color-converter": "color-converter-guide",
    "youtube-thumbnail-downloader": "youtube-thumbnail-downloader-guide",
    "remove-watermark-from-image": "remove-watermark-from-image-guide",
    "image-upscaler": "image-upscaler-guide",
    "exif-metadata-remover": "remove-exif-metadata-guide",
    "favicon-generator": "favicon-generator-guide",

    # Utility Tools & Web
    "seo-meta-tag-generator": "seo-meta-tag-generator-guide",
    "serp-preview": "serp-preview-guide",
    "keyword-density-checker": "keyword-density-checker-guide",
    "link-shortener": "link-shortener-guide",
    "audio-to-text": "audio-to-text-guide",
    "time-zone-converter": "time-zone-converter-guide",
    "password-generator": "password-generator-guide",
    "ip-address-lookup": "ip-address-lookup-guide",
    "invoice-generator": "invoice-generator-guide",
    "thermal-label-maker": "thermal-label-maker-guide",
    "email-signature-generator": "email-signature-generator-guide",
    "csv-to-json": "csv-to-json-guide",
    "cgpa-calculator": "cgpa-calculator-guide",
    "loan-comparison-calculator": "loan-comparison-calculator-guide",
    "video-compressor": "video-compressor-guide",
    "linkedin-creator-suite": "linkedin-creator-suite-guide",
    "video-to-gif": "video-to-gif-converter-guide",
    "video-to-mp3-converter": "video-to-mp3-extractor-guide",
    
    # Newly confirmed
    "json-ld-generator": "schema-markup-generator-guide",
    "schema-markup-generator": "schema-markup-generator-guide",
    "cron-expression-generator": "cron-expression-generator-guide",
    "css-minifier": "css-minifier-guide",
    "fancy-font-generator": "fancy-font-generator-guide",
    "uuid-generator": "uuid-generator-guide",
    "xml-formatter": "xml-formatter-guide",
    "barcode-generator": "barcode-generator-guide"
}

# The language map for the button text
L10N = {
    "en": "📖 Read Expert Guide",
    "es": "📖 Leer Guía Experta",
    "hi": "📖 एक्सपर्ट गाइड पढ़ें"
}

def clean_old_guide_button(content):
    # Regex to catch the old guide buttons wherever they appear
    # The old guide buttons sometimes had "target='_blank'" and "rel='follow'" or classes like "nb-btn"
    # Example 1: <a href="/guides/...html" class="btn" style="...">Read Full Expert Guía ?</a>
    # Example 2: <a class="btn btn-secondary" href="/guides/...html?lang=es" ...>📖 ...</a>
    # We will remove them entirely so that there are no duplicates.
    
    # We remove anything that matches <a ... href="/guides/...
    # But wait, there might be other valid links? Guide buttons typically contain "guide" or "guía" in the text
    # It's safer to remove any <a ... href="/guides/..."> inside .result-actions or just remove standalone guide links in paragraph blocks right before scripts.
    
    # Let's remove the specific "Expert Guide" paragraphs injected at the bottom:
    content = re.sub(r'<p style="margin-bottom:1\.5rem; color:var\(--text-muted\);">Check out our comprehensive expert guide.*?</p>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<a[^>]*href="/guides/[^"]*"[^>]*>.*?Read Full Expert.*?</a\s*>', '', content, flags=re.IGNORECASE|re.DOTALL)
    content = re.sub(r'<a[^>]*href="/guides/[^"]*"[^>]*>.*?Read Tool Guide.*?</a\s*>', '', content, flags=re.IGNORECASE|re.DOTALL)
    
    # And the 'btn-secondary' guide injected by inject_guides_and_recs.py
    # e.g. <a class="btn btn-secondary" href="/guides/...
    content = re.sub(r'<a(?=.*class="[^"]*btn[^"]*")[^>]*href="/guides/[^>]*>.*? Leer guía experta.*?</a>', '', content, flags=re.IGNORECASE|re.DOTALL)
    content = re.sub(r'<a(?=.*class="[^"]*btn[^"]*")[^>]*href="/guides/[^>]*>.*? एक्सपर्ट गाइड पढ़ें.*?</a>', '', content, flags=re.IGNORECASE|re.DOTALL)
    content = re.sub(r'<a(?=.*class="[^"]*btn[^"]*")[^>]*href="/guides/[^>]*>.*? Read Expert Guide.*?</a>', '', content, flags=re.IGNORECASE|re.DOTALL)
    content = re.sub(r'<a(?=.*class="[^"]*btn[^"]*")[^>]*href="/guides/[^>]*>\s*📖.*?</a\s*>', '', content, flags=re.IGNORECASE|re.DOTALL)
    
    return content

def process_file(filepath, lang, slug):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if it is an index or guide
    if slug == 'index' or slug == 'guides' or slug == '404' or 'guide.html' in filepath:
        return
    
    original_content = content
    content = clean_old_guide_button(content)
    
    # Determine the correct guide URL
    # Map back original slug if this is ES/HI.
    # We will use the English slug as base to look up the guide, 
    # but the tool filenames in es/ are translated. Let's find the original English slug.
    # Actually, the quickest way to get the guide filename is to just parse what link it previously had or just use the root map.
    
    # We need a reverse map for ES
    ES_SLUGS_INV = {
        "calculadora-de-edad": "age-calculator",
        "calculadora-imc": "bmi-calculator",
        "calculadora-sip": "sip-calculator",
        "calculadora-eligibilidad-prestamo": "loan-eligibility-calculator",
        "calculadora-ppf": "ppf-calculator",
        "calculadora-emi": "emi-calculator",
        "calculadora-gst": "gst-calculator",
        "calculadora-cientifica": "scientific-calculator",
        "calculadora-de-porcentaje": "percentage-calculator",
        "calculadora-relacion-aspecto": "aspect-ratio-calculator",
        "convertidor-numeros-a-letras": "number-to-words-converter",
        "convertidor-numeros-romanos": "roman-numerals-converter",
        "generador-numeros-aleatorios": "random-number-generator",
        "convertidor-de-unidades": "unit-converter",
        "formateador-json": "json-formatter",
        "generador-gradientes-css": "css-gradient-generator",
        "generador-de-hash": "hash-generator",
        "decodificador-jwt": "jwt-decoder",
        "formateador-sql": "sql-formatter",
        "probador-regex": "regex-tester",
        "codificador-decodificador-base64": "base64-encoder-decoder",
        "codificador-decodificador-url": "url-encoder-decoder",
        "contador-de-palabras": "word-counter",
        "generador-etiquetas-meta-seo": "seo-meta-tag-generator",
        "vista-previa-serp": "serp-preview",
        "comprobador-densidad-palabras-clave": "keyword-density-checker",
        "conversor-markdown-a-html": "markdown-to-html",
        "compresor-de-imagenes": "image-compressor",
        "eliminador-de-fondo": "background-remover",
        "generador-codigo-qr": "qr-code-generator",
        "prueba-velocidad-mecanografia": "typing-speed-test",
        "acortador-de-enlaces": "link-shortener",
        "audio-a-texto": "audio-to-text",
        "conversor-de-imagenes": "image-converter",
        "convertidor-de-color": "color-converter",
        "conversor-zona-horaria": "time-zone-converter",
        "descargador-miniaturas-youtube": "youtube-thumbnail-downloader",
        "generador-de-contrasenas": "password-generator",
        "buscador-direccion-ip": "ip-address-lookup",
        "generador-de-facturas": "invoice-generator",
        "creador-etiquetas-termicas": "thermal-label-maker",
        "generador-firmas-email": "email-signature-generator",
        "quitar-marca-agua-imagen": "remove-watermark-from-image",
        "escalador-imagenes-ai": "image-upscaler",
        "csv-a-json": "cv-to-json", # Wait, csv-to-json!
        "calculadora-cgpa": "cgpa-calculator",
        "comparador-de-prestamos": "loan-comparison-calculator",
        "herramienta-comparar-texto": "text-compare-tool",
        "conversor-texto-a-binario": "text-to-binary-converter",
        "compresor-de-video": "video-compressor",
        "herramientas-linkedin": "linkedin-creator-suite",
        "video-a-gif": "video-to-gif",
        "video-a-mp3": "video-to-mp3-converter"
    }

    base_eng_slug = slug
    if lang == 'es' and slug in ES_SLUGS_INV:
        base_eng_slug = ES_SLUGS_INV[slug]
    
    if base_eng_slug == 'csv-to-json':
        base_eng_slug = 'csv-to-json'
    if slug == 'csv-a-json':
        base_eng_slug = 'csv-to-json'

    # Check if there's a guide
    guide_slug = GUIDE_MAP.get(base_eng_slug)
    
    if not guide_slug:
        # Check if guide exists by file
        if os.path.exists(f"guides/{base_eng_slug}-guide.html"):
            guide_slug = f"{base_eng_slug}-guide"
    
    # Wait, some languages might not have a guide defined because it's not a tool. 
    # So if there's no guide_slug, we just write the cleaned content and continue
    if not guide_slug:
        if original_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        return

    button_text = L10N.get(lang, L10N["en"])
    button_html = f"""
        <a href="/guides/{guide_slug}.html" class="btn" style="background:#fff; color:#111827; border:3px solid #111827; border-radius:12px; padding:0.6rem 1.25rem; font-weight:800; font-size:0.95rem; display:inline-flex; align-items:center; gap:0.5rem; text-decoration:none; white-space:nowrap; transition:all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275); box-shadow:4px 4px 0 #111827;">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" style="color:var(--primary-color)"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg> 
            {button_text}
        </a>
"""

    # We need to wrap the H1
    # Match: <h1 ...>Title</h1>
    # However we should avoid wrapping multiple times if it's already wrapped!
    if "Read Expert Guide" in content or "Leer Guía Experta" in content or "एक्सपर्ट गाइड पढ़ें" in content:
        # Avoid dupes
        pass

    # Find the H1
    h1_match = re.search(r'(<h1[^>]*>)(.*?)(</h1>)', content, re.IGNORECASE | re.DOTALL)
    if h1_match:
        # Check if it's already wrapped in the flex container
        if '<div class="h1-guide-wrapper"' not in content:
            replacement = f"""<div class="h1-guide-wrapper" style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:1rem; margin-bottom:0.75rem;">
          {h1_match.group(1)}style="margin:0; flex:1;" {h1_match.group(2)}{h1_match.group(3)}
          {button_html}
        </div>"""
            # Wait, the h1 tag might already have a style. We can just inject the new flex wrapper around it.
            # It's cleaner to just wrap the original h1 without modifying its inner html:
            better_replacement = f"""<div class="h1-guide-wrapper" style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:1.2rem; margin-bottom:1rem;">
          {h1_match.group(1).replace('>', ' style="margin:0; flex:1;">')}{h1_match.group(2)}{h1_match.group(3)}
          {button_html.strip()}
        </div>"""
            # But the H1 already has `style=""` possibly. It's safer to just let the wrapper impose flex rules.
            # Flex item won't need margin:0 if it's handled by its own class, but let's just do:
            safest_replacement = f"""<div class="h1-guide-wrapper" style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:1rem; margin-bottom:1rem;">
          <div style="flex:1;">{h1_match.group(1)}{h1_match.group(2)}{h1_match.group(3)}</div>
          {button_html.strip()}
        </div>"""

            content = content[:h1_match.start()] + safest_replacement + content[h1_match.end():]

    if original_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

def process_all():
    directories = {'': 'en', 'es': 'es', 'hi': 'hi'}
    for d, lang in directories.items():
        base_path = d if d else '.'
        if not os.path.exists(base_path): continue
        for file in os.listdir(base_path):
            if file.endswith('.html'):
                filepath = os.path.join(base_path, file)
                slug = file[:-5]
                process_file(filepath, lang, slug)

if __name__ == "__main__":
    process_all()
