import os
import re

def force_refresh_repair():
    root_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    
    # Precision repair map for the LAST remaining garbled strings
    reps = {
        "Ã°Å¸â€ Â ": "🔍",
        "Ã°Å¸â€ Â¥": "🔥",
        "Ã°Å¸â€œÂ¦": "📦",
        "Ã°Å¸Å½Å¾Ã¯Â¸Â ": "🎞️",
        "Ã°Å¸â€“Â¨Ã¯Â¸Â ": "🏷️",
        "Ã°Å¸â€ºÂ¡Ã¯Â¸Â ": "🛡️",
        "Ã°Å¸â€œÂ ": "📍",
        "Ã°Å¸Â§Â®": "🧮",
        "Ã°Å¸â€ºÂ Ã¯Â¸Â ": "🛠️",
        "Ã°Å¸â€Ë†": "📈",
        "Ã¢Å“Â Ã¯Â¸Â ": "✍️",
        "Ã¢Â­Â ": "⭐",
        "Ã¢â€ â€™": "→",
        "Ã°Å¸â€Â ": "🔠",
        "Ã¢Å“Â¨": "✨"
    }

    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root: continue
        for file in files:
            if file.endswith(".html"):
                p = os.path.join(root, file)
                try:
                    with open(p, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    
                    # 1. CACHE BUSTING: Update CSS and JS links
                    content = content.replace('/css/style.css', '/css/style.css?v=3.0')
                    content = content.replace('/css/style.css?v=2.6', '/css/style.css?v=3.0')
                    content = content.replace('/js/common.js', '/js/common.js?v=3.0')
                    
                    # 2. FINAL LINE CLEAN: Scrub the lingering div
                    content = re.sub(r'<div style="[^"]*background-image:\s*linear-gradient\([^;]+\);?[^"]*">.*?</div>', '', content, flags=re.DOTALL)
                    
                    # 3. EMOJI REPAIR
                    for b, g in reps.items():
                        content = content.replace(b, g)

                    with open(p, "w", encoding="utf-8") as f:
                        f.write(content)
                except Exception as e:
                    print(f"Error {p}: {e}")

    print("Force Refresh and Final Emoji Repair Completed.")

if __name__ == "__main__":
    force_refresh_repair()
