import os
import re

def full_site_clean():
    root_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    
    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root: continue
        for file in files:
            if file.endswith(".html"):
                p = os.path.join(root, file)
                try:
                    with open(p, "rb") as f:
                        content = f.read().decode('utf-8', errors='ignore')
                    
                    # 1. Broad regex for the lines
                    content = re.sub(r'background-image:\s*linear-gradient\([^;]+\);?', '', content)
                    content = re.sub(r'background-size:\s*30px 30px;?', '', content)
                    
                    # 2. Fix the common corruption patterns precisely
                    # We'll use the strings as seen in the view_file report
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
                        "Â—": "—",
                        "â€”": "—"
                    }
                    for b, g in reps.items():
                        content = content.replace(b, g)

                    # 3. Ensure Header/Footer selectors match (some use id="header")
                    # No changes needed here yet, common.js uses document.querySelector('header')
                    
                    with open(p, "w", encoding="utf-8") as f:
                        f.write(content)
                except:
                    pass

    # Fix CSS lines too
    css_p = os.path.join(root_dir, "css", "style.css")
    with open(css_p, "r", encoding="utf-8") as f:
        css = f.read()
    css = re.sub(r'background-image: linear-gradient\([^;]+\);?', '', css)
    css = re.sub(r'background-size: 100% 25px;?', '', css)
    with open(css_p, "w", encoding="utf-8") as f:
        f.write(css)

    print("Full site clean completed.")

if __name__ == "__main__":
    full_site_clean()
