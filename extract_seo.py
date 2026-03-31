import re
import json
import os

def extract_seo_data():
    report_path = 'worldoftools-seo-master-report-v2.html'
    if not os.path.exists(report_path):
        print(f"File {report_path} not found.")
        return

    with open(report_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract rows
    rows = re.findall(r'<tr.*?>(.*?)</tr>', content, re.DOTALL)
    data = {}

    for row in rows:
        if '<code>' not in row:
            continue
        
        url_match = re.search(r'<code>(.*?)</code>', row)
        if not url_match:
            continue
        url = url_match.group(1).strip()
        
        # Extract Title (look for the exact class to be safe)
        title_match = re.search(r'<td class="meta-title">(.*?)(?=<span|</td>)', row, re.DOTALL)
        if not title_match:
             # Try a more generic match for categories
             title_match = re.search(r'<td>(.*?)</td>', row, re.DOTALL) # This is usually the tool name, need to skip it
             tds = re.findall(r'<td.*?>(.*?)</td>', row, re.DOTALL)
             if len(tds) >= 2:
                 title = tds[1].strip()
             else:
                 title = ''
        else:
            title = title_match.group(1).strip()
            
        title = re.sub(r'\s+', ' ', title).replace('&amp;', '&').replace('&quot;', '"')
        
        # Extract H1
        h1_match = re.search(r'<td class="h1-text">(.*?)</td>', row, re.DOTALL)
        if h1_match:
            h1 = h1_match.group(1).strip()
        else:
            # Fallback for categories
            tds = re.findall(r'<td.*?>(.*?)</td>', row, re.DOTALL)
            if len(tds) >= 3:
                h1 = tds[2].strip()
            else:
                h1 = ''
        h1 = re.sub(r'\s+', ' ', h1).replace('&amp;', '&').replace('&quot;', '"')
        
        # Extract Description
        desc_match = re.search(r'<td class="meta-desc">(.*?)(?=<span|</td>)', row, re.DOTALL)
        if desc_match:
            desc = desc_match.group(1).strip()
        else:
             # Fallback for categories
            tds = re.findall(r'<td.*?>(.*?)</td>', row, re.DOTALL)
            if len(tds) >= 4:
                desc = tds[3].strip()
            else:
                desc = ''
        desc = re.sub(r'\s+', ' ', desc).replace('&amp;', '&').replace('&quot;', '"')
        
        # Extract Keywords
        kw_match = re.search(r'<td class="kw">(.*?)</td>', row, re.DOTALL)
        if kw_match:
            kw_raw = kw_match.group(1).strip()
        else:
             # Fallback for categories
            tds = re.findall(r'<td.*?>(.*?)</td>', row, re.DOTALL)
            if len(tds) >= 5:
                kw_raw = tds[4].strip()
            else:
                kw_raw = ''
        
        keywords = [k.strip() for k in re.split(r'<br\s*/?>', kw_raw, flags=re.IGNORECASE) if k.strip()]
        
        data[url] = {
            'title': title,
            'h1': h1,
            'description': desc,
            'keywords': keywords
        }

    with open('seo_mapping.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f'Extracted {len(data)} entries.')

if __name__ == "__main__":
    extract_seo_data()
