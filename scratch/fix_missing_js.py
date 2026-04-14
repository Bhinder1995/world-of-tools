import os

def fix_missing_js():
    root_dir = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
    js_tag = '<script src="/js/common.js"></script>'
    
    for root, dirs, files in os.walk(root_dir):
        if "node_modules" in root or ".git" in root: continue
        for file in files:
            if file.endswith(".html"):
                p = os.path.join(root, file)
                try:
                    with open(p, "r", encoding="utf-8") as f:
                        content = f.read()
                    
                    if js_tag not in content:
                        # Add before </body>
                        if "</body>" in content:
                            content = content.replace("</body>", f"{js_tag}\n</body>")
                            with open(p, "w", encoding="utf-8") as f:
                                f.write(content)
                            print(f"Added common.js to {p}")
                except Exception as e:
                    print(f"Error {p}: {e}")

if __name__ == "__main__":
    fix_missing_js()
