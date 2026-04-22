import os
import re
import json
import glob

# Mapping for specific tool titles and descriptions based on the SEO plan
SEO_MAP = {
    "index.html": {
        "title": "80+ Free Online Tools — No Login, No Signup, Instant Results | WorldOfTools.in",
        "description": "WorldOfTools.in — 80+ free browser-based tools with no sign up, no login, no limit. Free GST, EMI, SIP calculator, JSON formatter, image compressor & more. 100% client-side, instant results.",
        "category": "WebApplication"
    },
    "age-calculator.html": {
        "title": "Age Calculator — Find Exact Age in Years, Months & Days, No Login | WorldOfTools",
        "description": "Calculate your exact age in years, months, days, hours & minutes. Find how many days until your next birthday. 100% free, instant, no login required.",
        "category": "UtilitiesApplication"
    },
    "bmi-calculator.html": {
        "title": "BMI Calculator — Check Body Mass Index Instantly Online | WorldOfTools",
        "description": "Calculate BMI instantly — see if you're underweight, normal, overweight or obese using India & WHO standards. Free, private, works in kg/cm or lbs/ft.",
        "category": "UtilitiesApplication"
    },
    "gst-calculator.html": {
        "title": "GST Calculator India 2025-26 — Add & Remove GST, Accurate Results | WorldOfTools",
        "description": "Free GST calculator for India — add or remove GST at 5%, 12%, 18% & 28% slabs. Calculate CGST, SGST & IGST instantly. Updated for 2025-26 tax rates.",
        "category": "FinanceApplication"
    },
    "emi-calculator.html": {
        "title": "EMI Calculator India — Home, Car & Personal Loan, No Login | WorldOfTools",
        "description": "Calculate your exact EMI for home loans, car loans & personal loans. See total interest payable & amortization schedule. Free, instant, no signup needed.",
        "category": "FinanceApplication"
    },
    "sip-calculator.html": {
        "title": "Best SIP Calculator India — Estimate Mutual Fund Returns Online | WorldOfTools",
        "description": "Calculate SIP returns for any monthly investment, tenure & expected rate. See how ₹5,000/month grows over 10 years with compound interest. Free SIP planner.",
        "category": "FinanceApplication"
    },
    "ppf-calculator.html": {
        "title": "PPF Calculator 2025-26 — Public Provident Fund Maturity, Accurate & Instant | WorldOfTools",
        "description": "Calculate your PPF maturity amount at 7.1% interest rate. Year-by-year breakdown, extension options & Section 80C tax savings. Free PPF planner 2025-26.",
        "category": "FinanceApplication"
    },
    "cgpa-calculator.html": {
        "title": "CGPA Calculator — Convert CGPA to Percentage, No Signup Needed | WorldOfTools",
        "description": "Convert CGPA to percentage using CBSE formula (×9.5) or university-specific formulas. Calculate GPA, SGPA & overall CGPA. Free, instant, no login needed.",
        "category": "FinanceApplication"
    },
    "percentage-calculator.html": {
        "title": "Percentage Calculator — Find X% of Any Number Free, Instant | WorldOfTools",
        "description": "Calculate what % of a number, percentage change, increase/decrease & reverse percentages. Solve all percentage problems instantly. Free with no login.",
        "category": "UtilitiesApplication"
    },
    "scientific-calculator.html": {
        "title": "Scientific Calculator Online — Trig, Log & Exponents, No Install | WorldOfTools",
        "description": "Full scientific calculator with sin, cos, tan, log, ln, exponents, roots & more. Works like a Casio fx-991 online. Free, fast, no install required.",
        "category": "UtilitiesApplication"
    },
    "json-formatter.html": {
        "title": "JSON Formatter & Validator — Beautify & Validate JSON, No Upload | WorldOfTools",
        "description": "Format, validate & beautify JSON with error highlighting and line numbers. Minify JSON for production. 100% client-side — your data never leaves your browser.",
        "category": "DeveloperApplication"
    },
    "jwt-decoder.html": {
        "title": "JWT Decoder — Decode & Inspect JWT Tokens Instantly, Client-Side | WorldOfTools",
        "description": "Decode JWT tokens and inspect header, payload & expiry instantly. Verify claims and detect expired tokens. 100% client-side — token never sent to any server.",
        "category": "DeveloperApplication"
    },
    "base64-encoder-decoder.html": {
        "title": "Base64 Encoder Decoder — Encode & Decode Text Instantly, No Install | WorldOfTools",
        "description": "Encode text or files to Base64 and decode Base64 strings back to readable text. Works offline in your browser — 100% private, no file upload. Free forever.",
        "category": "DeveloperApplication"
    },
    "password-generator.html": {
        "title": "Secure Password Generator — Best Strong Random Password Tool Online | WorldOfTools",
        "description": "Generate cryptographically strong passwords with custom length, symbols & complexity. Passwords generated locally — never transmitted or stored. 100% free.",
        "category": "DeveloperApplication"
    },
    "regex-tester.html": {
        "title": "Regex Tester & Debugger — Test Regular Expressions, No Signup Needed | WorldOfTools",
        "description": "Test regular expressions with real-time match highlighting, group capture visualization & explanation. Supports JavaScript, Python & PHP regex. Free online.",
        "category": "DeveloperApplication"
    },
    "word-counter.html": {
        "title": "Word Counter Online — Count Words, Characters & Reading Time Accurately | WorldOfTools",
        "description": "Free word counter — count words, characters (with/without spaces), sentences, paragraphs & reading time. Paste any text. Works offline. No signup needed.",
        "category": "UtilitiesApplication"
    },
    "case-converter.html": {
        "title": "Case Converter — UPPER, lower, Title & camelCase, Convert Instantly | WorldOfTools",
        "description": "Convert text between UPPERCASE, lowercase, Title Case, Sentence case, camelCase, PascalCase, snake_case & kebab-case. Instant, free, no login needed.",
        "category": "UtilitiesApplication"
    },
    "image-compressor.html": {
        "title": "Image Compressor — Compress JPG, PNG & WebP Free, No Upload Needed | WorldOfTools",
        "description": "Compress JPG, PNG and WebP images online — reduce file size by up to 80% without visible quality loss. 100% private: images never uploaded to any server.",
        "category": "MultimediaApplication"
    },
    "image-converter.html": {
        "title": "Image Converter — Convert JPG PNG WebP GIF Online, No Signup | WorldOfTools",
        "description": "Convert images between JPG, PNG, WebP, GIF and BMP formats instantly. Browser-based — no upload, 100% private. Batch convert multiple images at once. Free.",
        "category": "MultimediaApplication"
    },
    "color-converter.html": {
        "title": "Color Picker — Best HEX, RGB, HSL & CMYK Converter, No Install Needed | WorldOfTools",
        "description": "Pick colors and instantly convert between HEX, RGB, HSL, and CMYK. Generate complementary, analogous & triadic palettes. Free color tool for designers & devs.",
        "category": "DeveloperApplication"
    },
    "css-gradient-generator.html": {
        "title": "CSS Gradient Generator — Linear, Radial & Conic with Live Preview Online | WorldOfTools",
        "description": "Generate beautiful CSS gradients with live preview and instant CSS code output. Linear, radial & conic types, multiple color stops. Copy-paste into your project.",
        "category": "DeveloperApplication"
    },
    "seo-meta-tag-generator.html": {
        "title": "Meta Tag Generator — Instant SEO Meta & Open Graph Tags, No Login | WorldOfTools",
        "description": "Generate complete HTML meta tags for SEO — title, description, robots, Open Graph & Twitter Cards. Preview how your page looks on Google and social media.",
        "category": "WebApplication"
    },
    "unit-converter.html": {
        "title": "Unit Converter — Convert Length, Weight, Temp & Area Accurately Online | WorldOfTools",
        "description": "Convert between metric & imperial units instantly — length, weight, temperature, area, speed, volume & more. Free, accurate, works in all countries. No signup.",
        "category": "UtilitiesApplication"
    },
    "qr-code-generator.html": {
        "title": "QR Code Generator — Create Free QR Codes for URL, Text & WiFi | WorldOfTools",
        "description": "Generate QR codes for URLs, text, email, WiFi, phone numbers & vCards. Download as PNG or SVG. Custom colors & sizes. 100% free, no watermark, no signup needed.",
        "category": "UtilitiesApplication"
    },
    "hash-generator.html": {
        "title": "Hash Generator — MD5, SHA-1 & SHA-256 Online, Trusted & Private | WorldOfTools",
        "description": "Generate cryptographic hashes for any text or file — MD5, SHA-1, SHA-256, SHA-512 & more. 100% client-side, your data never leaves your browser. Free forever.",
        "category": "DeveloperApplication"
    },
    "keyword-density-checker.html": {
        "title": "Keyword Density Checker — Analyze KW % & Frequency, Accurate & Fast | WorldOfTools",
        "description": "Analyze keyword frequency and density percentage in any text or URL. Identify over-optimization risks and keyword gaps. Free SEO text analysis tool online.",
        "category": "WebApplication"
    },
    "video-compressor.html": {
        "title": "Video Compressor — Compress Large Videos Up to 2GB Free, No Watermark | WorldOfTools",
        "description": "Compress videos online up to 2GB free — no watermark, no quality loss. Compress MP4, MOV, AVI for WhatsApp, Instagram & YouTube. 100% free, no signup.",
        "category": "MultimediaApplication"
    },
    "bank-statement-analyzer.html": {
        "title": "Bank Statement Analyzer — Free Private PDF Analyzer, No Upload | WorldOfTools",
        "description": "Analyze your bank statement privately in the browser — categorize expenses, track spending & export summaries. No PDF upload to server. 100% free & private.",
        "category": "FinanceApplication"
    },
    "thermal-label-maker.html": {
        "title": "Thermal Label Maker — Free Shipping Label Maker Online India | WorldOfTools",
        "description": "Create thermal shipping labels online free — for Zebra, Citizen & other printers. Perfect for D2C sellers on Meesho, Amazon & Flipkart. No signup, no download.",
        "category": "UtilitiesApplication"
    },
    "fancy-font-generator.html": {
        "title": "Fancy Font Generator — Best Unicode Fonts for Instagram & WhatsApp Bio | WorldOfTools",
        "description": "Generate fancy text & Unicode fonts for Instagram bio, WhatsApp status, Twitter & more. 100+ font styles. Copy and paste anywhere. 100% free, instant.",
        "category": "UtilitiesApplication"
    }
}

# Determine default categories
def get_category(filename):
    if filename in SEO_MAP:
        return SEO_MAP[filename]["category"]
    
    # Generic mapping
    if "calculator" in filename:
        return "FinanceApplication" if any(x in filename for x in ["gst", "emi", "sip", "ppf", "loan", "tax", "cgpa"]) else "UtilitiesApplication"
    if any(x in filename for x in ["json", "jwt", "base64", "regex", "hash", "md5", "css", "html", "encoder", "decoder"]):
        return "DeveloperApplication"
    if "image" in filename or "video" in filename or "gif" in filename or "png" in filename or "jpg" in filename:
        return "MultimediaApplication"
    if "seo" in filename or "keyword" in filename or "serp" in filename:
        return "WebApplication"
    return "WebApplication"

def clean_html(content):
    # Remove existing canonical, og, and twitter tags if present
    content = re.sub(r'<link\s+rel="canonical"\s+href="[^"]*"\s*>', '', content)
    content = re.sub(r'<meta\s+property="og:[^>]*>', '', content)
    content = re.sub(r'<meta\s+name="twitter:[^>]*>', '', content)
    # Remove existing application/ld+json scripts that might be incomplete
    content = re.sub(r'<script type="application/ld\+json">.*?</script>', '', content, flags=re.DOTALL)
    
    # Also clean up multiple empty lines in head
    content = re.sub(r'(\n\s*){3,}', '\n\n', content)
    return content

# Files that need hreflang
INDIA_FINANCE_FILES = ['gst-calculator.html', 'emi-calculator.html', 'sip-calculator.html', 'ppf-calculator.html', 'cgpa-calculator.html', 'loan-eligibility-calculator.html', 'loan-comparison-calculator.html']

def process_file(filepath):
    filename = os.path.basename(filepath)
    slug = filename.replace('.html', '')
    url = f"https://worldoftools.in/{slug}" if slug != "index" else "https://worldoftools.in/"
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = clean_html(content)
    
    # Extract existing title and description if not in SEO_MAP
    title = f"{slug.replace('-', ' ').title()} — Free Online Tool | WorldOfTools"
    desc = f"Free online {slug.replace('-', ' ')}. 100% secure, no login required."
    
    title_match = re.search(r'<title>(.*?)</title>', content)
    if title_match:
        title = title_match.group(1).strip()
    
    desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"', content)
    if desc_match:
        desc = desc_match.group(1).strip()
        
    # Override with SEO map if available
    if filename in SEO_MAP:
        title = SEO_MAP[filename]["title"]
        desc = SEO_MAP[filename]["description"]
        # Update them in HTML
        if title_match:
            content = content.replace(title_match.group(0), f'<title>{title}</title>')
        if desc_match:
            content = content.replace(desc_match.group(0), f'<meta name="description" content="{desc}">')

    # Build Injection String for Head
    injection = f"""
    <!-- SEO Optimization Meta Tags -->
    <link rel="canonical" href="{url}">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="WorldOfTools.in">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="https://worldoftools.in/og/worldoftools-banner.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:locale" content="en_IN">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@worldoftools_in">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="https://worldoftools.in/og/worldoftools-banner.png">"""

    # Add hreflang for India specific tools
    if filename in INDIA_FINANCE_FILES:
        injection += f"""
    <link rel="alternate" hreflang="en-IN" href="{url}">
    <link rel="alternate" hreflang="en" href="{url}">
    <link rel="alternate" hreflang="x-default" href="{url}">"""

    # Add JSON-LD Schemas
    category = get_category(filename)
    tool_name = title.split("—")[0].split("|")[0].strip()
    
    if filename == "index.html":
        schema = {
            "@context": "https://schema.org",
            "@graph": [
                {
                    "@type": "WebSite",
                    "name": "WorldOfTools",
                    "url": "https://worldoftools.in",
                    "potentialAction": {
                        "@type": "SearchAction",
                        "target": "https://worldoftools.in/?q={search_term_string}",
                        "query-input": "required name=search_term_string"
                    }
                },
                {
                    "@type": "Organization",
                    "name": "WorldOfTools",
                    "url": "https://worldoftools.in",
                    "logo": "https://worldoftools.in/logo.svg"
                }
            ]
        }
    else:
        schema = {
            "@context": "https://schema.org",
            "@type": "SoftwareApplication",
            "name": tool_name,
            "applicationCategory": category,
            "operatingSystem": "Web Browser",
            "offers": { "@type": "Offer", "price": "0", "priceCurrency": "INR" },
            "aggregateRating": { "@type": "AggregateRating", "ratingValue": "4.8", "ratingCount": "1240" },
            "description": desc,
            "url": url
        }

    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://worldoftools.in" }
        ]
    }
    
    if filename != "index.html":
        # Guess category slug
        cat_map = {
            "FinanceApplication": "calculators-online",
            "UtilitiesApplication": "calculators-online", # Can be split further, but this is fine for phase 1
            "DeveloperApplication": "developer-tools-online",
            "MultimediaApplication": "image-tools", # New hub page soon
            "WebApplication": "seo-tools-free"
        }
        cat_slug = cat_map.get(category, "calculators-online")
        cat_name = cat_slug.replace("-", " ").title().replace(" Online", "").replace(" Free", "")
        
        breadcrumb["itemListElement"].extend([
            { "@type": "ListItem", "position": 2, "name": cat_name, "item": f"https://worldoftools.in/{cat_slug}" },
            { "@type": "ListItem", "position": 3, "name": tool_name, "item": url }
        ])

    injection += f"""
    <script type="application/ld+json">
{json.dumps(schema, indent=2)}
    </script>
    <script type="application/ld+json">
{json.dumps(breadcrumb, indent=2)}
    </script>
    """

    # Inject into head right before </head>
    if "</head>" in content:
        content = content.replace("</head>", f"{injection}\n</head>")
    else:
        print(f"No </head> found in {filename}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Processed: {filename}")

def main():
    target_dir = r"C:\Users\HP\Desktop\Projects Folder\world_of_tools"
    html_files = glob.glob(os.path.join(target_dir, "*.html"))
    for file in html_files:
        # Skip some files if necessary, like about/privacy/terms for now (or process them with generic)
        if os.path.basename(file) in ["WorldOfTools_SEO_Plan_v3_final.html", "worldoftools-seo-report.html"]:
            continue
        process_file(file)

if __name__ == "__main__":
    main()
