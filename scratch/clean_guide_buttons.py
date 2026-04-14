import os
import re

directories = ['.', 'hi', 'es']

# Look for: <div class="h1-guide-wrapper" ...> ... <h1>Something</h1> ... <a href="/guides/...> ... </a> ... </div>
# Replace entirely with: <h1>Something</h1>
# Ensure we capture the exact content inside h1
wrapper_pattern = re.compile(
    r'<div class="h1-guide-wrapper"[^>]*>.*?<div[^>]*>\s*(<h1[^>]*>.*?</h1>)\s*</div>.*?<a href="/guides/[^>]*>.*?</a>\s*</div>',
    re.DOTALL
)

# Second fallback: if there's no div but an a tag
# Sometimes it's just: <div class="h1-guide-wrapper"> <h1>..</h1> <a ...> </div>
wrapper_pattern2 = re.compile(
    r'<div class="h1-guide-wrapper"[^>]*>\s*(<h1[^>]*>.*?</h1>).*?<a href="/guides/[^>]*>.*?</a>\s*</div>',
    re.DOTALL
)

def run():
    count = 0
    for d in directories:
        if not os.path.exists(d): continue
        for f in os.listdir(d):
            if f.endswith('.html') and not f.startswith('guide-template.html'):
                filepath = os.path.join(d, f)
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Replace wrapper with just the extracted h1
                new_content = wrapper_pattern.sub(r'\1', content)
                new_content = wrapper_pattern2.sub(r'\1', new_content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as file:
                        file.write(new_content)
                    count += 1
    print(f"Cleaned {count} files")

run()
