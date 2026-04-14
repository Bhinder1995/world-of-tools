import os

def brute_overhaul_index():
    path = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools\index.html"
    with open(path, "rb") as f:
        data = f.read()

    # Repair encoding first (assuming double corruption)
    def repair(d):
        try:
            return d.decode('utf-8').encode('latin-1').decode('utf-8')
        except:
            return d.decode('utf-8', errors='ignore')

    content = repair(data)
    
    # Fix common garbled strings from previous views
    content = content.replace("Ã¢Å“Â¨", "✨")
    content = content.replace("Ã¢Å“â€œ", "✓")
    content = content.replace("Ã°Å¸â€ Â ", "🔍")
    content = content.replace("Ã°Å¸Å¡â‚¬", "🚀")
    content = content.replace("Ã°Å¸â€¢â€™", "🕒")
    content = content.replace("Ã°Å¸â€˜â€", "👔")
    content = content.replace("Ã°Å¸â€Â ", "🔠")
    content = content.replace("Ã°Å¸â€œÂ ", "📍")
    content = content.replace("Ã°Å¸Å½â€š", "🎂")
    content = content.replace("Ã°Å¸â€œÂ¹", "📹")
    content = content.replace("Ã°Å¸â€ºÂ¡ï¸", "🛡️")

    # Change 2px to 3px (Neo-Brutalist)
    content = content.replace("border: 2px solid var(--border-color)", "border: 3px solid var(--border-color)")
    content = content.replace("border: 2px solid rgba(230, 126, 34, 0.3)", "border: 3px solid var(--primary-color)")

    # Remove hero background lines
    bad_bg = 'background-image: linear-gradient(var(--bg-color) 24px, #f1ece1 25px); background-size: 30px 30px;'
    content = content.replace(bad_bg, "")
    
    # Simple clean background for hero section div
    content = content.replace('background: var(--bg-color); text-align: center; position: relative; overflow: hidden;', 'background: var(--bg-color); text-align: center; position: relative;')

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Overhauled {path} to Retro Neo-Brutalist.")

if __name__ == "__main__":
    brute_overhaul_index()
