import os
import re

def fix_guide(file_path):
    print(f"Fixing guide: {file_path}")
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Fix Button Contrast and Visibility
    # Use a stronger shadow and ensured black text on bright gradients if needed, 
    # but the user said "fonts not much visible". Usually means contrast.
    # We defined --primary-gradient as a purple/indigo mix. White text should be ok, 
    # but maybe we need a text-shadow or a bolder font.
    
    # Let's update the .back-btn internal style or the global CSS.
    # I already updated neo-brutalism.css. 
    # Now let's ensure the guides USE the standard button class or have enough padding.
    
    # 2. Site-wide Guide Standard: Ensure Lexend is used and contrast is high.
    content = content.replace('color: white;', 'color: #ffffff; text-shadow: 0 2px 4px rgba(0,0,0,0.3); font-size: 1.1rem; letter-spacing: 0.02em;')
    
    # 3. Fix absolute paths
    content = content.replace('href="/css/style.css"', 'href="/css/style.css"') # already absolute
    content = content.replace('href="../css/style.css"', 'href="/css/style.css"')
    content = content.replace('src="../js/common.js"', 'src="/js/common.js"')
    content = content.replace('href="../index.html"', 'href="/index.html"')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    guide_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools\guides"
    for filename in os.listdir(guide_dir):
        if filename.endswith(".html"):
            fix_guide(os.path.join(guide_dir, filename))

if __name__ == "__main__":
    main()
