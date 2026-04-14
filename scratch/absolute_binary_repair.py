import os
import re

def absolute_binary_repair():
    root_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    
    # Binary Mapping: Corrupted Bytes -> Correct UTF-8 Bytes
    # Based on observation of mojibake patterns (Interpret UTF-8 as Latin-1 and back)
    # 🔍 = \xF0\x9F\x94\x8D in UTF-8
    # 🔥 = \xF0\x9F\x94\xA5
    # ✨ = \xE2\x9C\xA8
    # ✓ = \xE2\x9C\x93
    # 🚀 = \xF0\x9F\x9A\x80
    
    # We will detect the specific mojibake byte sequences found in the file
    reps = {
        b'\xC3\xB0\xC5\xB8\xE2\x80\x9C\xC2\xA0': b'\xf0\x9f\x94\x8d', # 🔍 in some form
        b'\xC3\xB0\xC5\xB8\xE2\x80\x9C\xC2\x94': b'\xf0\x9f\x94\x8d', # 🔍 variation
        b'\xC3\xB0\xC5\xB8\xE2\x80\x9C\xC2\x9D': b'\xf0\x9f\x94\x8d', # 🔍 variation
        b'\xC3\xB0\xC5\xB8\xE2\x80\x9C\xC2\xA1': b'\xf0\x9f\x94\xa0', # 🔠
        b'\xC3\xB0\xC5\xB8\xE2\x80\x9C\xC2\x9C': b'\xf0\x9f\x93\x8d', # 📍
        b'\xC3\xB0\xC5\xB8\xE2\x80\xA2\xE2\x80\x99': b'\xf0\x9f\x95\x92', # 🕒
        b'\xC3\xA2\xE2\x80\x9C\xC2\x93': b'\xe2\x9c\x93', # ✓
        b'\xC3\xA2\xE2\x80\x9C\xC2\xA8': b'\xe2\x9c\xa8', # ✨
        b'\xC3\xB0\xC5\xB8\xC5\xA0\xE2\x82\xAC\xE2\x80\x93': b'\xf0\x9f\x9a\x80', # 🚀
        b'\xC3\xB0\xC5\xB8\xCB\x9C\xC2\xBE': b'\xf0\x9f\x8e\xbe', # 🎞️
        b'\xC3\xB0\xC5\xB8\xE2\x80\x94\xC2\xA8': b'\xf0\x9f\x96\xa8', # 🏷️
        b'\xC3\xB0\xC5\xB8\xE2\x80\x9B\xC2\xA1': b'\xf0\x9f\x9b\xa1', # 🛡️
        b'\xC3\xB0\xC5\xB8\xE2\x80\x9C\xC2\x9B': b'\xf0\x9f\x94\x9b', # 🔍 variation?
        b'Ã°Å¸â€ Â': b'\xf0\x9f\x94\x8d', # Literal string fix as bytes
    }

    # Common text-based fixes for things that survived earlier script errors
    text_reps = {
        "Ã°Å¸â€ Â ": "🔍",
        "Ã°Å¸Å¡â‚¬": "🚀",
        "Ã¢Å“Â¨": "✨",
        "Ã¢Å“â€ ": "✓",
        "Ã°Å¸â€ Â¥": "🔥",
        "Ã°Å¸â€œÂ¦": "📦"
    }

    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root: continue
        for file in files:
            if file.endswith(".html"):
                p = os.path.join(root, file)
                try:
                    # READ AS BINARY
                    with open(p, "rb") as f:
                        data = f.read()
                    
                    # 1. Binary replacements
                    for b, g in reps.items():
                        data = data.replace(b, g)
                    
                    # Convert to string to handle text patterns and normalization
                    content = data.decode('utf-8', errors='ignore')
                    
                    # 2. Text replacements
                    for b, g in text_reps.items():
                        content = content.replace(b, g)
                    
                    # 3. NORMALIZE NEWLINES (Kill the bloat)
                    content = re.sub(r'\n(\s*\n)+', '\n\n', content)
                    
                    # 4. Final background wipe
                    content = re.sub(r'<div style="[^"]*background-image:\s*linear-gradient\([^;]+\);?[^"]*">.*?</div>', '', content, flags=re.DOTALL)
                    
                    # WRITE BACK
                    with open(p, "w", encoding="utf-8") as f:
                        f.write(content)
                except Exception as e:
                    print(f"Error processing {p}: {e}")

    print("Absolute Binary Repair and Deep Normalization Complete.")

if __name__ == "__main__":
    absolute_binary_repair()
