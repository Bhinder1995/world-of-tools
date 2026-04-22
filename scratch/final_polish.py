import os
import re

BASE_DIR = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"

def final_polish():
    filepath = os.path.join(BASE_DIR, "bank-statement-analyzer.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove ANY SEO tag block that is NOT in the head
    # Identify head end
    head_end = html.find('</head>')
    body_content = html[head_end:]
    
    # Remove tech tags from body (they should only be in head)
    # This includes canonical, og, and scripts
    body_content = re.sub(r'<!-- SEO Optimization Meta Tags -->', '', body_content)
    body_content = re.sub(r'<link rel="canonical".*?>', '', body_content)
    body_content = re.sub(r'<meta property="og:.*?".*?>', '', body_content)
    body_content = re.sub(r'<meta name="twitter:.*?".*?>', '', body_content)
    # Remove JSON-LD from body
    body_content = re.sub(r'<script type="application/ld\+json">.*?</script>', '', body_content, flags=re.DOTALL)
    
    # 2. Add the "Competitor Gap" section to the SEO guide
    competitor_gap = """  <section style="margin-bottom:3rem; border:2.5px solid #000; padding:1.5rem; border-radius:16px; background:#fffbf0; box-shadow:4px 4px 0 #000;">
    <h2 style="color:#d97706; margin-top:0;">🚀 Why WorldOfTools Beats Other Analyzers</h2>
    <p>Most bank statement analysis tools (like those from major fintech firms or lending platforms) have a hidden catch: <strong>Your Data is the Price.</strong></p>
    <ul style="line-height:1.7; color:#444; margin-bottom:0; padding-left:1.5rem;">
      <li><strong>No Server Upload:</strong> Competitors upload your PDF to their servers. We process it 100% locally on your machine. Your balance stays YOUR business.</li>
      <li><strong>No Marketing Calls:</strong> Ever noticed getting loan calls after using a "free" analyzer? That's because they sell your lead. Since we don't store your data, we have nothing to sell.</li>
      <li><strong>HDFC, SBI, ICICI Ready:</strong> Our parser is tuned for the specific formatting quirks of Indian bank exports, including UPI-heavy statements that confuse global tools.</li>
      <li><strong>Zero Cost:</strong> No "Premium" tiers for larger statements or Excel exports. Everything is unlimited.</li>
    </ul>
  </section>"""

    # Inject into the seo-section
    if '<div class="seo-section">' in body_content:
        body_content = body_content.replace('<div class="seo-section">', f'<div class="seo-section">\n{competitor_gap}')

    # Reconstruct
    html = html[:head_end] + body_content
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Final polish complete for Bank Statement Analyzer.")

if __name__ == "__main__":
    final_polish()
