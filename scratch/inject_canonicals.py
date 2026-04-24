import os

directory = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"

def get_canonical(filename):
    if filename == "index.html":
        return "https://worldoftools.in/"
    # Remove .html extension
    name = filename[:-5]
    return f"https://worldoftools.in/{name}"

def fix_file(filepath, filename):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Check if canonical already exists
    has_canonical = any('<link rel="canonical"' in line for line in lines)
    if has_canonical:
        return False
    
    canonical_url = get_canonical(filename)
    canonical_tag = f'    <link rel="canonical" href="{canonical_url}">\n'
    
    # We want to insert it in the <head>
    # A good place is after <title> or after <meta charset>
    # Let's find line 4 or 5
    new_lines = []
    inserted = False
    for line in lines:
        new_lines.append(line)
        if not inserted and '<meta content="width=device-width, initial-scale=1.0" name="viewport"/>' in line:
            new_lines.append(canonical_tag)
            inserted = True
    
    if inserted:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return True
    return False

def main():
    files_fixed = 0
    for filename in os.listdir(directory):
        if filename.endswith(".html") and filename != "index.html":
            filepath = os.path.join(directory, filename)
            if fix_file(filepath, filename):
                files_fixed += 1
    
    print(f"Total files fixed with canonical: {files_fixed}")

if __name__ == "__main__":
    main()
