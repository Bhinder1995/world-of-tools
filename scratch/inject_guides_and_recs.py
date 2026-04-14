#!/usr/bin/env python3
"""
inject_guides_and_recs.py
Injects:
1. "Read Full Guide" button next to result action buttons
2. "You Might Also Need" post-recommendation widget after result-hero/actions
into all 70 tool HTML files copied from /des/ to root.
"""

import os, re, shutil

ROOT = r"C:\Users\HP\Desktop\Projects Folder\world_of_tools"
DES  = os.path.join(ROOT, "des")

# ─── Tool → Guide slug mapping ───────────────────────────────────────────────
GUIDE_MAP = {
    "age-calculator":                "age-calculator-guide",
    "aspect-ratio-calculator":       "aspect-ratio-calculator-guide",
    "audio-to-text":                 "audio-to-text-guide",
    "background-remover":            "background-remover-guide",
    "barcode-generator":             "barcode-generator-guide",
    "base64-encoder-decoder":        "base64-encoder-decoder-guide",
    "bmi-calculator":                "bmi-calculator-guide",
    "calculators-online":            None,  # category page, no guide
    "case-converter":                "case-converter-guide",
    "cgpa-calculator":               "cgpa-calculator-guide",
    "color-converter":               "color-converter-guide",
    "cron-expression-generator":     "cron-expression-generator-guide",
    "css-gradient-generator":        "css-gradient-generator-guide",
    "css-minifier":                  "css-minifier-guide",
    "csv-to-json":                   "csv-to-json-guide",
    "email-signature-generator":     "email-signature-generator-guide",
    "emi-calculator":                "emi-calculator-guide",
    "exif-metadata-remover":         "remove-exif-metadata-guide",
    "fancy-font-generator":          "fancy-font-generator-guide",
    "favicon-generator":             "favicon-generator-guide",
    "free-url-shortener-online":     "link-shortener-guide",
    "gst-calculator":                "gst-calculator-guide",
    "hash-generator":                "hash-generator-guide",
    "image-compressor":              "image-compressor-guide",
    "image-converter":               "image-converter-guide",
    "image-to-text-ocr":             "image-to-text-ocr-guide",
    "image-upscaler":                "image-upscaler-guide",
    "invoice-generator":             "invoice-generator-guide",
    "ip-address-lookup":             "ip-address-lookup-guide",
    "json-formatter":                "json-formatter-guide",
    "json-ld-generator":             "jwt-base64-hash-developer-security-guide",
    "jwt-decoder":                   "jwt-decoder-guide",
    "keyword-density-checker":       "keyword-density-checker-guide",
    "keyword-research-tool":         "keyword-research-guide",
    "link-shortener":                "link-shortener-guide",
    "linkedin-creator-suite":        "linkedin-creator-suite-guide",
    "loan-comparison-calculator":    "loan-comparison-calculator-guide",
    "loan-eligibility-calculator":   "loan-eligibility-calculator-guide",
    "lorem-ipsum-generator":         "lorem-ipsum-generator-guide",
    "markdown-to-html":              "markdown-to-html-guide",
    "number-to-words-converter":     "number-to-words-converter-guide",
    "password-generator":            "password-generator-guide",
    "percentage-calculator":         "percentage-calculator-guide",
    "ppf-calculator":                "ppf-calculator-guide",
    "qr-code-generator":             "qr-code-generator-guide",
    "random-number-generator":       "random-number-generator-guide",
    "regex-tester":                  "regex-tester-guide",
    "remove-watermark-from-image":   "remove-watermark-from-image-guide",
    "roman-numerals-converter":      "roman-numerals-converter-guide",
    "schema-generator-online":       "schema-markup-generator-guide",
    "scientific-calculator":         "scientific-calculator-guide",
    "secure-password-generator-online": "password-generator-guide",
    "seo-meta-tag-generator":        "seo-meta-tag-generator-guide",
    "serp-preview":                  "serp-preview-guide",
    "sip-calculator":                "sip-calculator-guide",
    "sql-formatter":                 "sql-formatter-guide",
    "text-compare-tool":             "text-compare-tool-guide",
    "text-to-binary-converter":      "text-to-binary-converter-guide",
    "thermal-label-maker":           "thermal-label-maker-guide",
    "time-zone-converter":           "time-zone-converter-guide",
    "typing-speed-test":             "typing-speed-test-guide",
    "unit-converter":                "unit-converter-guide",
    "url-encoder-decoder":           "url-encoder-decoder-guide",
    "uuid-generator":                "uuid-generator-guide",
    "video-compressor":              "video-compressor-guide",
    "video-to-gif":                  "video-to-gif-converter-guide",
    "video-to-mp3-converter":        "video-to-mp3-extractor-guide",
    "word-counter":                  "word-counter-guide",
    "xml-formatter":                 "xml-formatter-guide",
    "youtube-thumbnail-downloader":  "youtube-thumbnail-downloader-guide",
}

# ─── Tool → 3 Related Tools (post-rec) mapping ───────────────────────────────
RELATED_MAP = {
    "age-calculator": [
        ("/bmi-calculator", "⚖️", "BMI Calculator", "Check your body mass index"),
        ("/gst-calculator", "🧾", "GST Calculator", "Add or remove GST instantly"),
        ("/percentage-calculator", "💯", "Percentage Calculator", "Quick % calculations"),
    ],
    "gst-calculator": [
        ("/emi-calculator", "🏠", "EMI Calculator", "Loan EMI breakdown"),
        ("/sip-calculator", "📈", "SIP Calculator", "Mutual fund returns"),
        ("/invoice-generator", "🧾", "Invoice Maker", "Professional PDF invoices"),
    ],
    "emi-calculator": [
        ("/gst-calculator", "🧾", "GST Calculator", "Add or remove GST"),
        ("/sip-calculator", "📈", "SIP Calculator", "Investment planning"),
        ("/loan-comparison-calculator", "📊", "Loan Comparison", "Compare loan offers"),
    ],
    "sip-calculator": [
        ("/emi-calculator", "🏠", "EMI Calculator", "Loan EMI calculator"),
        ("/ppf-calculator", "🏦", "PPF Calculator", "PPF returns calculator"),
        ("/percentage-calculator", "💯", "% Calculator", "Quick percentage math"),
    ],
    "bmi-calculator": [
        ("/age-calculator", "🎂", "Age Calculator", "Your exact age"),
        ("/percentage-calculator", "💯", "% Calculator", "Quick calculations"),
        ("/scientific-calculator", "🔬", "Scientific Calc", "Advanced math"),
    ],
    "image-compressor": [
        ("/image-converter", "🔄", "Image Converter", "Convert PNG JPG WEBP"),
        ("/background-remover", "✂️", "BG Remover", "AI background removal"),
        ("/image-upscaler", "🔭", "Image Upscaler", "Upscale to 2× or 4K"),
    ],
    "video-compressor": [
        ("/video-to-gif", "🎞️", "Video to GIF", "Convert clips to GIFs"),
        ("/video-to-mp3-converter", "🎵", "Video to MP3", "Extract audio from video"),
        ("/image-compressor", "🖼️", "Image Compressor", "Compress images free"),
    ],
    "word-counter": [
        ("/case-converter", "🔠", "Case Converter", "UPPER lowercase Title"),
        ("/lorem-ipsum-generator", "📄", "Lorem Ipsum", "Placeholder text"),
        ("/keyword-density-checker", "📊", "Keyword Density", "SEO analysis"),
    ],
    "json-formatter": [
        ("/jwt-decoder", "🔑", "JWT Decoder", "Decode JSON web tokens"),
        ("/csv-to-json", "📊", "CSV to JSON", "Convert CSV data"),
        ("/xml-formatter", "🛠️", "XML Formatter", "Beautify XML code"),
    ],
    "password-generator": [
        ("/hash-generator", "🔐", "Hash Generator", "MD5 SHA-256 hashing"),
        ("/uuid-generator", "🆔", "UUID Generator", "Generate v1/v4 UUIDs"),
        ("/base64-encoder-decoder", "🔄", "Base64 Tools", "Encode/decode Base64"),
    ],
    "qr-code-generator": [
        ("/barcode-generator", "🏷️", "Barcode Generator", "CODE128 EAN UPC"),
        ("/link-shortener", "🔗", "Link Shortener", "Shorten any URL"),
        ("/image-compressor", "🖼️", "Image Compressor", "Compress images"),
    ],
    "ip-address-lookup": [
        ("/url-encoder-decoder", "🔗", "URL Encoder", "Encode decode URLs"),
        ("/hash-generator", "🔐", "Hash Generator", "Secure hashing"),
        ("/jwt-decoder", "🔑", "JWT Decoder", "Decode JWT tokens"),
    ],
    "case-converter": [
        ("/word-counter", "📝", "Word Counter", "Count words & chars"),
        ("/lorem-ipsum-generator", "📄", "Lorem Ipsum", "Placeholder text"),
        ("/markdown-to-html", "📑", "Markdown to HTML", "Convert markdown"),
    ],
    "hash-generator": [
        ("/password-generator", "🔒", "Password Generator", "Strong passwords"),
        ("/base64-encoder-decoder", "🔄", "Base64 Encoder", "Encode/decode"),
        ("/jwt-decoder", "🔑", "JWT Decoder", "Decode JWT tokens"),
    ],
    "base64-encoder-decoder": [
        ("/hash-generator", "🔐", "Hash Generator", "MD5 SHA hashing"),
        ("/url-encoder-decoder", "🔗", "URL Encoder", "Encode URLs"),
        ("/jwt-decoder", "🔑", "JWT Decoder", "Full JWT inspector"),
    ],
    "jwt-decoder": [
        ("/hash-generator", "🔐", "Hash Generator", "Cryptographic hashing"),
        ("/base64-encoder-decoder", "🔄", "Base64 Tools", "Encode decode Base64"),
        ("/password-generator", "🔒", "Password Gen", "Secure passwords"),
    ],
    "image-converter": [
        ("/image-compressor", "🖼️", "Image Compressor", "Reduce file size"),
        ("/background-remover", "✂️", "BG Remover", "Remove backgrounds"),
        ("/favicon-generator", "🖼️", "Favicon Maker", "Generate favicons"),
    ],
    "background-remover": [
        ("/image-compressor", "🖼️", "Image Compressor", "Compress images"),
        ("/image-upscaler", "🔭", "Image Upscaler", "AI upscaling"),
        ("/image-converter", "🔄", "Image Converter", "Convert formats"),
    ],
    "image-upscaler": [
        ("/background-remover", "✂️", "BG Remover", "Remove backgrounds"),
        ("/image-compressor", "🖼️", "Image Compressor", "Reduce file size"),
        ("/remove-watermark-from-image", "🧹", "Remove Watermark", "AI watermark removal"),
    ],
    "remove-watermark-from-image": [
        ("/background-remover", "✂️", "BG Remover", "Remove backgrounds"),
        ("/image-upscaler", "🔭", "Image Upscaler", "AI upscaling"),
        ("/image-compressor", "🖼️", "Image Compressor", "Compress images"),
    ],
    "url-encoder-decoder": [
        ("/base64-encoder-decoder", "🔄", "Base64 Tools", "Encode/decode data"),
        ("/hash-generator", "🔐", "Hash Generator", "MD5 SHA hashing"),
        ("/jwt-decoder", "🔑", "JWT Decoder", "Decode JWT tokens"),
    ],
    "percentage-calculator": [
        ("/scientific-calculator", "🔬", "Scientific Calc", "Advanced math"),
        ("/gst-calculator", "🧾", "GST Calculator", "GST calculations"),
        ("/emi-calculator", "🏠", "EMI Calculator", "Loan EMI"),
    ],
    "scientific-calculator": [
        ("/percentage-calculator", "💯", "% Calculator", "Percentage math"),
        ("/bmi-calculator", "⚖️", "BMI Calculator", "Body mass index"),
        ("/unit-converter", "📏", "Unit Converter", "Convert any unit"),
    ],
    "unit-converter": [
        ("/scientific-calculator", "🔬", "Scientific Calc", "Advanced calculator"),
        ("/aspect-ratio-calculator", "📐", "Aspect Ratio", "Image dimensions"),
        ("/percentage-calculator", "💯", "% Calculator", "Quick percentages"),
    ],
    "audio-to-text": [
        ("/word-counter", "📝", "Word Counter", "Analyze your transcript"),
        ("/case-converter", "🔠", "Case Converter", "Format text"),
        ("/markdown-to-html", "📑", "Markdown to HTML", "Format content"),
    ],
    "text-compare-tool": [
        ("/word-counter", "📝", "Word Counter", "Count words"),
        ("/case-converter", "🔠", "Case Converter", "Change text case"),
        ("/markdown-to-html", "📑", "Markdown to HTML", "Convert markdown"),
    ],
    "lorem-ipsum-generator": [
        ("/word-counter", "📝", "Word Counter", "Count your words"),
        ("/case-converter", "🔠", "Case Converter", "Change text case"),
        ("/markdown-to-html", "📑", "Markdown to HTML", "Convert markdown"),
    ],
    "fancy-font-generator": [
        ("/case-converter", "🔠", "Case Converter", "Change text case"),
        ("/word-counter", "📝", "Word Counter", "Count words & chars"),
        ("/qr-code-generator", "🔳", "QR Generator", "Create QR codes"),
    ],
    "typing-speed-test": [
        ("/word-counter", "📝", "Word Counter", "Count words & reading time"),
        ("/case-converter", "🔠", "Case Converter", "Text case tools"),
        ("/lorem-ipsum-generator", "📄", "Lorem Ipsum", "Practice text"),
    ],
    "barcode-generator": [
        ("/qr-code-generator", "🔳", "QR Generator", "Create QR codes"),
        ("/thermal-label-maker", "🖨️", "Label Maker", "Thermal printer labels"),
        ("/invoice-generator", "🧾", "Invoice Maker", "PDF invoices"),
    ],
    "thermal-label-maker": [
        ("/barcode-generator", "🏷️", "Barcode Generator", "CODE128 EAN barcodes"),
        ("/qr-code-generator", "🔳", "QR Generator", "Create QR codes"),
        ("/invoice-generator", "🧾", "Invoice Maker", "PDF invoices"),
    ],
    "invoice-generator": [
        ("/gst-calculator", "🧾", "GST Calculator", "Calculate GST"),
        ("/emi-calculator", "🏠", "EMI Calculator", "Loan EMI"),
        ("/barcode-generator", "🏷️", "Barcode Generator", "Barcodes for items"),
    ],
    "image-to-text-ocr": [
        ("/word-counter", "📝", "Word Counter", "Count extracted words"),
        ("/case-converter", "🔠", "Case Converter", "Format extracted text"),
        ("/audio-to-text", "🎙️", "Audio to Text", "Transcribe audio"),
    ],
    "youtube-thumbnail-downloader": [
        ("/image-compressor", "🖼️", "Image Compressor", "Compress thumbnails"),
        ("/image-converter", "🔄", "Image Converter", "Convert image formats"),
        ("/background-remover", "✂️", "BG Remover", "Edit thumbnails"),
    ],
    "regex-tester": [
        ("/json-formatter", "{ }", "JSON Formatter", "Beautify JSON"),
        ("/text-compare-tool", "⚖️", "Text Compare", "Diff two texts"),
        ("/csv-to-json", "📊", "CSV to JSON", "Convert CSV"),
    ],
    "sql-formatter": [
        ("/json-formatter", "{ }", "JSON Formatter", "Beautify JSON"),
        ("/xml-formatter", "🛠️", "XML Formatter", "Beautify XML"),
        ("/csv-to-json", "📊", "CSV to JSON", "Convert CSV to JSON"),
    ],
    "xml-formatter": [
        ("/json-formatter", "{ }", "JSON Formatter", "Beautify JSON"),
        ("/sql-formatter", "🗄️", "SQL Formatter", "Format SQL queries"),
        ("/csv-to-json", "📊", "CSV to JSON", "CSV conversion"),
    ],
    "csv-to-json": [
        ("/json-formatter", "{ }", "JSON Formatter", "Beautify JSON data"),
        ("/xml-formatter", "🛠️", "XML Formatter", "Format XML"),
        ("/sql-formatter", "🗄️", "SQL Formatter", "Format SQL"),
    ],
    "css-minifier": [
        ("/css-gradient-generator", "🎨", "CSS Gradient", "Create CSS gradients"),
        ("/json-formatter", "{ }", "JSON Formatter", "Format JSON"),
        ("/markdown-to-html", "📑", "Markdown to HTML", "Convert markdown"),
    ],
    "css-gradient-generator": [
        ("/css-minifier", "🗜️", "CSS Minifier", "Compress CSS"),
        ("/color-converter", "🎨", "Color Converter", "HEX RGB HSL"),
        ("/favicon-generator", "🖼️", "Favicon Maker", "Create favicons"),
    ],
    "color-converter": [
        ("/css-gradient-generator", "🎨", "CSS Gradient", "Create gradients"),
        ("/image-converter", "🔄", "Image Converter", "Convert formats"),
        ("/favicon-generator", "🖼️", "Favicon Maker", "Create favicons"),
    ],
    "favicon-generator": [
        ("/image-compressor", "🖼️", "Image Compressor", "Compress images"),
        ("/image-converter", "🔄", "Image Converter", "Convert formats"),
        ("/css-gradient-generator", "🎨", "CSS Gradient", "Create gradients"),
    ],
    "uuid-generator": [
        ("/password-generator", "🔒", "Password Generator", "Secure passwords"),
        ("/hash-generator", "🔐", "Hash Generator", "MD5 SHA hashing"),
        ("/random-number-generator", "🎲", "Random Numbers", "Generate numbers"),
    ],
    "random-number-generator": [
        ("/uuid-generator", "🆔", "UUID Generator", "Generate UUIDs"),
        ("/password-generator", "🔒", "Password Gen", "Strong passwords"),
        ("/hash-generator", "🔐", "Hash Generator", "Cryptographic hashing"),
    ],
    "markdown-to-html": [
        ("/word-counter", "📝", "Word Counter", "Count words"),
        ("/css-minifier", "🗜️", "CSS Minifier", "Minify CSS"),
        ("/json-formatter", "{ }", "JSON Formatter", "Format JSON"),
    ],
    "seo-meta-tag-generator": [
        ("/serp-preview", "🔎", "SERP Preview", "Preview in Google"),
        ("/keyword-density-checker", "📊", "Keyword Density", "Analyze keywords"),
        ("/schema-generator-online", "🧩", "Schema Generator", "Structured data"),
    ],
    "serp-preview": [
        ("/seo-meta-tag-generator", "🏷️", "Meta Tag Generator", "Create SEO tags"),
        ("/keyword-density-checker", "📊", "Keyword Density", "Analyze keywords"),
        ("/schema-generator-online", "🧩", "Schema Generator", "Rich snippets"),
    ],
    "keyword-density-checker": [
        ("/word-counter", "📝", "Word Counter", "Count words"),
        ("/seo-meta-tag-generator", "🏷️", "Meta Tags", "Create meta tags"),
        ("/serp-preview", "🔎", "SERP Preview", "Google preview"),
    ],
    "keyword-research-tool": [
        ("/keyword-density-checker", "📊", "Keyword Density", "Analyze density"),
        ("/seo-meta-tag-generator", "🏷️", "Meta Tags", "Create meta tags"),
        ("/serp-preview", "🔎", "SERP Preview", "Google preview"),
    ],
    "schema-generator-online": [
        ("/seo-meta-tag-generator", "🏷️", "Meta Tag Generator", "SEO meta tags"),
        ("/serp-preview", "🔎", "SERP Preview", "Google preview"),
        ("/json-ld-generator", "🧩", "JSON-LD Generator", "Structured data"),
    ],
    "json-ld-generator": [
        ("/schema-generator-online", "🧩", "Schema Generator", "Rich snippets"),
        ("/seo-meta-tag-generator", "🏷️", "Meta Tags", "Create meta tags"),
        ("/serp-preview", "🔎", "SERP Preview", "Google preview"),
    ],
    "link-shortener": [
        ("/free-url-shortener-online", "🔗", "URL Shortener", "Shorten URLs"),
        ("/qr-code-generator", "🔳", "QR Generator", "Create QR codes"),
        ("/url-encoder-decoder", "🔗", "URL Encoder", "Encode URLs"),
    ],
    "free-url-shortener-online": [
        ("/link-shortener", "🔗", "Link Shortener", "Shorten any link"),
        ("/qr-code-generator", "🔳", "QR Generator", "Create QR codes"),
        ("/url-encoder-decoder", "🔗", "URL Encoder", "Encode/decode URLs"),
    ],
    "aspect-ratio-calculator": [
        ("/image-compressor", "🖼️", "Image Compressor", "Reduce image size"),
        ("/unit-converter", "📏", "Unit Converter", "Convert measurements"),
        ("/scientific-calculator", "🔬", "Scientific Calc", "Advanced math"),
    ],
    "time-zone-converter": [
        ("/age-calculator", "🎂", "Age Calculator", "Calculate your age"),
        ("/unit-converter", "📏", "Unit Converter", "Convert measurements"),
        ("/cron-expression-generator", "⏰", "Cron Builder", "Schedule jobs"),
    ],
    "cron-expression-generator": [
        ("/time-zone-converter", "🌐", "Time Zone", "Convert timezones"),
        ("/regex-tester", "🔍", "Regex Tester", "Test patterns"),
        ("/json-formatter", "{ }", "JSON Formatter", "Format JSON"),
    ],
    "ppf-calculator": [
        ("/sip-calculator", "📈", "SIP Calculator", "Mutual fund SIP"),
        ("/emi-calculator", "🏠", "EMI Calculator", "Loan EMI"),
        ("/gst-calculator", "🧾", "GST Calculator", "Tax calculation"),
    ],
    "loan-comparison-calculator": [
        ("/emi-calculator", "🏠", "EMI Calculator", "Calculate EMI"),
        ("/loan-eligibility-calculator", "✅", "Loan Eligibility", "Check eligibility"),
        ("/sip-calculator", "📈", "SIP Calculator", "Investment planning"),
    ],
    "loan-eligibility-calculator": [
        ("/emi-calculator", "🏠", "EMI Calculator", "Calculate EMI"),
        ("/loan-comparison-calculator", "📊", "Loan Comparison", "Compare loans"),
        ("/gst-calculator", "🧾", "GST Calculator", "Tax calculator"),
    ],
    "cgpa-calculator": [
        ("/percentage-calculator", "💯", "% Calculator", "Quick percentages"),
        ("/scientific-calculator", "🔬", "Scientific Calc", "Advanced math"),
        ("/age-calculator", "🎂", "Age Calculator", "Calculate your age"),
    ],
    "email-signature-generator": [
        ("/linkedin-creator-suite", "👔", "LinkedIn Suite", "LinkedIn tools"),
        ("/qr-code-generator", "🔳", "QR Generator", "QR for your email"),
        ("/seo-meta-tag-generator", "🏷️", "Meta Tags", "SEO essentials"),
    ],
    "linkedin-creator-suite": [
        ("/email-signature-generator", "✉️", "Email Signature", "Professional signature"),
        ("/word-counter", "📝", "Word Counter", "Count your copy"),
        ("/typing-speed-test", "⌨️", "Typing Speed", "Test WPM"),
    ],
    "exif-metadata-remover": [
        ("/image-compressor", "🖼️", "Image Compressor", "Reduce file size"),
        ("/image-converter", "🔄", "Image Converter", "Convert formats"),
        ("/background-remover", "✂️", "BG Remover", "Remove backgrounds"),
    ],
    "secure-password-generator-online": [
        ("/password-generator", "🔒", "Password Generator", "Quick passwords"),
        ("/hash-generator", "🔐", "Hash Generator", "MD5 SHA hashing"),
        ("/uuid-generator", "🆔", "UUID Generator", "Generate UUIDs"),
    ],
    "number-to-words-converter": [
        ("/roman-numerals-converter", "🏛️", "Roman Numerals", "Convert numerals"),
        ("/percentage-calculator", "💯", "% Calculator", "Quick percentages"),
        ("/scientific-calculator", "🔬", "Scientific Calc", "Advanced math"),
    ],
    "roman-numerals-converter": [
        ("/number-to-words-converter", "💬", "Number to Words", "Numbers in words"),
        ("/percentage-calculator", "💯", "% Calculator", "Quick math"),
        ("/scientific-calculator", "🔬", "Scientific Calc", "Advanced calculator"),
    ],
    "text-to-binary-converter": [
        ("/base64-encoder-decoder", "🔄", "Base64 Tools", "Encode/decode"),
        ("/hash-generator", "🔐", "Hash Generator", "Generate hashes"),
        ("/url-encoder-decoder", "🔗", "URL Encoder", "Encode URLs"),
    ],
    "video-to-gif": [
        ("/video-compressor", "📹", "Video Compressor", "Compress videos"),
        ("/video-to-mp3-converter", "🎵", "Video to MP3", "Extract audio"),
        ("/image-compressor", "🖼️", "Image Compressor", "Compress GIFs"),
    ],
    "video-to-mp3-converter": [
        ("/video-compressor", "📹", "Video Compressor", "Compress videos"),
        ("/video-to-gif", "🎞️", "Video to GIF", "Create GIFs"),
        ("/audio-to-text", "🎙️", "Audio to Text", "Transcribe audio"),
    ],
    "calculators-online": [  # category page
        ("/gst-calculator", "🧾", "GST Calculator", "Indian GST tool"),
        ("/emi-calculator", "🏠", "EMI Calculator", "Loan EMI calculator"),
        ("/sip-calculator", "📈", "SIP Calculator", "Investment planning"),
    ],
}

# ─── Guide button HTML ────────────────────────────────────────────────────────
def guide_button(guide_slug):
    return f'''<a href="/guides/{guide_slug}.html" class="nb-btn" style="background:#e9ddff;color:#000;border:2.5px solid #000;border-radius:12px;padding:0.85rem 1.75rem;font-weight:800;font-size:1rem;display:inline-flex;align-items:center;gap:0.5rem;box-shadow:4px 4px 0 #000;text-decoration:none;white-space:nowrap;" target="_blank" rel="noopener">📖 Read Full Guide</a>'''

# ─── Post-rec widget HTML ─────────────────────────────────────────────────────
def rec_widget(related):
    cards = ""
    for url, icon, name, desc in related:
        cards += f'''
    <a href="{url}" style="display:flex;flex-direction:column;align-items:center;text-align:center;padding:1.1rem 0.75rem;background:#fff;border:2.5px solid #000;border-radius:14px;text-decoration:none;color:#000;box-shadow:3px 3px 0 #000;transition:transform 0.15s,box-shadow 0.15s;flex:1;min-width:120px;">
      <div style="font-size:1.6rem;margin-bottom:0.4rem;">{icon}</div>
      <div style="font-weight:800;font-size:0.85rem;line-height:1.2;margin-bottom:0.2rem;">{name}</div>
      <div style="font-size:0.73rem;color:#666;line-height:1.3;">{desc}</div>
    </a>'''
    return f'''
  <!-- Post-Recommendation Widget -->
  <div style="margin-top:2rem;padding:1.5rem;background:#fff0b3;border:2.5px solid #000;border-radius:20px;box-shadow:4px 4px 0 #000;">
    <div style="font-family:'Syne',sans-serif;font-weight:900;font-size:1rem;margin-bottom:1rem;">💡 You Might Also Need</div>
    <div style="display:flex;gap:0.75rem;flex-wrap:wrap;">
{cards}
    </div>
  </div>'''

# ─── MAIN ─────────────────────────────────────────────────────────────────────
def process_file(src_path, dst_path, slug):
    with open(src_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Fix common.js version reference
    html = html.replace('common.js?v=4.0', 'common.js?v=6.0')
    html = html.replace('common.js?v=5.3', 'common.js?v=6.0')
    html = html.replace('style.css?v=4.0', 'style.css?v=6.0')
    html = html.replace('style.css?v=5.3', 'style.css?v=6.0')

    # 2. Add neo-brutalism.css link if missing
    if 'neo-brutalism.css' not in html and '<link href="/css/style.css' in html:
        html = html.replace(
            '<link href="/css/style.css?v=6.0" rel="stylesheet"/>',
            '<link href="/css/style.css?v=6.0" rel="stylesheet"/>\n<link href="/css/neo-brutalism.css?v=6.0" rel="stylesheet"/>'
        )

    # 3. Inject guide button if guide exists for this tool
    guide_slug = GUIDE_MAP.get(slug)
    if guide_slug and guide_slug is not None:
        btn_html = guide_button(guide_slug)
        # Insert AFTER the first .result-actions div's Copy/Share buttons
        # Strategy: find </div> after result-actions and inject before closing
        # We target the result-actions area and inject guide button inside it
        # Pattern: look for "result-actions" div and add button before closing </div>
        
        # Method: find the first occurrence of class="result-actions" and inject before its </div>
        pattern_actions = r'(class="result-actions"[^>]*>)(.*?)(</div>)'
        def inject_guide(m):
            return m.group(1) + m.group(2) + '\n        ' + btn_html + '\n      ' + m.group(3)
        
        new_html = re.sub(pattern_actions, inject_guide, html, count=1, flags=re.DOTALL)
        if new_html != html:
            html = new_html
        else:
            # Fallback: inject before </div><!-- /tool-container
            html = html.replace(
                '</div><!-- /tool-container -->',
                btn_html + '\n</div><!-- /tool-container -->', 
                1
            )

    # 4. Inject post-recommendation widget
    related = RELATED_MAP.get(slug)
    if related:
        rec_html = rec_widget(related)
        # Inject AFTER the result-hero/result-actions div, before SEO content
        # Target: inject before <!-- SEO CONTENT -->
        if '<!-- SEO CONTENT -->' in html:
            html = html.replace(
                '</div><!-- /tool-container -->',
                rec_html + '\n</div><!-- /tool-container -->',
                1
            )
        elif '</div><!-- /tool-container' not in html:
            # Try inserting before </main>
            html = html.replace('</main>', rec_html + '\n</main>', 1)

    # 5. Write to destination
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(html)

def main():
    files = [f for f in os.listdir(DES) if f.endswith(".html")]
    success = 0
    errors = []
    
    for fname in sorted(files):
        slug = fname.replace(".html", "")
        src = os.path.join(DES, fname)
        dst = os.path.join(ROOT, fname)
        
        try:
            process_file(src, dst, slug)
            success += 1
            print(f"  OK {fname}")
        except Exception as e:
            errors.append((fname, str(e)))
            print(f"  ERR {fname}: {e}")
    
    print(f"\n{'='*60}")
    print(f"Done: {success}/{len(files)} files processed")
    if errors:
        print(f"Errors ({len(errors)}):")
        for fname, err in errors:
            print(f"  - {fname}: {err}")

if __name__ == "__main__":
    main()
