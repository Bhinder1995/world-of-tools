import glob
import re
import os
import sys

# Ensure we can import from the current scripts folder
sys.path.append(os.path.dirname(__file__))

try:
    from seo_data import tool_seo_data, fallback_categories
except ImportError as e:
    print(f"Error importing seo_data: {e}")
    sys.exit(1)

# Go up to the root from scripts/
os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")

files = glob.glob('*.html')
count = 0

def get_category(filename):
    if any(x in filename for x in ['json', 'sql', 'jwt', 'hash', 'base64', 'regex', 'schema', 'minifier']):
        return "developer"
    if any(x in filename for x in ['image', 'video', 'converter', 'compressor', 'favicon', 'background', 'exif']):
        return "images"
    if any(x in filename for x in ['word', 'text', 'case', 'lorem', 'font']):
        return "text"
    return "text" # Default

print(f"Starting SEO diversification for {len(files)} files...")

for f in files:
    filename = os.path.basename(f)
    if filename in ['index.html', 'about-us.html', 'contact-us.html', 'privacy.html', 'terms.html']:
        continue
        
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        data = tool_seo_data.get(filename, {})
        category = get_category(filename)
        fallback = fallback_categories.get(category)
        
        original_content = content

        # 1. Update Title tag if specific data exists
        if "title" in data:
            content = re.sub(r'<title>.*?</title>', f'<title>{data["title"]} | WorldOfTools</title>', content)
            
        # 2. Update Meta Description if specific data exists
        if "description" in data:
            desc = data["description"]
            content = re.sub(r'<meta content=".*?" name="description"/>', f'<meta content="{desc}" name="description"/>', content)
            content = re.sub(r'<meta content=".*?" property="og:description"/>', f'<meta content="{desc}" property="og:description"/>', content)

        # 3. Update H2 and P in the Use Cases section
        h2_text = data.get("use_cases_h2", fallback["use_cases_h2"])
        p_text = data.get("use_cases_p", fallback["use_cases_p"])
        
        # Search for the "Use Cases" section. Pattern: 📊 Use Cases ... </h2>
        # Regex to be more flexible with emoji and spaces
        content = re.sub(
            r'<h2[^>]*?>\s*(?:📊|🚀|🛠️|✍️|📸|💡|📼|🛡️|⚖️|💰)?\s*Use Cases\s*—\s*Who Uses the .*?\?\s*</h2>',
            f'<h2 style="font-size:1.75rem;font-weight:800;margin-bottom:1.25rem;letter-spacing:-0.02em;">{h2_text}</h2>',
            content,
            flags=re.IGNORECASE
        )
        
        # Also replace the accompanying paragraph if found
        generic_p_text = "Streamline your daily tasks with reliable, private utilities that respect your data security."
        if generic_p_text in content:
            content = content.replace(generic_p_text, p_text)

        if content != original_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            count += 1
            # print(f"Optimized {filename}")
    except Exception as e:
        print(f"Error on {f}: {e}")

print(f"Successfully diversified SEO content in {count} files.")
