import os
import re

BASE_DIR = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"

HUBS = {
    "calculators-online.html": {
        "title": "Online Calculators India — GST, EMI, SIP, BMI, Age & More Free | WorldOfTools",
        "description": "12+ free online calculators for India — GST, EMI, SIP, PPF, BMI, Age, CGPA, Percentage & more. Instant results, no login, 100% private.",
        "h1": "Free Online Calculators (Made for India)",
        "sub": "A complete suite of financial, health, and math calculators.",
        "keywords": ["calculator", "bmi", "age", "percentage", "cgpa", "scientific", "unit", "loan"],
        "breadcrumb_name": "Calculators",
        "app_name": "Online Calculators India"
    },
    "developer-tools-online.html": {
        "title": "Free Developer Tools Online — JSON, Base64, JWT, SQL Formatter | WorldOfTools",
        "description": "Essential web developer tools. Format JSON, decode JWT, encode Base64, test Regex, format SQL & XML online. Free, fast, browser-based.",
        "h1": "Free Developer & Programmer Tools",
        "sub": "Format, encode, decode, and test your code instantly.",
        "keywords": ["json", "base64", "jwt", "sql", "xml", "regex", "uuid", "hash", "url"],
        "breadcrumb_name": "Developer Tools",
        "app_name": "Developer Tools Online"
    },
    "text-tools-online.html": {
        "title": "Online Text Tools — Word Counter, Case Converter, Fonts | WorldOfTools",
        "description": "Free text utilities. Count words, convert text case, generate fancy fonts, compare text, and analyze readability online.",
        "h1": "Online Text & Content Tools",
        "sub": "Everything you need to format, analyze, and style your text.",
        "keywords": ["word", "text", "font", "lorem", "case", "compare", "typing"],
        "breadcrumb_name": "Text Tools",
        "app_name": "Online Text Tools"
    },
    "seo-tools-free.html": {
        "title": "Free SEO Tools — Schema Generator, Meta Tags, SERP Preview | WorldOfTools",
        "description": "Boost your search rankings with free SEO tools. Generate Schema markup, write Meta tags, preview SERP snippets, and analyze keyword density.",
        "h1": "Free SEO & Webmaster Tools",
        "sub": "Optimize your website for Google with our free technical SEO tools.",
        "keywords": ["seo", "schema", "meta", "serp", "keyword"],
        "breadcrumb_name": "SEO Tools",
        "app_name": "Free SEO Tools"
    },
    "india-tools.html": {
        "title": "India Finance Hub — EMI, SIP, GST, PPF Calculators | WorldOfTools",
        "description": "Dedicated financial calculators for India. Calculate GST, SIP returns, EMI schedules, and PPF maturity instantly.",
        "h1": "India Finance & Tax Hub",
        "sub": "Calculate your investments, loans, and taxes with ease.",
        "keywords": ["gst", "emi", "sip", "ppf", "loan"],
        "breadcrumb_name": "India Tools",
        "app_name": "India Finance Hub"
    },
    "image-tools.html": {
        "title": "Free Image Tools — Compress, Convert, Remove BG, OCR | WorldOfTools",
        "description": "Optimize and edit your images online. Free image compressor, background remover, JPG to PNG converter, and OCR image-to-text.",
        "h1": "Free Online Image Tools",
        "sub": "Compress, convert, and enhance your photos in the browser.",
        "keywords": ["image", "compressor", "background", "jpg", "png", "favicon", "watermark", "video"],
        "breadcrumb_name": "Image Tools",
        "app_name": "Free Image Tools"
    },
    "design-tools.html": {
        "title": "Web Design Tools — CSS Gradients, Aspect Ratio, Colors | WorldOfTools",
        "description": "Free utilities for web designers. Generate CSS gradients, calculate aspect ratios, convert colors, and build email signatures.",
        "h1": "Design & UI Tools",
        "sub": "Create beautiful assets and CSS for your next project.",
        "keywords": ["css", "color", "aspect", "signature", "barcode", "qr", "thermal"],
        "breadcrumb_name": "Design Tools",
        "app_name": "Web Design Tools"
    },
    "security-tools.html": {
        "title": "Security & Privacy Tools — Password Generator, Hash, IP Lookup | WorldOfTools",
        "description": "Generate strong passwords, create secure hashes (MD5, SHA), and lookup IP addresses. 100% private, client-side tools.",
        "h1": "Security & Privacy Tools",
        "sub": "Keep your data secure with our cryptographic utilities.",
        "keywords": ["password", "hash", "ip", "jwt", "base64", "secure"],
        "breadcrumb_name": "Security Tools",
        "app_name": "Security & Privacy Tools"
    }
}

# Simple list of tools we know exist, to populate the hubs
TOOLS = [
    {"url": "/age-calculator", "name": "Age Calculator", "icon": "🎂", "desc": "Find exact age"},
    {"url": "/bmi-calculator", "name": "BMI Calculator", "icon": "⚖️", "desc": "Check body mass index"},
    {"url": "/gst-calculator", "name": "GST Calculator", "icon": "🧾", "desc": "Add/Remove GST"},
    {"url": "/emi-calculator", "name": "EMI Calculator", "icon": "🏠", "desc": "Loan EMI"},
    {"url": "/sip-calculator", "name": "SIP Calculator", "icon": "📈", "desc": "Mutual Fund Returns"},
    {"url": "/ppf-calculator", "name": "PPF Calculator", "icon": "💰", "desc": "Tax-free returns"},
    {"url": "/cgpa-calculator", "name": "CGPA Calculator", "icon": "🎓", "desc": "Convert to %"},
    {"url": "/percentage-calculator", "name": "Percentage Calc", "icon": "💯", "desc": "Find X% of Y"},
    {"url": "/scientific-calculator", "name": "Scientific Calc", "icon": "🔬", "desc": "Advanced Math"},
    {"url": "/unit-converter", "name": "Unit Converter", "icon": "📏", "desc": "Convert lengths & weights"},
    
    {"url": "/json-formatter", "name": "JSON Formatter", "icon": "{ }", "desc": "Beautify JSON"},
    {"url": "/base64-encoder-decoder", "name": "Base64 Encoder", "icon": "🔒", "desc": "Encode/Decode"},
    {"url": "/jwt-decoder", "name": "JWT Decoder", "icon": "🔑", "desc": "Decode web tokens"},
    {"url": "/sql-formatter", "name": "SQL Formatter", "icon": "🗄️", "desc": "Beautify SQL"},
    {"url": "/xml-formatter", "name": "XML Formatter", "icon": "📄", "desc": "Format XML"},
    {"url": "/regex-tester", "name": "Regex Tester", "icon": "🔍", "desc": "Test regular expressions"},
    {"url": "/uuid-generator", "name": "UUID Generator", "icon": "🆔", "desc": "Generate v4 UUIDs"},
    {"url": "/url-encoder-decoder", "name": "URL Encoder", "icon": "🔗", "desc": "Format links"},

    {"url": "/word-counter", "name": "Word Counter", "icon": "📝", "desc": "Count words & chars"},
    {"url": "/case-converter", "name": "Case Converter", "icon": "🔠", "desc": "UPPER/lower case"},
    {"url": "/fancy-font-generator", "name": "Fancy Fonts", "icon": "✨", "desc": "Cool text styles"},
    {"url": "/text-compare-tool", "name": "Text Compare", "icon": "⚖️", "desc": "Find diffs"},
    {"url": "/lorem-ipsum-generator", "name": "Lorem Ipsum", "icon": "📜", "desc": "Dummy text"},
    {"url": "/typing-speed-test", "name": "Typing Test", "icon": "⌨️", "desc": "Check WPM"},

    {"url": "/schema-generator-online", "name": "Schema Gen", "icon": "🏗️", "desc": "JSON-LD Builder"},
    {"url": "/schema-markup-generator", "name": "Schema Markup", "icon": "⚡", "desc": "Rich Snippets"},
    {"url": "/seo-meta-tag-generator", "name": "Meta Tags", "icon": "🏷️", "desc": "Generate meta HTML"},
    {"url": "/serp-preview", "name": "SERP Preview", "icon": "👁️", "desc": "Google preview"},
    
    {"url": "/loan-eligibility-calculator", "name": "Loan Eligibility", "icon": "✅", "desc": "Check loan limits"},
    {"url": "/loan-comparison-calculator", "name": "Compare Loans", "icon": "⚖️", "desc": "Compare EMI"},
    
    {"url": "/image-compressor", "name": "Image Compressor", "icon": "🗜️", "desc": "Reduce image size"},
    {"url": "/background-remover", "name": "BG Remover", "icon": "✂️", "desc": "Remove background"},
    {"url": "/image-to-text-ocr", "name": "Image to Text", "icon": "👁️", "desc": "Extract text"},
    {"url": "/jpg-to-png-converter", "name": "JPG to PNG", "icon": "🔄", "desc": "Convert images"},
    {"url": "/favicon-generator", "name": "Favicon Maker", "icon": "🖼️", "desc": "App icons"},
    {"url": "/remove-watermark-from-image", "name": "Watermark Remover", "icon": "💧", "desc": "Clean images"},
    {"url": "/video-to-gif", "name": "Video to GIF", "icon": "🎞️", "desc": "Convert video"},

    {"url": "/css-gradient-generator", "name": "CSS Gradients", "icon": "🎨", "desc": "Linear & Radial"},
    {"url": "/aspect-ratio-calculator", "name": "Aspect Ratio", "icon": "📐", "desc": "Calculate WxH"},
    {"url": "/color-converter", "name": "Color Converter", "icon": "🖌️", "desc": "HEX/RGB/HSL"},
    {"url": "/email-signature-generator", "name": "Email Signature", "icon": "✉️", "desc": "HTML signatures"},
    {"url": "/qr-code-generator", "name": "QR Generator", "icon": "📱", "desc": "Create QR codes"},
    {"url": "/barcode-generator", "name": "Barcode Gen", "icon": "🏷️", "desc": "Retail barcodes"},

    {"url": "/password-generator", "name": "Password Gen", "icon": "🛡️", "desc": "Secure pass"},
    {"url": "/secure-password-generator-online", "name": "Secure Pass Gen", "icon": "🔑", "desc": "Extra secure"},
    {"url": "/hash-generator", "name": "Hash Generator", "icon": "#️⃣", "desc": "MD5/SHA"},
    {"url": "/ip-address-lookup", "name": "IP Lookup", "icon": "🌐", "desc": "Find location"},
    {"url": "/random-number-generator", "name": "Random Number Generator", "icon": "🎲", "desc": "True random numbers"}
]

def generate_hubs():
    # Use index.html as a reference for a clean head if possible, 
    # but we already have calculators-online.html as the base.
    template_path = os.path.join(BASE_DIR, "calculators-online.html")
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()

    # Clean the template first: remove any existing SoftwareApplication or BreadcrumbList in the head
    template = re.sub(r'<script type="application/ld\+json">.*?</script>', '', template, flags=re.DOTALL)

    for filename, data in HUBS.items():
        out_html = template
        
        # 1. Update Canonical & OG URL
        page_url = f"https://worldoftools.in/{filename.replace('.html', '')}"
        out_html = re.sub(r'<link href="https://worldoftools.in/calculators-online" rel="canonical"/>', f'<link href="{page_url}" rel="canonical"/>', out_html)
        out_html = re.sub(r'<meta content="https://worldoftools.in/calculators-online" property="og:url"/>', f'<meta content="{page_url}" property="og:url"/>', out_html)
        out_html = re.sub(r'<link rel="alternate" hreflang="x-default" href="https://worldoftools.in/calculators-online"/>', f'<link rel="alternate" hreflang="x-default" href="{page_url}"/>', out_html)
        
        # 2. Update Title
        out_html = re.sub(r'<title>.*?</title>', f'<title>{data["title"]}</title>', out_html, flags=re.DOTALL)
        out_html = re.sub(r'<meta content=".*?" property="og:title"/>', f'<meta content="{data["title"]}" property="og:title"/>', out_html)
        out_html = re.sub(r'<meta content=".*?" name="twitter:title"/>', f'<meta content="{data["title"]}" name="twitter:title"/>', out_html)
        
        # 3. Update Description
        out_html = re.sub(r'<meta content=".*?" name="description"/>', f'<meta content="{data["description"]}" name="description"/>', out_html)
        out_html = re.sub(r'<meta content=".*?" property="og:description"/>', f'<meta content="{data["description"]}" property="og:description"/>', out_html)
        out_html = re.sub(r'<meta content=".*?" name="twitter:description"/>', f'<meta content="{data["description"]}" name="twitter:description"/>', out_html)
        
        # 4. Inject Schema Scripts into head (before </head>)
        software_schema = f'''  {{
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "{data["app_name"]}",
    "applicationCategory": "UtilitiesApplication",
    "operatingSystem": "Web Browser",
    "offers": {{
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "INR"
    }},
    "aggregateRating": {{
      "@type": "AggregateRating",
      "ratingValue": "4.8",
      "ratingCount": "1240"
    }},
    "description": "{data["description"]}",
    "url": "{page_url}"
  }}'''
        
        breadcrumb_schema = f'''  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://worldoftools.in"
      }},
      {{
        "@type": "ListItem",
        "position": 2,
        "name": "{data["breadcrumb_name"]}",
        "item": "{page_url}"
      }}
    ]
  }}'''
        
        schema_scripts = f'''    <script type="application/ld+json">\n{software_schema}\n    </script>\n    <script type="application/ld+json">\n{breadcrumb_schema}\n    </script>\n'''
        
        out_html = out_html.replace('</head>', f'{schema_scripts}</head>')

        # 5. Update Body Breadcrumb
        out_html = re.sub(r'<div class="breadcrumb"><a href="/">Home</a> .*? <span>.*?</span></div>', 
                          f'<div class="breadcrumb"><a href="/">Home</a> — <span>{data["breadcrumb_name"]}</span></div>', out_html)

        # 6. Update H1
        out_html = re.sub(r'<h1>.*?</h1>', f'<h1>{data["h1"]}</h1>', out_html, flags=re.DOTALL)
        
        # 7. Update Hero P
        out_html = re.sub(r'</h1>\s*<p>.*?</p>', f'</h1>\n    <p>{data["sub"]}</p>', out_html, flags=re.DOTALL)

        # 8. Update Hero Badge
        out_html = re.sub(r'<div class="hero-badge">.*?</div>', f'<div class="hero-badge">Built for India — 100% Free</div>', out_html)

        # 9. Generate grid items
        grid_html = ""
        for tool in TOOLS:
            matches = any(k in tool['url'] for k in data["keywords"])
            if matches:
                grid_html += f'''
      <a class="calc-card" href="{tool['url']}">
        <span class="calc-icon">{tool['icon']}</span>
        <h3 class="calc-name">{tool['name']}</h3>
        <p class="calc-desc">{tool['desc']}</p>
      </a>'''
        
        if not grid_html:
            grid_html = "<p>Tools coming soon...</p>"

        # 10. Replace grid
        out_html = re.sub(r'<div class="calc-grid">.*?</div>\s*<!-- Category explore strip -->', 
                          f'<div class="calc-grid">{grid_html}\n    </div>\n\n    <!-- Category explore strip -->', 
                          out_html, flags=re.DOTALL)
        
        if "Category explore strip" not in out_html:
             out_html = re.sub(r'<div class="calc-grid">.*?</div>', f'<div class="calc-grid">{grid_html}\n    </div>', out_html, flags=re.DOTALL)

        # 11. Save file
        out_path = os.path.join(BASE_DIR, filename)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(out_html)
        print(f"Generated {filename} with corrected schema and tools.")

if __name__ == "__main__":
    generate_hubs()
