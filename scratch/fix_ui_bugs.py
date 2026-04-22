import os
import glob
import re

BASE_DIR = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"

FOOTER_HTML = """<footer style="background:#fff; border-top:2.5px solid #000; padding:4rem 0 2rem; margin-top:5rem;">
  <div style="max-width:1200px; margin:0 auto; padding:0 1.5rem;">
    <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:3rem; margin-bottom:4rem;">
      <div>
        <div style="font-family:'Syne',sans-serif; font-weight:900; font-size:1.5rem; margin-bottom:1rem;">WorldOfTools</div>
        <p style="color:#666; line-height:1.6; font-size:0.95rem;">Premium, private, and fast online utility tools. 100% free forever. Made with ❤️ for the global developer and user community.</p>
      </div>
      <div>
        <h4 style="font-weight:800; text-transform:uppercase; font-size:0.85rem; letter-spacing:0.05em; margin-bottom:1.25rem;">Popular Hubs</h4>
        <ul style="list-style:none; padding:0; margin:0; line-height:2;">
          <li><a href="/calculators-online" style="text-decoration:none; color:#444; font-weight:600; font-size:0.9rem;">Financial Calculators</a></li>
          <li><a href="/developer-tools-online" style="text-decoration:none; color:#444; font-weight:600; font-size:0.9rem;">Developer Utilities</a></li>
          <li><a href="/image-tools" style="text-decoration:none; color:#444; font-weight:600; font-size:0.9rem;">Image Tools</a></li>
          <li><a href="/text-tools-online" style="text-decoration:none; color:#444; font-weight:600; font-size:0.9rem;">Text Tools</a></li>
        </ul>
      </div>
      <div>
        <h4 style="font-weight:800; text-transform:uppercase; font-size:0.85rem; letter-spacing:0.05em; margin-bottom:1.25rem;">Quick Links</h4>
        <ul style="list-style:none; padding:0; margin:0; line-height:2;">
          <li><a href="/about-us" style="text-decoration:none; color:#444; font-weight:600; font-size:0.9rem;">About Us</a></li>
          <li><a href="/contact-us" style="text-decoration:none; color:#444; font-weight:600; font-size:0.9rem;">Contact Us</a></li>
          <li><a href="/faq" style="text-decoration:none; color:#444; font-weight:600; font-size:0.9rem;">FAQ</a></li>
          <li><a href="/privacy" style="text-decoration:none; color:#444; font-weight:600; font-size:0.9rem;">Privacy Policy</a></li>
        </ul>
      </div>
    </div>
    <div style="border-top:2px solid #eee; padding-top:2rem; text-align:center; font-size:0.85rem; color:#888; font-weight:600;">
      &copy; 2026 WorldOfTools.in. All rights reserved. Locally processed. Zero-Knowledge tools.
    </div>
  </div>
</footer>"""

def fix_bugs():
    files = glob.glob(os.path.join(BASE_DIR, "*.html"))
    fixed_count = 0
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()

        # 1. Fix stray /> after description
        # Example: content="...">/>
        new_html = html.replace('">/>', '">')
        
        # 2. Inject standard footer
        if '<footer></footer>' in new_html:
            new_html = new_html.replace('<footer></footer>', FOOTER_HTML)
        elif '<footer>' in new_html and '</footer>' in new_html:
            # Replace existing footer content if any
            new_html = re.sub(r'<footer>.*?</footer>', FOOTER_HTML, new_html, flags=re.DOTALL)
        
        if new_html != html:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_html)
            fixed_count += 1

    print(f"Fixed {fixed_count} files (Stray tags and Footer injection).")

if __name__ == "__main__":
    fix_bugs()
