import os
import re

def ultimate_fix():
    root_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    
    # Precise byte-level repairs for the garbled emojis
    # These are common "UTF8-as-Latin1" artifacts
    byte_reps = {
        b'\xc3\xa2\xc2\x9c\xc2\xa8': '✨'.encode('utf-8'),
        b'\xc3\xa2\xc2\x9c\xc2\xb3': '✓'.encode('utf-8'),
        b'\xc3\xb0\xc2\x9f\xc2\x9a\xc2\x80': '🚀'.encode('utf-8'),
        b'\xc3\xb0\xc2\x9f\xc2\x95\xc2\x92': '🕒'.encode('utf-8'),
        b'\xc3\xb0\xc2\x9f\xc2\x9b\xc2\xa1': '🛡️'.encode('utf-8'),
        b'\xc3\xb0\xc2\x9f\xc2\x93\xc2\xa0': '🔍'.encode('utf-8'),
        b'\xc3\xb0\xc2\x9f\xc2\x93\xc2\xb9': '📹'.encode('utf-8'),
        b'\xc3\xb0\xc2\x9f\xc2\x93\xc2\x8a': '📊'.encode('utf-8'),
        b'\xc3\xb0\xc2\x9f\xc2\x92\xc2\xa1': '💡'.encode('utf-8'),
        b'\xc3\xb0\xc2\x9f\xc2\x8e\xc2\x93': '🎓'.encode('utf-8'),
        b'\xc3\xb0\xc2\x9f\xc2\x9b\xc2\xa0': '🛠️'.encode('utf-8'),
        b'\xc3\xa2\xc2\x80\xc2\x94': '—'.encode('utf-8')
    }

    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root: continue
        for file in files:
            if file.endswith(".html"):
                p = os.path.join(root, file)
                try:
                    with open(p, "rb") as f:
                        data = f.read()
                    
                    # Apply byte-level emoji fixes
                    for bad, good in byte_reps.items():
                        data = data.replace(bad, good)
                    
                    # Decode to clean up strings
                    content = data.decode('utf-8', errors='ignore')
                    
                    # Remove multiple extra newlines
                    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
                    
                    # Style updates: Site-wide 3px borders for Brutalist
                    content = content.replace("border: 2px solid", "border: 3px solid")
                    content = content.replace("border: 1px solid", "border: 3px solid")
                    
                    # Remove all instances of the notebook background
                    content = re.sub(r'background-image:\s*linear-gradient\([^;]+\);?', '', content)
                    content = re.sub(r'background-size:\s*30px 30px;?', '', content)
                    content = re.sub(r'background-size:\s*100% 25px;?', '', content)

                    # Ensure common.js in head with defer (BEST practice for injection)
                    js_tag = '<script src="/js/common.js" defer></script>'
                    if js_tag not in content:
                        # Remove existing common.js if any at end
                        content = content.replace('<script src="/js/common.js"></script>', '')
                        content = content.replace('</head>', f'  {js_tag}\n</head>')

                    # Ensure header and footer containers are correctly structured
                    if '<header>' not in content and '<header ' not in content:
                        content = content.replace('<body>', '<body>\n<header></header>')
                    if '<footer>' not in content and '<footer ' not in content:
                        if '</body>' in content:
                            content = content.replace('</body>', '<footer></footer>\n</body>')

                    with open(p, "w", encoding="utf-8") as f:
                        f.write(content)
                except Exception as e:
                    print(f"Error processing {p}: {e}")

    # Fix CSS too
    css_p = os.path.join(root_dir, "css", "style.css")
    with open(css_p, "r", encoding="utf-8") as f:
        css = f.read()
    css = re.sub(r'background-image:\s*linear-gradient\([^;]+\);?', '', css)
    css = re.sub(r'\n\s*\n\s*\n+', '\n\n', css)
    with open(css_p, "w", encoding="utf-8") as f:
        f.write(css)

    print("Ultimate Retro Neo-Brutalist fix applied.")

if __name__ == "__main__":
    ultimate_fix()
