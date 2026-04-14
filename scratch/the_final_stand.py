import os
import re

def the_final_stand():
    root_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    
    # 1. CSS DOMINANCE OVERHAUL
    css_p = os.path.join(root_dir, "css", "style.css")
    css_content = r"""@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@400;600;700;800;900&display=swap');

:root {
    --bg-color: #fdfcf9 !important;
    --text-color: #2c2520 !important;
    --border-color: #3d342d !important;
    --primary-color: #e67e22 !important;
    --paper-shadow: 6px 6px 0px #3d342d !important;
    --paper-shadow-hover: 8px 8px 0px #e67e22 !important;
    --font-heading: 'Outfit', sans-serif !important;
    --font-body: 'Inter', sans-serif !important;
}

body {
    font-family: var(--font-body);
    background: var(--bg-color) !important;
    background-image: none !important;
    color: var(--text-color);
}

.card, .pop-card, .tool-chip, .bmi-card, .info-card {
    background: #ffffff !important;
    border: 3px solid var(--border-color) !important;
    box-shadow: var(--paper-shadow) !important;
    border-radius: 4px !important;
}

.btn, .unit-btn.active {
    border: 3px solid var(--border-color) !important;
    box-shadow: 4px 4px 0px #3d342d !important;
}
"""
    with open(css_p, "w", encoding="utf-8") as f:
        f.write(css_content)

    # 2. BATCH HTML NORMALIZATION
    reps = {
        "Ã°Å¸â€ Â ": "🔍", "Ã°Å¸â€ Â¥": "🔥", "Ã°Å¸â€œÂ¦": "📦", "Ã°Å¸Å½Å¾Ã¯Â¸Â ": "🎞️",
        "Ã°Å¸â€“Â¨Ã¯Â¸Â ": "🏷️", "Ã°Å¸â€ºÂ¡Ã¯Â¸Â ": "🛡️", "Ã°Å¸â€œÂ ": "📍", "Ã°Å¸Â§Â®": "🧮",
        "Ã°Å¸â€ºÂ Ã¯Â¸Â ": "🛠️", "Ã°Å¸â€Ë†": "📈", "Ã¢Å“Â Ã¯Â¸Â ": "✍️", "Ã°Å¸â€Â¦": "📦",
        "Ã¢Â­Â ": "⭐", "Ã¢â€ â€™": "→", "Ã°Å¸â€Â ": "🔠", "Ã¢Å“Â¨": "✨", "Ã¢Å“â€œ": "✓",
        "ðŸ“–": "📖", "Ã°Å¸â€œâ€": "📖", "Ã¢â‚¬â€": "—"
    }

    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root: continue
        for file in files:
            if file.endswith(".html"):
                p = os.path.join(root, file)
                try:
                    with open(p, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    
                    # A. DE-BLOAT: Collapse ALL multiple newlines into ONE
                    content = re.sub(r'\n(\s*\n)+', '\n\n', content)
                    
                    # B. HARD-DELETE LINES: Remove the specific div tag
                    content = re.sub(r'<div style="[^"]*background-image:\s*linear-gradient\([^;]+\);?[^"]*">.*?</div>', '', content, flags=re.DOTALL)
                    
                    # C. CACHE BUST: Move to v=4.0
                    content = content.replace('/css/style.css', '/css/style.css?v=4.0')
                    content = content.replace('/js/common.js', '/js/common.js?v=4.0')
                    # Clean up double versioning if any
                    content = content.replace('v=2.6?v=4.0', 'v=4.0')
                    content = content.replace('v=3.0?v=4.0', 'v=4.0')

                    # D. EMOJI REPAIR
                    for b, g in reps.items():
                        content = content.replace(b, g)
                    
                    with open(p, "w", encoding="utf-8") as f:
                        f.write(content)
                except:
                    pass

    print("The Final Stand: Global Repair Sequence Completed.")

if __name__ == "__main__":
    the_final_stand()
