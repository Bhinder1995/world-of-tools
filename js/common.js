// Common JS for Mega Utility Hub

document.addEventListener('DOMContentLoaded', () => {
    injectHeader();
    injectFooter();
    registerServiceWorker();
    highlightActiveLink();
    if (typeof autoRenderBreadcrumbs === 'function') {
        autoRenderBreadcrumbs();
    }
    injectPostRecommendations();
    trackRecentTool();
    if (window.location.pathname === '/' || window.location.pathname === '/index.html' || window.location.pathname.endsWith('/')) {
        renderRecentTools();
    }
});


function injectHeader() {
    const headerHTML = `
        <div class="container">
            <div class="header-content">
                <a href="/" class="logo-center" aria-label="WorldOfTools Home">
                    <img src="/logo.svg" alt="WorldOfTools Logo" width="40" height="40" style="flex-shrink:0; border-radius: 8px;">
                    <div class="logo-text-block">
                        <span class="logo-brand">WorldOfTools</span>
                        <span class="logo-tagline">Fast. Free. Private.</span>
                    </div>
                </a>

                <nav id="main-nav">
                    <ul>
                        <li class="nav-dropdown">
                            <span class="dropdown-trigger">All Tools <svg width="10" height="6" viewBox="0 0 10 6" fill="none" style="vertical-align:middle;margin-left:2px;"><path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg></span>
                            <div class="dropdown-menu">
                                <div class="mega-dropdown-inner">

                                    <div class="mega-col">
                                        <div class="mega-col-header">Calculators</div>
                                        <a href="/age-calculator" class="mega-item">
                                            <span class="nav-icon" style="background:#e74c3c;">🎂</span> Age Calculator
                                        </a>
                                        <a href="/bmi-calculator" class="mega-item">
                                            <span class="nav-icon" style="background:#2ecc71;">⚖️</span> BMI Calculator
                                        </a>
                                        <a href="/sip-calculator" class="mega-item">
                                            <span class="nav-icon" style="background:#3498db;">📈</span> SIP Calculator
                                        </a>
                                        <a href="/loan-eligibility-calculator" class="mega-item">
                                            <span class="nav-icon" style="background:#9b59b6;">🏦</span> Loan Eligibility
                                        </a>
                                        <a href="/ppf-calculator" class="mega-item">
                                            <span class="nav-icon" style="background:#1abc9c;">💰</span> PPF Calculator
                                        </a>
                                        <a href="/emi-calculator" class="mega-item">
                                            <span class="nav-icon" style="background:#e67e22;">🏠</span> EMI Calculator
                                        </a>
                                        <a href="/gst-calculator" class="mega-item">
                                            <span class="nav-icon" style="background:#2ecc71;">🧾</span> GST Calculator
                                        </a>
                                        <a href="/scientific-calculator" class="mega-item">
                                            <span class="nav-icon" style="background:#34495e;">🔬</span> Scientific Calculator
                                        </a>
                                        <a href="/percentage-calculator" class="mega-item">
                                            <span class="nav-icon" style="background:#e74c3c;">%</span> Percentage Calculator
                                        </a>
                                        <a href="/aspect-ratio-calculator" class="mega-item">
                                            <span class="nav-icon" style="background:#f39c12;">📐</span> Aspect Ratio
                                        </a>
                                        <a href="/number-to-words-converter" class="mega-item">
                                            <span class="nav-icon" style="background:#8e44ad;">🔢</span> Number to Words
                                        </a>
                                        <a href="/roman-numerals-converter" class="mega-item">
                                            <span class="nav-icon" style="background:#c0392b;">🏛️</span> Roman Numerals
                                        </a>
                                        <a href="/random-number-generator" class="mega-item">
                                            <span class="nav-icon" style="background:#16a085;">🎲</span> Random Number
                                        </a>
                                        <a href="/unit-converter" class="mega-item">
                                            <span class="nav-icon" style="background:#27ae60;">📏</span> Unit Converter
                                        </a>
                                        <a href="/cgpa-calculator" class="mega-item">
                                            <span class="nav-icon" style="background:#f39c12;">🎓</span> CGPA Calculator
                                        </a>
                                        <a href="/loan-comparison-calculator" class="mega-item">
                                            <span class="nav-icon" style="background:#2ecc71;">⚖️</span> Loan Comparison
                                        </a>
                                    </div>

                                    <div class="mega-col">
                                        <div class="mega-col-header">Developer Tools</div>
                                        <a href="/json-formatter" class="mega-item">
                                            <span class="nav-icon" style="background:#f39c12;">{ }</span> JSON Formatter
                                        </a>
                                        <a href="/css-gradient-generator" class="mega-item">
                                            <span class="nav-icon" style="background:linear-gradient(135deg,#667eea,#764ba2);">🎨</span> CSS Gradient
                                        </a>
                                        <a href="/hash-generator" class="mega-item">
                                            <span class="nav-icon" style="background:#8e44ad;">#</span> Hash Generator
                                        </a>
                                        <a href="/jwt-decoder" class="mega-item">
                                            <span class="nav-icon" style="background:#2980b9;">🔑</span> JWT Decoder
                                        </a>
                                        <a href="/sql-formatter" class="mega-item">
                                            <span class="nav-icon" style="background:#16a085;">🗄️</span> SQL Formatter
                                        </a>
                                        <a href="/regex-tester" class="mega-item">
                                            <span class="nav-icon" style="background:#c0392b;">.*</span> Regex Tester
                                        </a>
                                        <a href="/base64-encoder-decoder" class="mega-item">
                                            <span class="nav-icon" style="background:#27ae60;">64</span> Base64 Encode/Decode
                                        </a>
                                        <a href="/url-encoder-decoder" class="mega-item">
                                            <span class="nav-icon" style="background:#2c3e50;">🔗</span> URL Encode/Decode
                                        </a>
                                        <a href="/csv-to-json" class="mega-item">
                                            <span class="nav-icon" style="background:#d35400;">⇌</span> CSV to JSON
                                        </a>
                                        <a href="/css-minifier" class="mega-item">
                                            <span class="nav-icon" style="background:#2980b9;">🗜️</span> CSS Minifier
                                        </a>
                                        <a href="/xml-formatter" class="mega-item">
                                            <span class="nav-icon" style="background:#1abc9c;">📜</span> XML Formatter
                                        </a>
                                        <a href="/uuid-generator" class="mega-item">
                                            <span class="nav-icon" style="background:#8e44ad;">🆔</span> UUID Generator
                                        </a>
                                        <a href="/cron-expression-generator" class="mega-item">
                                            <span class="nav-icon" style="background:#e67e22;">⏰</span> Cron Generator
                                        </a>
                                        <a href="/text-to-binary-converter" class="mega-item">
                                            <span class="nav-icon" style="background:#34495e;">01</span> Text to Binary
                                        </a>
                                    </div>

                                    <div class="mega-col">
                                        <div class="mega-col-header">Text & SEO</div>
                                        <a href="/word-counter" class="mega-item">
                                            <span class="nav-icon" style="background:#3498db;">Aa</span> Word Counter
                                        </a>
                                        <a href="/case-converter" class="mega-item">
                                            <span class="nav-icon" style="background:#9b59b6;">Cc</span> Case Converter
                                        </a>
                                        <a href="/keyword-research-tool" class="mega-item">
                                            <span class="nav-icon" style="background:#f59e0b;">🔑</span> Keyword Researcher
                                        </a>
                                        <a href="/seo-meta-tag-generator" class="mega-item">
                                            <span class="nav-icon" style="background:#e74c3c;">🔍</span> Meta Tag Generator
                                        </a>
                                        <a href="/serp-preview" class="mega-item">
                                            <span class="nav-icon" style="background:#4285f4;">G</span> SERP Preview
                                        </a>
                                        <a href="/keyword-density-checker" class="mega-item">
                                            <span class="nav-icon" style="background:#1abc9c;">📊</span> Keyword Density
                                        </a>
                                        <a href="/markdown-to-html" class="mega-item">
                                            <span class="nav-icon" style="background:#34495e;">MD</span> Markdown to HTML
                                        </a>
                                        <a href="/text-compare-tool" class="mega-item">
                                            <span class="nav-icon" style="background:#e67e22;">≠</span> Text Compare
                                        </a>
                                        <a href="/lorem-ipsum-generator" class="mega-item">
                                            <span class="nav-icon" style="background:#7f8c8d;">¶</span> Lorem Ipsum Generator
                                        </a>
                                        <a href="/typing-speed-test" class="mega-item">
                                            <span class="nav-icon" style="background:#2c3e50;">⌨️</span> Typing Speed Test
                                        </a>
                                        <a href="/link-shortener" class="mega-item">
                                            <span class="nav-icon" style="background:#e74c3c;">🔗</span> Link Shortener
                                        </a>
                                        <a href="/linkedin-creator-suite" class="mega-item">
                                            <span class="nav-icon" style="background:#0a66c2;">💼</span> LinkedIn Suite
                                        </a>
                                        <a href="/audio-to-text" class="mega-item">
                                            <span class="nav-icon" style="background:#3498db;">🎙️</span> Audio to Text
                                        </a>
                                        <a href="/schema-markup-generator" class="mega-item">
                                            <span class="nav-icon" style="background:#4f46e5;">🛠️</span> Schema Generator
                                        </a>
                                    </div>

                                    <div class="mega-col">
                                        <div class="mega-col-header">Image & Web Tools</div>
                                        <a href="/image-compressor" class="mega-item">
                                            <span class="nav-icon" style="background:#e91e63;">🖼️</span> Image Compressor
                                        </a>
                                        <a href="/background-remover" class="mega-item">
                                            <span class="nav-icon" style="background:#00bcd4;">✂️</span> Background Remover
                                        </a>
                                        <a href="/image-upscaler" class="mega-item">
                                            <span class="nav-icon" style="background:#673ab7;">↑</span> Image Upscaler
                                        </a>
                                        <a href="/favicon-generator" class="mega-item">
                                            <span class="nav-icon" style="background:#ff5722;">⭐</span> Favicon Generator
                                        </a>
                                        <a href="/qr-code-generator" class="mega-item">
                                            <span class="nav-icon" style="background:#212121;">▦</span> QR Code Generator
                                        </a>
                                        <a href="/barcode-generator" class="mega-item">
                                            <span class="nav-icon" style="background:#37474f;">|||</span> Barcode Generator
                                        </a>
                                        <a href="/thermal-label-maker" class="mega-item">
                                            <span class="nav-icon" style="background:#1e293b;">🖨️</span> Thermal Label Maker
                                        </a>
                                        <a href="/video-compressor" class="mega-item">
                                            <span class="nav-icon" style="background:#e91e63;">📹</span> Video Compressor
                                        </a>
                                        <a href="/video-to-gif" class="mega-item">
                                            <span class="nav-icon" style="background:#8b5cf6;">🎞️</span> Video to GIF
                                        </a>
                                        <a href="/video-to-mp3-converter" class="mega-item">
                                            <span class="nav-icon" style="background:#06b6d4;">🎵</span> Video to MP3
                                        </a>
                                        <a href="/exif-metadata-remover" class="mega-item">
                                            <span class="nav-icon" style="background:#ef4444;">🛡️</span> EXIF Remover
                                        </a>
                                        <a href="/image-converter" class="mega-item">
                                            <span class="nav-icon" style="background:#673ab7;">🔄</span> Image Converter
                                        </a>
                                        <a href="/color-converter" class="mega-item">
                                            <span class="nav-icon" style="background:#ffc107;">🎨</span> Color Converter
                                        </a>
                                        <a href="/time-zone-converter" class="mega-item">
                                            <span class="nav-icon" style="background:#03a9f4;">🌍</span> Time Zone
                                        </a>
                                        <a href="/youtube-thumbnail-downloader" class="mega-item">
                                            <span class="nav-icon" style="background:#ff0000;">📺</span> YT Thumbnail
                                        </a>
                                        <a href="/password-generator" class="mega-item">
                                            <span class="nav-icon" style="background:#4caf50;">🔐</span> Password Generator
                                        </a>
                                        <a href="/ip-address-lookup" class="mega-item">
                                            <span class="nav-icon" style="background:#2196f3;">📍</span> IP Lookup
                                        </a>
                                        <a href="/email-signature-generator" class="mega-item">
                                            <span class="nav-icon" style="background:#4caf50;">✉️</span> Email Signature
                                        </a>
                                        <a href="/invoice-generator" class="mega-item">
                                            <span class="nav-icon" style="background:#ff9800;">📄</span> Invoice Generator
                                        </a>
                                        <a href="/remove-watermark-from-image" class="mega-item">
                                            <span class="nav-icon" style="background:#673ab7;">✨</span> Remove Watermark
                                        </a>
                                        <div style="font-size: 0.7rem; color: #64748b; padding: 0.5rem; margin-top: 0.5rem; border-top: 1px solid #eee;">Note: Video tools require COOP/COEP headers.</div>
                                    </div>

                                </div>
                            </div>
                        </li>
                        <li><a href="/calculators-online">Calculators</a></li>
                        <li><a href="/guides/">Guides</a></li>
                    </ul>
                </nav>

                <div class="header-actions" style="display: flex; align-items: center; gap: 1rem; position: relative; z-index: 2;">
                    <div class="global-privacy-badge" style="display: flex; align-items: center; gap: 0.5rem; background: rgba(16, 185, 129, 0.1); color: #059669; padding: 0.4rem 0.8rem; border-radius: 99px; font-size: 0.75rem; font-weight: 700; border: 1px solid rgba(16, 185, 129, 0.2);" class="hide-mobile">
                        🛡️ <span class="badge-text" style="white-space: nowrap;">100% Private</span>
                    </div>
                    <button class="menu-toggle" aria-label="Toggle navigation">
                        ☰
                    </button>
                </div>

            </div>
        </div>
    `;

    const header = document.querySelector('header');
    if (header) {
        // Add compact-header class if not on homepage
        const isHomePage = window.location.pathname === '/' || window.location.pathname === '/index.html' || window.location.pathname.endsWith('/');
        if (!isHomePage) {
            header.classList.add('compact-header');
        }
        header.innerHTML = headerHTML;
        setupMobileMenu();
    }
}

function setupMobileMenu() {
    const toggle = document.querySelector('.menu-toggle');
    const nav = document.getElementById('main-nav');
    const dropdownTrigger = document.querySelector('.dropdown-trigger');

    if (toggle && nav) {
        toggle.addEventListener('click', (e) => {
            e.stopPropagation();
            nav.classList.toggle('active');
            toggle.textContent = nav.classList.contains('active') ? '✕' : '☰';
        });

        if (dropdownTrigger) {
            dropdownTrigger.addEventListener('click', (e) => {
                if (window.innerWidth <= 960) {
                    e.preventDefault();
                    e.stopPropagation();
                    document.querySelector('.nav-dropdown').classList.toggle('open');
                }
            });
        }

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (nav.classList.contains('active') && !nav.contains(e.target) && !toggle.contains(e.target)) {
                nav.classList.remove('active');
                toggle.textContent = '☰';
            }
        });

        // Close menu when clicking a link
        nav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                nav.classList.remove('active');
                toggle.textContent = '☰';
            });
        });
    }
}

function injectFooter() {
    const footerHTML = `

        <!-- ══ PRE-FOOTER CTA STRIP ══ -->
        <div style="background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%); padding: 2.5rem 1.5rem; text-align: center;">
            <div style="max-width: 1200px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1.5rem;">
                <div>
                    <div style="font-size: 1.2rem; font-weight: 800; color: white; margin-bottom: 0.3rem;">Explore 45+ Free Tools — Fast, Private &amp; No Signup Required</div>
                    <div style="color: rgba(255,255,255,0.75); font-size: 0.9rem;">Calculators, Developer Utilities, SEO Tools &amp; more — all 100% in your browser.</div>
                </div>
                <a href="/" style="display: inline-flex; align-items: center; gap: 0.5rem; background: white; color: #4f46e5; padding: 0.85rem 1.75rem; border-radius: 12px; font-weight: 800; font-size: 0.95rem; text-decoration: none; white-space: nowrap; transition: all 0.2s; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">🚀 Explore All Tools</a>
            </div>
        </div>

        <!-- ══ MAIN FOOTER ══ -->
        <footer style="background: #0f172a; color: white; padding: 5rem 1.5rem 0; position: relative; overflow: hidden;">
            <div style="position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 600px; height: 300px; background: radial-gradient(circle, rgba(79, 70, 229, 0.06) 0%, transparent 70%); pointer-events: none;"></div>

            <div style="max-width: 1200px; margin: 0 auto; position: relative; z-index: 1;">

                <!-- Brand Row -->
                <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1.5rem; margin-bottom: 3.5rem; padding-bottom: 3rem; border-bottom: 1px solid rgba(255,255,255,0.06);">
                    <div style="display: flex; align-items: center; gap: 0.75rem;">
                        <img src="/logo.svg" alt="WorldOfTools" style="width: 38px; height: 38px; border-radius: 8px;">
                        <div>
                            <div style="font-family: var(--font-heading); font-weight: 800; font-size: 1.2rem; color: white;">WorldOfTools</div>
                            <div style="font-size: 0.72rem; color: #64748b; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">Fast. Free. Private.</div>
                        </div>
                    </div>
                    <p style="color: #64748b; font-size: 0.88rem; max-width: 420px; line-height: 1.7; margin: 0;">
                        The ultimate privacy-focused utility hub. 45+ professional tools that run 100% in your browser — no uploads, no accounts, no fees.
                    </p>
                    <div style="display: flex; gap: 0.6rem; flex-wrap: wrap;">
                        <span style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.08); color: #94a3b8; padding: 0.3rem 0.85rem; border-radius: 99px; font-size: 0.75rem; font-weight: 600;">⚡ Instant</span>
                        <span style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.08); color: #94a3b8; padding: 0.3rem 0.85rem; border-radius: 99px; font-size: 0.75rem; font-weight: 600;">🔒 Private</span>
                        <span style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.08); color: #94a3b8; padding: 0.3rem 0.85rem; border-radius: 99px; font-size: 0.75rem; font-weight: 600;">🆓 Free</span>
                    </div>
                </div>

                <!-- 4-Column Links Grid -->
                <div class="footer-link-grid">

                    <!-- Col 1: Popular Tools -->
                    <div class="footer-col">
                        <h4 class="footer-col-heading">Popular Tools</h4>
                        <ul class="footer-links">
                            <li><a href="/ip-address-lookup" class="featured-link">📍 IP Lookup</a></li>
                            <li><a href="/image-compressor" class="featured-link">🖼️ Image Compressor</a></li>
                            <li><a href="/sip-calculator" class="featured-link">📈 SIP Calculator</a></li>
                            <li><a href="/invoice-generator" class="featured-link">📄 Invoice Generator</a></li>
                            <li><a href="/typing-speed-test" class="featured-link">⌨️ Typing Speed Test</a></li>
                        </ul>
                    </div>

                    <!-- Col 2: Calculators -->
                    <div class="footer-col">
                        <h4 class="footer-col-heading">Calculators</h4>
                        <ul class="footer-links">
                            <li><a href="/sip-calculator">SIP Calculator</a></li>
                            <li><a href="/emi-calculator">EMI Calculator</a></li>
                            <li><a href="/ppf-calculator">PPF Calculator</a></li>
                            <li><a href="/bmi-calculator">BMI Calculator</a></li>
                            <li><a href="/gst-calculator">GST Calculator</a></li>
                            <li><a href="/calculators-online">→ View All</a></li>
                        </ul>
                    </div>

                    <!-- Col 3: SEO & Web -->
                    <div class="footer-col">
                        <h4 class="footer-col-heading">SEO &amp; Web</h4>
                        <ul class="footer-links">
                            <li><a href="/ip-address-lookup">IP Address</a></li>
                            <li><a href="/seo-meta-tag-generator">Meta Tag Generator</a></li>
                            <li><a href="/serp-preview">SERP Preview</a></li>
                            <li><a href="/qr-code-generator">QR Code Generator</a></li>
                            <li><a href="/schema-markup-generator">Schema Generator</a></li>
                            <li><a href="/seo-tools-free">→ View All</a></li>
                        </ul>
                    </div>

                    <!-- Col 4: Developer -->
                    <div class="footer-col">
                        <h4 class="footer-col-heading">Developer</h4>
                        <ul class="footer-links">
                            <li><a href="/json-formatter">JSON Formatter</a></li>
                            <li><a href="/base64-encoder-decoder">Base64 Encoder/Decoder</a></li>
                            <li><a href="/regex-tester">Regex Tester</a></li>
                            <li><a href="/developer-tools-online">→ View All</a></li>
                        </ul>
                    </div>

                </div>

                <!-- Recently Added + Guides Row -->
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; margin-top: 3.5rem; padding-top: 3rem; border-top: 1px solid rgba(255,255,255,0.05);" class="footer-two-col">

                    <!-- Recently Added -->
                    <div>
                        <h4 class="footer-col-heading">✨ Recently Added</h4>
                        <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem;">
                            <a href="/bmi-calculator" class="footer-badge">BMI Calculator</a>
                            <a href="/sip-calculator" class="footer-badge">SIP Calculator</a>
                            <a href="/loan-eligibility-calculator" class="footer-badge">Loan Eligibility</a>
                            <a href="/ppf-calculator" class="footer-badge">PPF Calculator</a>
                            <a href="/css-gradient-generator" class="footer-badge">CSS Gradient</a>
                            <a href="/email-signature-generator" class="footer-badge">Email Signature</a>
                            <a href="/favicon-generator" class="footer-badge">Favicon Generator</a>
                            <a href="/invoice-generator" class="footer-badge">Invoice Generator</a>
                            <a href="/audio-to-text" class="footer-badge">Audio to Text</a>
                            <a href="/cgpa-calculator" class="footer-badge">CGPA Calculator</a>
                            <a href="/video-to-gif" class="footer-badge">Video to GIF ✨</a>
                            <a href="/video-to-mp3-converter" class="footer-badge">Video to MP3 ✨</a>
                            <a href="/exif-metadata-remover" class="footer-badge">EXIF Remover 🛡️</a>
                            <a href="/loan-comparison-calculator" class="footer-badge">Loan Comparison</a>
                            <a href="/remove-watermark-from-image" class="footer-badge">Remove Watermark</a>
                            <a href="/thermal-label-maker" class="footer-badge">Thermal Label Maker ✨</a>
                        </div>
                    </div>

                    <!-- Essential Pages -->
                    <div>
                        <h4 class="footer-col-heading">Company &amp; Info</h4>
                        <div style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin-top: 1rem;">
                            <a href="/about-us" style="color: #94a3b8; text-decoration: none; font-size: 0.85rem; font-weight: 500; transition: color 0.15s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#94a3b8'">About Us</a>
                            <span style="color: #334155;">|</span>
                            <a href="/contact-us" style="color: #94a3b8; text-decoration: none; font-size: 0.85rem; font-weight: 500; transition: color 0.15s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#94a3b8'">Contact</a>
                            <span style="color: #334155;">|</span>
                            <a href="/privacy" style="color: #94a3b8; text-decoration: none; font-size: 0.85rem; font-weight: 500; transition: color 0.15s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#94a3b8'">Privacy Policy</a>
                            <span style="color: #334155;">|</span>
                            <a href="/terms" style="color: #94a3b8; text-decoration: none; font-size: 0.85rem; font-weight: 500; transition: color 0.15s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#94a3b8'">Terms of Service</a>
                            <span style="color: #334155;">|</span>
                            <a href="/sitemap.xml" style="color: #94a3b8; text-decoration: none; font-size: 0.85rem; font-weight: 500; transition: color 0.15s;" onmouseover="this.style.color='white'" onmouseout="this.style.color='#94a3b8'">Sitemap</a>
                        </div>
                        <div style="margin-top: 1.5rem;">
                            <a href="/guides/" style="display:inline-flex; align-items:center; gap:0.5rem; background:rgba(99,102,241,0.12); border:1px solid rgba(99,102,241,0.25); color:#a5b4fc; padding:0.6rem 1.2rem; border-radius:10px; font-size:0.8rem; font-weight:700; text-decoration:none; transition:all 0.2s;">📚 Browse All Guides</a>
                        </div>
                    </div>
                </div>

                <!-- Bottom Bar -->
                <div style="margin-top: 3.5rem; padding: 2rem 0; border-top: 1px solid rgba(255,255,255,0.05); display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem;">
                    <div style="color: #475569; font-size: 0.82rem;">
                        &copy; ${new Date().getFullYear()} <strong style="color:#64748b;">WorldOfTools</strong>. All rights reserved. Built with ❤️ for developers, creators &amp; curious minds.
                    </div>
                    <div style="display: flex; gap: 1.25rem; align-items: center;">
                        <span style="color: #334155; font-size: 0.78rem; display:flex; align-items:center; gap:0.3rem;">⚡ Fast</span>
                        <span style="color: #334155; font-size: 0.78rem; display:flex; align-items:center; gap:0.3rem;">🔒 Privacy First</span>
                        <span style="color: #334155; font-size: 0.78rem; display:flex; align-items:center; gap:0.3rem;">🆓 No Signup</span>
                    </div>
                </div>

            </div>
        </footer>
    `;

    const footer = document.querySelector('footer');
    if (footer) {
        footer.outerHTML = footerHTML;
    }
}

function injectPostRecommendations() {
    const toolCard = document.querySelector('.tool-main-card');
    if (!toolCard) return;

    // Get current path and normalize it (remove .html for local testing comparison)
    const currentPath = window.location.pathname;
    const normalizedCurrentPath = currentPath.replace(/\.html$/, '');

    // Don't inject on home page or non-tool pages
    if (normalizedCurrentPath === '/' || normalizedCurrentPath === '/index' || normalizedCurrentPath.startsWith('/guides/')) return;

    // Extract tool data from the mega menu
    const menuColumns = document.querySelectorAll('.mega-col');
    if (!menuColumns.length) return;

    let allTools = [];
    let currentCategoryTools = [];

    menuColumns.forEach(col => {
        const toolLinks = Array.from(col.querySelectorAll('.mega-item'));
        if (!toolLinks.length) return;

        const toolsInCol = toolLinks.map(a => {
            const iconObj = a.querySelector('.nav-icon');
            // Clean text nodes from 'a' excluding the icon
            let text = '';
            a.childNodes.forEach(node => {
                if (node.nodeType === 3) text += node.textContent; // Text node
            });
            text = text.trim();

            return {
                name: text,
                url: a.getAttribute('href'),
                iconHtml: iconObj ? iconObj.outerHTML : ''
            };
        });
        
        allTools.push(...toolsInCol);

        if (toolsInCol.some(t => t.url.replace(/\.html$/, '') === normalizedCurrentPath)) {
            currentCategoryTools = toolsInCol;
        }
    });

    // Strategy to find related tools:
    // 1. Get other tools in same category
    // 2. If < 3, fill with random tools from all categories
    let related = currentCategoryTools.filter(t => t.url.replace(/\.html$/, '') !== normalizedCurrentPath);
    
    if (related.length < 3) {
        const others = allTools.filter(t => t.url.replace(/\.html$/, '') !== normalizedCurrentPath && !related.some(r => r.url === t.url));
        others.sort(() => 0.5 - Math.random());
        related = [...related, ...others].slice(0, 3);
    } else {
        // Pick 3 random from the related category
        related.sort(() => 0.5 - Math.random());
        related = related.slice(0, 3);
    }

    if (related.length === 0) return;

    const recContainer = document.createElement('div');
    recContainer.className = 'post-recommendation-container';
    
    let html = `
        <div class="post-rec-title">💡 Might you need these next?</div>
        <div class="post-rec-capsules">
    `;
    related.forEach(t => {
        html += `
            <a href="${t.url}" class="rec-capsule">
                ${t.iconHtml} ${t.name}
            </a>
        `;
    });
    html += `</div>`;
    recContainer.innerHTML = html;

    toolCard.appendChild(recContainer);

    // Bind events to primary actions
    const triggers = toolCard.querySelectorAll('button, input[type="file"], input[type="submit"]');
    
    if (triggers.length > 0) {
        let showed = false;
        triggers.forEach(trigger => {
            const eventName = trigger.tagName.toLowerCase() === 'input' && trigger.type === 'file' ? 'change' : 'click';
            trigger.addEventListener(eventName, () => {
                if (!showed) {
                    showed = true;
                    recContainer.style.display = 'block';
                }
            });
        });
    } else {
        // If no buttons, just show it
        recContainer.style.display = 'block';
    }
}

function registerServiceWorker() {
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
            navigator.serviceWorker.register('/service-worker.js', { updateViaCache: 'none' })
                .then(registration => {
                    console.log('ServiceWorker registration successful');

                    // Check for updates
                    registration.addEventListener('updatefound', () => {
                        const newWorker = registration.installing;
                        newWorker.addEventListener('statechange', () => {
                            if (newWorker.state === 'installed' && navigator.serviceWorker.controller) {
                                // New worker is installed and waiting — tell it to skip waiting
                                newWorker.postMessage({ type: 'SKIP_WAITING' });
                            }
                        });
                    });
                })
                .catch(err => {
                    console.log('ServiceWorker registration failed: ', err);
                });
        });

        // Reload the page once when the new service worker takes over
        let refreshing = false;
        navigator.serviceWorker.addEventListener('controllerchange', () => {
            if (!refreshing) {
                refreshing = true;
                const updateMsg = document.getElementById('pwa-update-msg');
                if (updateMsg) {
                    updateMsg.style.display = 'flex';
                    setTimeout(() => window.location.reload(), 1000);
                } else {
                    window.location.reload();
                }
            }
        });
    }
}

function highlightActiveLink() {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath.split('/').pop()) {
            link.style.textDecoration = 'underline';
        }
    });
}

function trackRecentTool() {
    const path = window.location.pathname;
    const normalizedPath = path.replace(/\.html$/, '');
    
    // Don't track homepage or guides index
    if (normalizedPath === '/' || normalizedPath === '/index' || normalizedPath === '/guides/' || normalizedPath === '/guides') return;
    
    // If it's a sub-guide, we don't necessarily want to track it as a "tool" unless it's a tool page
    // For now, let's assume anything that's not home/guides index is a candidate if it's in the mega menu
    
    // We'll wait a bit for the header to be injected if it isn't already, 
    // but DOMContentLoaded should have handled it.
    const allTools = [];
    const megaItems = document.querySelectorAll('.mega-item');
    megaItems.forEach(item => {
        const url = item.getAttribute('href').replace(/\.html$/, '');
        if (url === normalizedPath || (url.startsWith('/') && url === normalizedPath) || ('/' + url === normalizedPath)) {
            const name = item.innerText.replace(/[^\x00-\x7F]/g, '').trim(); // Remove emojis for the name part
            const icon = item.querySelector('.nav-icon')?.innerText || '🛠️';
            const fullUrl = item.getAttribute('href');
            
            allTools.push({ name, url: fullUrl, icon });
        }
    });

    if (allTools.length > 0) {
        const tool = allTools[0];
        let recent = JSON.parse(localStorage.getItem('recentTools') || '[]');
        
        // Remove if already exists to move to front
        recent = recent.filter(t => t.url !== tool.url);
        
        // Add to front
        recent.unshift(tool);
        
        // Keep only 4
        recent = recent.slice(0, 4);
        
        localStorage.setItem('recentTools', JSON.stringify(recent));
    }
}

function renderRecentTools() {
    const recentContainer = document.querySelector('.recent-tools');
    if (!recentContainer) return;

    const recent = JSON.parse(localStorage.getItem('recentTools') || '[]');
    if (recent.length === 0) {
        // If no recent tools, maybe hide the section or keep defaults?
        // User said "if someone use another tools its not shows", implying it should show what was used.
        // Let's keep the hardcoded ones as fallback if localStorage is empty, 
        // OR just render what's in localStorage if it exists.
        return; 
    }

    // Find the container that holds the capsules (it's the children after the label)
    const label = recentContainer.querySelector('.popular-label');
    if (!label) return;

    // Clear existing links but keep the label
    while (recentContainer.lastChild !== label) {
        recentContainer.removeChild(recentContainer.lastChild);
    }

    recent.forEach(tool => {
        const a = document.createElement('a');
        a.href = tool.url;
        a.className = 'rec-capsule';
        a.innerHTML = `<span class="nav-icon" style="font-size: 1.1rem; filter: grayscale(1) opacity(0.8);">${tool.icon}</span> ${tool.name}`;
        recentContainer.appendChild(a);
    });
}
