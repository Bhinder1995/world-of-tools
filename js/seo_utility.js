/**
 * WorldOfTools SEO & UX Utility v1.1
 * Managed Schema, FAQ & Global Hreflang Manager
 */

document.addEventListener('DOMContentLoaded', () => {
    initL10n(); // Global Hreflang & Canonical Logic
    initFAQs();
    injectBreadcrumbSchema();
});

/**
 * Handles Global L10n (hreflang) injection 
 */
async function initL10n() {
    try {
        const response = await fetch('/js/l10n_map.json');
        const map = await response.json();
        
        const path = window.location.pathname;
        const segments = path.split('/').filter(s => s !== '');
        
        // Find current tool slug and language
        let currentLang = 'en';
        let currentSlug = 'index';
        
        if (segments.length > 0 && map.languages.some(l => l.code === segments[0])) {
            currentLang = segments[0];
            currentSlug = segments[1] || 'index';
        } else if (segments.length > 0) {
            currentSlug = segments[0];
        }

        // Logic to find translation group
        const translationKey = Object.keys(map.translations).find(key => 
            Object.values(map.translations[key]).includes(currentSlug)
        );

        if (translationKey) {
            const group = map.translations[translationKey];
            map.languages.forEach(lang => {
                const targetSlug = group[lang.code] || group['en'];
                const href = lang.code === 'en' 
                    ? `https://worldoftools.in/${targetSlug === 'index' ? '' : targetSlug}`
                    : `https://worldoftools.in/${lang.code}/${targetSlug === 'index' ? '' : targetSlug}`;
                
                injectHeaderTag('link', {
                    rel: 'alternate',
                    hreflang: lang.code,
                    href: href
                }, `hreflang-${lang.code}`);
            });

            // Default x-default
            injectHeaderTag('link', {
                rel: 'alternate',
                hreflang: 'x-default',
                href: `https://worldoftools.in/${group['en'] === 'index' ? '' : group['en']}`
            }, `hreflang-default`);
        }
    } catch (e) { console.error("L10n Init Error", e); }
}

/**
 * Handles FAQ Toggles and Injecting FAQPage JSON-LD
 */
function initFAQs() {
    const faqDetails = document.querySelectorAll('details');
    if (!faqDetails.length) return;

    const faqItems = [];

    faqDetails.forEach(detail => {
        const summary = detail.querySelector('summary');
        const content = detail.querySelector('p') || detail.querySelector('div');

        if (summary && content) {
            faqItems.push({
                "@type": "Question",
                "name": summary.textContent.trim(),
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": content.textContent.trim()
                }
            });
        }
    });

    if (faqItems.length) {
        const schema = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": faqItems
        };
        injectSchema(schema, 'faq-schema');
    }
}

/**
 * Auto-injects BreadcrumbList Schema based on URL structure
 */
function injectBreadcrumbSchema() {
    const path = window.location.pathname;
    const segments = path.split('/').filter(s => s !== '');
    
    // Localized Breadcrumb Labels
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
        let currentPath = "https://worldoftools.in/";
        const startIdx = labels[segments[0]] ? 1 : 0;
        
        segments.slice(startIdx).forEach((seg, index) => {
            currentPath += (currentLang === 'en' ? '' : currentLang + '/') + seg;
            crumbs.push({
                "@type": "ListItem",
                "position": crumbs.length + 1,
                "name": seg.split('-').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' '),
                "item": currentPath
            });
        });
    }

    injectSchema({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": crumbs
    }, 'breadcrumb-schema');
}

/**
 * Generic Helper to inject JSON-LD into the head
 */
function injectSchema(data, id) {
    if (document.getElementById(id)) return;
    const script = document.createElement('script');
    script.type = 'application/ld+json';
    script.id = id;
    script.text = JSON.stringify(data);
    document.head.appendChild(script);
}

/**
 * Helper to inject generic <head> tags
 */
function injectHeaderTag(tag, attributes, id) {
    if (document.getElementById(id)) return;
    const el = document.createElement(tag);
    el.id = id;
    for (let key in attributes) el.setAttribute(key, attributes[key]);
    document.head.appendChild(el);
}
