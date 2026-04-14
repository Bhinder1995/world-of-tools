import glob
import os
import re

def fix_files():
    files = glob.glob('c:/Users/HP/Desktop/Projects Folder/world_of_tools/*.html')
    
    for f in files:
        basename = os.path.basename(f)
        
        # Skip certain structural files that don't need tool-specific SEO logic
        is_tool = 'index.html' not in basename and 'terms.html' not in basename and 'privacy.html' not in basename and 'about-us.html' not in basename and 'contact-us.html' not in basename and 'seo-tools-free' not in basename and 'developer-tools-online' not in basename and 'calculators-online' not in basename and 'text-tools-online' not in basename and 'web-utilities-free' not in basename
        
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        original_content = content
        
        # 1. Duplicate guide buttons
        btn_pattern = r'(<div style="margin-bottom:1\.75rem;"><a class="btn" href="/guides/[^"]+"[^>]*>.*?Read Tool Guide</a></div>)'
        # Remove consecutive duplicates
        while True:
            new_content = re.sub(btn_pattern + r'\s*' + btn_pattern, r'\1', content)
            if new_content == content:
                break
            content = new_content
            
        # 2. Theme color
        # Remove existing theme-color meta tags to normalize
        content = re.sub(r'<meta[^>]*name="theme-color"[^>]*>', '', content)
        # Re-inject correct theme color before </head>
        content = content.replace('</head>', '<meta name="theme-color" content="#ffe066"/>\n</head>')
        
        # 3. Cache-busting
        content = re.sub(r'/css/style\.css\?v=[0-9.]+', '/css/style.css?v=4.0', content)
        content = re.sub(r'/css/neo-brutalism\.css\?v=[0-9.]+', '/css/neo-brutalism.css?v=4.0', content)
        content = re.sub(r'/js/common\.js\?v=[0-9.]+', '/js/common.js?v=4.0', content)
        
        # Determine canonical slug
        slug = basename.replace('.html', '')
        if slug == 'index':
            slug = ''
        url = f"https://worldoftools.in/{slug}"
        
        # 4. Canonical
        if 'rel="canonical"' not in content:
            content = content.replace('</head>', f'<link rel="canonical" href="{url}"/>\n</head>')
            
        # 5. Hreflang x-default
        # Only inject if doesn't exist
        if 'hreflang="x-default"' not in content:
            content = content.replace('</head>', f'<link rel="alternate" hreflang="x-default" href="{url}"/>\n</head>')
            
        # 6. Schema Image mapping
        if is_tool:
            # We look for SoftwareApplication schema block
            schema_pattern = r'("@type":\s*"SoftwareApplication".*?})'
            # We can't use simple regex to parse JSON safely if it's nested but typical JSON-LD is relatively flat at the top.
            # Instead let's just use string operations on the block
            
            blocks = re.findall(r'<script type="application/ld\+json">([\s\S]*?)</script>', content)
            for block in blocks:
                if '"@type": "SoftwareApplication"' in block and '"image"' not in block:
                    new_block = re.sub(r'("name":\s*"[^"]+",)', r'\1\n  "image": "https://worldoftools.in/app-icon.png",', block)
                    content = content.replace(block, new_block)
        
        if content != original_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
                print(f"Updated {basename}")

if __name__ == '__main__':
    fix_files()
