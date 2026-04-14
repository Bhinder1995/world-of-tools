import os
import re

def final_repair():
    root_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    
    # 1. PRECISE REPAIR MAPPING (Correct sequences as per text views)
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
        "Ã¢Å“â€ ": "✓"
    }

    # 2. PROCESSS ALL HTML FILES
    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root: continue
        for file in files:
            if file.endswith(".html"):
                p = os.path.join(root, file)
                try:
                    with open(p, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    
                    # Remove notebook lines
                    content = re.sub(r'background-image: linear-gradient\([^;]+\);?', '', content)
                    content = re.sub(r'background-size: [0-9]+px [0-9]+px;?', '', content)
                    content = re.sub(r'background-image:\s*linear-gradient\([^;]+\);?', '', content) # with spaces
                    
                    # Fix encoding
                    for b, g in reps.items():
                        content = content.replace(b, g)
                    
                    # Normalization: Fix bloated newlines
                    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
                    
                    # Neo-Brutalist: Ensure 3px borders
                    content = content.replace('border: 2px solid', 'border: 3px solid')
                    content = content.replace('border: 1px solid', 'border: 3px solid')
                    
                    # Script Injection: Ensure common.js is in head with defer
                    if '/js/common.js' not in content:
                        content = content.replace('</head>', '  <script src="/js/common.js" defer></script>\n</head>')
                    elif '<script src="/js/common.js"></script>' in content:
                        content = content.replace('<script src="/js/common.js"></script>', '<script src="/js/common.js" defer></script>')
                    
                    # Verify Header/Footer tags exist
                    if '<header></header>' not in content and '<header>' not in content and '<header ' not in content:
                        content = content.replace('<body>', '<body>\n<header></header>')
                    if '<footer></footer>' not in content and '<footer>' not in content and '<footer ' not in content:
                        if '</body>' in content:
                            content = content.replace('</body>', '<footer></footer>\n</body>')

                    with open(p, "w", encoding="utf-8") as f:
                        f.write(content)
                except:
                    pass

    # 3. OVERHAUL CSS (Pure Neo-Brutalist)
    css_p = os.path.join(root_dir, "css", "style.css")
    css_content = r"""@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@400;600;700;800;900&display=swap');

:root {
    --bg-color: #fdfcf9;
    --text-color: #2c2520;
    --text-muted: #6b635c;
    --primary-color: #e67e22;
    --primary-hover: #d35400;
    --secondary-color: #27ae60;
    --accent-color: #f59e0b;
    --border-color: #3d342d;
    --success-color: #22c55e;
    --error-color: #ef4444;
    --border-width: 3px;
    --radius-md: 4px;
    --paper-shadow: 6px 6px 0px #3d342d;
    --paper-shadow-hover: 8px 8px 0px #e67e22;
    --font-heading: 'Outfit', sans-serif;
    --font-body: 'Inter', sans-serif;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: var(--font-body);
    background-color: var(--bg-color);
    color: var(--text-color);
    line-height: 1.6;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
}

main { flex: 1; }

.container {
    max-width: 1200px;
    margin: 0 auto;
    width: 100%;
    padding: 2rem 1.5rem;
}

.card {
    background: #fff;
    border: var(--border-width) solid var(--border-color);
    border-radius: var(--radius-md);
    padding: 2rem;
    box-shadow: var(--paper-shadow);
    transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.card:hover {
    transform: translate(-4px, -4px);
    box-shadow: var(--paper-shadow-hover);
}

.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.8rem 2rem;
    background: var(--primary-color);
    color: white;
    border: var(--border-width) solid var(--border-color);
    border-radius: var(--radius-md);
    font-family: var(--font-heading);
    font-weight: 900;
    text-transform: uppercase;
    cursor: pointer;
    box-shadow: 4px 4px 0px #3d342d;
    transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    text-decoration: none;
}

.btn:hover {
    transform: translate(-3px, -3px);
    box-shadow: 6px 6px 0px #3d342d;
    background: var(--primary-hover);
}

header { z-index: 1000; position: sticky; top: 0; }
.hero-title { font-size: clamp(2rem, 6vw, 4rem); font-weight: 900; letter-spacing: -0.02em; }
.hero-subtitle { font-size: 1.1rem; opacity: 0.8; margin-top: 1rem; }
"""
    with open(css_p, "w", encoding="utf-8") as f:
        f.write(css_content)

    print("Final Site Repair Completed.")

if __name__ == "__main__":
    final_repair()
