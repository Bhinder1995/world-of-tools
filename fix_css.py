import re

with open(r'c:\Users\HP\Desktop\Projects Folder\world_of_tools\css\style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_content = '''.logo-center {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    align-items: center;
    gap: 0.65rem;
    text-decoration: none;
    color: inherit;
    z-index: 10;
}'''

css = re.sub(r'\.logo-center\s*\{.*?\n\}', new_content, css, count=1, flags=re.DOTALL)

with open(r'c:\Users\HP\Desktop\Projects Folder\world_of_tools\css\style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('CSS updated successfully')
