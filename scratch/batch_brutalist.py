import os
import re

def batch_overhaul():
    root_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    
    # Repair mapping
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
        "Ã¢â‚¬â€": "—"
    }

    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root: continue
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "rb") as f:
                        data = f.read()
                    
                    # Try double-repair logic for emojis
                    def repair(d):
                        try:
                            # Reverses UTF-8 -> Latin-1 -> UTF-8 corruption
                            return d.decode('utf-8').encode('latin-1').decode('utf-8')
                        except:
                            return d.decode('utf-8', errors='ignore')
                    
                    content = repair(data)
                    
                    orig = content
                    
                    # Style updates: 2px -> 3px
                    content = content.replace("border: 2px solid var(--border-color)", "border: 3px solid var(--border-color)")
                    content = content.replace("border: 2px solid #3d342d", "border: 3px solid var(--border-color)")
                    
                    # Remove hero lines
                    content = content.replace('background-image: linear-gradient(var(--bg-color) 24px, #f1ece1 25px); background-size: 30px 30px;', '')
                    
                    # Quick fix for any other lingering 2px card borders in common themes
                    content = content.replace('border: 2px solid', 'border: 3px solid')

                    # Fix standard corrupted strings
                    for b, g in reps.items():
                        content = content.replace(b, g)

                    if content != orig:
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(content)
                        print(f"Batch overhauled {filepath}")
                except Exception as e:
                    print(f"Error {filepath}: {e}")

if __name__ == "__main__":
    batch_overhaul()
