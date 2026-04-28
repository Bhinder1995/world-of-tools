import os
import re
import json

def get_meta(content, tag_name):
    match = re.search(f'<meta [^>]*name="{tag_name}" [^>]*content="([^"]*)"', content, re.I)
    if not match:
        match = re.search(f'<meta [^>]*content="([^"]*)" [^>]*name="{tag_name}"', content, re.I)
    return match.group(1) if match else ""

def get_title(content):
    match = re.search(r'<title>(.*?)</title>', content, re.I | re.S)
    return match.group(1).strip() if match else ""

def get_faqs(content):
    # Regex to find <details><summary>Q</summary><p>A</p></details>
    # Note: This is a bit simplified but should work for the current site structure
    faq_matches = re.findall(r'<details\s*[^>]*>\s*<summary\s*[^>]*>(.*?)</summary>\s*<p\s*[^>]*>(.*?)</p>\s*</details>', content, re.I | re.S)
    
    if not faq_matches:
        return None
        
    faq_items = []
    for q, a in faq_matches:
        q_clean = re.sub('<[^>]*>', '', q).strip()
        a_clean = re.sub('<[^>]*>', '', a).strip()
        faq_items.append({
            "@type": "Question",
            "name": q_clean,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a_clean
            }
        })
    
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": faq_items
    }

def get_breadcrumbs(content, file_url):
    # Extract data attributes from <main>
    # <main class="container" data-category-name="Calculators Online" data-category-url="/calculators-online" data-tool-name="Age Calculator">
    main_match = re.search(r'<main[^>]*data-category-name="([^"]*)"[^>]*data-category-url="([^"]*)"[^>]*data-tool-name="([^"]*)"', content)
    
    items = [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://worldoftools.in/"
        }
    ]
    
    if main_match:
        cat_name = main_match.group(1)
        cat_url = main_match.group(2)
        tool_name = main_match.group(3)
        
        items.append({
            "@type": "ListItem",
            "position": 2,
            "name": cat_name,
            "item": f"https://worldoftools.in{cat_url}"
        })
        items.append({
            "@type": "ListItem",
            "position": 3,
            "name": tool_name,
            "item": file_url
        })
    else:
        # Fallback to simple breadcrumb if data attributes missing
        title = get_title(content).split('|')[0].strip()
        items.append({
            "@type": "ListItem",
            "position": 2,
            "name": title,
            "item": file_url
        })
        
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items
    }

def inject_enhanced_schema():
    base_path = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    
    skip_root = [
        "index.html", "404.html", "privacy.html", "terms.html", "faq.html", 
        "about-us.html", "contact-us.html", "web-utilities-free.html",
        "calculators-online.html", "developer-tools-online.html", "seo-tools-free.html",
        "text-tools-online.html", "image-tools.html", "security-tools.html",
        "design-tools.html", "india-tools.html"
    ]

    # Process all files
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if not file.endswith(".html"):
                continue
                
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, base_path).replace('\\', '/')
            
            # Identify if it's a tool or a guide
            is_guide = "guides/" in rel_path
            is_root_tool = root == base_path and file not in skip_root
            
            if not (is_guide or is_root_tool) or file == "index.html":
                continue

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Remove existing custom JSON-LD blocks to avoid duplicates/mess
            # (Only those injected by our previous script which have certain markers or are SoftwareApplication/Article)
            content = re.sub(r'\n<script type="application/ld\+json">\n{\s*"@context": "https://schema\.org",\s*"@type": "(SoftwareApplication|Article|FAQPage|BreadcrumbList)".*?\n</script>\n', '', content, flags=re.S)
            
            # Start fresh array of schemas
            schemas = []
            
            file_url = f"https://worldoftools.in/{rel_path.replace('.html', '')}"
            if file_url.endswith("/index"): file_url = file_url[:-5]
            
            # 1. SoftwareApplication or Article
            title = get_title(content).split('|')[0].strip()
            desc = get_meta(content, "description")
            
            if is_root_tool:
                schemas.append({
                    "@context": "https://schema.org",
                    "@type": "SoftwareApplication",
                    "name": title,
                    "operatingSystem": "Any",
                    "applicationCategory": "UtilitiesApplication",
                    "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
                    "description": desc,
                    "url": file_url
                })
            elif is_guide:
                schemas.append({
                    "@context": "https://schema.org",
                    "@type": "Article",
                    "headline": title,
                    "description": desc,
                    "url": file_url,
                    "author": {"@type": "Organization", "name": "WorldOfTools"},
                    "publisher": {
                        "@type": "Organization",
                        "name": "WorldOfTools",
                        "logo": {"@type": "ImageObject", "url": "https://worldoftools.in/logo.svg"}
                    }
                })

            # 2. FAQ Schema
            faq_schema = get_faqs(content)
            if faq_schema:
                schemas.append(faq_schema)
                
            # 3. Breadcrumb Schema
            schemas.append(get_breadcrumbs(content, file_url))
            
            # Inject
            schema_html = f'\n<script type="application/ld+json">\n{json.dumps(schemas, indent=2)}\n</script>\n'
            new_content = content.replace("</head>", f"{schema_html}</head>")
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Injected enhanced schemas into {rel_path}")

if __name__ == "__main__":
    inject_enhanced_schema()
