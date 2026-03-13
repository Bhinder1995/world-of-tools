import os
import re

def inject_guide_button():
    root_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    files = [f for f in os.listdir(root_dir) if f.endswith(".html")]
    
    # Exclude non-tool pages
    exclude = ["index.html", "contact.html", "privacy.html", "terms.html", "calculators-online.html", 
               "developer-tools-online.html", "seo-tools-free.html", "text-tools-online.html", "web-utilities-free.html"]
    
    for filename in files:
        if filename in exclude:
            continue
            
        filepath = os.path.join(root_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Check if it has a tool-header
        if 'class="tool-header"' in content:
            tool_slug = filename.replace(".html", "")
            guide_url = f"/guides/{tool_slug}-guide"
            
            # Button HTML
            # Check if button already exists
            if f'href="{guide_url}"' in content:
                print(f"Skipping {filename}, button already exists.")
                continue
            
            button_html = f'''
                <div style="margin-top: 1.5rem;">
                    <a href="{guide_url}" class="btn btn-secondary" style="display: inline-flex; align-items: center; gap: 0.5rem; text-decoration: none; font-weight: 700; border-radius: 12px; padding: 0.6rem 1.2rem; font-size: 0.95rem;">
                        📖 Read {tool_slug.replace("-", " ").title()} Guide
                    </a>
                </div>'''
            
            # Inject after the description <p> inside tool-header
            # Regex to find <section class="tool-header">...<p>...</p>
            pattern = re.compile(r'(<section class="tool-header">.*?<p.*?>.*?</p>)', re.DOTALL)
            
            if pattern.search(content):
                new_content = pattern.sub(r'\1' + button_html, content)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Injected button into {filename}")
            else:
                print(f"Could not find injection point in {filename}")

if __name__ == "__main__":
    inject_guide_button()
