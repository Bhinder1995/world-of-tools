import glob
import re
import os

files = glob.glob('*.html')
count = 0

# New SEO section content
seo_footer_html = """
    <!-- Global SEO Restoration: Trust & Privacy Block -->
    <section style="margin-top: 4rem; padding: 3rem 2rem; background: #f1f5f9; border-radius: 2rem; border: 2px solid #000; box-shadow: 6px 6px 0 #000;">
        <div style="max-width: 800px; margin: 0 auto; text-align: center;">
            <h2 style="font-size: 2rem; font-weight: 950; margin-bottom: 1.5rem; letter-spacing: -0.03em;">Privacy & Precision: The WorldOfTools Standard</h2>
            <p style="font-size: 1.1rem; line-height: 1.7; color: #334155; font-weight: 500; margin-bottom: 2rem;">
                Unlike other online utilities that store your personal data or upload files to remote servers, WorldOfTools operates on a <strong>Local-First architecture</strong>. This means 100% of the logic happens right in your browser. Whether you are calculating your precise age or converting sensitive images, your data never leaves your device. 
            </p>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; text-align: left;">
                <div style="background: white; padding: 1.5rem; border-radius: 12px; border: 1px solid #e2e8f0;">
                    <h4 style="margin: 0 0 0.5rem; color: #4338ca; font-weight: 800;">🔒 No Latency, 100% Privacy</h4>
                    <p style="margin: 0; font-size: 0.9rem; color: #64748b;">No server-side uploads mean instant processing and zero data leaks. Perfect for enterprise use.</p>
                </div>
                <div style="background: white; padding: 1.5rem; border-radius: 12px; border: 1px solid #e2e8f0;">
                    <h4 style="margin: 0 0 0.5rem; color: #4338ca; font-weight: 800;">⚙️ Developer-Verified Logic</h4>
                    <p style="margin: 0; font-size: 0.9rem; color: #64748b;">Our algorithms are open-spec and verified against global standards for financial and temporal math.</p>
                </div>
            </div>
        </div>
    </section>
"""

# Categorized SEO Facts for the "Empty Space" at the top
# (We'll only apply to Age Calculator specifically for now as requested, 
# but could be expanded if needed)

for f in files:
    filename = os.path.basename(f)
    if filename in ['index.html', 'about-us.html', 'contact-us.html', 'privacy.html', 'terms.html', 'sitemap.xml', 'manifest.json']:
        continue
        
    try:
        with open(f, 'r', encoding='utf-8') as f_in:
            content = f_in.read()
        
        # Don't duplicate if already added
        if 'Global SEO Restoration: Trust & Privacy Block' in content:
            continue
            
        # We look for the end of the related tools grid or the end of the <main> tag.
        # Pattern: </section>\s*</div>\s*</main>
        # Or better: after <!-- SEO Content Block -->
        
        target = "<!-- SEO Content Block -->"
        if target in content:
            parts = content.split(target)
            new_content = parts[0] + target + seo_footer_html + parts[1]
            
            with open(f, 'w', encoding='utf-8') as f_out:
                f_out.write(new_content)
            count += 1
            
    except Exception as e:
        print(f"Error on {f}: {e}")

print(f"Global SEO Footer Enhancement: {count} tool pages updated.")
