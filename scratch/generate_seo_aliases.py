import os
import json
import xml.etree.ElementTree as ET
from datetime import datetime

# Rule engine to create sensible organic SEO aliases
def generate_aliases(slug):
    aliases = []
    
    if "calculator" in slug:
        topic = slug.replace("-calculator", "")
        aliases.append(f"online-{topic}-calculator")
        aliases.append(f"free-{slug}")
    elif "generator" in slug:
        topic = slug.replace("-generator", "")
        aliases.append(f"free-{topic}-generator")
        aliases.append(f"create-{topic}-online")
    elif "converter" in slug:
        # e.g., unit-converter -> online-unit-converter
        aliases.append(f"online-{slug}")
        aliases.append(f"fast-{slug}")
    elif "formatter" in slug:
        topic = slug.replace("-formatter", "")
        aliases.append(f"format-{topic}-online")
        aliases.append(f"free-{slug}")
    else:
        # Generic tool fallback
        aliases.append(f"free-{slug}-online")
        aliases.append(f"best-{slug}")

    # A few highly specific manual overrides for max traffic terms
    manual_overrides = {
        "age-calculator": ["exact-age-calculator", "date-of-birth-calculator"],
        "emi-calculator": ["home-loan-emi-calculator", "personal-loan-emi-calculator"],
        "gst-calculator": ["india-gst-calculator", "calculate-gst-online"],
        "free-url-shortener-online": ["link-shortener-free", "url-shortener-no-signup"],
        "qr-code-generator": ["create-qr-code-free", "custom-qr-generator"],
        "json-formatter": ["json-beautifier-online", "json-validator-tool"],
        "password-generator": ["strong-password-creator", "secure-password-generator"],
        "image-compressor": ["compress-image-size", "reduce-image-size-online"],
        "background-remover": ["remove-bg-online", "free-background-eraser"],
        "typing-speed-test": ["wpm-typing-test", "type-speed-calculator"],
        "word-counter": ["character-count-tool", "online-word-counter"]
    }
    
    if slug in manual_overrides:
        return manual_overrides[slug]
        
    return aliases

def main():
    root_dir = "."
    tools = []
    
    # 1. Identify all core HTML files in the root directory (excluding exceptions)
    ignore_files = ['404.html', 'index.html', 'guide-template.html']
    category_indexes = ['calculators-online.html', 'image-tools-online.html', 
                        'developer-tools-online.html', 'text-content-tools-online.html', 
                        'web-utilities-free.html']
                        
    for f in os.listdir(root_dir):
        if f.endswith(".html") and f not in ignore_files:
            slug = f.replace(".html", "")
            if f not in category_indexes:
                tools.append(slug)

    # 2. Build the rewrites for vercel.json
    rewrites = []
    seo_routes = []
    
    for tool in tools:
        aliases = generate_aliases(tool)
        for alias in aliases:
            seo_routes.append(alias)
            rewrites.append({
                "source": f"/{alias}",
                "destination": f"/{tool}"
            })

    # Update vercel.json
    with open("vercel.json", "r", encoding='utf-8') as f:
        vercel_config = json.load(f)
        
    # Overwrite the rewrites (or extend them if they exist but let's just assert our control)
    # Actually, we shouldn't wipe custom rewrites if there are any crucial ones.
    # Let's check what's currently in there
    existing_rewrites = vercel_config.get("rewrites", [])
    
    # Filter out our previous auto-generated ones if we ever ran this, but keep the ones missing from ours
    # Let's just create a new list for SEO and prepend it to any existing rewrites that aren't touching tools
    final_rewrites = []
    existing_sources = set([ r["source"] for r in rewrites ])
    for er in existing_rewrites:
        if er["source"] not in existing_sources:
            # We assume anything not currently in our alias map is a custom one the user had
            final_rewrites.append(er)
            
    # Append all our new SEO rewrites
    final_rewrites.extend(rewrites)
    vercel_config["rewrites"] = final_rewrites

    with open("vercel.json", "w", encoding='utf-8') as f:
        json.dump(vercel_config, f, indent=4)
        
    print(f"Updated vercel.json with {len(rewrites)} SEO rewrites.")

    # 3. Compile Unified sitemap.xml
    # Priorities: 
    #   Home/Categories/Tools -> 1.0 / 0.9, daily
    #   SEO Aliases -> 0.8, daily
    #   Guides -> 0.8, weekly
    #   Locales -> 0.8, weekly

    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    date_str = datetime.now().strftime("%Y-%m-%d")

    def add_url(path, priority, freq):
        url = ET.SubElement(urlset, "url")
        ET.SubElement(url, "loc").text = f"https://www.worldoftools.in{path}"
        ET.SubElement(url, "lastmod").text = date_str
        ET.SubElement(url, "changefreq").text = freq
        ET.SubElement(url, "priority").text = priority

    # Root
    add_url("/", "1.0", "daily")
    for category in category_indexes:
        add_url(f"/{category.replace('.html','')}", "0.9", "daily")

    # Base Tools
    for slug in tools:
        add_url(f"/{slug}", "0.9", "daily")
        
    # SEO Aliases
    for alias in seo_routes:
        add_url(f"/{alias}", "0.8", "daily")

    # Guides
    if os.path.exists("guides"):
        for g in os.listdir("guides"):
            if g.endswith(".html") and g != "guide-template.html":
                add_url(f"/guides/{g.replace('.html','')}", "0.8", "weekly")

    # Locales (Spanish and Hindi)
    for lang in ['es', 'hi']:
        if os.path.exists(lang):
            # Index
            add_url(f"/{lang}/", "0.8", "weekly")
            for lc in category_indexes:
                add_url(f"/{lang}/{lc.replace('.html','')}", "0.7", "weekly")
            for f in os.listdir(lang):
                if f.endswith(".html") and f not in ignore_files and f not in category_indexes:
                    add_url(f"/{lang}/{f.replace('.html','')}", "0.7", "weekly")

    # Write out sitemap
    tree = ET.ElementTree(urlset)
    # Simple pretty print using a temporary string
    xml_str = ET.tostring(urlset, encoding='utf-8', xml_declaration=True).decode('utf-8')
    # Adding line breaks
    xml_str = xml_str.replace("><url>", ">\\n  <url>")
    xml_str = xml_str.replace("</urlset>", "\\n</urlset>")
    xml_str = xml_str.replace("</url>", "</url>\\n")
    
    # Just use dom minidom for clean formatting
    import xml.dom.minidom
    xml_dom = xml.dom.minidom.parseString(ET.tostring(urlset, encoding='utf-8'))
    pretty_xml = xml_dom.toprettyxml(indent="  ")
    # minidom adds empty lines sometimes, clean it
    pretty_xml = os.linesep.join([s for s in pretty_xml.splitlines() if s.strip()])

    with open("sitemap.xml", "w", encoding='utf-8') as f:
        f.write(pretty_xml)
        
    print(f"Generated unified sitemap.xml with {len(urlset)} total routes.")

if __name__ == "__main__":
    main()
