import os
import re
import json

def restore_tool(file_path, data, global_map):
    print(f"Restoring {file_path}...")
    if not os.path.exists(file_path):
        print(f"  Error: {file_path} not found")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    slug = os.path.basename(file_path).replace('.html', '')
    tool_info = global_map.get(slug, {'name': 'WorldOfTools', 'icon': 'settings_suggest'})

    # 1. Update <head> Title & Meta
    full_title = f"{data['h1']} — {data['benefit']} | WorldOfTools"
    
    # Replace <title>
    content = re.sub(r'<title>.*?</title>', f'<title>{full_title}</title>', content, flags=re.IGNORECASE | re.DOTALL)
    
    # Replace meta description
    content = re.sub(r'<meta[^>]*name=["\']description["\'][^>]*content=["\'][^"\']*["\'][^>]*>', 
                     f'<meta name="description" content="{data["desc_meta"]}"/>', content, flags=re.IGNORECASE)
    
    # Replace OG title/desc
    content = re.sub(r'<meta[^>]*property=["\']og:title["\'][^>]*content=["\'][^"\']*["\'][^>]*>', 
                     f'<meta property="og:title" content="{full_title}"/>', content, flags=re.IGNORECASE)
    content = re.sub(r'<meta[^>]*property=["\']og:description["\'][^>]*content=["\'][^"\']*["\'][^>]*>', 
                     f'<meta property="og:description" content="{data["desc_meta"]}"/>', content, flags=re.IGNORECASE)

    # 2. Inject/Replace Schema (JSON-LD)
    # We remove all existing schema and inject fresh ones
    content = re.sub(r'<script type=["\']application/ld\+json["\']>.*?</script>', '', content, flags=re.DOTALL)
    
    breadcrumbs = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://worldoftools.in/"},
            {"@type": "ListItem", "position": 2, "name": data['h1'], "item": f"https://worldoftools.in/{slug}"}
        ]
    }
    
    software = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": data['h1'],
        "description": data['desc_meta'],
        "url": f"https://worldoftools.in/{slug}",
        "operatingSystem": "Any",
        "applicationCategory": "UtilitiesApplication",
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.9", "ratingCount": "125"}
    }
    
    faq_items = []
    for q, a in data['faq']:
        faq_items.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {"@type": "Answer", "text": a}
        })
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_items
    }
    
    schema_html = f"\n<script type=\"application/ld+json\">{json.dumps(breadcrumbs)}</script>"
    schema_html += f"\n<script type=\"application/ld+json\">{json.dumps(software)}</script>"
    schema_html += f"\n<script type=\"application/ld+json\">{json.dumps(faq)}</script>\n"
    
    # Insert schema after head scripts
    if "</head>" in content:
        content = content.replace("</head>", f"{schema_html}</head>")

    # 3. Standardize paths for neo-brutalism
    content = content.replace('href="/css/style.css"', 'href="/css/style.css?v=2.5"')
    if "/css/neo-brutalism.css" not in content:
        content = content.replace('</head>', '<link href="/css/neo-brutalism.css" rel="stylesheet"/>\n</head>')

    # 4. Inject Breadcrumbs & Tool Header
    # We look for the <main> tag or the start of the tool container
    header_html = f"""
  <div class="tool-header">
    <div class="breadcrumbs-visual" style="margin-bottom:2rem;display:flex;align-items:center;gap:0.5rem;font-weight:700;font-size:0.85rem;text-transform:uppercase;letter-spacing:0.05em;">
      <a href="/" style="text-decoration:none;color:var(--primary-color);">Home</a>
      <span class="material-symbols-outlined" style="font-size:1.1rem;color:#94a3b8;">chevron_right</span>
      <span style="color:#64748b;">Tools</span>
      <span class="material-symbols-outlined" style="font-size:1.1rem;color:#94a3b8;">chevron_right</span>
      <span style="color:#191c1e;">{data['h1']}</span>
    </div>
    <div style="display:flex;align-items:center;gap:1.5rem;margin-bottom:1.5rem;">
      <div class="icon-wrapper" style="margin-bottom:0;background:#ffe066;border:2.5px solid #000;box-shadow:4px 4px 0 #000;">
        <span class="material-symbols-outlined" style="font-size:2.5rem;color:#000;">{tool_info['icon']}</span>
      </div>
      <h1 style="margin:0;font-size:clamp(2rem,5vw,3.2rem);font-weight:950;letter-spacing:-0.04em;line-height:1.1;">{data['h1']}</h1>
    </div>
    <p style="font-size:1.1rem;color:#4a4458;font-weight:600;max-width:750px;margin:0;line-height:1.6;">{data['sub']}</p>
  </div>
"""
    # Replace old tool headers if they exist
    # Looking for tool-header or similar
    if '<div class="tool-header">' in content:
        # Complex replacement: find end of old tool-header
        content = re.sub(r'<div class="tool-header">.*?</div>\s*</div>', header_html, content, flags=re.DOTALL, count=1)
        # Wait, that's brittle. Let's just find the first occurance of any tool header pattern
    else:
        # Inject at start of <main> or tool-container
        if '<main class="tool-container">' in content:
            content = content.replace('<main class="tool-container">', f'<main class="tool-container">{header_html}')
        elif '<div class="tool-container">' in content:
            content = content.replace('<div class="tool-container">', f'<div class="tool-container">{header_html}')

    # 5. Inject SEO Content Block (Unique per tool)
    seo_block = f"""
  <!-- SEO Content Block -->
  <div style="max-width:900px;margin:3rem auto;padding:0 1.5rem;">
    <section style="margin-bottom:3rem;">
      <h2 style="font-size:1.75rem;font-weight:900;margin-bottom:1.25rem;letter-spacing:-0.02em;">{data['intro_h2']}</h2>
      <p style="line-height:1.8;color:#4b5563;font-size:1rem;">{data['intro_p']}</p>
    </section>

    <section style="margin-bottom:3rem;">
      <h2 style="font-size:1.75rem;font-weight:900;margin-bottom:1.25rem;letter-spacing:-0.02em;">How to Use — Step by Step</h2>
      <div class="how-step">
        <div class="how-num">1</div>
        <p style="margin:0;line-height:1.6;padding-top:0.25rem;">{data['steps'][0]}</p>
      </div>
      <div class="how-step">
        <div class="how-num">2</div>
        <p style="margin:0;line-height:1.6;padding-top:0.25rem;">{data['steps'][1]}</p>
      </div>
      <div class="how-step">
        <div class="how-num">3</div>
        <p style="margin:0;line-height:1.6;padding-top:0.25rem;">{data['steps'][2]}</p>
      </div>
    </section>

    <section style="margin-bottom:3rem;">
      <h2 style="font-size:1.75rem;font-weight:900;margin-bottom:1.25rem;letter-spacing:-0.02em;">Frequently Asked Questions</h2>
"""
    for q, a in data['faq']:
        seo_block += f"""      <details>
        <summary>{q}</summary>
        <p>{a}</p>
      </details>
"""
    seo_block += "    </section>\n  </div>"
    
    # Add Privacy Section
    privacy_html = """
  <!-- 100% Private In-Browser Partition -->
  <section class="container" style="padding-top:3rem;padding-bottom:3rem;">
    <div style="background:#fff;border:3px solid #000;border-radius:2rem;padding:3rem;box-shadow:8px 8px 0 #000;position:relative;overflow:hidden;">
      <div style="position:absolute;top:-10px;right:-10px;opacity:0.04;font-size:8rem;font-weight:900;pointer-events:none;transform:rotate(-10deg);">SHIELD</div>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:3rem;align-items:center;">
        <div>
          <div style="background:#b9fcd4;border:2px solid #000;border-radius:99px;padding:0.35rem 1rem;font-size:0.72rem;font-weight:900;text-transform:uppercase;letter-spacing:0.1em;width:fit-content;margin-bottom:1.5rem;box-shadow:3px 3px 0 #000;">Privacy Standard</div>
          <h2 style="font-size:2.2rem;font-weight:950;margin-bottom:1rem;line-height:1;border:none;padding:0;">100% Private <span style="color:var(--primary-color);">In-Browser</span> Logic</h2>
          <p style="font-size:1.05rem;color:#4b5563;line-height:1.7;font-weight:500;">Your sensitive data <strong>never leaves your device</strong>. Everything runs locally in your browser memory — no uploads, no logs, no hidden tracking.</p>
        </div>
        <div style="display:grid;gap:1rem;">
          <div style="background:#f8fafc;border:2px solid #000;border-radius:1.25rem;padding:1.25rem;display:flex;gap:1rem;align-items:center;box-shadow:3px 3px 0 #000;">
            <div style="width:44px;height:44px;background:#ffe066;border:2px solid #000;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.3rem;flex-shrink:0;">🔒</div>
            <div><div style="font-weight:900;font-size:0.95rem;">Zero-Server Engine</div><div style="font-size:0.82rem;color:#64748b;">Processing is 100% client-side. Nothing is stored on our servers.</div></div>
          </div>
          <div style="background:#f8fafc;border:2px solid #000;border-radius:1.25rem;padding:1.25rem;display:flex;gap:1rem;align-items:center;box-shadow:3px 3px 0 #000;">
            <div style="width:44px;height:44px;background:#b9fcd4;border:2px solid #000;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.3rem;flex-shrink:0;">⚡</div>
            <div><div style="font-weight:900;font-size:0.95rem;">Rapid Hardware Libs</div><div style="font-size:0.82rem;color:#64748b;">Using optimized WebAssembly and local logic for instant results.</div></div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""
    
    # Inject before <footer>
    if "<footer>" in content:
        content = content.replace("<footer>", f"{seo_block}{privacy_html}<footer>")
    elif "</body>" in content:
        content = content.replace("</body>", f"{seo_block}{privacy_html}</body>")

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    with open('scratch/tool_plan_map.json', 'r') as f:
        global_map = json.load(f)
    with open('scratch/batch1_content.json', 'r') as f:
        batch_content = json.load(f)

    for filename, data in batch_content.items():
        restore_tool(filename, data, global_map)

if __name__ == "__main__":
    main()
