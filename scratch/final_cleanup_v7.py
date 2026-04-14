import os
import re

def final_cleanup_v7():
    root_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    
    # 1. PRECISE REPAIR MAPPING (from view_file Step 96)
    reps = {
        "Ã°Å¸â€ Â ": "🔍",
        "Ã°Å¸â€ Â ": "🔠",
        "Ã°Å¸â€œÂ ": "📍",
        "Ã°Å¸â€ºÂ¡Ã¯Â¸Â ": "🛡️",
        "Ã°Å¸Å½Å¾Ã¯Â¸Â ": "🎞️",
        "Ã°Å¸â€“Â¨Ã¯Â¸Â ": "🏷️",
        "Ã°Å¸Â§Â®": "🧮",
        "Ã°Å¸â€ºÂ Ã¯Â¸Â ": "🛠️",
        "Ã°Å¸â€Ë†": "📈",
        "Ã¢Å“Â Ã¯Â¸Â ": "✍️",
        "Ã°Å¸â€Â¦": "📦",
        "Ã°Å¸â€ Â¥": "🔥",
        "Ã¢â€ â€™": "→",
        "Ã¢Â­Â ": "⭐",
        "Ã¢â‚¬â€": "—",
        "Ã°Å¸â€œâ€": "📖",
        "Ã¢Å“â€ ": "✓"
    }

    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root: continue
        for file in files:
            if file.endswith(".html"):
                p = os.path.join(root, file)
                try:
                    with open(p, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    
                    # A. FIX LINK VERSIONING (Kill the triple ????)
                    content = re.sub(r'\.css\?v=[0-9.]+(\?v=[0-9.]+)*', '.css?v=5.0', content)
                    content = re.sub(r'\.js\?v=[0-9.]+(\?v=[0-9.]+)*', '.js?v=5.0', content)
                    
                    # Regular links if they missed versioning
                    content = content.replace('.css" rel="stylesheet"', '.css?v=5.0" rel="stylesheet"')
                    content = content.replace('.js" defer', '.js?v=5.0" defer')

                    # B. EMOJI REPAIR
                    for b, g in reps.items():
                        content = content.replace(b, g)

                    # C. NORMALIZE EXTRA NEWLINES (Very important)
                    content = re.sub(r'\n(\s*\n)+', '\n\n', content)

                    with open(p, "w", encoding="utf-8") as f:
                        f.write(content)
                except:
                    pass

    print("V7 Site-wide precision cleanup completed.")

if __name__ == "__main__":
    final_cleanup_v7()
