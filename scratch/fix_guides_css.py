import os
import re

CSS_OVERRIDES = """
    /* Neo-Brutalism Overrides for Guides */
    body {
        background-color: var(--bg-color);
        font-family: 'Lexend', 'Inter', sans-serif;
    }
    .guide-container {
        max-width: 900px;
        margin: 2rem auto;
        padding: 3rem 2rem;
        background: #ffffff;
        border: 3px solid #111827;
        box-shadow: 8px 8px 0px #111827;
        border-radius: var(--nb-radius-lg, 12px);
        line-height: 1.8;
        color: #111827;
    }
    .guide-header h1 {
        font-family: 'Space Grotesk', 'Lexend', sans-serif;
        font-weight: 900;
        letter-spacing: -0.04em;
        color: #111827;
    }
    .guide-content h2, .guide-content h3 {
        font-family: 'Space Grotesk', 'Lexend', sans-serif;
        font-weight: 800;
        color: #111827;
    }
    .guide-badge {
        background: var(--nb-lavender, #e9ddff);
        color: #111827;
        border: 2.5px solid #111827;
        box-shadow: 3px 3px 0 #111827;
        border-radius: 999px;
        font-weight: 800;
        padding: 0.5rem 1.25rem;
    }
    .back-btn {
        background: var(--nb-yellow, #fef08a);
        color: #111827;
        border: 3px solid #111827;
        box-shadow: 5px 5px 0 #111827;
        border-radius: 999px;
        font-weight: 850;
        text-shadow: none;
        transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    .back-btn:hover {
        transform: translate(-3px, -3px);
        box-shadow: 8px 8px 0 #111827;
    }
    .info-card {
        background: var(--nb-mint, #dcfce7);
        border: 3px solid #111827;
        box-shadow: 5px 5px 0 #111827;
        border-radius: var(--nb-radius, 8px);
        padding: 2rem;
        color: #111827;
    }
    .faq-item {
        border-bottom: 2px dashed #111827;
    }
    .faq-question {
        font-weight: 800;
        font-family: 'Space Grotesk', sans-serif;
    }
    .guide-content table {
        border: 3px solid #111827;
        box-shadow: 4px 4px 0 #111827;
        border-collapse: collapse;
        width: 100%;
        margin-bottom: 2rem;
    }
    .guide-content th {
        background: var(--nb-pink, #fce7f3);
        border: 2px solid #111827;
        font-weight: 800;
        padding: 1rem;
    }
    .guide-content td {
        border: 2px solid #111827;
        padding: 1rem;
    }
    .guide-content pre, .guide-content code {
        background: #f1f5f9;
        border: 2px solid #111827;
        border-radius: 6px;
        font-family: monospace;
    }
"""

def update_guide_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # 1. Update css link
    # Old might be `<link href="/css/style.css?v=2.5" rel="stylesheet"/>` or similar
    if '<link href="/css/neo-brutalism.css?v=6.1"' not in content:
        content = re.sub(r'<link href="/css/style\.css\?v=[0-9.]+" rel="stylesheet"/>',
                         '<link href="/css/style.css?v=6.1" rel="stylesheet"/>\n<link href="/css/neo-brutalism.css?v=6.1" rel="stylesheet"/>', content)

    # 2. Add overrides to style block or head
    # We will just append the CSS_OVERRIDES before </head> if they don't exist
    if 'Neo-Brutalism Overrides for Guides' not in content:
        content = content.replace("</head>", f"<style>{CSS_OVERRIDES}</style>\n</head>")

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated UI for {filepath}")

if __name__ == "__main__":
    for file in os.listdir('guides'):
        if file.endswith('.html'):
            update_guide_file(os.path.join('guides', file))
