/**
 * WorldOfTools SEO & UX Utility v2.0
 * Managed Schema, FAQ, Hreflang & Breadcrumb Manager
 */
document.addEventListener('DOMContentLoaded', () => {
    initL10n();
    initFAQs();
    injectBreadcrumbSchema();
    injectSoftwareApplicationSchema();
});

function initL10n() {
    try {
        const canonical = document.querySelector('link[rel="canonical"]');
        if (!canonical) return;
        const currentUrl = canonical.getAttribute('href');
        const path = new URL(currentUrl).pathname.replace(/\/$/, '');
        const slug = path.split('/').filter(Boolean).pop() || 'index';

        const map = {
            "en": "https://worldoftools.in",
            "es": "https://worldoftools.in/es",
            "pt": "https://worldoftools.in/pt",
            "hi": "https://worldoftools.in/hi",
            "fr": "https://worldoftools.in/fr",
            "de": "https://worldoftools.in/de"
        };

        Object.entries(map).forEach(([lang, base]) => {
            const href = slug === 'index' ? base + '/' : base + '/' + slug;
            injectTag('link', {
                rel: 'alternate',
                hreflang: lang,
                href: href
            }, `hreflang-${lang}`);
        });

        injectTag('link', {
            rel: 'alternate',
            hreflang: 'x-default',
            href: 'https://worldoftools.in/' + (slug === 'index' ? '' : slug)
        }, 'hreflang-default');
    } catch (e) {
        console.warn('L10n init skipped:', e.message);
    }
}

function initFAQs() {
    const faqDetails = document.querySelectorAll('details');
    if (!faqDetails.length) return;
    const items = [];
    faqDetails.forEach(detail => {
        const summary = detail.querySelector('summary');
        const p = detail.querySelector('p') || detail.querySelector('div.faq-body');
        if (summary && p) {
            items.push({
                "@type": "Question",
                "name": summary.textContent.trim(),
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": p.textContent.trim()
                }
            });
        }
    });
    if (items.length) {
        injectSchema({
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": items
        }, 'faq-schema');
    }
}

function injectSoftwareApplicationSchema() {
    const h1 = document.querySelector('h1');
    if (!h1) return;
    const title = h1.textContent.trim();
    const canonical = document.querySelector('link[rel="canonical"]');
    const url = canonical ? canonical.getAttribute('href') : window.location.href;
    const desc = document.querySelector('meta[name="description"]');
    const description = desc ? desc.getAttribute('content') : '';

    const appSchema = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": title,
        "url": url,
        "description": description,
        "applicationCategory": "UtilityApplication",
        "operatingSystem": "All",
        "browserRequirements": "Requires JavaScript",
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "USD",
            "availability": "https://schema.org/InStock"
        }
    };

    // If it's a calculator, use more specific type
    if (url.includes('calculator') || title.toLowerCase().includes('calculator')) {
        appSchema["@type"] = "WebApplication";
    }

    injectSchema(appSchema, 'software-app-schema');
}

function injectBreadcrumbSchema() {
    const path = window.location.pathname;
    const segments = path.split('/').filter(s => s !== '');
    const labels = {
        'es': { 'home': 'Inicio', 'guides': 'Guías' },
        'pt': { 'home': 'Início', 'guides': 'Guias' },
        'hi': { 'home': 'होम', 'guides': 'गाइड' },
        'fr': { 'home': 'Accueil', 'guides': 'Guides' },
        'de': { 'home': 'Start', 'guides': 'Ratgeber' },
        'en': { 'home': 'Home', 'guides': 'Guides' }
    };
    const currentLang = labels[segments[0]] ? segments[0] : 'en';
    const l10n = labels[currentLang];
    const crumbs = [{
        "@type": "ListItem",
        "position": 1,
        "name": l10n.home,
        "item": "https://worldoftools.in/" + (currentLang === 'en' ? '' : currentLang + '/')
    }];
    if (segments.length > 0) {
        const startIdx = labels[segments[0]] ? 1 : 0;
        let currentPath = "https://worldoftools.in/";
        segments.slice(startIdx).forEach((seg) => {
            currentPath += (currentLang === 'en' ? '' : currentLang + '/') + seg + '/';
            crumbs.push({
                "@type": "ListItem",
                "position": crumbs.length + 1,
                "name": seg.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' '),
                "item": currentPath.replace(/\/+$/, '')
            });
        });
    }
    injectSchema({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": crumbs
    }, 'breadcrumb-schema');
}

function injectSchema(data, id) {
    if (document.getElementById(id)) return;
    const script = document.createElement('script');
    script.type = 'application/ld+json';
    script.id = id;
    script.textContent = JSON.stringify(data);
    document.head.appendChild(script);
}

function injectTag(tag, attributes, id) {
    if (document.getElementById(id)) return;
    const el = document.createElement(tag);
    el.id = id;
    for (const [key, value] of Object.entries(attributes)) {
        el.setAttribute(key, value);
    }
    document.head.appendChild(el);
}
