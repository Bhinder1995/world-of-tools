// Common JS for Mega Utility Hub

document.addEventListener('DOMContentLoaded', () => {
    injectHeader();
    injectFooter();
    registerServiceWorker();
    highlightActiveLink();
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
                        <li><a href="/#calculators">Calculators</a></li>
                        <li><a href="/#tools">Tools</a></li>
                        <li><a href="/#dev-tools">Developers</a></li>
                        <li><a href="/#utilities">Utilities</a></li>
                    </ul>
                </nav>

                <button class="menu-toggle" aria-label="Toggle navigation">
                    ☰
                </button>
            </div>
        </div>
    `;

    const header = document.querySelector('header');
    if (header) {
        header.innerHTML = headerHTML;
        setupMobileMenu();
    }
}

function setupMobileMenu() {
    const toggle = document.querySelector('.menu-toggle');
    const nav = document.getElementById('main-nav');

    if (toggle && nav) {
        toggle.addEventListener('click', (e) => {
            e.stopPropagation();
            nav.classList.toggle('active');
            toggle.textContent = nav.classList.contains('active') ? '✕' : '☰';
        });

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
        <footer style="background: #0f172a; color: white; padding: 10rem 1.5rem 4rem; position: relative; overflow: hidden; margin-top: 8rem;">
            <div style="position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 600px; height: 300px; background: radial-gradient(circle, rgba(79, 70, 229, 0.08) 0%, transparent 70%); pointer-events: none;"></div>
            
            <div class="footer-content" style="max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 4rem; position: relative; z-index: 1;">
                <div class="footer-section">
                    <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 2rem;">
                        <img src="/logo.svg" alt="WorldOfTools" style="width: 36px; height: 36px;">
                        <span style="font-family: var(--font-heading); font-weight: 800; font-size: 1.25rem;">WorldOfTools</span>
                    </div>
                    <p style="color: #94a3b8; line-height: 1.8; margin-bottom: 2rem; max-width: 300px; font-size: 0.95rem;">
                        The ultimate privacy-focused utility hub. Every tool runs 100% in your browser for maximum speed and security.
                    </p>
                    <div style="color: white; font-weight: 700; font-size: 0.9rem;">Fast. Free. Private.</div>
                </div>
                <div class="footer-section">
                    <h4 style="color: white; font-weight: 800; margin-bottom: 2rem; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.85rem;">Utilities</h4>
                    <ul>
                        <li><a href="/image-compressor">Image Resizer & Compressor</a></li>
                        <li><a href="/background-remover">Background Remover</a></li>
                        <li><a href="/image-upscaler">Image Upscaler</a></li>
                        <li><a href="/image-converter">Image Converter</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4 style="color: white; font-weight: 800; margin-bottom: 2rem; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.85rem;">Calculators</h4>
                    <ul>
                        <li><a href="/age-calculator">Age Calculator</a></li>
                        <li><a href="/emi-calculator">EMI Calculator</a></li>
                        <li><a href="/gst-calculator">GST Calculator</a></li>
                        <li><a href="/scientific-calculator">Scientific Calculator</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4 style="color: white; font-weight: 800; margin-bottom: 2rem; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.85rem;">Categories</h4>
                    <ul>
                        <li><a href="/calculators-online">Calculators</a></li>
                        <li><a href="/developer-tools-online">Dev Tools</a></li>
                        <li><a href="/seo-tools-free">SEO Tools</a></li>
                        <li><a href="/text-tools-online">Text Tools</a></li>
                        <li><a href="/web-utilities-free">Web Utilities</a></li>
                    </ul>
                </div>
                <div class="footer-section how-to-use-section" style="grid-column: span 2;">
                    <h4 style="color: white; font-weight: 800; margin-bottom: 2rem; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.85rem;">How to Use Our Tools</h4>
                    <ul style="display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 0.75rem; font-size: 0.85rem;">
                        <li><a href="/guides/age-calculator-guide">Age Calculator Guide</a></li>
                        <li><a href="/guides/background-remover-guide">Background Remover Guide</a></li>
                        <li><a href="/guides/barcode-generator-guide">Barcode Generator Guide</a></li>
                        <li><a href="/guides/base64-encoder-decoder-guide">Base64 Conv. Guide</a></li>
                        <li><a href="/guides/case-converter-guide">Case Converter Guide</a></li>
                        <li><a href="/guides/color-converter-guide">Color Converter Guide</a></li>
                        <li><a href="/guides/cron-expression-generator-guide">Cron Generator Guide</a></li>
                        <li><a href="/guides/css-minifier-guide">CSS Minifier Guide</a></li>
                        <li><a href="/guides/csv-to-json-guide">CSV to JSON Guide</a></li>
                        <li><a href="/guides/emi-calculator-guide">EMI Calculator Guide</a></li>
                        <li><a href="/guides/gst-calculator-guide">GST Calculator Guide</a></li>
                        <li><a href="/guides/hash-generator-guide">Hash Generator Guide</a></li>
                        <li><a href="/guides/image-compressor-guide">Image Compressor Guide</a></li>
                        <li><a href="/guides/image-converter-guide">Image Converter Guide</a></li>
                        <li><a href="/guides/image-upscaler-guide">Image Upscaler Guide</a></li>
                        <li><a href="/guides/json-formatter-guide">JSON Formatter Guide</a></li>
                        <li><a href="/guides/jwt-decoder-guide">JWT Decoder Guide</a></li>
                        <li><a href="/guides/keyword-density-checker-guide">Keyword Density Guide</a></li>
                        <li><a href="/guides/link-shortener-guide">Link Shortener Guide</a></li>
                        <li><a href="/guides/linkedin-creator-suite-guide">LinkedIn Suite Guide</a></li>
                        <li><a href="/guides/lorem-ipsum-generator-guide">Lorem Ipsum Guide</a></li>
                        <li><a href="/guides/markdown-to-html-guide">Markdown to HTML Guide</a></li>
                        <li><a href="/guides/number-to-words-converter-guide">Number to Words Guide</a></li>
                        <li><a href="/guides/password-generator-guide">Password Generator Guide</a></li>
                        <li><a href="/guides/percentage-calculator-guide">Percentage Calc Guide</a></li>
                        <li><a href="/guides/qr-code-generator-guide">QR Code Gen Guide</a></li>
                        <li><a href="/guides/random-number-generator-guide">Random Number Guide</a></li>
                        <li><a href="/guides/regex-tester-guide">Regex Tester Guide</a></li>
                        <li><a href="/guides/roman-numerals-converter-guide">Roman Numerals Guide</a></li>
                        <li><a href="/guides/scientific-calculator-guide">Scientific Calc Guide</a></li>
                        <li><a href="/guides/seo-meta-tag-generator-guide">SEO Meta Tag Guide</a></li>
                        <li><a href="/guides/sql-formatter-guide">SQL Formatter Guide</a></li>
                        <li><a href="/guides/text-compare-tool-guide">Text Compare Guide</a></li>
                        <li><a href="/guides/text-to-binary-converter-guide">Text to Binary Guide</a></li>
                        <li><a href="/guides/time-zone-converter-guide">Time Zone Guide</a></li>
                        <li><a href="/guides/unit-converter-guide">Unit Converter Guide</a></li>
                        <li><a href="/guides/url-encoder-decoder-guide">URL Enc/Dec Guide</a></li>
                        <li><a href="/guides/uuid-generator-guide">UUID Generator Guide</a></li>
                        <li><a href="/guides/xml-formatter-guide">XML Formatter Guide</a></li>
                        <li><a href="/guides/youtube-thumbnail-downloader-guide">YT Thumbnail Guide</a></li>
                        <li><a href="/guides/word-counter-guide">Word Counter Guide</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4 style="color: white; font-weight: 800; margin-bottom: 2rem; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.85rem;">Company</h4>
                    <ul>
                        <li><a href="/contact">Contact Us</a></li>
                        <li><a href="/privacy">Privacy Policy</a></li>
                        <li><a href="/terms">Terms of Service</a></li>
                    </ul>
                </div>
            </div>
            <div class="footer-bottom" style="max-width: 1200px; margin: 6rem auto 0; padding-top: 3rem; border-top: 1px solid rgba(255, 255, 255, 0.05); text-align: center; color: #64748b; font-size: 0.9rem;">
                <p>&copy; ${new Date().getFullYear()} WorldOfTools. Professional utilities for developers and creators. All rights reserved.</p>
            </div>
        </footer>
    `;

    const footer = document.querySelector('footer');
    if (footer) {
        footer.innerHTML = footerHTML;
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
                                // New worker is installed and waiting
                                // controllerchange listener below will handle the reload
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
                window.location.reload();
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
