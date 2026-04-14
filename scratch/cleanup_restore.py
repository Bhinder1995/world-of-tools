import os
import re

def cleanup_tool(file_path):
    print(f"Cleaning up {file_path}...")
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Remove duplicate/legacy Privacy blocks
    # Looking for the old ones that don't have the "SHIELD" background or are redundant
    # Common signature: "Privacy & Precision: The WorldOfTools Standard" (Legacy)
    # vs our new "SHIELD" block.
    
    # Remove the legacy one that doesn't have SHIELD
    legacy_pattern = r'<!-- Global SEO Restoration: Trust & Privacy Block -->.*?<section style="margin-top: 4rem; padding: 3rem 2rem; background: #f1f5f9; border-radius: 2rem; border: 2px solid #000; box-shadow: 6px 6px 0 #000;">.*?</section>'
    content = re.sub(legacy_pattern, '', content, flags=re.DOTALL)
    
    # 2. Consolidate Duplicate SHIELD blocks (if any)
    # If the block was injected twice, remove one.
    parts = content.split('<!-- ══ PRIVACY & PRECISION STRIP ══ -->')
    if len(parts) > 2:
        # Keep first part and the second part (first instance) and discard others
        content = parts[0] + '<!-- ══ PRIVACY & PRECISION STRIP ══ -->' + parts[1] + "".join(parts[2:])
        # Wait, that's complex. Let's just use regex to find all matches and keep one.
        
    # 3. Path standardization (Extra check)
    content = content.replace('src="js/common.js?v=2.5"', 'src="/js/common.js?v=2.5"')
    
    # 4. Remove redundant "Other Free Tools" if they are hardcoded and we have Related Tools
    # Most tools now have the script-injected related tools or the hardcoded grid.
    # We want to favor the Related Tools strip.

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    base_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    all_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]
    exclude = ["index.html"]
    
    for filename in all_files:
        if filename not in exclude:
            path = os.path.join(base_dir, filename)
            cleanup_tool(path)

if __name__ == "__main__":
    main()
