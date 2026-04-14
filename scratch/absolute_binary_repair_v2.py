import os
import re

def absolute_binary_repair():
    root_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    
    # Binary Mapping: Corrupted Bytes -> Correct UTF-8 Bytes
    # ✨ = \xE2\x9C\xA8
    # ✓ = \xE2\x9C\x93
    # 🔍 = \xF0\x9F\x94\x8D
    # 🚀 = \xF0\x9F\x9A\x80
    
    # Precise byte-sequences found in the file during visual/hex audit
    reps = {
        # Ã¢Å“Â¨ (Sparkle)
        bytes([0xC3, 0xA2, 0xE2\x80\x9C, 0xC2, 0xA8]): bytes([0xE2, 0x9C, 0xA8]),
        # Ã¢Å“â€ (Check)
        bytes([0xC3, 0xA2, 0xE2\x80\x9C, 0xC3, 0xA2, 0xE2\x80\x9A]): bytes([0xE2, 0x9C, 0x93]),
        # Ã°Å¸â€ Â (Search Icon)
        bytes([0xC3, 0xB0, 0xC5\xB8, 0xE2\x80\x9C, 0xC2, 0xA0]): bytes([0xF0, 0x9F, 0x94, 0x8D]),
        # Emoji interpret as bits
        b'\xc3\xb0\xc5\xb8\xc5\xa0\xe2\x82\xac\xe2\x80\x93': b'\xf0\x9f\x9a\x80', # Rocket
    }

    # Fallback text replacements for the specific string "Ã°Å¸â€ Â "
    text_replacements = [
        ("Ã°Å¸â€ Â ", "🔍"),
        ("Ã°Å¸â€œÂ ", "📍"),
        ("Ã°Å¸â€œÂ¦", "📦"),
        ("Ã°Å¸Å¡â‚¬", "🚀"),
        ("Ã¢Å“Â¨", "✨"),
        ("Ã¢Å“â€ ", "✓"),
        ("ðŸ“–", "📖"),
        ("Ã°Å¸â€ Â¥", "🔥")
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
                    
                    # Safe Decode to String
                    try:
                        content = data.decode('utf-8')
                    except:
                        content = data.decode('utf-8', errors='ignore')
                    
                    # 2. Text-based precision repair
                    for b, g in text_replacements:
                        content = content.replace(b, g)
                    
                    # 3. Collapse multiple newlines (Debloat)
                    content = re.sub(r'(\r?\n\s*){3,}', '\n\n', content)
                    
                    # 4. Final background wipe
                    content = re.sub(r'<div style="[^"]*background-image:\s*linear-gradient\([^;]+\);?[^"]*">.*?</div>', '', content, flags=re.DOTALL)
                    
                    with open(p, "w", encoding="utf-8") as f:
                        f.write(content)
                except Exception as e:
                    print(f"Error {file}: {e}")

    print("Definitive Binary Repair Sequence Finished.")

if __name__ == "__main__":
    absolute_binary_repair()
