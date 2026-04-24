import os
import xml.etree.ElementTree as ET

directory = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"
sitemap_path = os.path.join(directory, "sitemap.xml")

def get_sitemap_urls():
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    urls = []
    for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
        loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}url/loc') # This might be wrong due to namespace
        loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc').text
        urls.append(loc)
    return urls

def main():
    sitemap_urls = get_sitemap_urls()
    sitemap_names = [url.split('/')[-1] for url in sitemap_urls]
    
    html_files = [f for f in os.listdir(directory) if f.endswith('.html')]
    # Remove .html extension for comparison if needed, but sitemap usually doesn't have .html
    # Let's see what sitemap looks like
    
    missing_in_sitemap = []
    for f in html_files:
        name = f[:-5] # remove .html
        if name == "index":
            if "https://worldoftools.in/" not in sitemap_urls:
                missing_in_sitemap.append(f)
        else:
            if name not in sitemap_names:
                missing_in_sitemap.append(f)
                
    print(f"Total HTML files: {len(html_files)}")
    print(f"Total Sitemap URLs: {len(sitemap_urls)}")
    print(f"Missing in Sitemap: {missing_in_sitemap}")

if __name__ == "__main__":
    main()
