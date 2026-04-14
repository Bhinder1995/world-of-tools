import os
import json
import re
from bs4 import BeautifulSoup

def audit_seo(directory):
    results = {}
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    
    for filename in html_files:
        path = os.path.join(directory, filename)
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                soup = BeautifulSoup(content, 'html.parser')
                
                # SEO Tags
                title = soup.title.string.strip() if soup.title and soup.title.string else None
                desc = soup.find('meta', attrs={'name': 'description'})
                desc_content = desc['content'] if desc else None
                canonical = soup.find('link', attrs={'rel': 'canonical'})
                canonical_href = canonical['href'] if canonical else None
                
                # OG Tags
                og_title = soup.find('meta', attrs={'property': 'og:title'})
                og_desc = soup.find('meta', attrs={'property': 'og:description'})
                og_image = soup.find('meta', attrs={'property': 'og:image'})
                
                # Twitter Tags
                twitter_card = soup.find('meta', attrs={'name': 'twitter:card'})
                
                # Schema
                schema_tags = soup.find_all('script', attrs={'type': 'application/ld+json'})
                schemas = []
                for s in schema_tags:
                    if s.string:
                        try:
                            schemas.append(json.loads(s.string))
                        except:
                            pass
                
                schema_types = []
                for s in schemas:
                    if isinstance(s, dict):
                        schema_types.append(s.get('@type'))
                    elif isinstance(s, list):
                        for item in s:
                            if isinstance(item, dict):
                                schema_types.append(item.get('@type'))
                
                # UI/Technical
                h1s = soup.find_all('h1')
                h1_count = len(h1s)
                
                results[filename] = {
                    'title': title,
                    'description': bool(desc_content),
                    'canonical': bool(canonical_href),
                    'og_tags': bool(og_title and og_desc),
                    'twitter_tags': bool(twitter_card),
                    'schema_types': sorted(list(set(filter(None, schema_types)))),
                    'h1_count': h1_count,
                    'trust_block': 'Privacy & Precision' in content
                }
        except Exception as e:
            print(f"Error auditing {filename}: {e}")

    return results

if __name__ == "__main__":
    base_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    audit_data = audit_seo(base_dir)
    
    with open('deep_audit_results.json', 'w') as out:
        json.dump(audit_data, out, indent=2)
    
    print(f"Audit completed for {len(audit_data)} files.")
