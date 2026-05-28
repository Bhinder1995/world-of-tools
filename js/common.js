/**
 * WorldOfTools — common.js v6.1
 * Fixes: dropdown click, guide buttons, post-rec timing, footer, related tools dedup
 */

// ─── Tool → Guide slug mapping ───────────────────────────────────────────────
const GUIDE_MAP = {
  "age-calculator":                "age-calculator-guide",
  "aspect-ratio-calculator":       "aspect-ratio-calculator-guide",
  "audio-to-text":                 "audio-to-text-guide",
  "background-remover":            "background-remover-guide",
  "barcode-generator":             "barcode-generator-guide",
  "base64-encoder-decoder":        "base64-encoder-decoder-guide",
  "bank-statement-analyzer":       "bank-statement-analyzer-guide",
  "bmi-calculator":                "bmi-calculator-guide",
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
  "free-url-shortener-online":                "link-shortener-guide",
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
};

// ─── Related tools map (3 per tool — post-rec widget) ────────────────────────
const POST_REC_MAP = {
  "bank-statement-analyzer": [["/emi-calculator","🏠","EMI Calculator","Loan EMI breakdown"],["/sip-calculator","📈","SIP Calculator","Investment returns"],["/gst-calculator","🧾","GST Calculator","Tax tools"]],
  "age-calculator":          [["/bmi-calculator","⚖️","BMI Calculator","Body mass index"],["/gst-calculator","🧾","GST Calculator","Tax calculations"],["/percentage-calculator","💯","% Calculator","Quick percentages"]],
  "gst-calculator":          [["/emi-calculator","🏠","EMI Calculator","Loan EMI breakdown"],["/sip-calculator","📈","SIP Calculator","Investment returns"],["/invoice-generator","🧾","Invoice Maker","PDF invoices"]],
  "emi-calculator":          [["/gst-calculator","🧾","GST Calculator","Tax tool"],["/sip-calculator","📈","SIP Calculator","Mutual fund SIP"],["/loan-comparison-calculator","📊","Loan Compare","Best loan offer"]],
  "sip-calculator":          [["/emi-calculator","🏠","EMI Calculator","Loan EMI"],["/ppf-calculator","🏦","PPF Calculator","PPF returns"],["/percentage-calculator","💯","% Calculator","Quick math"]],
  "bmi-calculator":          [["/age-calculator","🎂","Age Calculator","Your exact age"],["/percentage-calculator","💯","% Calculator","Quick calc"],["/scientific-calculator","🔬","Scientific Calc","Advanced math"]],
  "image-compressor":        [["/image-converter","🔄","Image Converter","Convert formats"],["/background-remover","✂️","BG Remover","Remove background"],["/image-upscaler","🔭","AI Upscaler","Upscale to 4K"]],
  "video-compressor":        [["/video-to-gif","🎞️","Video to GIF","Create GIFs"],["/video-to-mp3-converter","🎵","Video to MP3","Extract audio"],["/image-compressor","🖼️","Image Compressor","Compress images"]],
  "word-counter":            [["/case-converter","🔠","Case Converter","Text case tools"],["/lorem-ipsum-generator","📄","Lorem Ipsum","Placeholder text"],["/keyword-density-checker","📊","Keyword Density","SEO analysis"]],
  "json-formatter":          [["/jwt-decoder","🔑","JWT Decoder","Decode JWT tokens"],["/csv-to-json","📊","CSV to JSON","Convert CSV"],["/xml-formatter","🛠️","XML Formatter","Beautify XML"]],
  "password-generator":      [["/hash-generator","🔐","Hash Generator","MD5 SHA-256"],["/uuid-generator","🆔","UUID Generator","Generate UUIDs"],["/base64-encoder-decoder","🔄","Base64 Tools","Encode/decode"]],
  "qr-code-generator":       [["/barcode-generator","🏷️","Barcode Generator","CODE128 EAN"],["/free-url-shortener-online","🔗","Link Shortener","Shorten URLs"],["/image-compressor","🖼️","Image Compressor","Compress images"]],
  "ip-address-lookup":       [["/url-encoder-decoder","🔗","URL Encoder","Encode URLs"],["/hash-generator","🔐","Hash Generator","Secure hashing"],["/jwt-decoder","🔑","JWT Decoder","Decode JWT"]],
  "case-converter":          [["/word-counter","📝","Word Counter","Count words"],["/lorem-ipsum-generator","📄","Lorem Ipsum","Placeholder text"],["/markdown-to-html","📑","Markdown HTML","Convert markdown"]],
  "hash-generator":          [["/password-generator","🔒","Password Gen","Strong passwords"],["/base64-encoder-decoder","🔄","Base64 Tools","Encode/decode"],["/jwt-decoder","🔑","JWT Decoder","Decode JWT"]],
  "base64-encoder-decoder":  [["/hash-generator","🔐","Hash Generator","MD5 SHA"],["/url-encoder-decoder","🔗","URL Encoder","Encode URLs"],["/jwt-decoder","🔑","JWT Decoder","Full JWT inspector"]],
  "jwt-decoder":             [["/hash-generator","🔐","Hash Generator","Cryptographic hash"],["/base64-encoder-decoder","🔄","Base64 Tools","Encode decode"],["/password-generator","🔒","Password Gen","Secure passwords"]],
  "image-converter":         [["/image-compressor","🖼️","Image Compressor","Reduce file size"],["/background-remover","✂️","BG Remover","Remove backgrounds"],["/favicon-generator","🖼️","Favicon Maker","Create favicons"]],
  "background-remover":      [["/image-compressor","🖼️","Image Compressor","Compress images"],["/image-upscaler","🔭","AI Upscaler","Upscale images"],["/image-converter","🔄","Image Converter","Convert formats"]],
  "image-upscaler":          [["/background-remover","✂️","BG Remover","Remove backgrounds"],["/image-compressor","🖼️","Image Compressor","Reduce file size"],["/remove-watermark-from-image","🧹","Remove Watermark","AI watermark erasure"]],
  "url-encoder-decoder":     [["/base64-encoder-decoder","🔄","Base64 Tools","Encode/decode"],["/hash-generator","🔐","Hash Generator","MD5 SHA"],["/jwt-decoder","🔑","JWT Decoder","Decode JWT"]],
  "percentage-calculator":   [["/scientific-calculator","🔬","Scientific Calc","Advanced math"],["/gst-calculator","🧾","GST Calculator","Tax tool"],["/emi-calculator","🏠","EMI Calculator","Loan EMI"]],
  "scientific-calculator":   [["/percentage-calculator","💯","% Calculator","Quick math"],["/bmi-calculator","⚖️","BMI Calculator","Health index"],["/unit-converter","📏","Unit Converter","Convert measurements"]],
  "unit-converter":          [["/scientific-calculator","🔬","Scientific Calc","Advanced calculator"],["/aspect-ratio-calculator","📐","Aspect Ratio","Image dimensions"],["/percentage-calculator","💯","% Calculator","Quick percentages"]],
  "audio-to-text":           [["/word-counter","📝","Word Counter","Analyze transcript"],["/case-converter","🔠","Case Converter","Format text"],["/markdown-to-html","📑","Markdown HTML","Format content"]],
  "text-compare-tool":       [["/word-counter","📝","Word Counter","Count words"],["/case-converter","🔠","Case Converter","Change case"],["/markdown-to-html","📑","Markdown HTML","Convert markdown"]],
  "lorem-ipsum-generator":   [["/word-counter","📝","Word Counter","Count your words"],["/case-converter","🔠","Case Converter","Change text case"],["/markdown-to-html","📑","Markdown HTML","Convert markdown"]],
  "fancy-font-generator":    [["/case-converter","🔠","Case Converter","Change text case"],["/word-counter","📝","Word Counter","Count words"],["/qr-code-generator","🔳","QR Generator","Create QR codes"]],
  "typing-speed-test":       [["/word-counter","📝","Word Counter","Count words"],["/case-converter","🔠","Case Converter","Text case tools"],["/lorem-ipsum-generator","📄","Lorem Ipsum","Practice text"]],
  "barcode-generator":       [["/qr-code-generator","🔳","QR Generator","Create QR codes"],["/thermal-label-maker","🖨️","Label Maker","Thermal labels"],["/invoice-generator","🧾","Invoice Maker","PDF invoices"]],
  "invoice-generator":       [["/gst-calculator","🧾","GST Calculator","Calculate GST"],["/emi-calculator","🏠","EMI Calculator","Loan EMI"],["/barcode-generator","🏷️","Barcode Generator","Barcodes"]],
  "image-to-text-ocr":       [["/word-counter","📝","Word Counter","Count extracted words"],["/case-converter","🔠","Case Converter","Format text"],["/audio-to-text","🎙️","Audio to Text","Transcribe audio"]],
  "youtube-thumbnail-downloader": [["/image-compressor","🖼️","Image Compressor","Compress thumbnails"],["/image-converter","🔄","Image Converter","Convert formats"],["/background-remover","✂️","BG Remover","Edit thumbnails"]],
  "regex-tester":            [["/json-formatter","{}","JSON Formatter","Beautify JSON"],["/text-compare-tool","⚖️","Text Compare","Diff texts"],["/csv-to-json","📊","CSV to JSON","Convert CSV"]],
  "sql-formatter":           [["/json-formatter","{}","JSON Formatter","Beautify JSON"],["/xml-formatter","🛠️","XML Formatter","Beautify XML"],["/csv-to-json","📊","CSV to JSON","Convert CSV"]],
  "xml-formatter":           [["/json-formatter","{}","JSON Formatter","Beautify JSON"],["/sql-formatter","🗄️","SQL Formatter","Format SQL"],["/csv-to-json","📊","CSV to JSON","CSV conversion"]],
  "csv-to-json":             [["/json-formatter","{}","JSON Formatter","Beautify JSON"],["/xml-formatter","🛠️","XML Formatter","Format XML"],["/sql-formatter","🗄️","SQL Formatter","Format SQL"]],
  "css-minifier":            [["/css-gradient-generator","🎨","CSS Gradient","Create gradients"],["/json-formatter","{}","JSON Formatter","Format JSON"],["/markdown-to-html","📑","Markdown HTML","Convert markdown"]],
  "css-gradient-generator":  [["/css-minifier","🗜️","CSS Minifier","Compress CSS"],["/color-converter","🎨","Color Converter","HEX RGB HSL"],["/favicon-generator","🖼️","Favicon Maker","Create favicons"]],
  "color-converter":         [["/css-gradient-generator","🎨","CSS Gradient","Create gradients"],["/image-converter","🔄","Image Converter","Convert formats"],["/favicon-generator","🖼️","Favicon Maker","Create favicons"]],
  "favicon-generator":       [["/image-compressor","🖼️","Image Compressor","Compress images"],["/image-converter","🔄","Image Converter","Convert formats"],["/css-gradient-generator","🎨","CSS Gradient","Create gradients"]],
  "uuid-generator":          [["/password-generator","🔒","Password Gen","Secure passwords"],["/hash-generator","🔐","Hash Generator","MD5 SHA"],["/random-number-generator","🎲","Random Numbers","Generate numbers"]],
  "random-number-generator": [["/uuid-generator","🆔","UUID Generator","Generate UUIDs"],["/password-generator","🔒","Password Gen","Strong passwords"],["/hash-generator","🔐","Hash Generator","Cryptographic hash"]],
  "markdown-to-html":        [["/word-counter","📝","Word Counter","Count words"],["/css-minifier","🗜️","CSS Minifier","Minify CSS"],["/json-formatter","{}","JSON Formatter","Format JSON"]],
  "seo-meta-tag-generator":  [["/serp-preview","🔎","SERP Preview","Preview in Google"],["/keyword-density-checker","📊","Keyword Density","Analyze keywords"],["/schema-generator-online","🧩","Schema Generator","Rich snippets"]],
  "serp-preview":            [["/seo-meta-tag-generator","🏷️","Meta Tag Generator","Create SEO tags"],["/keyword-density-checker","📊","Keyword Density","Analyze keywords"],["/schema-generator-online","🧩","Schema Generator","Rich snippets"]],
  "keyword-density-checker": [["/word-counter","📝","Word Counter","Count words"],["/seo-meta-tag-generator","🏷️","Meta Tags","Create meta tags"],["/serp-preview","🔎","SERP Preview","Google preview"]],
  "keyword-research-tool":   [["/keyword-density-checker","📊","Keyword Density","Analyze density"],["/seo-meta-tag-generator","🏷️","Meta Tags","Create meta tags"],["/serp-preview","🔎","SERP Preview","Google preview"]],
  "schema-generator-online": [["/seo-meta-tag-generator","🏷️","Meta Tag Generator","SEO meta tags"],["/serp-preview","🔎","SERP Preview","Google preview"],["/json-ld-generator","🧩","JSON-LD Generator","Structured data"]],
  "free-url-shortener-online":          [["/free-url-shortener-online","🔗","URL Shortener","Shorten URLs"],["/qr-code-generator","🔳","QR Generator","Create QR codes"],["/url-encoder-decoder","🔗","URL Encoder","Encode URLs"]],
  "free-url-shortener-online":[["/free-url-shortener-online","🔗","Link Shortener","Shorten any link"],["/qr-code-generator","🔳","QR Generator","Create QR codes"],["/url-encoder-decoder","🔗","URL Encoder","Encode/decode URLs"]],
  "aspect-ratio-calculator": [["/image-compressor","🖼️","Image Compressor","Reduce image size"],["/unit-converter","📏","Unit Converter","Convert measurements"],["/scientific-calculator","🔬","Scientific Calc","Advanced math"]],
  "time-zone-converter":     [["/age-calculator","🎂","Age Calculator","Calculate your age"],["/unit-converter","📏","Unit Converter","Convert measurements"],["/cron-expression-generator","⏰","Cron Builder","Schedule jobs"]],
  "cron-expression-generator":[["/time-zone-converter","🌐","Time Zone","Convert timezones"],["/regex-tester","🔍","Regex Tester","Test patterns"],["/json-formatter","{}","JSON Formatter","Format JSON"]],
  "ppf-calculator":          [["/sip-calculator","📈","SIP Calculator","Mutual fund SIP"],["/emi-calculator","🏠","EMI Calculator","Loan EMI"],["/gst-calculator","🧾","GST Calculator","Tax calculation"]],
  "loan-comparison-calculator":[["/emi-calculator","🏠","EMI Calculator","Calculate EMI"],["/loan-eligibility-calculator","✅","Loan Eligibility","Check eligibility"],["/sip-calculator","📈","SIP Calculator","Investment planning"]],
  "loan-eligibility-calculator":[["/emi-calculator","🏠","EMI Calculator","Calculate EMI"],["/loan-comparison-calculator","📊","Loan Comparison","Compare loans"],["/gst-calculator","🧾","GST Calculator","Tax calculator"]],
  "cgpa-calculator":         [["/percentage-calculator","💯","% Calculator","Quick percentages"],["/scientific-calculator","🔬","Scientific Calc","Advanced math"],["/age-calculator","🎂","Age Calculator","Calculate your age"]],
  "email-signature-generator":[["/linkedin-creator-suite","👔","LinkedIn Suite","LinkedIn tools"],["/qr-code-generator","🔳","QR Generator","QR for email"],["/seo-meta-tag-generator","🏷️","Meta Tags","SEO essentials"]],
  "linkedin-creator-suite":  [["/email-signature-generator","✉️","Email Signature","Professional signature"],["/word-counter","📝","Word Counter","Count your copy"],["/typing-speed-test","⌨️","Typing Speed","Test WPM"]],
  "exif-metadata-remover":   [["/image-compressor","🖼️","Image Compressor","Reduce file size"],["/image-converter","🔄","Image Converter","Convert formats"],["/background-remover","✂️","BG Remover","Remove backgrounds"]],
  "secure-password-generator-online":[["/password-generator","🔒","Password Generator","Quick passwords"],["/hash-generator","🔐","Hash Generator","MD5 SHA"],["/uuid-generator","🆔","UUID Generator","Generate UUIDs"]],
  "number-to-words-converter":[["/roman-numerals-converter","🏛️","Roman Numerals","Convert numerals"],["/percentage-calculator","💯","% Calculator","Quick percentages"],["/scientific-calculator","🔬","Scientific Calc","Advanced math"]],
  "roman-numerals-converter": [["/number-to-words-converter","💬","Number in Words","Numbers to words"],["/percentage-calculator","💯","% Calculator","Quick math"],["/scientific-calculator","🔬","Scientific Calc","Advanced calculator"]],
  "text-to-binary-converter": [["/base64-encoder-decoder","🔄","Base64 Tools","Encode/decode"],["/hash-generator","🔐","Hash Generator","Generate hashes"],["/url-encoder-decoder","🔗","URL Encoder","Encode URLs"]],
  "video-to-gif":            [["/video-compressor","📹","Video Compressor","Compress videos"],["/video-to-mp3-converter","🎵","Video to MP3","Extract audio"],["/image-compressor","🖼️","Image Compressor","Compress GIFs"]],
  "video-to-mp3-converter":  [["/video-compressor","📹","Video Compressor","Compress videos"],["/video-to-gif","🎞️","Video to GIF","Create GIFs"],["/audio-to-text","🎙️","Audio to Text","Transcribe audio"]],
  "json-ld-generator":       [["/schema-generator-online","🧩","Schema Generator","Rich snippets"],["/seo-meta-tag-generator","🏷️","Meta Tags","Create meta tags"],["/serp-preview","🔎","SERP Preview","Google preview"]],
  "remove-watermark-from-image":[["/background-remover","✂️","BG Remover","Remove backgrounds"],["/image-upscaler","🔭","AI Upscaler","AI upscaling"],["/image-compressor","🖼️","Image Compressor","Compress images"]],
  "thermal-label-maker":     [["/barcode-generator","🏷️","Barcode Generator","CODE128 EAN"],["/qr-code-generator","🔳","QR Generator","Create QR codes"],["/invoice-generator","🧾","Invoice Maker","PDF invoices"]],
};

// ─────────────────────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
    injectHeader();
    injectFooter();
    registerServiceWorker();
    highlightActiveLink();
    injectGuideButton();
    injectPostRecWidget();
    trackRecentTool();
    initScrollHeader();
    dedupRelatedTools();
});

// ── SCROLL-AWARE HEADER ───────────────────────────────────────────────────────
function initScrollHeader() {
    const nav = document.querySelector('.nav-container');
    if (!nav) return;
    window.addEventListener('scroll', () => {
        if (window.scrollY > 60) nav.classList.add('nav-scrolled');
        else nav.classList.remove('nav-scrolled');
    }, { passive: true });
}

// ── HEADER INJECTION ─────────────────────────────────────────────────────────
function injectHeader() {
    const headerHTML = `
        <nav class="nav-container" role="navigation" aria-label="Main navigation">
            <div class="nav-inner">
                <a href="/" class="nav-logo" aria-label="WorldOfTools Home">
                    <span class="nav-logo-mark">W</span>
                    <div class="nav-logo-text">
                        <div class="nav-logo-name">WorldOfTools</div>
                        <div class="nav-logo-tag">The Playful Powerhouse ✦</div>
                    </div>
                </a>

                <nav id="main-nav" class="nav-links-wrap" aria-label="Tool categories">
                    <ul class="nav-ul">
                        <li class="nav-dropdown-wrap" id="tools-dropdown-wrap">
                            <button class="nav-link dropdown-trigger" id="tools-dropdown-btn" aria-expanded="false" aria-haspopup="true" type="button">
                                All Tools
                                <svg width="11" height="7" viewBox="0 0 11 7" fill="none" class="dd-arrow"><path d="M1 1l4.5 4.5L10 1" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
                            </button>
                            <div class="mega-dropdown" id="mega-dropdown" role="region">
                                <div class="dropdown-inner">
                                    <div class="dropdown-col">
                                        <h4><span>🧮</span> Calculators</h4>
                                        <a href="/bank-statement-analyzer">Statement Analyzer</a>
                                        <a href="/sip-calculator">SIP Calculator</a>
                                        <a href="/gst-calculator">GST Calculator</a>
                                        <a href="/emi-calculator">EMI Calculator</a>
                                        <a href="/age-calculator">Age Calculator</a>
                                        <a href="/bmi-calculator">BMI Calculator</a>
                                        <a href="/ppf-calculator">PPF Calculator</a>
                                        <a href="/calculators-online" class="view-all">View All Calculators →</a>
                                    </div>
                                    <div class="dropdown-col">
                                        <h4><span>🛠️</span> Dev Tools</h4>
                                        <a href="/json-formatter">JSON Formatter</a>
                                        <a href="/jwt-decoder">JWT Decoder</a>
                                        <a href="/sql-formatter">SQL Formatter</a>
                                        <a href="/hash-generator">Hash Generator</a>
                                        <a href="/password-generator">Password Gen</a>
                                        <a href="/regex-tester">Regex Tester</a>
                                        <a href="/developer-tools-online" class="view-all">View All Dev Tools →</a>
                                    </div>
                                    <div class="dropdown-col">
                                        <h4><span>📝</span> SEO &amp; Text</h4>
                                        <a href="/word-counter">Word Counter</a>
                                        <a href="/case-converter">Case Converter</a>
                                        <a href="/keyword-research-tool">Keyword Tool</a>
                                        <a href="/seo-meta-tag-generator">Meta Tags</a>
                                        <a href="/serp-preview">SERP Preview</a>
                                        <a href="/fancy-font-generator">Fancy Fonts</a>
                                        <a href="/text-tools-online" class="view-all">View All Text Tools →</a>
                                    </div>
                                    <div class="dropdown-col">
                                        <h4><span>🖼️</span> Image &amp; Media</h4>
                                        <a href="/image-compressor">Image Compressor</a>
                                        <a href="/video-compressor">Video Compressor</a>
                                        <a href="/background-remover">BG Remover</a>
                                        <a href="/image-upscaler">AI Upscaler</a>
                                        <a href="/image-converter">Image Converter</a>
                                        <a href="/free-url-shortener-online">URL Shortener</a>
                                        <a href="/thermal-label-maker">Label Maker</a>
                                        <a href="/web-utilities-free" class="view-all">View All Utilities →</a>
                                    </div>
                                </div>
                                <div class="dropdown-promo">
                                    <span>⚡ All 70+ tools — 100% free, private &amp; instant</span>
                                    <a href="/">Browse All →</a>
                                </div>
                            </div>
                        </li>
                        <li><a href="/guides/" class="nav-link">📖 Guides</a></li>
                        <li><a href="/calculators-online" class="nav-link hide-tablet">Calculators</a></li>
                        <li><a href="/developer-tools-online" class="nav-link hide-tablet">Dev Tools</a></li>
                    </ul>
                </nav>

                <div class="nav-right">
                    <a href="/" class="nav-free-badge hide-mobile">🎉 100% Free</a>
                    <button class="menu-toggle" id="mobile-menu-btn" aria-label="Toggle menu" type="button">
                        <span class="hamburger-line"></span>
                        <span class="hamburger-line"></span>
                        <span class="hamburger-line"></span>
                    </button>
                </div>
            </div>
        </nav>
        <div class="header-spacer"></div>
        <style>
            .nav-container { position:fixed; top:0; left:0; width:100%; z-index:9999; background:#fff; border-bottom:3px solid #000; transition:box-shadow 0.25s; }
            .nav-container.nav-scrolled { box-shadow:0 4px 0 #000; background:rgba(255,255,255,0.97); backdrop-filter:blur(8px); }
            .nav-inner { display:flex; justify-content:space-between; align-items:center; padding:0 1.5rem; max-width:1280px; margin:0 auto; height:68px; }
            .nav-logo { display:flex; align-items:center; gap:0.65rem; text-decoration:none; flex-shrink:0; }
            .nav-logo-mark { width:36px; height:36px; background:#ffe066; border:2.5px solid #000; border-radius:9px; box-shadow:3px 3px 0 #000; display:flex; align-items:center; justify-content:center; font-family:'Syne',sans-serif; font-weight:900; font-size:1.25rem; color:#000; flex-shrink:0; transition:transform 0.15s,box-shadow 0.15s; }
            .nav-logo:hover .nav-logo-mark { transform:translate(-1px,-1px); box-shadow:4px 4px 0 #000; }
            .nav-logo-name { font-family:'Syne',sans-serif; font-weight:800; font-size:1.15rem; color:#000; line-height:1; letter-spacing:-0.01em; }
            .nav-logo-tag { font-size:0.55rem; font-weight:700; color:#ff6b9d; letter-spacing:0.07em; text-transform:uppercase; font-family:'Space Grotesk',sans-serif; }
            .nav-ul { display:flex; list-style:none; margin:0; padding:0; align-items:center; gap:0.15rem; }
            .nav-link { display:inline-flex; align-items:center; gap:0.3rem; padding:0.5rem 0.85rem; background:transparent; border:none; cursor:pointer; font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:0.88rem; color:#111; text-decoration:none; border-radius:8px; transition:background 0.15s; white-space:nowrap; }
            .nav-link:hover { background:#f5f5f5; }
            .dd-arrow { transition:transform 0.2s; flex-shrink:0; }
            /* ── DROPDOWN — click-based, NO hover ── */
            .nav-dropdown-wrap { position:relative; }
            .mega-dropdown { display:none; position:absolute; top:calc(100% + 12px); left:50%; transform:translateX(-50%); background:#fff; border:2.5px solid #000; border-radius:18px; box-shadow:8px 8px 0 #000; padding:1.5rem; width:780px; max-width:92vw; z-index:10000; animation:ddIn 0.15s ease-out; }
            .mega-dropdown.is-open { display:block; }
            @keyframes ddIn { from{opacity:0;transform:translateX(-50%) translateY(-6px)} to{opacity:1;transform:translateX(-50%) translateY(0)} }
            .dropdown-inner { display:grid; grid-template-columns:repeat(4,1fr); gap:1.25rem; margin-bottom:1rem; }
            .dropdown-col h4 { font-family:'Syne',sans-serif; font-size:0.68rem; text-transform:uppercase; margin:0 0 0.75rem; color:#555; letter-spacing:0.06rem; font-weight:900; display:flex; align-items:center; gap:0.3rem; }
            .dropdown-col a { display:block; text-decoration:none; color:#111; font-weight:600; font-size:0.875rem; margin-bottom:0.5rem; padding:0.3rem 0.5rem; border-radius:7px; transition:background 0.1s,transform 0.1s; font-family:'Space Grotesk',sans-serif; }
            .dropdown-col a:hover { background:#f0f0f0; transform:translateX(3px); color:#ff6b9d; }
            .dropdown-col a.view-all { margin-top:0.6rem; color:#4f46e5; font-weight:800; font-size:0.72rem; text-transform:uppercase; letter-spacing:0.04em; background:none; padding-left:0; }
            .dropdown-col a.view-all:hover { background:none; color:#000; }
            .dropdown-promo { border-top:2px dashed #eee; padding-top:0.85rem; display:flex; justify-content:space-between; align-items:center; font-size:0.8rem; font-weight:700; color:#555; background:#fffbe8; border-radius:10px; padding:0.65rem 0.9rem; }
            .dropdown-promo a { font-weight:900; color:#000; text-decoration:none; border-bottom:2px solid #000; }
            /* ── Right action area ── */
            .nav-right { display:flex; align-items:center; gap:0.85rem; }
            .nav-free-badge { display:inline-flex; align-items:center; gap:0.35rem; background:#ffe066; border:2.5px solid #000; border-radius:999px; padding:0.4rem 1rem; font-weight:800; font-size:0.8rem; box-shadow:3px 3px 0 #000; text-decoration:none; color:#000; font-family:'Space Grotesk',sans-serif; transition:transform 0.12s,box-shadow 0.12s; }
            .nav-free-badge:hover { transform:translate(-1px,-1px); box-shadow:4px 4px 0 #000; }
            .menu-toggle { display:none; flex-direction:column; gap:5px; background:#fff; border:2.5px solid #000; border-radius:9px; padding:0.5rem 0.6rem; cursor:pointer; box-shadow:3px 3px 0 #000; }
            .menu-toggle.open { background:#ffe066; }
            .hamburger-line { width:20px; height:2px; background:#000; border-radius:2px; transition:transform 0.2s,opacity 0.2s; display:block; }
            .menu-toggle.open .hamburger-line:nth-child(1) { transform:translateY(7px) rotate(45deg); }
            .menu-toggle.open .hamburger-line:nth-child(2) { opacity:0; }
            .menu-toggle.open .hamburger-line:nth-child(3) { transform:translateY(-7px) rotate(-45deg); }
            .header-spacer { height:68px; }
            .hide-mobile { display:flex; }
            .hide-tablet { display:block; }
            @media(max-width:1100px) { .hide-tablet { display:none; } }
            @media(max-width:960px) {
                .hide-mobile { display:none !important; }
                .menu-toggle { display:flex; }
                #main-nav { display:none; position:fixed; top:68px; left:0; width:100%; height:calc(100vh - 68px); background:#fff; border-top:3px solid #000; overflow-y:auto; padding:1.25rem; z-index:9998; }
                #main-nav.active { display:block; }
                .nav-ul { flex-direction:column; align-items:stretch; gap:0.35rem; }
                .nav-link { font-size:1.05rem; padding:0.8rem 1rem; border-radius:10px; }
                .mega-dropdown { position:static; width:100%; transform:none; box-shadow:none; border:2px solid #eee; border-radius:12px; padding:0.85rem; margin-top:0.4rem; animation:none; }
                .dropdown-inner { grid-template-columns:1fr 1fr; gap:0.75rem; }
                .dropdown-promo { display:none; }
            }
            @media(max-width:480px) { .nav-logo-name { font-size:1rem; } .nav-logo-tag { display:none; } .dropdown-inner { grid-template-columns:1fr; } }
            /* ── Guide button ── */
            .wot-guide-btn { display:inline-flex; align-items:center; gap:0.45rem; padding:0.7rem 1.4rem; background:#e9ddff; color:#000; border:2.5px solid #000; border-radius:10px; font-weight:800; font-size:0.88rem; box-shadow:3px 3px 0 #000; text-decoration:none; transition:transform 0.12s,box-shadow 0.12s; margin-top:1rem; font-family:'Space Grotesk',sans-serif; }
            .wot-guide-btn:hover { transform:translate(-1px,-1px); box-shadow:5px 5px 0 #000; }
            /* ── Post-rec widget ── */
            .wot-post-rec { display:none; margin-top:2rem; padding:1.4rem; background:#fff0b3; border:2.5px solid #000; border-radius:18px; box-shadow:4px 4px 0 #000; }
            .wot-post-rec-title { font-family:'Syne',sans-serif; font-weight:900; font-size:0.95rem; margin-bottom:1rem; }
            .wot-post-rec-grid { display:flex; gap:0.75rem; flex-wrap:wrap; }
            .wot-rec-card { display:flex; flex-direction:column; align-items:center; text-align:center; padding:1rem 0.7rem; background:#fff; border:2.5px solid #000; border-radius:12px; text-decoration:none; color:#000; box-shadow:3px 3px 0 #000; flex:1; min-width:110px; transition:transform 0.12s,box-shadow 0.12s; }
            .wot-rec-card:hover { transform:translate(-2px,-2px); box-shadow:5px 5px 0 #000; }
            .wot-rec-icon { font-size:1.5rem; margin-bottom:0.35rem; }
            .wot-rec-name { font-weight:800; font-size:0.82rem; line-height:1.2; margin-bottom:0.15rem; }
            .wot-rec-desc { font-size:0.7rem; color:#666; line-height:1.3; }
            /* Global tool h1 size fix */
            .tool-hero h1, .tool-hero h1 * { font-size:clamp(1.25rem,3vw,1.75rem) !important; letter-spacing:-0.01em !important; font-weight:800 !important; text-transform:none !important; line-height:1.2 !important; }
            /* Fix stretched Syne in hero-badge locations */
            .hero-badge { letter-spacing:0.05em !important; }
        </style>
    `;
    const header = document.querySelector('header');
    if (header) {
        // Replace SEO placeholder nav with full interactive nav
        header.innerHTML = headerHTML;
        setupDropdown();
        setupMobileMenu();
    }
}

// ── DROPDOWN — pure click-based, closes on outside click ─────────────────────
function setupDropdown() {
    const wrap    = document.getElementById('tools-dropdown-wrap');
    const btn     = document.getElementById('tools-dropdown-btn');
    const dd      = document.getElementById('mega-dropdown');
    const arrow   = btn ? btn.querySelector('.dd-arrow') : null;
    if (!wrap || !btn || !dd) return;

    function openDD() {
        dd.classList.add('is-open');
        btn.setAttribute('aria-expanded', 'true');
        if (arrow) arrow.style.transform = 'rotate(180deg)';
    }
    function closeDD() {
        dd.classList.remove('is-open');
        btn.setAttribute('aria-expanded', 'false');
        if (arrow) arrow.style.transform = '';
    }
    function toggleDD(e) {
        e.stopPropagation();
        dd.classList.contains('is-open') ? closeDD() : openDD();
    }

    btn.addEventListener('click', toggleDD);
    // Keep open when clicking inside dropdown
    dd.addEventListener('click', (e) => e.stopPropagation());
    // Close on outside click
    document.addEventListener('click', closeDD);
    // Close on Escape
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeDD(); });
}

// ── MOBILE MENU ──────────────────────────────────────────────────────────────
function setupMobileMenu() {
    const toggle = document.getElementById('mobile-menu-btn');
    const nav    = document.getElementById('main-nav');
    if (!toggle || !nav) return;

    toggle.addEventListener('click', (e) => {
        e.stopPropagation();
        const isOpen = nav.classList.toggle('active');
        toggle.classList.toggle('open', isOpen);
    });

    document.addEventListener('click', (e) => {
        if (nav.classList.contains('active') && !nav.contains(e.target) && !toggle.contains(e.target)) {
            nav.classList.remove('active');
            toggle.classList.remove('open');
        }
    });
}

// ── FOOTER INJECTION ──────────────────────────────────────────────────────────
function injectFooter() {
    const footerHTML = `
        <footer class="wot-footer" role="contentinfo">
            <div class="footer-accent-bar">
                <span class="footer-accent-pill" style="background:#ffe066;">🧮 Calculators</span>
                <span class="footer-accent-pill" style="background:#b2f5ea;">🛠️ Dev Tools</span>
                <span class="footer-accent-pill" style="background:#e9ddff;">📝 SEO & Text</span>
                <span class="footer-accent-pill" style="background:#bfecff;">🖼️ Image Tools</span>
                <span class="footer-accent-pill" style="background:#ffd6e0;">📹 Video Tools</span>
                <span class="footer-accent-pill" style="background:#c3f584;">🔐 Security</span>
            </div>
            <div class="footer-main">
                <div class="footer-grid">
                    <div class="footer-brand">
                        <div class="footer-logo">
                            <span class="footer-logo-mark">W</span>
                            <span class="footer-logo-name">WorldOfTools.in</span>
                        </div>
                        <p class="footer-brand-desc">70+ free online tools built for speed, privacy, and productivity. No login, no uploads. 100% browser-based.</p>
                        <div class="footer-trust-pills">
                            <span>🔒 Zero Data Storage</span>
                            <span>⚡ Instant Results</span>
                            <span>🚫 No Login</span>
                        </div>
                        <div class="footer-about-links">
                            <a href="/about-us">About Us</a>
                            <a href="/contact-us">Contact</a>
                            <a href="/privacy">Privacy</a>
                        </div>
                    </div>
                    <div class="footer-col">
                        <h3 class="footer-col-title">🔥 Top Tools</h3>
                        <nav>
                            <a href="/age-calculator">🎂 Age Calculator</a>
                            <a href="/gst-calculator">🧾 GST Calculator</a>
                            <a href="/image-compressor">🖼️ Image Compressor</a>
                            <a href="/json-formatter">{ } JSON Formatter</a>
                            <a href="/video-compressor">📹 Video Compressor</a>
                            <a href="/word-counter">📝 Word Counter</a>
                            <a href="/ip-address-lookup">📍 IP Lookup</a>
                        </nav>
                    </div>
                    <div class="footer-col">
                        <h3 class="footer-col-title">⚙️ Dev &amp; SEO</h3>
                        <nav>
                            <a href="/jwt-decoder">🔑 JWT Decoder</a>
                            <a href="/hash-generator">🔐 Hash Generator</a>
                            <a href="/password-generator">🔒 Password Gen</a>
                            <a href="/base64-encoder-decoder">🔄 Base64 Tools</a>
                            <a href="/seo-meta-tag-generator">🏷️ Meta Tags</a>
                            <a href="/keyword-research-tool">🔑 Keyword Tool</a>
                            <a href="/serp-preview">🔎 SERP Preview</a>
                        </nav>
                    </div>
                    <div class="footer-col">
                        <h3 class="footer-col-title">🕒 Recently Used</h3>
                        <div id="recent-tools-list" class="recent-list-v6">
                            <p style="font-size:0.82rem;color:#888;font-weight:600;margin:0;">No tools used yet.<br><span style="font-size:0.76rem;">Visit any tool to track it here.</span></p>
                        </div>
                        <div style="margin-top:1.25rem;">
                            <a href="/" class="footer-browse-btn">Browse All 70+ Tools →</a>
                        </div>
                    </div>
                </div>
                <div class="footer-bottom">
                    <div class="footer-copy">© 2026 WorldOfTools — <span style="color:#ff6b9d;">The Playful Powerhouse.</span> 🚀</div>
                    <div class="footer-util-links">
                        <a href="/privacy">Privacy Policy</a>
                        <a href="/terms">Terms of Use</a>
                        <a href="/sitemap.xml">Sitemap</a>
                        <a href="/guides/">Guides</a>
                    </div>
                </div>
            </div>
        </footer>
        <style>
            .wot-footer { background:#fff; border-top:4px solid #000; font-family:'Space Grotesk',sans-serif; margin-top:0; }
            .footer-accent-bar { display:flex; gap:0.55rem; flex-wrap:wrap; padding:0.85rem 1.5rem; border-bottom:2px solid #000; background:#fafaf8; justify-content:center; }
            .footer-accent-pill { display:inline-block; padding:0.28rem 0.85rem; border:2px solid #000; border-radius:999px; font-weight:800; font-size:0.68rem; text-transform:uppercase; letter-spacing:0.04em; box-shadow:2px 2px 0 #000; }
            .footer-main { max-width:1280px; margin:0 auto; padding:2.5rem 1.5rem 1.75rem; }
            .footer-grid { display:grid; grid-template-columns:1.8fr 1fr 1fr 1fr; gap:2.5rem; margin-bottom:2.5rem; }
            .footer-logo { display:flex; align-items:center; gap:0.6rem; margin-bottom:0.9rem; }
            .footer-logo-mark { width:34px; height:34px; background:#ffe066; border:2.5px solid #000; border-radius:9px; box-shadow:3px 3px 0 #000; display:flex; align-items:center; justify-content:center; font-family:'Syne',sans-serif; font-weight:900; font-size:1.2rem; color:#000; flex-shrink:0; }
            .footer-logo-name { font-family:'Syne',sans-serif; font-weight:900; font-size:1.1rem; color:#000; letter-spacing:-0.01em; }
            .footer-brand-desc { font-size:0.85rem; font-weight:500; color:#555; line-height:1.65; margin:0 0 1.1rem; max-width:300px; }
            .footer-trust-pills { display:flex; flex-direction:column; gap:0.4rem; margin-bottom:1.25rem; }
            .footer-trust-pills span { display:inline-block; font-size:0.75rem; font-weight:700; color:#333; background:#f5f5f5; border:1.5px solid #ccc; border-radius:7px; padding:0.28rem 0.65rem; width:fit-content; }
            .footer-about-links { display:flex; gap:1.1rem; flex-wrap:wrap; }
            .footer-about-links a { color:#000; font-weight:800; font-size:0.8rem; text-decoration:none; border-bottom:2px solid #000; transition:color 0.12s; }
            .footer-about-links a:hover { color:#ff6b9d; border-bottom-color:#ff6b9d; }
            .footer-col-title { font-family:'Syne',sans-serif; font-size:0.75rem; font-weight:900; text-transform:uppercase; letter-spacing:0.06rem; margin:0 0 1.1rem; color:#000; padding-bottom:0.55rem; border-bottom:2px solid #000; }
            .footer-col nav a { display:flex; align-items:center; gap:0.4rem; text-decoration:none; color:#444; font-weight:600; font-size:0.85rem; margin-bottom:0.65rem; transition:transform 0.1s,color 0.1s; padding:0.15rem 0; }
            .footer-col nav a:hover { transform:translateX(5px); color:#ff6b9d; }
            .recent-list-v6 { display:flex; flex-direction:column; gap:0.55rem; }
            .recent-list-v6 a { display:flex; align-items:center; padding:0.5rem 0.85rem; background:#ffe066; border:2px solid #000; border-radius:9px; text-decoration:none; color:#000; font-weight:800; font-size:0.8rem; box-shadow:3px 3px 0 #000; transition:all 0.1s; width:fit-content; max-width:100%; }
            .recent-list-v6 a:hover { transform:translate(-2px,-2px); box-shadow:5px 5px 0 #000; }
            .footer-browse-btn { display:inline-flex; align-items:center; padding:0.55rem 1rem; background:#000; color:#fff; border:2px solid #000; border-radius:9px; font-weight:800; font-size:0.8rem; text-decoration:none; box-shadow:3px 3px 0 #ffe066; transition:all 0.12s; }
            .footer-browse-btn:hover { background:#ffe066; color:#000; box-shadow:3px 3px 0 #000; }
            .footer-bottom { display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem; border-top:2px solid #000; padding-top:1.25rem; }
            .footer-copy { font-size:0.82rem; font-weight:700; color:#000; }
            .footer-util-links { display:flex; gap:1.25rem; flex-wrap:wrap; }
            .footer-util-links a { text-decoration:none; color:#666; font-weight:700; font-size:0.72rem; text-transform:uppercase; letter-spacing:0.05em; transition:color 0.12s; }
            .footer-util-links a:hover { color:#000; }
            @media(max-width:1100px) { .footer-grid { grid-template-columns:1fr 1fr; gap:2rem; } .footer-brand { grid-column:span 2; } .footer-brand-desc { max-width:100%; } }
            @media(max-width:640px) { .footer-grid { grid-template-columns:1fr; gap:1.75rem; } .footer-brand { grid-column:span 1; } .footer-bottom { flex-direction:column; align-items:flex-start; } .footer-util-links { gap:0.85rem; } }
        </style>
    `;
    // Always replace or insert footer
    let footer = document.querySelector('footer');
    if (footer) {
        footer.outerHTML = footerHTML;
    } else {
        document.body.insertAdjacentHTML('beforeend', footerHTML);
    }
    setTimeout(renderRecentTools, 80);
}

// ── GUIDE BUTTON INJECTION (via JS, reliable) ────────────────────────────────
function injectGuideButton() {
    let slug = window.location.pathname.replace(/\.html$/, '').replace(/^\//, '');
    slug = slug.replace(/^([a-z]{2}(-[a-z]{2})?)\//i, '');
    const guideSlug = GUIDE_MAP[slug];
    if (!guideSlug) return;

    if (document.querySelector('.wot-guide-btn')) return;

    const btn = document.createElement('a');
    btn.href      = `/guides/${guideSlug}.html`;
    btn.className = 'wot-guide-btn';
    btn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg> Read Expert Guide`;

    // Try multiple selectors to find h1 — works for both old (.tool-header) and new (.tool-hero) layouts
    const h1 = document.querySelector('.tool-hero h1, .tool-header h1, main h1, .tool-container h1');
    if (h1 && h1.parentNode) {
        const wrapper = document.createElement('div');
        wrapper.className = 'h1-guide-wrapper';
        wrapper.style.cssText = 'display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;';
        h1.parentNode.insertBefore(wrapper, h1);
        const h1Container = document.createElement('div');
        h1Container.style.flex = '1';
        h1Container.appendChild(h1);
        wrapper.appendChild(h1Container);
        wrapper.appendChild(btn);
    } else {
        const main = document.querySelector('main');
        if (main) main.prepend(btn);
    }
}

// ── POST-RECOMMENDATION WIDGET ────────────────────────────────────────────────
function injectPostRecWidget() {
    const slug = window.location.pathname.replace(/\.html$/, '').replace(/^\//, '');
    if (!slug || slug === '' || slug === 'index' || slug.startsWith('guides')) return;

    const recs = POST_REC_MAP[slug];
    if (!recs) return;

    // Don't inject if already present
    if (document.querySelector('.wot-post-rec')) return;

    const widget = document.createElement('div');
    widget.className = 'wot-post-rec';
    widget.id = 'post-rec-widget';

    let cards = '';
    recs.forEach(([url, icon, name, desc]) => {
        cards += `<a href="${url}" class="wot-rec-card"><div class="wot-rec-icon">${icon}</div><div class="wot-rec-name">${name}</div><div class="wot-rec-desc">${desc}</div></a>`;
    });
    widget.innerHTML = `<div class="wot-post-rec-title">💡 You Might Also Need</div><div class="wot-post-rec-grid">${cards}</div>`;

    // Insert after the main tool card
    const toolCard =
        document.querySelector('.nb-card-lg') ||
        document.querySelector('.nb-card') ||
        document.querySelector('.tool-main-card');

    if (toolCard && toolCard.parentNode) {
        toolCard.parentNode.insertBefore(widget, toolCard.nextSibling);
    } else {
        const main = document.querySelector('main');
        if (main) main.appendChild(widget);
    }

    // Show only after result is generated ─────────────────────────────────────
    watchForResult(widget);
}

function watchForResult(widget) {
    let shown = false;

    function showWidget() {
        if (shown) return;
        shown = true;
        widget.style.display = 'block';
        widget.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    // Primary: watch for #results or result containers becoming visible
    const RESULT_IDS = ['results','result','resultSection','outputSection','gstResult','ageResult',
        'emiResult','sipResult','bmiResult','output','resultContainer','wpmResult'];

    const observer = new MutationObserver((mutations) => {
        if (shown) return;

        // Check if any known result element just became visible
        for (const id of RESULT_IDS) {
            const el = document.getElementById(id);
            if (el) {
                const style = el.getAttribute('style') || '';
                const cls   = el.className || '';
                const isVisible = !style.includes('display:none') &&
                    !style.includes('display: none') &&
                    !cls.includes('hidden') &&
                    el.offsetHeight > 0;
                if (isVisible) {
                    const txt = el.textContent.trim();
                    if (txt.length > 10) { showWidget(); return; }
                }
            }
        }

        // Also check for result-hero becoming visible
        const hero = document.querySelector('.result-hero, .result-card-hero, .result-section');
        if (hero && hero.offsetHeight > 0 && !hero.closest('[style*="display:none"]') && !hero.closest('[style*="display: none"]')) {
            const txt = hero.textContent.trim();
            if (txt.length > 5) { showWidget(); return; }
        }
    });

    observer.observe(document.body, {
        subtree: true, attributes: true, attributeFilter: ['style', 'class'], childList: true
    });

    // Secondary: listen for ANY button click → check 500ms later
    document.addEventListener('click', (e) => {
        if (shown) return;
        const btn = e.target.closest('button');
        if (!btn) return;
        const txt = (btn.textContent || '').trim().toLowerCase();
        // Skip nav/UI buttons
        if (txt.length < 2 || btn.closest('nav') || btn.closest('.nav-container')) return;
        setTimeout(() => {
            if (shown) return;
            for (const id of RESULT_IDS) {
                const el = document.getElementById(id);
                if (el && el.offsetHeight > 0) {
                    const t = el.textContent.trim();
                    if (t.length > 5 && t !== '0' && t !== 'Error') { showWidget(); return; }
                }
            }
        }, 500);
    }, true);

    // Tertiary: scientific calculator — watch display value change from 0
    const calcDisplay = document.getElementById('calcDisplay');
    if (calcDisplay) {
        const calcObs = new MutationObserver(() => {
            const val = calcDisplay.textContent.trim();
            if (val && val !== '0' && val !== 'Error' && val !== 'NaN') showWidget();
        });
        calcObs.observe(calcDisplay, { childList: true, characterData: true, subtree: true });
    }
}

// ── DEDUP RELATED TOOLS (remove extra "More Free Tools" / "Next Tools") ───────
function dedupRelatedTools() {
    // Remove any injected ".wot-post-rec" text-based duplicates in HTML
    // (from the old injection script that no longer applies)
    const oldWidgets = document.querySelectorAll('[style*="background:#fff0b3"]');
    oldWidgets.forEach(el => {
        if (el.textContent.includes('You Might Also Need') && !el.classList.contains('wot-post-rec')) {
            el.remove();
        }
    });

    // If there are 2+ ".tools-grid" sections in the tool, keep only the first
    const path = window.location.pathname;
    if (path === '/' || path.startsWith('/guides')) return;
    const grids = document.querySelectorAll('.tools-grid');
    if (grids.length > 1) {
        // Keep only the first one; the others are duplicates
        for (let i = 1; i < grids.length; i++) {
            const parent = grids[i].closest('section, div[class]');
            if (parent && parent.querySelector('h2, h3')) {
                // Has a heading = probably the "More Free Tools" section from des/ built-in
                // Only remove it if we already injected our post-rec widget
                if (document.querySelector('.wot-post-rec')) {
                    parent.remove();
                }
            }
        }
    }
}

// ── UTILITY ───────────────────────────────────────────────────────────────────
function injectPostRecommendations() { /* legacy stub — handled by injectPostRecWidget */ }

function registerServiceWorker() {
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
            navigator.serviceWorker.register('/service-worker.js').then(reg => {
                // Check for updates periodically
                reg.update();

                reg.onupdatefound = () => {
                    const newWorker = reg.installing;
                    newWorker.onstatechange = () => {
                        if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                            // New worker installed, skipWaiting is called in SW, so it will activate
                            console.log('New content available, preparing to refresh...');
                        }
                    };
                };
            }).catch(err => console.error('SW subscription error:', err));
        });

        // This event fires when the new service worker takes control
        let refreshing = false;
        navigator.serviceWorker.addEventListener('controllerchange', () => {
            if (!refreshing) {
                refreshing = true;
                console.log('New Service Worker activating. Reloading page for instant update...');
                window.location.reload();
            }
        });
    }
}

function highlightActiveLink() {
    const path = window.location.pathname.replace(/\.html$/, '').replace(/\/$/, '') || '/';
    document.querySelectorAll('a[href]').forEach(link => {
        const href = link.getAttribute('href').replace(/\.html$/, '').replace(/\/$/, '') || '/';
        if (href === path && href !== '/' && href.length > 1) {
            link.style.color = '#ff6b9d';
            link.style.fontWeight = '900';
        }
    });
}

function trackRecentTool() {
    const path = window.location.pathname.replace(/\.html$/, '');
    if (['/','','/index'].includes(path) || path.startsWith('/guides')) return;
    const name = document.title.split('—')[0].split('|')[0].trim();
    const tool = { name: name.length > 32 ? name.slice(0, 30) + '…' : name, url: path };
    let recent = [];
    try { recent = JSON.parse(localStorage.getItem('wotRecentV6') || '[]'); } catch(e) {}
    recent = recent.filter(t => t.url !== tool.url);
    recent.unshift(tool);
    try { localStorage.setItem('wotRecentV6', JSON.stringify(recent.slice(0, 5))); } catch(e) {}
}

function renderRecentTools() {
    const target = document.getElementById('recent-tools-list');
    if (!target) return;
    let recent = [];
    try { recent = JSON.parse(localStorage.getItem('wotRecentV6') || '[]'); } catch(e) {}
    if (!recent.length) return;
    target.innerHTML = '';
    recent.forEach(tool => {
        const a = document.createElement('a');
        a.href = tool.url;
        a.textContent = tool.name;
        target.appendChild(a);
    });
}
