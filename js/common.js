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
                <a href="index.html" class="logo">
                    <span>⚡</span> HUB
                </a>
                <nav>
                    <ul>
                        <li><a href="index.html#calculators">Calculators</a></li>
                        <li><a href="index.html#tools">Text Tools</a></li>
                        <li><a href="index.html#converters">Converters</a></li>
                        <li><a href="index.html#generators">Generators</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    `;

    // Only inject if header exists and is empty, or replace it if it's default
    const header = document.querySelector('header');
    if (header) {
        header.innerHTML = headerHTML;
    }
}

function injectFooter() {
    const footerHTML = `
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>WorldOfTools</h4>
                    <p>Free. Fast. Private. No server-side processing for your data.</p>
                </div>
                <div class="footer-section">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="index.html">Home</a></li>
                        <li><a href="age-calculator.html">Age Calculator</a></li>
                        <li><a href="link-shortener.html">Link Shortener</a></li>
                        <li><a href="password-generator.html">Password Gen</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Legal</h4>
                    <ul>
                        <li><a href="privacy.html">Privacy Policy</a></li>
                        <li><a href="terms.html">Terms of Service</a></li>
                        <li><a href="contact.html">Contact</a></li>
                    </ul>
                </div>
            </div>
            <div class="text-center" style="margin-top: 2rem; opacity: 0.6; font-size: 0.8rem;">
                &copy; ${new Date().getFullYear()} WorldOfTools. All rights reserved.
            </div>
        </div>
    `;

    const footer = document.querySelector('footer');
    if (footer) {
        footer.innerHTML = footerHTML;
    }
}

function registerServiceWorker() {
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', () => {
            navigator.serviceWorker.register('sw.js')
                .then(registration => {
                    console.log('ServiceWorker registration successful');
                })
                .catch(err => {
                    console.log('ServiceWorker registration failed: ', err);
                });
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
