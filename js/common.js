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
                <a href="index" class="logo">
                    <span>⚡</span> HUB
                </a>
                <button class="menu-toggle" aria-label="Toggle navigation">
                    ☰
                </button>
                <nav id="main-nav">
                    <ul>
                        <li><a href="index#calculators">Calculators</a></li>
                        <li><a href="index#tools">Text Tools</a></li>
                        <li><a href="index#converters">Converters</a></li>
                        <li><a href="index#generators">Generators</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    `;

    // Only inject if header exists and is empty, or replace it if it's default
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
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>WorldOfTools</h4>
                    <p>Free. Fast. Private. No server-side processing for your data.</p>
                </div>
                <div class="footer-section">
                    <h4>Quick Links</h4>
                    <ul>
                        <li><a href="index">Home</a></li>
                        <li><a href="age-calculator">Age Calculator</a></li>
                        <li><a href="link-shortener">Link Shortener</a></li>
                        <li><a href="password-generator">Password Gen</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Legal</h4>
                    <ul>
                        <li><a href="privacy">Privacy Policy</a></li>
                        <li><a href="terms">Terms of Service</a></li>
                        <li><a href="contact">Contact</a></li>
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
