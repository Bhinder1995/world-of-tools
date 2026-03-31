import os
import json
import re
from bs4 import BeautifulSoup

def merge_keywords(existing_str, new_list):
    """Merges and deduplicates keywords, preserving original casing for regional languages."""
    if not existing_str:
        return ", ".join(new_list)
    
    existing_list = [k.strip() for k in existing_str.split(',') if k.strip()]
    
    # Use lowercase for deduplication but keep original for the final list
    lower_existing = {k.lower() for k in existing_list}
    
    final_list = existing_list.copy()
    for kw in new_list:
        if kw.lower() not in lower_existing:
            final_list.append(kw)
            lower_existing.add(kw.lower())
    
    return ", ".join(final_list)

def update_file(filepath, entry, is_guide=False, is_regional=False):
    """Updates a single HTML file with SEO metadata and schema."""
    if not os.path.exists(filepath):
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # 1. Update Title
    title_tag = soup.find('title')
    target_title = entry['title']
    if is_guide:
        # Avoid double-appending "Guide" if already there
        if "Guide" not in target_title:
             # Shorten if necessary to stay under 60
             base_title = target_title.split('|')[0].strip()
             if len(base_title + " Guide | WorldOfTools") <= 60:
                 target_title = f"{base_title} Guide | WorldOfTools"
             else:
                 target_title = f"{base_title[:45]} Guide | WorldOfTools"

    if title_tag and not is_regional:
        title_tag.string = target_title
    elif not title_tag and not is_regional:
        new_title = soup.new_tag('title')
        new_title.string = target_title
        if soup.head:
            soup.head.insert(0, new_title)

    # 2. Update Description
    desc_tag = soup.find('meta', attrs={'name': 'description'})
    target_desc = entry['description']
    if is_guide:
        target_desc = f"Complete user guide for {entry['h1']}. " + target_desc
        if len(target_desc) > 155:
            target_desc = target_desc[:152] + "..."

    if desc_tag and not is_regional:
        desc_tag['content'] = target_desc
    elif not desc_tag and not is_regional:
        new_desc = soup.new_tag('meta', attrs={'name': 'description', 'content': target_desc})
        if soup.head:
            soup.head.append(new_desc)

    # 3. Update H1
    h1_tag = soup.find('h1')
    target_h1 = entry['h1']
    if is_guide:
        target_h1 = f"{target_h1} — Step-by-Step Guide"

    if h1_tag and not is_regional:
        h1_tag.string = target_h1

    # 4. Update Keywords (Merge)
    kw_tag = soup.find('meta', attrs={'name': 'keywords'})
    new_kws = entry['keywords']
    if is_guide:
        new_kws = new_kws + ["guide", "tutorial", "how to"]
    
    if kw_tag:
        kw_tag['content'] = merge_keywords(kw_tag.get('content', ''), new_kws)
    else:
        new_kw_tag = soup.new_tag('meta', attrs={'name': 'keywords', 'content': ", ".join(new_kws)})
        if soup.head:
            soup.head.append(new_kw_tag)

    # 5. Schema Injection (Tools)
    if not is_guide and not is_regional:
        # Check for existing WebApplication or SoftwareApplication
        existing_scripts = soup.find_all('script', type='application/ld+json')
        has_app_schema = False
        for script in existing_scripts:
            if '"@type": "WebApplication"' in script.string or '"@type": "SoftwareApplication"' in script.string:
                has_app_schema = True
                break
        
        if not has_app_schema:
            schema_data = {
                "@context": "https://schema.org",
                "@type": "WebApplication",
                "name": entry['title'].split('|')[0].strip(),
                "description": entry['description'],
                "url": "https://worldoftools.in" + entry.get('url', ''),
                "applicationCategory": "UtilitiesApplication",
                "operatingSystem": "Any"
            }
            script_tag = soup.new_tag('script', type='application/ld+json')
            script_tag.string = json.dumps(schema_data, indent=2)
            if soup.head:
                soup.head.append(script_tag)

    # 6. Canonical Tag
    canonical = soup.find('link', rel='canonical')
    if not canonical:
        new_canonical = soup.new_tag('link', rel='canonical', href="https://worldoftools.in" + filepath.replace('\\', '/').replace('c:/Users/HP/Desktop/Projects Folder/world_of_tools', '').replace('.html', ''))
        if soup.head:
            soup.head.append(new_canonical)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(soup.prettify())
    
    return True

def main():
    with open('seo_mapping.json', 'r', encoding='utf-8') as f:
        mapping = json.load(f)

    base_path = r'c:\Users\HP\Desktop\Projects Folder\world_of_tools'
    guides_path = os.path.join(base_path, 'guides')

    stats = {'tools': 0, 'guides': 0, 'regional': 0, 'missing': 0}

    for url, entry in mapping.items():
        entry['url'] = url
        # 1. Determine tool filename
        if url == '/':
            tool_filename = 'index.html'
        else:
            tool_filename = url.lstrip('/') + '.html'
        
        tool_path = os.path.join(base_path, tool_filename)
        
        if update_file(tool_path, entry):
            stats['tools'] += 1
            print(f"Updated Tool: {tool_filename}")
        else:
            stats['missing'] += 1
            print(f"Missing Tool: {tool_filename}")

        # 2. Check for Guides
        # Default guide: tool-name-guide.html
        base_name = url.lstrip('/').replace('.html', '')
        if not base_name: continue # Skip root

        potential_guide = f"{base_name}-guide.html"
        guide_path = os.path.join(guides_path, potential_guide)
        
        if update_file(guide_path, entry, is_guide=True):
            stats['guides'] += 1
            print(f"Updated Guide: {potential_guide}")
        
        # 3. Check for Regional Guides (matching base_name)
        # e.g., gst-calculator-telugu-guide.html
        if os.path.exists(guides_path):
            for file in os.listdir(guides_path):
                if base_name in file and ('-hindi-' in file or '-telugu-' in file or '-bengali-' in file or '-marathi-' in file or '-tamil-' in file):
                    reg_path = os.path.join(guides_path, file)
                    if update_file(reg_path, entry, is_guide=True, is_regional=True):
                        stats['regional'] += 1
                        print(f"Updated Regional Guide: {file}")

    print("\n--- Final Stats ---")
    print(f"Tools Updated: {stats['tools']}")
    print(f"Guides Updated: {stats['guides']}")
    print(f"Regional Guides Updated: {stats['regional']}")
    print(f"Missing Files: {stats['missing']}")

if __name__ == "__main__":
    main()
