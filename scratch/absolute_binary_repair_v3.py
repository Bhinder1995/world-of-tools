import os
import re

def absolute_binary_repair():
    root_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    
    # Binary Mapping: Corrupted Bytes -> Correct UTF-8 Bytes
    # I will use literal byte strings to avoid list syntax errors
    reps = {
        b'\xC3\xA2\xE2\x80\x9C\xC2\xA8': b'\xE2\x9C\xA8', # ✨
        b'\xC3\xB0\xC5\xB8\xE2\x80\x9C\xC2\xA0': b'\xF0\x9F\x94\x8D', # 🔍
        b'\xC3\xB0\xC5\xB8\xC5\xA0\xE2\x82\xAC\xE2\x80\x93': b'\xF0\x9F\x9A\x80', # 🚀
    }

    # High-precision text replacements for the literal "mojibake" strings
    text_reps = [
        ("Ã°Å¸â€ Â ", "🔍"),
        ("Ã°Å¸â€ Â", "🔍"),
        ("Ã°Å¸Å¡â‚¬", "🚀"),
        ("Ã¢Å“Â¨", "✨"),
        ("Ã¢Å“â€ ", "✓"),
        ("Ã°Å¸â€ Â¥", "🔥"),
        ("Ã°Å¸â€œÂ¦", "📦"),
        ("Ã°Å¸Å½Å¾Ã¯Â¸Â ", "🎞️"),
        ("Ã°Å¸â€“Â¨Ã¯Â¸Â ", "🏷️"),
        ("Ã°Å¸â€ºÂ¡Ã¯Â¸Â ", "🛡️"),
        ("Ã°Å¸â€œÂ ", "📍"),
        ("Ã°Å¸Â§Â®", "🧮"),
        ("Ã°Å¸â€ºÂ Ã¯Â¸Â ", "🛠️"),
        ("Ã°Å¸â€Ë†", "📈"),
        ("Ã¢Å“Â Ã¯Â¸Â ", "✍️"),
        ("Ã¢Â­Â ", "⭐"),
        ("Ã¢â€ â€™", "→"),
        ("Ã°Å¸â€Â ", "🔠"),
        ("ðŸ“–", "📖")
    ]

    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root: continue
        for file in files:
            if file.endswith(".html"):
                p = os.path.join(root, file)
                try:
                    with open(p, "rb") as f:
                        data = f.read()
                    
                    # 1. Binary replacements
                    for b, g in reps.items():
                        data = data.replace(b, g)
                    
                    # 2. Decode and text cleanup
                    content = data.decode('utf-8', errors='ignore')
                    
                    for b, g in text_reps:
                        content = content.replace(b, g)
                    
                    # 3. Collapse multiple newlines (Debloat)
                    content = re.sub(r'(\r?\n\s*){3,}', '\n\n', content)
                    
                    # 4. Final background wipe
                    content = re.sub(r'<div style="[^"]*background-image:\s*linear-gradient\([^;]+\);?[^"]*">.*?</div>', '', content, flags=re.DOTALL)
                    
                    with open(p, "w", encoding="utf-8") as f:
                        f.write(content)
                except Exception as e:
                    print(f"Error {file}: {e}")

    print("Definitive Binary Repair Sequence Complete.")

if __name__ == "__main__":
    absolute_binary_repair()
