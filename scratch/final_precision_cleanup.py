import os
import re

def final_precision_cleanup():
    root_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    
    # Comprehensive Garbled-to-Emoji Mapping
    reps = {
        "Ã°Å¸â€ Â ": "🔍",
        "Ã°Å¸â€ Â": "🔍", # without trailing space
        "Ã°Å¸Å¡â‚¬": "🚀",
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
        "Ã¢Å“Â¨": "✨",
        "Ã¢Å“â€œ": "✓",
        "Ã°Å¸Å½â€š": "🎂",
        "Ã°Å¸â€œÂ¹": "📹",
        "Ã°Å¸â€˜â€": "👔"
    }

    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root: continue
        for file in files:
            if file.endswith(".html"):
                p = os.path.join(root, file)
                try:
                    with open(p, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                    
                    # 1. Brutal Normalization: Collapse ANY group of 2+ empty lines into 1
                    content = re.sub(r'\n(\s*\n)+', '\n\n', content)
                    
                    # 2. Precision Emoji Repair
                    for b, g in reps.items():
                        content = content.replace(b, g)

                    # 3. Final background line wipe (Broad)
                    content = re.sub(r'background-image: linear-gradient\([^;]+\);?', '', content)
                    content = re.sub(r'background-size: [0-9]+px [0-9]+px;?', '', content)

                    with open(p, "w", encoding="utf-8") as f:
                        f.write(content)
                except Exception as e:
                    print(f"Error {p}: {e}")

    print("Final Precision Cleanup Success.")

if __name__ == "__main__":
    final_precision_cleanup()
