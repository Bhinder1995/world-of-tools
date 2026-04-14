import os, glob, re

# Files to delete
to_delete = ['link-shortener.html', 'hi/link-shortener.html', 'es/acortador-de-enlaces.html']
for p in to_delete:
    if os.path.exists(p): os.remove(p)

def replace_in_file(f):
    if not os.path.isfile(f): return
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    orig = content
    
    # Remove link-shortener card entirely from index.html and seo tools
    if f == 'index.html' or f.endswith('seo-tools-free.html'):
        content = re.sub(r'<a[^>]*href="/link-shortener(?:\.html)?"[^>]*>.*?</a>', '', content, flags=re.DOTALL)
        content = re.sub(r'<a[^>]*href="/hi/link-shortener(?:\.html)?"[^>]*>.*?</a>', '', content, flags=re.DOTALL)
        content = re.sub(r'<a[^>]*href="/es/acortador-de-enlaces(?:\.html)?"[^>]*>.*?</a>', '', content, flags=re.DOTALL)

    # In other tools (related tools sections)
    content = content.replace('href="/link-shortener"', 'href="/free-url-shortener-online"')
    content = content.replace('href="/link-shortener.html"', 'href="/free-url-shortener-online"')

    if content != orig:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)

for f in glob.glob('*.html') + glob.glob('guides/*.html') + glob.glob('hi/*.html') + glob.glob('es/*.html'):
    replace_in_file(f)

# Update js/common.js
if os.path.exists('js/common.js'):
    with open('js/common.js', 'r', encoding='utf-8') as f:
        js = f.read()
    js = js.replace('"/link-shortener"', '"/free-url-shortener-online"')
    js = js.replace('"link-shortener"', '"free-url-shortener-online"')
    with open('js/common.js', 'w', encoding='utf-8') as f:
        f.write(js)

# Update service-worker.js
if os.path.exists('service-worker.js'):
    with open('service-worker.js', 'r', encoding='utf-8') as f:
        sw = f.read()
    sw = sw.replace("'/link-shortener',", "")
    with open('service-worker.js', 'w', encoding='utf-8') as f:
        f.write(sw)
