import os
from datetime import datetime

def generate_sitemap(base_path, base_url):
    urls = []
    
    # Priority defaults
    priorities = {
        'index.html': '1.0',
        'age-calculator.html': '0.9',
        'word-counter.html': '0.9',
        'gst-calculator.html': '0.9'
    }

    # Static pages
    static_pages = ['about-us', 'contact-us', 'faq', 'privacy', 'terms']

    print("Scanning directories for HTML files...")
    
    # Scan root directory
    for f in os.listdir(base_path):
        if f.endswith('.html') and os.path.isfile(os.path.join(base_path, f)):
            name = f.replace('.html', '')
            # Skip non-indexable files and the guide template
            if name.startswith('guide-template'):
                continue
            url_path = "" if f == "index.html" else name
            is_static = name in static_pages
            priority = priorities.get(f, '0.7' if is_static else '0.8')
            changefreq = 'monthly' if is_static else 'weekly'
            loc = f"{base_url}/" if f == "index.html" else f"{base_url}/{url_path}"
            urls.append({
                'loc': loc,
                'lastmod': datetime.utcnow().strftime('%Y-%m-%d'),
                'changefreq': changefreq,
                'priority': priority
            })

    # Scan guides directory
    guides_dir = os.path.join(base_path, 'guides')
    if os.path.exists(guides_dir):
        for f in sorted(os.listdir(guides_dir)):
            if f.endswith('.html') and os.path.isfile(os.path.join(guides_dir, f)):
                name = f.replace('.html', '')
                # Skip guide-template
                if name == 'guide-template':
                    continue
                url_path = "guides" if name == "index" else f"guides/{name}"
                urls.append({
                    'loc': f"{base_url}/{url_path}",
                    'lastmod': datetime.utcnow().strftime('%Y-%m-%d'),
                    'changefreq': 'monthly',
                    'priority': '0.6'
                })

    # Generate XML
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]
    
    for u in urls:
        xml_lines.append(f"  <url>")
        xml_lines.append(f"    <loc>{u['loc']}</loc>")
        xml_lines.append(f"    <lastmod>{u['lastmod']}</lastmod>")
        xml_lines.append(f"    <changefreq>{u['changefreq']}</changefreq>")
        xml_lines.append(f"    <priority>{u['priority']}</priority>")
        xml_lines.append(f"  </url>")
    
    xml_lines.append('</urlset>')

    output_path = os.path.join(base_path, 'sitemap.xml')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(xml_lines))
        
    print(f"Generated sitemap.xml with {len(urls)} URLs successfully.")

if __name__ == "__main__":
    base_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    site_url = "https://worldoftools.in"
    generate_sitemap(base_dir, site_url)
