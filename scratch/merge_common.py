import re

def main():
    # Read files
    with open('js/common.js', 'r', encoding='utf-8') as f:
        common_js = f.read()

    with open('old_common_utf8.js', 'r', encoding='utf-8') as f:
        old_common = f.read()

    # Extract old header HTML block
    header_start = old_common.find('const headerHTML = `')
    header_html_end = old_common.find('`;', header_start) + 1
    old_header_html = old_common[header_start:header_html_end]

    # Convert static hrefs to getLocalPath(...) in the old header
    # Match href="/some-path" but ignore href="/" and href="#"
    def replace_href(match):
        path = match.group(1)
        if path == '/' or path == '#':
            return match.group(0) # don't touch / or #
        return f'href="${{getLocalPath(\'{path}\')}}"'

    old_header_html = re.sub(r'href="(/[^"]+?)"', replace_href, old_header_html)
    old_header_html = old_header_html.replace('href="/"', 'href="${root}"')
    
    # We replace the old language switcher with the new one.
    old_switcher_start = old_header_html.find('<!-- Language Switcher -->')
    old_switcher_end = old_header_html.find('</div>\n\n                    <div class="global-privacy-badge"')
    
    # Extract the new language switcher from common.js
    new_switcher_start = common_js.find('<div class="lang-switcher">')
    new_switcher_end = common_js.find('</div>', new_switcher_start) + 6
    new_switcher_html = common_js[new_switcher_start:new_switcher_end]
    
    # Inject it into old_header_html
    old_header_html = old_header_html[:old_switcher_start] + new_switcher_html + old_header_html[old_switcher_end:]

    # Rename `headerHTML` variable to `html`
    old_header_html = old_header_html.replace('const headerHTML = `', 'const html = `')

    # Now construct the new injectHeader function body
    # We'll take the beginning of the new injectHeader (which defines lang, t, root)
    new_inject_header_start = common_js.find('function injectHeader() {')
    new_header_html_var = common_js.find('const html = `', new_inject_header_start)
    new_inject_header_top = common_js[new_inject_header_start:new_header_html_var]

    # and the bottom of the new injectHeader function logic
    old_header_bottom_start = old_common.find('const header = document.querySelector(\'header\');', header_start)
    old_header_bottom_end = old_common.find('}\n\nwindow.switchLanguage', header_start)
    
    # Actually, old style had `setupMobileMenu()` which we can just append, but new one handles mobile menu inline.
    # We will just append setupMobileMenu logic to JS.

    inject_header_func = new_inject_header_top + old_header_html + "\n\n    " + old_common[old_header_bottom_start:old_header_bottom_end]

    # Extract old footer HTML
    footer_start = old_common.find('const footerHTML = `')
    footer_end = old_common.find('`;', footer_start) + 1
    old_footer_html = old_common[footer_start:footer_end]
    
    old_footer_html = re.sub(r'href="(/[^"]+?)"', replace_href, old_footer_html)
    old_footer_html = old_footer_html.replace('href="/"', 'href="${root}"')
    
    old_footer_bottom_start = old_common.find('const footer = document.querySelector(\'footer\');', footer_start)
    old_footer_bottom_end = old_common.find('}\n\nfunction injectPostRecommendations', footer_start)
    
    inject_footer_func = 'function injectFooter() {\n' + '    const lang = getLang();\n    const root = lang === \'en\' ? \'/\' : `/${lang}/index.html`;\n    ' + old_footer_html + '\n\n    ' + old_common[old_footer_bottom_start:old_footer_bottom_end]
    
    # setupMobileMenu
    setup_mobile_menu_start = old_common.find('function setupMobileMenu() {')
    setup_mobile_menu_end = old_common.find('function injectFooter() {')
    setup_mobile_menu_func = old_common[setup_mobile_menu_start:setup_mobile_menu_end]

    # Reconstruct common.js
    top_common = common_js[:new_inject_header_start]
    bottom_common = common_js[common_js.find('document.addEventListener('):]

    final_js = top_common + inject_header_func + setup_mobile_menu_func + inject_footer_func + bottom_common

    with open('js/common.js', 'w', encoding='utf-8') as f:
        f.write(final_js)

if __name__ == '__main__':
    main()
