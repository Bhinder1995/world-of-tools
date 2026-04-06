import os
import json
from bs4 import BeautifulSoup

def update_tool_file(filepath, entry):
    if not os.path.exists(filepath):
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')
    filename = entry['filename']
    url_slug = filename.replace('.html', '')

    # --- 1. HEAD INJECTIONS (Canonical & Schemas) ---
    
    # 1A. Canonical
    canonical = soup.find('link', rel='canonical')
    if not canonical:
        new_canonical = soup.new_tag('link', rel='canonical', href=f"https://worldoftools.in/{url_slug}")
        if soup.head:
            soup.head.append(new_canonical)

    # 1B. Remove old SoftwareApplication/WebApplication to avoid duplicates
    for script in soup.find_all('script', type='application/ld+json'):
        if '"@type": "SoftwareApplication"' in script.string or '"@type": "WebApplication"' in script.string or '"@type": "FAQPage"' in script.string or '"@type": "BreadcrumbList"' in script.string:
            script.decompose()

    # 1C. Breadcrumb Schema
    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [{
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://worldoftools.in/"
        },{
            "@type": "ListItem",
            "position": 2,
            "name": entry['name'],
            "item": f"https://worldoftools.in/{url_slug}"
        }]
    }
    b_script = soup.new_tag('script', type='application/ld+json')
    b_script.string = json.dumps(breadcrumb_schema, indent=2)
    if soup.head:
        soup.head.append(b_script)

    # 1D. FAQ Schema
    if entry.get('faq') and len(entry['faq']) > 0:
        faq_schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": []
        }
        for q in entry['faq']:
            faq_schema["mainEntity"].append({
                "@type": "Question",
                "name": q['question'],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": q['answer']
                }
            })
        f_script = soup.new_tag('script', type='application/ld+json')
        f_script.string = json.dumps(faq_schema, indent=2)
        if soup.head:
            soup.head.append(f_script)

    # 1E. SoftwareApplication Schema with AggregateRating
    app_schema = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": entry['name'],
        "operatingSystem": "Any",
        "applicationCategory": "UtilitiesApplication",
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "USD"
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.9",
            "ratingCount": "125"
        }
    }
    a_script = soup.new_tag('script', type='application/ld+json')
    a_script.string = json.dumps(app_schema, indent=2)
    if soup.head:
        soup.head.append(a_script)

    # --- 2. BODY INJECTIONS ---

    # 2A. Visual Breadcrumbs
    header = soup.find('section', class_='tool-header')
    if header:
        # Check if breadcrumbs already exist
        existing_bc = header.find('div', class_='breadcrumbs-visual')
        if not existing_bc:
            bc_div = soup.new_tag('div', attrs={'class': 'breadcrumbs-visual'})
            bc_div['style'] = "font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1rem; font-weight: 600;"
            
            a_home = soup.new_tag('a', href='/')
            a_home['style'] = "color: var(--primary-color); text-decoration: none;"
            a_home.string = "Home"
            
            bc_div.append(a_home)
            bc_div.append(" > Tools > ")
            
            span_name = soup.new_tag('span')
            span_name.string = entry['name']
            bc_div.append(span_name)
            
            # Insert before h1
            h1 = header.find('h1')
            if h1:
                h1.insert_before(bc_div)

    # 2B. Content Wrapper (if missing)
    main_tag = soup.find('main')
    if main_tag:
        # Check if we already have the SEO content block
        existing_content = str(main_tag)
        if '<!-- SEO Content Block -->' not in existing_content and entry.get('how_it_works'):
            
            seo_block = soup.new_tag('div')
            seo_block['style'] = "max-width:900px;margin:3rem auto;padding:0 1.5rem;"
            
            html_parts = ["\n<!-- SEO Content Block -->\n"]
            
            # Features
            if entry.get('features'):
                html_parts.append('<section style="margin-bottom:3rem;">')
                html_parts.append(f'<h2 style="font-size:1.75rem;font-weight:800;margin-bottom:1.25rem;letter-spacing:-0.02em;">Key Features of {entry["name"]}</h2>')
                html_parts.append('<ul style="list-style:none;padding:0;margin:0;">')
                for feat in entry['features']:
                    html_parts.append(f'<li style="display:flex;align-items:flex-start;gap:0.6rem;margin-bottom:0.8rem;"><span style="color:#10b981;font-weight:bold;flex-shrink:0;">✓</span><span style="line-height:1.6;"><strong>{feat["title"]}:</strong> {feat["desc"]}</span></li>')
                html_parts.append('</ul></section>')
                
            # How it works
            if entry.get('how_it_works'):
                html_parts.append('<section style="margin-bottom:3rem;">')
                html_parts.append(f'<h2 style="font-size:1.75rem;font-weight:800;margin-bottom:1.25rem;letter-spacing:-0.02em;">How Does {entry["name"]} Work?</h2>')
                html_parts.append(f'<div style="line-height:1.8;color:#4b5563;">{entry["how_it_works"]}</div>')
                html_parts.append('</section>')
                
            # Steps
            if entry.get('steps'):
                html_parts.append('<section style="margin-bottom:3rem;">')
                html_parts.append(f'<h2 style="font-size:1.75rem;font-weight:800;margin-bottom:1.25rem;letter-spacing:-0.02em;">How to Use {entry["name"]} \u2014 Step-by-Step</h2>')
                for i, step in enumerate(entry['steps']):
                    html_parts.append(f'<div style="display:flex;align-items:flex-start;gap:1rem;background:#f8f9ff;border:1px solid #e5e7eb;border-radius:12px;padding:1rem 1.25rem;margin-bottom:0.5rem;"><span style="min-width:32px;height:32px;background:#4f46e5;color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:0.9rem;flex-shrink:0;">{i+1}</span><p style="margin:0;line-height:1.6;padding-top:0.3rem;">{step}</p></div>')
                html_parts.append('</section>')

            # FAQs
            if entry.get('faq'):
                html_parts.append('<section style="margin-bottom:3rem;">')
                html_parts.append('<h2 style="font-size:1.75rem;font-weight:800;margin-bottom:1.25rem;letter-spacing:-0.02em;">Frequently Asked Questions</h2>')
                for faq in entry['faq']:
                    html_parts.append(f'<details style="border:1px solid #e5e7eb;border-radius:12px;padding:1rem 1.25rem;margin-bottom:0.5rem;"><summary style="font-weight:700;cursor:pointer;">{faq["question"]}</summary><p style="margin:0.75rem 0 0;color:#6b7280;line-height:1.6;">{faq["answer"]}</p></details>')
                html_parts.append('</section>')
                
            # Conclusion
            if entry.get('conclusion'):
                html_parts.append('<section style="margin-bottom:3rem;">')
                html_parts.append('<h2 style="font-size:1.75rem;font-weight:800;margin-bottom:1.25rem;letter-spacing:-0.02em;">Final Thoughts</h2>')
                html_parts.append(f'<div style="line-height:1.8;color:#4b5563;">{entry["conclusion"]}</div>')
                html_parts.append('</section>')

            # Append the raw html parts
            parsed_block = BeautifulSoup("".join(html_parts), 'html.parser')
            seo_block.append(parsed_block)
            main_tag.append(seo_block)

    with open(filepath, 'w', encoding='utf-8') as f:
        # Use str(soup) instead of prettify to avoid messing up inline formatting
        f.write(str(soup))
    
    return True

def main():
    with open('seo_content_batch2.json', 'r', encoding='utf-8') as f:
        mapping = json.load(f)

    base_path = r'c:\Users\HP\Desktop\Projects Folder\world_of_tools'
    count = 0

    # Only dealing with the tools listed in seo_content.json
    for key, entry in mapping.items():
        if key == 'index.html':
            continue  # skip homepage for now
            
        filepath = os.path.join(base_path, entry['filename'])
        if update_tool_file(filepath, entry):
            count += 1
            print(f"Updated: {entry['filename']}")
        else:
            print(f"Missing: {entry['filename']}")
            
    print(f"Total tools updated: {count}")

if __name__ == "__main__":
    main()
