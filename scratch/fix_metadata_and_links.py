import os
import re

def get_meta(content, tag_name):
    match = re.search(f'<meta [^>]*name="{tag_name}" [^>]*content="([^"]*)"', content, re.I)
    if not match:
        match = re.search(f'<meta [^>]*content="([^"]*)" [^>]*name="{tag_name}"', content, re.I)
    return match.group(1) if match else ""

def get_title(content):
    match = re.search(r'<title>(.*?)</title>', content, re.I | re.S)
    return match.group(1).strip() if match else ""

def fix_metadata():
    base_path = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    guides_path = os.path.join(base_path, "guides")
    
    # 1. Process Root Tools
    for file in os.listdir(base_path):
        if file.endswith(".html") and file != "index.html":
            path = os.path.join(base_path, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            title = get_title(content)
            desc = get_meta(content, "description")
            url = f"https://worldoftools.in/{file.replace('.html', '')}"
            
            # Check for existing OG tags
            has_og = 'property="og:title"' in content
            
            social_tags = ""
            if not has_og:
                social_tags = f"""
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="WorldOfTools.in">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="https://worldoftools.in/og/worldoftools-banner.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="https://worldoftools.in/og/worldoftools-banner.png">"""
                content = content.replace("</title>", f"</title>{social_tags}")

            # 2. Add Guide Link if exists
            guide_filename = file.replace(".html", "-guide.html")
            if os.path.exists(os.path.join(guides_path, guide_filename)):
                guide_url = f"/guides/{guide_filename.replace('.html', '')}"
                if f'href="{guide_url}"' not in content:
                    guide_link_html = f'\n    <div style="margin-top:1rem;"><a href="{guide_url}" class="nb-btn nb-btn-mint" style="font-size:0.85rem;padding:0.5rem 1rem;">📖 Read Detailed Guide & FAQ</a></div>'
                    # Inject into tool-hero
                    if '<section class="tool-hero">' in content:
                        content = content.replace('</section>', f'{guide_link_html}\n  </section>', 1)
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed metadata/links for {file}")

if __name__ == "__main__":
    fix_metadata()
