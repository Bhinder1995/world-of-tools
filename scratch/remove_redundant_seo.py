import os
import re

directory = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"

# Pattern to find the SEO block
# It starts with <!-- SEO Optimization Meta Tags --> and ends with </script></head>
# We want to replace it with just </head>
pattern = re.compile(r'<!-- SEO Optimization Meta Tags -->.*?<\/script><\/head>', re.DOTALL)

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "<!-- SEO Optimization Meta Tags -->" in content:
        new_content = pattern.sub('</head>', content)
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            return True
    return False

def main():
    files_fixed = 0
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            if clean_file(filepath):
                print(f"Fixed: {filename}")
                files_fixed += 1
    
    print(f"\nTotal files cleaned: {files_fixed}")

if __name__ == "__main__":
    main()
