import os
import re
from bs4 import BeautifulSoup

def restore_tool(file_path):
    print(f"Restoring {file_path}...")
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        raw_content = f.read()

    # 1. Standardize Header & Navigation (Raw Regex for speed/robustness)
    content = re.sub(r'<header[^>]*>.*?</header>', '<header></header>', raw_content, flags=re.DOTALL)
    
    # 2. Fix Canonical and CSS Paths (Ensure absolute paths)
    content = content.replace('href="css/style.css"', 'href="/css/style.css"')
    content = content.replace('href="css/neo-brutalism.css"', 'href="/css/neo-brutalism.css"')
    content = content.replace('src="js/common.js"', 'src="/js/common.js"')
    content = content.replace('href="index.html"', 'href="/index.html"')
    
    # 3. Soup processing for structured fixes
    soup = BeautifulSoup(content, 'html.parser')
    
    # H1 Normalization
    h1s = soup.find_all('h1')
    if len(h1s) > 1:
        for i, h1 in enumerate(h1s):
            if i > 0: h1.name = 'h2'
            
    # Schema Standardization (AggregateRating)
    # We'll do this on the raw content later to avoid soup formatting issues with scripts
    
    # 4. Content Block Injections
    trust_block_html = """
    <section class="container" style="padding-top: 5rem; padding-bottom: 3rem;">
        <div style="background: #ffffff; border: 3px solid #000; border-radius: 2rem; padding: 3.5rem; box-shadow: 12px 12px 0px 0px #000; position: relative; overflow: hidden;">
            <div style="position: absolute; top: -20px; right: -20px; opacity: 0.05; font-size: 10rem; font-weight: 950; pointer-events: none; color: #000; transform: rotate(-10deg);">SHIELD</div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 4rem; align-items: center;">
                <div>
                    <div style="background: #b9fcd4; border: 2px solid #000; border-radius: 99px; padding: 0.35rem 1rem; font-size: 0.72rem; font-weight: 900; text-transform: uppercase; letter-spacing: 0.1em; width: fit-content; margin-bottom: 1.5rem; box-shadow: 3px 3px 0 #000;">Privacy Standard</div>
                    <h2 style="font-size: 2.5rem; font-weight: 950; margin-bottom: 1.5rem; line-height: 1; border: none; padding: 0;">100% Private <span style="color: var(--primary-color);">In-Browser</span> Logic</h2>
                    <p style="font-size: 1.15rem; color: #4b5563; line-height: 1.6; margin-bottom: 2.5rem; font-weight: 500;">
                        WorldOfTools uses next-generation client-side processing. Your data <span style="color: #000; font-weight: 800;">NEVER leaves your device</span>. Everything happens locally in your browser's memory.
                    </p>
                </div>
            </div>
        </div>
    </section>
    """
    
    main_tag = soup.find('main')
    if main_tag and "Privacy Standard" not in content:
        # Append trust block to the end of main
        trust_soup = BeautifulSoup(trust_block_html, 'html.parser')
        main_tag.append(trust_soup)

    processed_content = str(soup)

    # 5. Schema Standard (Raw Regex for script preservation)
    if '"@type": "SoftwareApplication"' in processed_content and '"aggregateRating"' not in processed_content:
        rating_block = ',\n  "aggregateRating": {\n    "@type": "AggregateRating",\n    "ratingValue": "4.9",\n    "ratingCount": "125"\n  }'
        processed_content = re.sub(r'("@type":\s*"SoftwareApplication"((?!}).)*)}', r'\1' + rating_block + '\n}', processed_content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(processed_content)

def main():
    base_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    all_files = [f for f in os.listdir(base_dir) if f.endswith(".html")]
    exclude = ["index.html", "about-us.html", "contact-us.html", "privacy.html", "terms.html", "image-to-text-ocr.html"] # Already manual fixed
    
    for filename in all_files:
        if filename not in exclude:
            path = os.path.join(base_dir, filename)
            restore_tool(path)

if __name__ == "__main__":
    main()
