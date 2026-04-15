import os

def remove_www():
    target_pattern1 = "https://www.worldoftools.in"
    replacement1 = "https://worldoftools.in"
    
    target_pattern2 = "http://www.worldoftools.in"
    replacement2 = "https://worldoftools.in"
    
    target_pattern3 = "www.worldoftools.in"
    replacement3 = "worldoftools.in"

    extensions = ('.html', '.xml', '.js', '.json', '.css', '.txt')
    count = 0
    file_count = 0

    print("Starting site-wide 'www.' removal...")

    for root, dirs, files in os.walk('.'):
        # Skip node_modules and .git
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        if '.git' in dirs:
            dirs.remove('.git')
            
        for file in files:
            if file.endswith(extensions):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = content.replace(target_pattern1, replacement1)
                    new_content = new_content.replace(target_pattern2, replacement2)
                    # Use a more cautious replacement for just 'www.' to avoid breaking other things
                    # Only replace if it's likely a domain part
                    # (e.g., skip if it's already part of the replaced string above)
                    # Actually, pattern1 and pattern2 cover 99% of cases. 
                    # Let's see if pattern3 is still needed.
                    new_content = new_content.replace(target_pattern3, replacement3)

                    if content != new_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        occ = content.count(target_pattern1) + content.count(target_pattern2) + content.count(target_pattern3)
                        print(f"Updated: {file_path} ({occ} occurrences)")
                        count += occ
                        file_count += 1
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    print(f"\nFinished. Updated {file_count} files with {count} total replacements.")

if __name__ == "__main__":
    remove_www()
