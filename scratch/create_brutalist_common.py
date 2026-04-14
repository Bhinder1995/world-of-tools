import os

def create_brutalist_common():
    # We will build the common.js content from scratch to ensure zero corruption
    # and perfect Neo-Brutalist styling.
    
    content = r"""// Common JS for Mega Utility Hub 2026 - Retro Neo-Brutalist Edition

function getLocalPath(path) {
    if (!path || path.startsWith('http') || path.startsWith('mailto:') || path.startsWith('#')) return path;
    let normalizedPath = path.startsWith('/') ? path : '/' + path;
    const langCodes = ['hi', 'es'];
    const currentPath = window.location.pathname;
    const match = currentPath.match(/^\/(hi|es)\//);
    const currentLang = match ? match[1] : 'en';
    if (currentLang === 'en') return normalizedPath;
    if (normalizedPath.match(/^\/(hi|es)\//)) return normalizedPath;
    if (normalizedPath === '/' || normalizedPath === '/index' || normalizedPath === '/index.html') return `/${currentLang}/index.html`;
    let cleanPath = normalizedPath.slice(1);
    if (cleanPath.startsWith('guides/')) return `/${cleanPath}${normalizedPath.includes('?') ? '&' : '?'}lang=${currentLang}`;
    if (!cleanPath.includes('.') && !cleanPath.endsWith('/')) cleanPath += '.html';
    return `/${currentLang}/${cleanPath}`;
}

const TRANSLATIONS = {
    'hi': {
        'all_tools': 'सभी उपकरण', 'calculators': 'कैलकुलेटर', 'dev_tools': 'डेवलपर टूल्स',
        'text_seo': 'टेक्स्ट और एसईओ', 'image_web': 'इमेज और वेब टूल्स',
        'might_need': '💡 क्या आपको इनकी भी आवश्यकता हो सकती है?',
        'back_to_tool': '← उपकरण पर वापस जाएं',
        'tag_new': '✨ नया', 'tag_advanced': '🧪 उन्नत', 'badge_private': '🛡️ 100% निजी'
    },
    'es': {
        'all_tools': 'Herramientas', 'calculators': 'Calculadoras', 'dev_tools': 'Desarrolladores',
        'text_seo': 'Texto y SEO', 'image_web': 'Imagen y Web',
        'might_need': '💡 ¿Podrías necesitar estos también?',
        'back_to_tool': '← Volver',
        'tag_new': '✨ Nuevo', 'tag_advanced': '🧪 Avanzado', 'badge_private': '🛡️ 100% Privado'
    },
    'en': {
        'all_tools': 'All Tools', 'calculators': 'Calculators', 'dev_tools': 'Developer Tools',
        'text_seo': 'Text & SEO', 'image_web': 'Image & Web Tools',
        'might_need': '💡 Might you need these next?',
        'back_to_tool': '← Back to Tool',
        'tag_new': '✨ New', 'tag_advanced': '🧪 Advanced', 'badge_private': '🛡️ 100% Private'
    }
};

function injectHeader() {
    const currentPath = window.location.pathname;
    const match = currentPath.match(/^\/(hi|es)\//);
    const lang = match ? match[1] : 'en';
    const t = TRANSLATIONS[lang];
    const root = lang === 'en' ? '/' : `/${lang}/index.html`;

    const headerHTML = `
        <div class="container" style="padding: 0.5rem 1.5rem;">
            <div class="header-content" style="display: flex; justify-content: space-between; align-items: center;">
                <a href="${root}" style="display: flex; align-items: center; gap: 0.75rem; text-decoration: none;">
                    <img src="/logo.svg" alt="Logo" width="32" height="32" style="border: 2px solid white; border-radius: 4px;">
                    <span style="font-family: 'Outfit', sans-serif; font-weight: 900; color: white; font-size: 1.4rem; letter-spacing: -0.02em;">WorldOfTools</span>
                </a>
                
                <nav style="display: flex; gap: 1.5rem; align-items: center;">
                    <a href="${getLocalPath('/calculators-online')}" style="color: white; text-decoration: none; font-weight: 700; font-size: 0.9rem; text-transform: uppercase;">${t.calculators}</a>
                    <a href="${getLocalPath('/guides/')}" style="color: white; text-decoration: none; font-weight: 700; font-size: 0.9rem; text-transform: uppercase;">Guides</a>
                    
                    <div class="lang-switcher" style="display: flex; gap: 0.5rem; background: rgba(0,0,0,0.3); padding: 0.25rem; border-radius: 4px; border: 1px solid rgba(255,255,255,0.2);">
                        <a href="javascript:void(0)" onclick="location.href='/'" style="color: white; text-decoration: none; font-size: 0.7rem; font-weight: 800; padding: 0.2rem 0.4rem;">EN</a>
                        <a href="javascript:void(0)" onclick="location.href='/hi/index.html'" style="color: white; text-decoration: none; font-size: 0.7rem; font-weight: 800; padding: 0.2rem 0.4rem;">HI</a>
                        <a href="javascript:void(0)" onclick="location.href='/es/index.html'" style="color: white; text-decoration: none; font-size: 0.7rem; font-weight: 800; padding: 0.2rem 0.4rem;">ES</a>
                    </div>
                </nav>
            </div>
        </div>
    `;

    const header = document.querySelector('header');
    if (header) {
        header.style.background = '#3d342d';
        header.style.borderBottom = '3px solid #3d342d';
        header.innerHTML = headerHTML;
    }
}

function injectFooter() {
    const currentPath = window.location.pathname;
    const match = currentPath.match(/^\/(hi|es)\//);
    const lang = match ? match[1] : 'en';
    const t = TRANSLATIONS[lang];

    const footerHTML = `
        <div style="background: #e67e22; border-top: 3px solid #3d342d; padding: 2rem 1rem; text-align: center;">
            <div class="container" style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; padding: 0;">
                <div style="font-weight: 900; color: #3d342d; text-transform: uppercase;">45+ Professional Tools - 100% Private</div>
                <a href="${getLocalPath('/')}" style="background: #3d342d; color: white; padding: 0.75rem 1.5rem; text-decoration: none; font-weight: 900; border-radius: 4px; box-shadow: 4px 4px 0px rgba(0,0,0,0.2); transition: all 0.3s;">EXPLORE ALL</a>
            </div>
        </div>
        <footer style="background: #2c2520; color: #fdfcf9; padding: 4rem 1.5rem; border-top: 3px solid #3d342d;">
            <div class="container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 3rem; padding: 0;">
                <div>
                    <div style="font-weight: 900; font-size: 1.5rem; margin-bottom: 1rem;">WorldOfTools</div>
                    <p style="font-size: 0.9rem; opacity: 0.7; line-height: 1.6;">The ultimate Neo-Brutalist utility hub. Fast, free, and runs entirely in your browser.</p>
                </div>
                <div>
                    <h4 style="text-transform: uppercase; margin-bottom: 1.5rem; font-size: 0.8rem; letter-spacing: 0.1em;">Links</h4>
                    <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.75rem;">
                        <li><a href="/about-us" style="color: inherit; text-decoration: none; opacity: 0.8;">About</a></li>
                        <li><a href="/privacy" style="color: inherit; text-decoration: none; opacity: 0.8;">Privacy</a></li>
                        <li><a href="/terms" style="color: inherit; text-decoration: none; opacity: 0.8;">Terms</a></li>
                        <li><a href="/contact-us" style="color: inherit; text-decoration: none; opacity: 0.8;">Contact</a></li>
                    </ul>
                </div>
                <div>
                    <h4 style="text-transform: uppercase; margin-bottom: 1.5rem; font-size: 0.8rem; letter-spacing: 0.1em;">Trust</h4>
                    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                        <span style="background: rgba(255,255,255,0.1); padding: 0.25rem 0.75rem; border-radius: 100px; font-size: 0.7rem; font-weight: 700;">🛡️ PRIVATE</span>
                        <span style="background: rgba(255,255,255,0.1); padding: 0.25rem 0.75rem; border-radius: 100px; font-size: 0.7rem; font-weight: 700;">⚡ INSTANT</span>
                    </div>
                </div>
            </div>
            <div class="container" style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1); text-align: center; font-size: 0.8rem; opacity: 0.5;">
                &copy; ${new Date().getFullYear()} WorldOfTools. No cookies. No tracking. Just tools.
            </div>
        </footer>
    `;

    const footer = document.querySelector('footer');
    if (footer) {
        footer.outerHTML = footerHTML;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    injectHeader();
    injectFooter();
});
"""
    
    with open(r"c:\Users\HP\Desktop\Projects Folder\world_of_tools\js\common.js", "w", encoding="utf-8") as f:
        f.write(content)
    print("Rewritten common.js with Retro Neo-Brutalist elements.")

if __name__ == "__main__":
    create_brutalist_common()
