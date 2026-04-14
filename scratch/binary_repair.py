import os

def repair_binary(data):
    # This logic assumes the data was UTF-8, then read as Latin-1 and re-saved as UTF-8.
    # To reverse: 
    # 1. Decode as UTF-8 (gives the 'fake' Latin-1 chars)
    # 2. Encode as Latin-1 (gives the original bytes)
    # 3. Decode as UTF-8 (gives the original text)
    try:
        text = data.decode('utf-8')
        # We only apply the fix if we see the 'A-with-tilde' marker of this corruption
        if '\u00c3' in text:
            repaired_bytes = text.encode('latin-1')
            # Check if this helped
            repaired_text = repaired_bytes.decode('utf-8')
            return repaired_text.encode('utf-8')
        return data
    except:
        return data

def fix_all(directory):
    for root, dirs, files in os.walk(directory):
        if "node_modules" in root or ".git" in root: continue
        for file in files:
            if file.endswith((".html", ".js", ".css")):
                p = os.path.join(root, file)
                try:
                    with open(p, "rb") as f:
                        data = f.read()
                    
                    fixed_data = repair_binary(data)
                    # Loop once more for double-corruption
                    fixed_data = repair_binary(fixed_data)
                    
                    if fixed_data != data:
                        with open(p, "wb") as f:
                            f.write(fixed_data)
                        print(f"Repaired {p}")
                except:
                    pass

if __name__ == "__main__":
    fix_all(r"c:\Users\HP\Desktop\Projects Folder\world_of_tools")
