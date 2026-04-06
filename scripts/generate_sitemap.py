import os
import json
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

    print("Scanning directories for HTML files...")
    
    # Scan root directory
    for f in os.listdir(base_path):
        if f.endswith('.html') and os.path.isfile(os.path.join(base_path, f)):
            url_path = "" if f == "index.html" else f.replace('.html', '')
            priority = priorities.get(f, '0.8')
            urls.append({
                'loc': f"{base_url}/{url_path}".rstrip('/'),
                'lastmod': datetime.utcnow().strftime('%Y-%m-%d'),
                'changefreq': 'weekly',
                'priority': priority
            })

    # Scan guides directory
    guides_dir = os.path.join(base_path, 'guides')
    if os.path.exists(guides_dir):
        for f in os.listdir(guides_dir):
            if f.endswith('.html') and os.path.isfile(os.path.join(guides_dir, f)):
                url_path = f"guides/{f.replace('.html', '')}"
                urls.append({
                    'loc': f"{base_url}/{url_path}",
                    'lastmod': datetime.utcnow().strftime('%Y-%m-%d'),
                    'changefreq': 'monthly',
                    'priority': '0.6'
                })

    # Read Vercel.json for programmatic SEO routes
    vercel_path = os.path.join(base_path, 'vercel.json')
    if os.path.exists(vercel_path):
        with open(vercel_path, 'r', encoding='utf-8') as vf:
            vercel_data = json.load(vf)
            rewrites = vercel_data.get('rewrites', [])
            for r in rewrites:
                source = r.get('source', '')
                # Ignore dynamic routes or workers
                if ':' not in source and not source.startswith('/go'):
                    # Source already has a leading slash
                    full_loc = f"{base_url}{source}"
                    urls.append({
                        'loc': full_loc,
                        'lastmod': datetime.utcnow().strftime('%Y-%m-%d'),
                        'changefreq': 'monthly',
                        'priority': '0.7'
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
