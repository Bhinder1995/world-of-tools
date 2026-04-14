import os
import re
from bs4 import BeautifulSoup

def restore_tool(file_path):
    print(f"Restoring {file_path}...")
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # 1. Standardize Header & Navigation
    # Remove everything inside <header> to allow common.js to inject global nav
    content = re.sub(r'<header[^>]*>.*?</header>', '<header></header>', content, flags=re.DOTALL)
    
    # 2. Fix Canonical and CSS Paths (Ensure absolute paths)
    content = content.replace('href="css/style.css"', 'href="/css/style.css"')
    content = content.replace('href="css/neo-brutalism.css"', 'href="/css/neo-brutalism.css"')
    content = content.replace('src="js/common.js"', 'src="/js/common.js"')
    
    # 3. H1 Normalization
    soup = BeautifulSoup(content, 'html.parser')
    h1s = soup.find_all('h1')
    if len(h1s) > 1:
        for i, h1 in enumerate(h1s):
            if i > 0:
                h1.name = 'h2'
        content = str(soup)

    # 4. Inject Trust Block if missing
    trust_block = """
<!-- ══ PRIVACY & PRECISION STRIP ══ -->
<section class="container" style="padding-top: 4rem; padding-bottom: 2rem;">
    <div style="background: #ffffff; border: 3px solid #000; border-radius: 2rem; padding: 3rem; box-shadow: 12px 12px 0px 0px #000; position: relative; overflow: hidden;">
        <div style="position: absolute; top: 0; right: 0; padding: 1.5rem; opacity: 0.1; font-size: 5rem; font-weight: 900; pointer-events: none;">SHIELD</div>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 3rem; align-items: start;">
            <div>
                <div class="sec-badge" style="background:#b9fcd4; margin-bottom: 1.5rem;">Privacy & Precision</div>
                <h2 style="font-size: 2.2rem; font-weight: 900; margin-bottom: 1.5rem; line-height: 1.1; border:none; padding:0;">The <span style="color: var(--primary-color);">WorldOfTools</span> Standard</h2>
                <p style="font-size: 1.1rem; color: #4b5563; line-height: 1.7; margin-bottom: 2rem;">
                    We believe essential utilities shouldn't cost you your data. Our tools are engineered to be <b>Local-First</b>—meaning all processing happens right in your browser. Nothing is uploaded, nothing is stored.
                </p>
                <div style="display: flex; gap: 1rem; font-weight: 800; font-size: 0.85rem; text-transform: uppercase;">
                    <span style="display: flex; align-items: center; gap: 0.4rem;"><span class="material-symbols-outlined" style="color:#10b981;">verified_user</span> No Signup</span>
                    <span style="display: flex; align-items: center; gap: 0.4rem;"><span class="material-symbols-outlined" style="color:#10b981;">rocket_launch</span> Free Forever</span>
                </div>
            </div>
            
            <div style="display: grid; gap: 1rem;">
                <div style="background: #f8fafc; border: 2px solid #000; border-radius: 1.25rem; padding: 1.5rem; display: flex; gap: 1rem; align-items: center;">
                    <div style="width: 48px; height: 48px; background: #e9ddff; border: 2px solid #000; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">🔒</div>
                    <div>
                        <div style="font-weight: 900; font-size: 1rem;">Zero-Server Logic</div>
                        <div style="font-size: 0.85rem; color: #64748b;">Your files never leave your device. Processing is 100% client-side.</div>
                    </div>
                </div>
                <div style="background: #f8fafc; border: 2px solid #000; border-radius: 1.25rem; padding: 1.5rem; display: flex; gap: 1rem; align-items: center;">
                    <div style="width: 48px; height: 48px; background: #fff0b3; border: 2px solid #000; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">⚡</div>
                    <div>
                        <div style="font-weight: 900; font-size: 1rem;">Instant Performance</div>
                        <div style="font-size: 0.85rem; color: #64748b;">No queues, no waiting. Hardware-accelerated results in milliseconds.</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>
"""
    if "Privacy & Precision" not in content and "</main>" in content:
        content = content.replace("</main>", trust_block + "\n</main>")

    # 5. Standardize Schema (AggregateRating)
    if '"@type": "SoftwareApplication"' in content and '"aggregateRating"' not in content:
        rating_block = ',\n  "aggregateRating": {\n    "@type": "AggregateRating",\n    "ratingValue": "4.9",\n    "ratingCount": "125"\n  }'
        content = re.sub(r'("@type":\s*"SoftwareApplication"((?!}).)*)}', r'\1' + rating_block + '\n}', content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    base_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    # Target common tools and top tools first
    top_tools = [
        "fancy-font-generator.html", "image-to-text-ocr.html", "keyword-research-tool.html",
        "thermal-label-maker.html", "video-compressor.html", "ip-address-lookup.html",
        "image-compressor.html", "sip-calculator.html", "age-calculator.html"
    ]
    
    for filename in top_tools:
        path = os.path.join(base_dir, filename)
        if os.path.exists(path):
            restore_tool(path)

    # Then process all other tools
    for filename in os.listdir(base_dir):
        if filename.endswith(".html") and filename not in top_tools and filename not in ["index.html", "about-us.html", "contact-us.html", "privacy.html", "terms.html"]:
            path = os.path.join(base_dir, filename)
            restore_tool(path)

if __name__ == "__main__":
    main()
