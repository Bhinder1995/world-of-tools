$jsPath = "c:\Users\HP\Desktop\Projects Folder\world_of_tools\js\common.js"
$content = Get-Content $jsPath -Raw

# 1. Update Header Background in common.js
$content = $content -replace 'background: rgba\(248, 250, 252, 0.8\);', 'background: var(--border-color);'
$content = $content -replace 'color: var\(--text-muted\);', 'color: rgba(255, 255, 255, 0.8);'

# 2. Update Footer/Pre-footer Colors
$content = $content -replace 'background: linear-gradient\(135deg, #4f46e5 0%, #7c3aed 100%\);', 'background: #3d342d; border-top: 2px solid #e67e22;'
$content = $content -replace 'color: #4f46e5;', 'color: #e67e22;' # Button text color
$content = $content -replace 'background: #0f172a;', 'background: #2c2520;' # Main footer bg

# 3. Update the button/link styles in common.js injected HTML
$content = $content -replace 'border-radius: 12px;', 'border-radius: 4px; border: 2px solid #e67e22;'
$content = $content -replace 'box-shadow: 0 4px 12px rgba\(0,0,0,0.15\);', 'box-shadow: 4px 4px 0px #000;'

# 4. Overhaul the mega dropdown Col Header
$content = $content -replace 'color: #1A56DB;', 'color: #e67e22;' # Tagline color

# 5. Fix Hover Transition in style.css was already done but can refine in JS if inline styles exist
$content = $content -replace 'transition: all 0.2s;', 'transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);'

Set-Content -Path $jsPath -Value $content -Encoding UTF8
