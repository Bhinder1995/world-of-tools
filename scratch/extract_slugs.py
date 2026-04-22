import re
with open('WorldOfTools_Guides_and_InterLink_Report.html', 'r', encoding='utf-8') as f:
    text = f.read()
matches = re.findall(r'<div class="guide-slug">worldoftools\.in/(.*?) ·', text)
for i, m in enumerate(matches):
    print(f"{i+1}. {m}")
