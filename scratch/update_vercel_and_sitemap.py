#!/usr/bin/env python3
"""
update_vercel_and_sitemap.py
1. Adds missing URL aliases (2-3 per tool) to vercel.json rewrites
2. Adds .html -> clean URL redirects for all 70 tools
3. Regenerates sitemap.xml with all tool URLs + aliases
"""
import json, os, re
from datetime import datetime

ROOT = r"C:\Users\HP\Desktop\Projects Folder\world_of_tools"
VERCEL_PATH = os.path.join(ROOT, "vercel.json")
SITEMAP_PATH = os.path.join(ROOT, "sitemap.xml")
BASE_URL = "https://worldoftools.in"
TODAY = datetime.now().strftime("%Y-%m-%d")

# ─── All 70 tools with their extra URL aliases ────────────────────────────────
TOOL_ALIASES = {
    # Calculator tools
    "age-calculator": ["how-old-am-i", "age-calculator-by-dob", "age-from-date-of-birth"],
    "bmi-calculator": ["bmi-calculator-india", "body-weight-calculator"],
    "gst-calculator": ["tax-calculator-india", "cgst-sgst-calculator"],
    "emi-calculator": ["loan-emi-calculator", "car-loan-emi-calculator"],
    "sip-calculator": ["sip-return-calculator", "monthly-sip-calculator"],
    "ppf-calculator": ["ppf-maturity-calculator", "ppf-interest-calculator"],
    "percentage-calculator": ["percent-calculator-online", "find-percentage-calculator"],
    "scientific-calculator": ["advanced-calculator-online", "engineering-calculator-free"],
    "cgpa-calculator": ["cgpa-percentage-calculator", "university-grade-calculator"],
    "loan-comparison-calculator": ["compare-home-loan", "loan-interest-rate-comparison"],
    "loan-eligibility-calculator": ["personal-loan-eligibility", "home-loan-eligibility-calculator"],
    
    # Text & content tools
    "word-counter": ["words-in-text", "free-word-count-tool"],
    "case-converter": ["convert-text-case", "sentence-case-converter"],
    "fancy-font-generator": ["instagram-fonts-generator", "stylish-text-copy-paste"],
    "lorem-ipsum-generator": ["dummy-text-generator", "placeholder-text-generator"],
    "number-to-words-converter": ["number-in-words-english", "numbers-to-english-words"],
    "roman-numerals-converter": ["convert-to-roman-numerals", "roman-number-calculator"],
    "text-compare-tool": ["online-text-diff-checker", "compare-text-online-free"],
    "typing-speed-test": ["wpm-speed-test", "free-typing-test-online"],
    "audio-to-text": ["speech-to-text-converter", "audio-transcription-free"],
    "markdown-to-html": ["markdown-converter-online", "md-to-html-free"],
    "text-to-binary-converter": ["binary-converter-online", "text-binary-ascii"],
    
    # SEO tools
    "seo-meta-tag-generator": ["open-graph-tag-generator", "html-meta-tags-generator"],
    "keyword-density-checker": ["keyword-density-analyzer", "seo-content-analyzer"],
    "keyword-research-tool": ["keyword-planner-free", "keyword-ideas-generator"],
    "schema-generator-online": ["structured-data-generator", "rich-snippet-generator"],
    "serp-preview": ["google-search-preview", "meta-title-preview-tool"],
    "json-ld-generator": ["json-ld-schema-generator", "schema-org-generator"],
    "link-shortener": ["custom-link-shortener", "short-url-generator-free"],
    "free-url-shortener-online": ["url-shortener-without-ads", "shorten-url-free"],
    "linkedin-creator-suite": ["linkedin-post-generator", "linkedin-formatting-tool"],
    
    # Developer tools
    "json-formatter": ["minify-json-online", "json-viewer-online"],
    "jwt-decoder": ["jwt-parser-online", "decode-jwt-token-online"],
    "hash-generator": ["checksum-generator-online", "file-hash-calculator"],
    "base64-encoder-decoder": ["base64-image-encoder", "decode-base64-string"],
    "url-encoder-decoder": ["percent-encode-url", "decode-url-percent-encoding"],
    "regex-tester": ["regular-expression-tester", "regex-validator-online"],
    "sql-formatter": ["sql-query-beautifier", "format-sql-query-online"],
    "xml-formatter": ["xml-validator-online", "xml-beautifier-free"],
    "csv-to-json": ["csv-converter-online", "spreadsheet-to-json"],
    "css-minifier": ["minify-css-online", "css-compressor-free"],
    "css-gradient-generator": ["gradient-background-generator", "css3-gradient-maker"],
    "cron-expression-generator": ["cron-schedule-generator", "cron-syntax-builder"],
    "uuid-generator": ["guid-generator-online", "generate-uuid-online"],
    "random-number-generator": ["random-number-picker", "number-randomizer-online"],
    "password-generator": ["secure-password-maker", "random-password-creator"],
    "secure-password-generator-online": ["passphrase-generator", "complex-password-generator"],
    
    # Image & media tools
    "image-compressor": ["jpg-compressor-online", "reduce-image-size-free"],
    "image-converter": ["png-to-jpg-converter", "convert-heic-to-jpg"],
    "image-upscaler": ["ai-image-enlarger", "upscale-photo-online-free"],
    "background-remover": ["cut-out-background-online", "remove-image-background-free"],
    "remove-watermark-from-image": ["remove-text-from-image", "photo-watermark-eraser"],
    "exif-metadata-remover": ["photo-metadata-cleaner", "strip-exif-data-online"],
    "favicon-generator": ["ico-file-creator", "website-icon-generator"],
    "color-converter": ["hex-to-rgb-converter", "rgb-to-hsl-converter"],
    "aspect-ratio-calculator": ["image-resize-calculator", "16-9-ratio-calculator"],
    "barcode-generator": ["ean13-barcode-generator", "code128-barcode-maker"],
    "qr-code-generator": ["create-qr-code-free", "wifi-qr-code-generator"],
    "youtube-thumbnail-downloader": ["youtube-thumbnail-extractor", "yt-thumbnail-saver"],
    "image-to-text-ocr": ["photo-to-text-converter", "extract-text-from-image"],
    
    # Video tools
    "video-compressor": ["compress-mp4-online-free", "reduce-video-file-size"],
    "video-to-gif": ["convert-video-to-gif", "mp4-to-gif-online"],
    "video-to-mp3-converter": ["extract-audio-from-video", "mp4-to-mp3-converter"],
    
    # Web & utility
    "ip-address-lookup": ["my-ip-address-finder", "ip-geolocation-checker"],
    "time-zone-converter": ["world-clock-converter", "timezone-calculator-online"],
    "unit-converter": ["measurement-converter-online", "metric-imperial-converter"],
    "invoice-generator": ["free-gst-invoice-maker", "create-invoice-pdf-free"],
    "thermal-label-maker": ["shipping-label-generator", "zebra-label-template-free"],
    "email-signature-generator": ["gmail-signature-maker", "professional-email-signature"],
}

# ─── Load existing vercel.json ─────────────────────────────────────────────────
with open(VERCEL_PATH, "r", encoding="utf-8") as f:
    vercel = json.load(f)

existing_sources = set()
for item in vercel.get("rewrites", []):
    existing_sources.add(item["source"])
for item in vercel.get("redirects", []):
    existing_sources.add(item["source"])

# ─── Build new rewrites for missing aliases ────────────────────────────────────
new_rewrites = []
for tool, aliases in TOOL_ALIASES.items():
    for alias in aliases:
        src = f"/{alias}"
        if src not in existing_sources:
            new_rewrites.append({"source": src, "destination": f"/{tool}"})
            existing_sources.add(src)

# ─── Build .html → clean URL redirects for all 70 tools ───────────────────────
all_tools = list(TOOL_ALIASES.keys())
new_redirects = []
for tool in all_tools:
    src = f"/{tool}.html"
    if src not in existing_sources:
        new_redirects.append({"source": src, "destination": f"/{tool}", "permanent": True})
        existing_sources.add(src)

# Merge into vercel.json
vercel["rewrites"] = vercel.get("rewrites", []) + new_rewrites
vercel["redirects"] = vercel.get("redirects", []) + new_redirects

with open(VERCEL_PATH, "w", encoding="utf-8") as f:
    json.dump(vercel, f, indent=4)

print(f"vercel.json: added {len(new_rewrites)} rewrites, {len(new_redirects)} redirects")

# ─── Generate sitemap.xml ──────────────────────────────────────────────────────
# Priority/changefreq config
TOOL_PRIORITY = "0.8"
GUIDE_PRIORITY = "0.6"
ALIAS_PRIORITY = "0.5"
HOME_PRIORITY = "1.0"

urls = []

# Homepage
urls.append({
    "loc": f"{BASE_URL}/",
    "changefreq": "daily",
    "priority": HOME_PRIORITY,
    "lastmod": TODAY,
})

# Category pages
for cat in ["calculators-online", "developer-tools-online", "seo-tools-free", "text-tools-online", "web-utilities-free"]:
    urls.append({"loc": f"{BASE_URL}/{cat}", "changefreq": "weekly", "priority": "0.7", "lastmod": TODAY})

# Guides index
urls.append({"loc": f"{BASE_URL}/guides/", "changefreq": "weekly", "priority": "0.7", "lastmod": TODAY})

# All 70 tools (main URLs)
for tool in all_tools:
    urls.append({
        "loc": f"{BASE_URL}/{tool}",
        "changefreq": "monthly",
        "priority": TOOL_PRIORITY,
        "lastmod": TODAY,
    })

# Tool aliases (secondary URLs)
for tool, aliases in TOOL_ALIASES.items():
    for alias in aliases[:2]:  # Only top 2 aliases in sitemap
        urls.append({
            "loc": f"{BASE_URL}/{alias}",
            "changefreq": "monthly",
            "priority": ALIAS_PRIORITY,
            "lastmod": TODAY,
        })

# All guides
guides_dir = os.path.join(ROOT, "guides")
guide_files = [f for f in os.listdir(guides_dir) if f.endswith(".html") and f != "index.html" and not f.startswith("guide-template")]
for gf in sorted(guide_files):
    slug = gf.replace(".html", "")
    urls.append({
        "loc": f"{BASE_URL}/guides/{slug}",
        "changefreq": "monthly",
        "priority": GUIDE_PRIORITY,
        "lastmod": TODAY,
    })

# Static pages
for page in ["about-us", "contact-us", "privacy", "terms"]:
    urls.append({"loc": f"{BASE_URL}/{page}", "changefreq": "monthly", "priority": "0.4", "lastmod": TODAY})

# Build XML
xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
xml_lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"')
xml_lines.append('        xmlns:xhtml="http://www.w3.org/1999/xhtml">')

for u in urls:
    xml_lines.append("  <url>")
    xml_lines.append(f"    <loc>{u['loc']}</loc>")
    xml_lines.append(f"    <lastmod>{u['lastmod']}</lastmod>")
    xml_lines.append(f"    <changefreq>{u['changefreq']}</changefreq>")
    xml_lines.append(f"    <priority>{u['priority']}</priority>")
    xml_lines.append("  </url>")

xml_lines.append("</urlset>")

sitemap_content = "\n".join(xml_lines)
with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"sitemap.xml: {len(urls)} URLs written")
print("Done!")
