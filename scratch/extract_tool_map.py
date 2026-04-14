import re
import json
import os

def extract_map():
    file_path = 'worldoftools-master-fix-plan.html'
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find tool name, slug and icon
    # Patterns look like:
    # <td><span class="tool-name">Word Counter</span></td>
    # <td><span class="tool-slug">/word-counter</span></td>
    # <td><span class="icon-chip"><span class="mi">spellcheck</span> spellcheck</span></td>
    
    pattern = re.compile(r'class="tool-name">(.*?)</span>.*?class="tool-slug">/(.*?)</span>.*?class="mi">(.*?)</span>', re.DOTALL)
    matches = pattern.findall(content)

    tool_map = {}
    for name, slug, icon in matches:
        tool_map[slug.strip()] = {
            'name': name.strip(),
            'icon': icon.strip()
        }

    print(f"Extracted {len(tool_map)} tools from the plan.")
    
    if not os.path.exists('scratch'):
        os.makedirs('scratch')
        
    output_path = 'scratch/tool_plan_map.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(tool_map, f, indent=2)
    print(f"Saved mapping to {output_path}")

if __name__ == "__main__":
    extract_map()
