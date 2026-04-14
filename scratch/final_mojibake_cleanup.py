import os
import re

ROOT = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"

BAD_STRINGS = [
    (" ï¸ ", ""),
    ("¼ï¸ ", ""),
    ("âšï¸ ", ""),
    ("Žï¸ ", ""),
    ("â¨ï¸ ", ""),
    ("â ï¸ ", ""),
    ("ï¸ ", ""),
    ("ðŸ", ""),
    ("Ã°Å¸", ""),
]

def clean_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    new_content = content
    for bad, good in BAD_STRINGS:
        new_content = new_content.replace(bad, good)
        
    if new_content != content:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

count = 0
for root, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in ('node_modules', '.git', 'scratch', '__pycache__')]
    for fn in files:
        if fn.endswith('.html'):
            if clean_file(os.path.join(root, fn)):
                count += 1

print(f"Cleaned mojibake from {count} files.")
