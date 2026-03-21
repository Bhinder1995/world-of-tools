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
                        <li class="nav-dropdown">
                            <span class="dropdown-trigger">All Tools</span>
                            <div class="dropdown-menu">
                                <div class="dropdown-col">
                                    <h5>Calculators</h5>
                                    <ul>
                                        <li><a href="/age-calculator">Age Calculator</a></li>
                                        <li><a href="/bmi-calculator">BMI Calculator</a></li>
                                        <li><a href="/sip-calculator">SIP Calculator</a></li>
                                        <li><a href="/loan-eligibility-calculator">Loan Eligibility</a></li>
                                        <li><a href="/ppf-calculator">PPF Calculator</a></li>
                                        <li><a href="/emi-calculator">EMI Calculator</a></li>
                                        <li><a href="/gst-calculator">GST Calculator</a></li>
                                        <li><a href="/scientific-calculator">Scientific Calc</a></li>
                                        <li><a href="/percentage-calculator">Percentage Calc</a></li>
                                    </ul>
                                </div>
                                <div class="dropdown-col">
                                    <h5>Developers</h5>
                                    <ul>
                                        <li><a href="/json-formatter">JSON Formatter</a></li>
                                        <li><a href="/css-gradient-generator">CSS Gradient</a></li>
                                        <li><a href="/hash-generator">Hash Generator</a></li>
                                        <li><a href="/jwt-decoder">JWT Decoder</a></li>
                                        <li><a href="/sql-formatter">SQL Formatter</a></li>
                                        <li><a href="/cron-expression-generator">Cron Generator</a></li>
                                        <li><a href="/url-encoder-decoder">URL Encode/Decode</a></li>
                                        <li><a href="/base64-encoder-decoder">Base64 Encode/Decode</a></li>
                                        <li><a href="/regex-tester">Regex Tester</a></li>
                                        <li><a href="/csv-to-json">CSV to JSON</a></li>
                                    </ul>
                                </div>
                                <div class="dropdown-col">
                                    <h5>SEO & Web</h5>
                                    <ul>
                                        <li><a href="/word-counter">Word Counter</a></li>
                                        <li><a href="/seo-meta-tag-generator">Meta Tag Gen</a></li>
                                        <li><a href="/serp-preview">SERP Preview</a></li>
                                        <li><a href="/image-compressor">Image Compressor</a></li>
                                        <li><a href="/background-remover">Bg Remover</a></li>
                                        <li><a href="/qr-code-generator">QR Generator</a></li>
                                        <li><a href="/favicon-generator">Favicon Gen</a></li>
                                        <li><a href="/ip-address-lookup">IP Lookup</a></li>
                                        <li><a href="/aspect-ratio-calculator">Aspect Ratio</a></li>
                                        <li><a href="/invoice-generator">Invoice Gen</a></li>
                                    </ul>
                                </div>
                            </div>
                        </li>
                        <li><a href="/#calculators">Calculators</a></li>
                        <li><a href="/#tools">Gallery</a></li>
                        <li><a href="/guides/">Guides</a></li>
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
                <div class="footer-section">
                    <h4 style="color: white; font-weight: 800; margin-bottom: 2rem; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.85rem;">Popular Guides</h4>
                    <ul>
                        <li><a href="/guides/age-calculator-guide">Age Calculator Guide</a></li>
                        <li><a href="/guides/background-remover-guide">Background Remover Guide</a></li>
                        <li><a href="/guides/emi-calculator-guide">EMI Calculator Guide</a></li>
                        <li><a href="/guides/gst-calculator-guide">GST Calculator Guide</a></li>
                        <li><a href="/guides/unit-converter-guide">Unit Converter Guide</a></li>
                    </ul>
                    <a href="/guides/" style="display: inline-flex; align-items: center; gap: 0.5rem; margin-top: 1.5rem; background: rgba(255,255,255,0.05); color: white; padding: 0.6rem 1.2rem; border-radius: 10px; font-size: 0.8rem; font-weight: 700; text-decoration: none; border: 1px solid rgba(255,255,255,0.1); transition: all 0.2s;">
                        📚 Explore All 40+ Guides
                    </a>
                </div>
                <div class="footer-section">
                    <h4 style="color: white; font-weight: 800; margin-bottom: 2rem; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.85rem;">Company</h4>
                    <ul>
                        <li><a href="/about-us">About Us</a></li>
                        <li><a href="/contact-us">Contact Us</a></li>
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
