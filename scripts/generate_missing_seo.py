import os
import json

def format_name(filename):
    # e.g. "image-to-text-ocr.html" -> "Image To Text Ocr"
    name = filename.replace('.html', '').replace('-', ' ')
    return name.title()

def generate_seo_dict(filename):
    tool_name = format_name(filename)
    
    return {
        "name": tool_name,
        "filename": filename,
        "title": f"{tool_name} | Fast & Free Online Utility - WorldOfTools",
        "description": f"Use our free {tool_name} online. Fast, secure, and fully browser-based. No data uploads or installation required.",
        "keywords": [
            tool_name.lower(),
            f"free {tool_name.lower()}",
            f"{tool_name.lower()} online",
            "worldoftools"
        ],
        "h1": f"{tool_name} - Fast, Secure & Free Online",
        "intro": [],
        "features": [
            {
                "title": "Instant Results",
                "desc": f"Process your data instantly with our optimized {tool_name}."
            },
            {
                "title": "100% Privacy",
                "desc": "Everything runs securely in your browser. No files or data are uploaded to our servers."
            },
            {
                "title": "Completely Free",
                "desc": "Enjoy full access without subscriptions, hidden fees, or intrusive ads."
            }
        ],
        "how_it_works": f"Our {tool_name} leverages modern web technologies to process your input locally in your browser. This ensures maximum speed and guarantees your privacy.",
        "steps": [
            "Input your desired content or file.",
            "Select any available options or parameters.",
            "Click execute to generate your result instantly."
        ],
        "faq": [
            {
                "question": f"Is this {tool_name} free to use?",
                "answer": "Yes, it is completely free to use with no hidden charges or limits."
            },
            {
                "question": "Is my data secure?",
                "answer": "Absolutely. Your data never leaves your device because all processing happens client-side in your browser."
            }
        ],
        "conclusion": f"Bookmark this {tool_name} for quick access whenever you need it.",
        "related_tools": []
    }

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Load existing covered tools so we don't overwrite
    with open(os.path.join(base_dir, 'seo_content.json'), 'r', encoding='utf-8') as f:
        existing_data = json.load(f)
        
    covered_filenames = {v.get('filename', k) for k, v in existing_data.items()}
    
    ignored_files = {'index.html', 'about-us.html', 'contact-us.html', 'privacy.html', 'terms.html'}
    
    missing_dict = {}
    
    for f in os.listdir(base_dir):
        if (f.endswith('.html') and 
            f not in covered_filenames and 
            f not in ignored_files and 
            'guide' not in f and 
            'report' not in f and 
            'audit' not in f and
            'calculators-online' not in f and
            'developer-tools' not in f):
            
            missing_dict[f] = generate_seo_dict(f)
            
    output_path = os.path.join(base_dir, 'seo_content_batch2.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(missing_dict, f, indent=4)
        
    print(f"Generated generic SEO content for {len(missing_dict)} missing tools in seo_content_batch2.json.")

if __name__ == "__main__":
    main()
