import os

def repair_content(content):
    try:
        # The logic: 
        # 1. Content was originally UTF-8.
        # 2. It was read as Latin-1 (interpreting bytes as chars).
        # 3. It was saved as UTF-8 (encoding those Latin-1 chars).
        # To fix: Reverse it.
        
        # Step 1: Get the bytes that would produce this string in Latin-1
        # (This effectively recovers the 'middle' state bytes)
        bytes_content = content.encode('latin-1')
        
        # Step 2: Decode those bytes as UTF-8 (recovering the original text)
        return bytes_content.decode('utf-8')
    except Exception:
        # If it fails (e.g. invalid UTF-8 after decoding Latin-1), return original
        return content

def walk_and_repair(directory):
    for root, dirs, files in os.walk(directory):
        if "node_modules" in root or ".git" in root:
            continue
        for file in files:
            if file.endswith((".html", ".js", ".css")):
                filepath = os.path.join(root, file)
                try:
                    # Read as UTF-8 (which gives us the corrupted string)
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                    
                    # Try to repair
                    # We look for a marker of corruption like the ones found by browser subagent
                    # e.g. "Ã¢" or "Ã°" or "Ãœ"
                    if "Ã" in content or "â" in content or "ð" in content:
                        repaired = repair_content(content)
                        if repaired != content:
                            with open(filepath, "w", encoding="utf-8") as f:
                                f.write(repaired)
                            print(f"Repaired encoding in {filepath}")
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    walk_and_repair(r"c:\Users\HP\Desktop\Projects Folder\world_of_tools")
