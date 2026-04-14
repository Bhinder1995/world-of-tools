import os
import re

def extreme_normalize():
    root_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    
    # Precise repair map for the specific garbled strings seen in browser and views
    reps = {
        "ðŸ“–": "📖",
        "Ã°Å¸â€œÂ ": "📍",
        "Ã¢Å“Â¨": "✨",
        "Ã¢Å“â€œ": "✓",
        "Ã°Å¸Å¡â‚¬": "🚀",
        "Ã°Å¸â€¢â€™": "🕒",
        "Ã°Å¸â€˜â€": "👔",
        "Ã°Å¸â€Â ": "🔠",
        "Ã°Å¸â€œÂ ": "📍",
        "Ã°Å¸Å½â€š": "🎂",
        "Ã°Å¸â€œÂ¹": "📹",
        "Ã°Å¸â€ºÂ¡ï¸": "🛡️",
        "Ã¢â‚¬â€": "—",
        "Ã¢Å“â€ ": "✓",
        "â–▼": "▼",
        "ðŸ’¡": "💡",
        "ðŸ§ª": "🧪",
        "🛡ï¸": "🛡️",
        "⚡ï¸": "⚡",
        "âœ…": "✓"
    }

    # 1. Process all HTML files
    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root: continue
        for file in files:
            if file.endswith(".html"):
                p = os.path.join(root, file)
                try:
                    with open(p, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    
                    # A. NORMALIZE NEWLINES: Collapse bloated code
                    content = re.sub(r'(\r?\n\s*){3,}', '\n\n', content)
                    
                    # B. DELETE BACKGROUND LINES: Remove the specific div tag
                    # Matching the pattern seen in index.html line 68
                    content = re.sub(r'<div style="[^"]*background-image:\s*linear-gradient\([^;]+\);?[^"]*">.*?</div>', '', content, flags=re.DOTALL)
                    
                    # C. REPAIR ENCODING
                    for b, g in reps.items():
                        content = content.replace(b, g)

                    # D. STYLE SYNC: Ensure 3px borders
                    content = content.replace('border: 1px solid var(--border-color)', 'border: 3px solid var(--border-color)')
                    content = content.replace('border: 2px solid var(--border-color)', 'border: 3px solid var(--border-color)')
                    
                    # E. SCRIPT SYNC: Final head injection
                    js_tag = '<script src="/js/common.js" defer></script>'
                    if js_tag not in content:
                        content = content.replace('</head>', f'  {js_tag}\n</head>')
                    
                    with open(p, "w", encoding="utf-8") as f:
                        f.write(content)
                except Exception as e:
                    print(f"Error processing {p}: {e}")

    # 2. Fix CSS background line too
    css_p = os.path.join(root_dir, "css", "style.css")
    try:
        with open(css_p, "r", encoding="utf-8") as f:
            css = f.read()
        css = re.sub(r'background-image:\s*linear-gradient\([^;]+\);?', '', css)
        css = re.sub(r'background-size:\s*[0-9]+px [0-9]+px;?', '', css)
        css = re.sub(r'(\r?\n\s*){3,}', '\n\n', css)
        with open(css_p, "w", encoding="utf-8") as f:
            f.write(css)
    except:
        pass

    print("Extreme Normalization and UI Repair Completed.")

if __name__ == "__main__":
    extreme_normalize()
