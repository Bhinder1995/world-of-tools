/**
 * WorldOfTools SEO & UX Utility v3.0
 * Schema, FAQ, Hreflang, Geo, Twitter Tags & Breadcrumb Manager
 * Updated: en-IN hreflang dedup, guide schema, twitter:site, hi-IN support
 */
document.addEventListener('DOMContentLoaded', () => {
    initL10n();
    initFAQs();
    injectSoftwareAppOrArticleSchema();
    injectGeoMeta();
    injectOGLocale();
    injectTwitterSite();
    injectGuideToolAlternate();
});

// ── HREFLANG (no duplicate en / x-default with en-IN) ─────────────────────
function initL10n() {
    try {
        const canonical = document.querySelector('link[rel="canonical"]');
        if (!canonical) return;
        const currentUrl = canonical.getAttribute('href');
        const path = new URL(currentUrl).pathname.replace(/\/$/, '');
        const slug = path.split('/').filter(Boolean).pop() || 'index';

        // Only inject alternate languages (skip en-IN and x-default — already hardcoded in HTML)
        const map = {
            "es": "https://worldoftools.in/es",
            "pt": "https://worldoftools.in/pt",
            "hi": "https://worldoftools.in/hi",
            "fr": "https://worldoftools.in/fr",
            "de": "https://worldoftools.in/de"
        };

        // Add hi-IN specific hreflang pointing to the same slug
        // (actual Hindi content not available yet, but signals intent)
        injectTag('link', {
            rel: 'alternate',
            hreflang: 'hi-IN',
            href: 'https://worldoftools.in/hi/' + (slug === 'index' ? '' : slug)
        }, 'hreflang-hi-IN');

        Object.entries(map).forEach(([lang, base]) => {
            const href = slug === 'index' ? base + '/' : base + '/' + slug;
            injectTag('link', {
                rel: 'alternate',
                hreflang: lang,
                href: href
            }, `hreflang-${lang}`);
        });
    } catch (e) {
        console.warn('L10n init skipped:', e.message);
    }
}

// ── FAQ SCHEMA ────────────────────────────────────────────────────────────
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

// ── SOFTWARE APPLICATION (tool pages) / ARTICLE (guide pages) ────────────
function injectSoftwareAppOrArticleSchema() {
    const h1 = document.querySelector('h1');
    if (!h1) return;
    const title = h1.textContent.trim();
    const canonical = document.querySelector('link[rel="canonical"]');
    const url = canonical ? canonical.getAttribute('href') : window.location.href;
    const desc = document.querySelector('meta[name="description"]');
    const description = desc ? desc.getAttribute('content') : '';
    const isGuide = window.location.pathname.startsWith('/guides/');
    const today = '2026-05-28';

    if (isGuide) {
        const articleSchema = {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title,
            "description": description,
            "url": url,
            "mainEntityOfPage": { "@type": "WebPage", "@id": url },
            "datePublished": today + "T00:00:00+05:30",
            "dateModified": today + "T00:00:00+05:30",
            "author": {
                "@type": "Organization",
                "name": "WorldOfTools"
            },
            "publisher": {
                "@type": "Organization",
                "name": "WorldOfTools",
                "logo": {
                    "@type": "ImageObject",
                    "url": "https://worldoftools.in/logo.svg"
                }
            },
            "image": "https://worldoftools.in/app-icon.png"
        };
        injectSchema(articleSchema, 'article-schema');
    } else {
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
                "priceCurrency": "INR",
                "availability": "https://schema.org/InStock"
            }
        };
        if (url.includes('calculator') || title.toLowerCase().includes('calculator')) {
            appSchema["@type"] = "WebApplication";
        }
        injectSchema(appSchema, 'software-app-schema');
    }

    // Breadcrumb for both tool and guide pages
    injectBreadcrumbSchema();
}

// ── BREADCRUMB SCHEMA ────────────────────────────────────────────────────
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

// ── HELPERS ──────────────────────────────────────────────────────────────
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

// ── GEO META TAGS ────────────────────────────────────────────────────────
function injectGeoMeta() {
    if (document.getElementById('geo-region')) return;
    const tags = [
        ['geo.region', 'IN'],
        ['geo.placename', 'India'],
        ['geo.position', '20.593684;78.96288'],
        ['ICBM', '20.593684, 78.96288']
    ];
    tags.forEach(([name, content]) => {
        const meta = document.createElement('meta');
        meta.name = name;
        meta.content = content;
        document.head.appendChild(meta);
    });
}

// ── OG LOCALE ────────────────────────────────────────────────────────────
function injectOGLocale() {
    if (document.querySelector('[property="og:locale"]')) return;
    const meta = document.createElement('meta');
    meta.setAttribute('property', 'og:locale');
    meta.setAttribute('content', 'en_IN');
    document.head.appendChild(meta);
}

// ── TWITTER SITE ─────────────────────────────────────────────────────────
function injectTwitterSite() {
    if (document.querySelector('[name="twitter:site"]')) return;
    const meta = document.createElement('meta');
    meta.name = 'twitter:site';
    meta.content = '@worldoftools';
    document.head.appendChild(meta);
}

// ── GUIDE ↔ TOOL INTERLINKING (alternate links) ─────────────────────────
function injectGuideToolAlternate() {
    const path = window.location.pathname;
    if (path.startsWith('/guides/')) {
        // Guide page: link back to the tool page
        const toolSlug = path.replace('/guides/', '').replace('-guide', '').replace(/\/$/, '');
        if (toolSlug && toolSlug !== 'index') {
            injectTag('link', {
                rel: 'alternate',
                title: 'Tool',
                href: 'https://worldoftools.in/' + toolSlug
            }, 'guide-tool-link');
        }
    } else if (path !== '/') {
        // Tool page: link to its guide
        const slug = path.replace(/^\//, '').replace(/\/$/, '');
        if (slug && slug !== 'index') {
            const guideSlug = slug + '-guide';
            injectTag('link', {
                rel: 'alternate',
                title: 'Guide',
                href: 'https://worldoftools.in/guides/' + guideSlug
            }, 'tool-guide-link');
        }
    }
}
