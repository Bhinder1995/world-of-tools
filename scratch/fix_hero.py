import re

with open('index.html', encoding='utf-8') as f:
    content = f.read()

# 1. Update hero badge - add badge-dot, remove inline style, update count to 70+
old_badge = '<div class="hero-badge" style="background: var(--nb-yellow); font-weight: 850;">\u2728 60+ Free Online Tools \u2014 Instant. Private. Pro.</div>'
new_badge = '<div class="hero-badge">\n    <span class="badge-dot"></span>\n    \u2728 70+ Free Online Tools \u2014 Instant. Private. Pro.\n  </div>'
content = content.replace(old_badge, new_badge)
print('Badge updated:', old_badge[:40] in content == False)

# 2. Update hero h1
old_h1 = '<h1 class="hero-h1">60+ Free Online Tools<br><span>Instant &amp; Private.</span></h1>'
new_h1 = '<h1 class="hero-h1">Your Free <span>All-in-One</span><br>Toolkit &mdash; 70+ Tools</h1>'
content = content.replace(old_h1, new_h1)
print('H1 updated')

# 3. Update hero sub - remove inline style (use CSS class instead), update text
old_sub = '<p class="hero-sub" style="font-size: 1.1rem; font-weight: 600; line-height: 1.5; color: #444; max-width: 700px; margin: 0 auto 1.5rem;">The only utility toolkit you\'ll ever need. High-performance browser tools for developers, creators, and daily productivity.</p>'
new_sub = '<p class="hero-sub">The ultimate free toolkit for developers, creators &amp; everyday productivity. 70+ browser-based tools \u2014 zero sign-up, zero tracking, instant results.</p>'
content = content.replace(old_sub, new_sub)
print('Sub updated')

# 4. Update search placeholder 60 -> 70
content = content.replace(
    'Search 60+ free online tools...',
    'Search 70+ free tools...'
)

# 5. Fix /index.html -> / links
content = content.replace('href="/index.html"', 'href="/"')
content = content.replace("href='/index.html'", "href='/'")

# 6. Fix footer brand copy
content = content.replace(
    '60+ free online utility tools. 100% private.',
    '70+ free online utility tools. 100% private.'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done! All homepage updates applied.')
