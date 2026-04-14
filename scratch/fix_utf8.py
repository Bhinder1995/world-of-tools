import os

def fix_encoding(directory):
    replacements = {
        "Ã¢â‚¬â€": "—",
        "Ã¢â‚¬â€": "—",
        "Ãœâ€”": "✨",
        "Ãœâ€œ": "✅",
        "âœ¨": "✨",
        "âœ“": "✓",
        "ðŸ›¡ï¸": "🛡️",
        "ðŸ“¹": "📹",
        "ðŸŽ‚": "🎂",
        "ðŸ“ ": "📍",
        "ðŸ” ": "🔍",
        "ðŸš€": "🚀",
        "Ã°Å¸â€ Â ": "🔍",
        "ðŸ•’": "🕒",
        "ðŸ‘”": "👔",
        "ðŸ” ": "🔠"
    }

    for root, dirs, files in os.walk(directory):
        if "node_modules" in root or ".git" in root:
            continue
        for file in files:
            if file.endswith((".html", ".js", ".css")):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                    
                    original_content = content
                    for bad, good in replacements.items():
                        content = content.replace(bad, good)
                    
                    if content != original_content:
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(content)
                        print(f"Fixed encoding in {filepath}")
                except Exception as e:
                    print(f"Error processing {filepath}: {e}")

if __name__ == "__main__":
    fix_encoding(r"c:\Users\HP\Desktop\Projects Folder\world_of_tools")
