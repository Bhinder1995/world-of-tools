import os
import re

def ultimate_repair():
    root_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    
    # 1. PRECISE REPAIR MAPPING (Corrupted UTF-8 seen in browser)
    reps = {
        "Ã¢Å“Â¨": "✨",
        "Ã¢Å“â€œ": "✓",
        "Ã°Å¸â€ Â ": "🔍",
        "Ã°Å¸Å¡â‚¬": "🚀",
        "Ã°Å¸â€¢â€™": "🕒",
        "Ã°Å¸â€˜â€": "👔",
        "Ã°Å¸â€Â ": "🔠",
        "Ã°Å¸â€œÂ ": "📍",
        "Ã°Å¸Å½â€š": "🎂",
        "Ã°Å¸â€œÂ¹": "📹",
        "Ã°Å¸â€ºÂ¡ï¸": "🛡️",
        "Ã¢â‚¬â€": "—",
        "Â—": "—",
        "Ã¢Å“â€ ": "✓"
    }

    # 2. PROCESSS ALL HTML FILES
    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root: continue
        for file in files:
            if file.endswith(".html"):
                p = os.path.join(root, file)
                try:
                    # Read as bytes to avoid encoding issues initially, then decode
                    with open(p, "rb") as f:
                        data = f.read()
                    
                    content = data.decode('utf-8', errors='ignore')
                    
                    # Normalization: Remove excessive empty lines (more than 2 together)
                    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
                    
                    # Remove ALL notebook backgrounds (solid clean backgrounds only)
                    content = re.sub(r'background-image:\s*linear-gradient\([^;]+\);?', '', content, flags=re.MULTILINE)
                    content = re.sub(r'background-size:\s*[0-9]+px [0-9]+px;?', '', content, flags=re.MULTILINE)
                    
                    # Fix character corruption
                    for b, g in reps.items():
                        content = content.replace(b, g)
                    
                    # Neo-Brutalist: Ensure 3px borders site-wide
                    content = content.replace('border: 2px solid', 'border: 3px solid')
                    content = content.replace('border: 1px solid', 'border: 3px solid')
                    
                    # Script Injection: Ensure common.js is in head with defer
                    js_tag = '<script src="/js/common.js" defer></script>'
                    if js_tag not in content:
                        # Wipe any old incorrect links
                        content = content.replace('<script src="/js/common.js"></script>', '')
                        content = content.replace('</head>', f'  {js_tag}\n</head>')
                    
                    # Placeholder validation
                    if '<header></header>' not in content and '<header>' not in content and '<header ' not in content:
                        content = content.replace('<body>', '<body>\n<header></header>')
                    if '<footer></footer>' not in content and '<footer>' not in content and '<footer ' not in content:
                        if '</body>' in content:
                            content = content.replace('</body>', '<footer></footer>\n</body>')

                    with open(p, "w", encoding="utf-8") as f:
                        f.write(content)
                except Exception as e:
                    print(f"Error processing {p}: {e}")

    print("Ultimate Retro Neo-Brutalist Batch Repair Completed.")

if __name__ == "__main__":
    ultimate_repair()
