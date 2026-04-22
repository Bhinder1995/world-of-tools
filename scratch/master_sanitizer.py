import os
import glob
import re

BASE_DIR = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"

# 1. Map of files to their specific metadata if they aren't standard
# Most files will follow the slug-to-title pattern
SPECIAL_METADATA = {
    "calculators-online.html": {"title": "Online Calculators India — GST, EMI, SIP, BMI, Age & More Free | WorldOfTools", "desc": "12+ free online calculators for India — GST, EMI, SIP, PPF, BMI, Age, CGPA, Percentage & more. Instant results, no login, 100% private.", "category": "Calculators", "app": "Online Calculators India"},
    "developer-tools-online.html": {"title": "Free Developer Tools Online — JSON, Base64, JWT, SQL Formatter | WorldOfTools", "desc": "Essential web developer tools. Format JSON, decode JWT, encode Base64, test Regex, format SQL & XML online. Free, fast, browser-based.", "category": "Developer Tools", "app": "Developer Tools Online"},
    "bank-statement-analyzer.html": {"title": "Bank Statement Analyzer — Free Private PDF Analyzer, No Upload | WorldOfTools", "desc": "Free online bank statement analyzer. Analyze your PDF, CSV, or Excel statements instantly in your browser. 100% private, no data upload.", "category": "Finance Tools", "app": "Bank Statement Analyzer"}
}

def sanitize_and_fix_site():
    files = glob.glob(os.path.join(BASE_DIR, "*.html"))
    for filepath in files:
        filename = os.path.basename(filepath)
        if filename in ['sitemap.xml', 'robots.txt']: continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()

        # --- A. CLEAN HEAD ---
        # Identify the head block
        head_match = re.search(r'<head>(.*?)</head>', html, re.DOTALL)
        if not head_match: continue
        head_content = head_match.group(1)
        
        # Remove everything that we want to standardize
        clean_head = head_content
        # Remove canonicals
        clean_head = re.sub(r'<link.*?rel=["\']canonical["\'].*?>', '', clean_head, flags=re.IGNORECASE)
        # Remove og and twitter tags
        clean_head = re.sub(r'<meta.*?property=["\']og:.*?["\'].*?>', '', clean_head, flags=re.IGNORECASE)
        clean_head = re.sub(r'<meta.*?name=["\']twitter:.*?["\'].*?>', '', clean_head, flags=re.IGNORECASE)
        clean_head = re.sub(r'<meta.*?property=["\']website["\'].*?>', '', clean_head, flags=re.IGNORECASE)
        # Remove existing BreadcrumbList and SoftwareApplication JSON-LD
        # (This is aggressive but needed to fix duplicates)
        clean_head = re.sub(r'<script type="application/ld\+json">.*?</script>', '', clean_head, flags=re.DOTALL)
        # Remove old SEO comments
        clean_head = re.sub(r'<!-- SEO Optimization Meta Tags -->', '', clean_head)
        # Remove excess whitespace
        clean_head = re.sub(r'\n\s*\n', '\n', clean_head)

        # --- B. PREPARE NEW SEO BLOCK ---
        slug = filename.replace('.html', '')
        if filename in SPECIAL_METADATA:
            title = SPECIAL_METADATA[filename]["title"]
            desc = SPECIAL_METADATA[filename]["desc"]
            cat = SPECIAL_METADATA[filename]["category"]
            app = SPECIAL_METADATA[filename]["app"]
        else:
            # Auto-generate title/desc if not special
            clean_name = slug.replace('-', ' ').title()
            title = f"{clean_name} — Free Online Tool | WorldOfTools"
            desc = f"Use our free {clean_name} online. Fast, private, and no signup required. Part of WorldOfTools utility suite."
            cat = "Utility Tools"
            app = clean_name

        page_url = f"https://worldoftools.in/{slug}"
        
        new_seo = f'''
    <!-- SEO Optimization Meta Tags -->
    <link rel="canonical" href="{page_url}">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="WorldOfTools.in">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="{page_url}">
    <meta property="og:image" content="https://worldoftools.in/og/worldoftools-banner.png">
    <meta property="og:locale" content="en_IN">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="https://worldoftools.in/og/worldoftools-banner.png">
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "{app}",
      "applicationCategory": "UtilitiesApplication",
      "operatingSystem": "Web Browser",
      "offers": {{ "@type": "Offer", "price": "0", "priceCurrency": "INR" }},
      "aggregateRating": {{ "@type": "AggregateRating", "ratingValue": "4.8", "ratingCount": "1200" }},
      "description": "{desc}",
      "url": "{page_url}"
    }}
    </script>
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://worldoftools.in" }},
        {{ "@type": "ListItem", "position": 2, "name": "{cat}", "item": "{page_url}" }}
      ]
    }}
    </script>'''

        # Reconstruct head
        # We'll put our new SEO block right before </head>
        final_head = clean_head + new_seo
        html = html.replace(head_match.group(1), final_head)

        # --- C. CLEAN BODY SEO CONTENT ---
        # Ensure only one seo-section exists
        if html.count('<div class="seo-section">') > 1:
            # Keep only the last one (usually the most updated one)
            parts = html.split('<div class="seo-section">')
            html = parts[0] + '<div class="seo-section">' + parts[-1]
            # Also remove extra comment markers
            html = re.sub(r'<!-- SEO CONTENT -->', '', html)
            html = html.replace('<div class="seo-section">', '<!-- SEO CONTENT -->\n<div class="seo-section">')

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
    
    print(f"Master Sanitization complete for {len(files)} files.")

if __name__ == "__main__":
    sanitize_and_fix_site()
