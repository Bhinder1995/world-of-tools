import re

with open(r'c:\Users\HP\Desktop\Projects Folder\world_of_tools\index.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Fix tool categories links - find original words plus whatever garbage precedes them inside the a tag
text = re.sub(r'(<a class=\"btn btn-secondary\"[^>]*>\n\n).*?(Calculators)', r'\1🧮 \2', text, flags=re.DOTALL)
text = re.sub(r'(<a class=\"btn btn-secondary\"[^>]*>\n\n).*?(Developer Tools)', r'\1🛠️ \2', text, flags=re.DOTALL)
text = re.sub(r'(<a class=\"btn btn-secondary\"[^>]*>\n\n).*?(SEO Tools)', r'\1📈 \2', text, flags=re.DOTALL)
text = re.sub(r'(<a class=\"btn btn-secondary\"[^>]*>\n\n).*?(Text Tools)', r'\1✍️ \2', text, flags=re.DOTALL)
text = re.sub(r'(<a class=\"btn btn-secondary\"[^>]*>\n\n).*?(Web Utilities)', r'\1🌐 \2', text, flags=re.DOTALL)

# Fix Mobile Nav CSS
# Mobile nav links are visible because nav gets display: flex due to CSS overrides or missing media query
text = text.replace("nav.style.display = 'none';", "nav.style.display = 'none'; nav.classList.remove('open');")

with open(r'c:\Users\HP\Desktop\Projects Folder\world_of_tools\index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Categories fixed')
