$cssPath = "c:\Users\HP\Desktop\Projects Folder\world_of_tools\css\style.css"
$content = Get-Content $cssPath -Raw

# 1. Update Design System Name
$content = $content -replace '/\* Modern & Premium Design System 2026 \*/', '/* Vintage Notebook & Academic Retro Design System 2026 */'

# 2. Update Variables
$content = $content -replace '--bg-color: #f8fafc', '--bg-color: #fdfcf9'
$content = $content -replace '--text-color: #0f172a', '--text-color: #2c2520'
$content = $content -replace '--text-muted: #64748b', '--text-muted: #6b635c'
$content = $content -replace '--primary-color: #4f46e5', '--primary-color: #e67e22'
$content = $content -replace '--primary-gradient: linear-gradient\(135deg, #4f46e5, #7c3aed\)', '--primary-gradient: linear-gradient(135deg, #e67e22, #d35400)'
$content = $content -replace '--primary-hover: #4338ca', '--primary-hover: #d35400'
$content = $content -replace '--secondary-color: #10b981', '--secondary-color: #27ae60'
$content = $content -replace '--border-color: rgba\(226, 232, 240, 0.8\)', '--border-color: #3d342d'
$content = $content -replace '--radius-md: 16px', '--radius-md: 4px'
$content = $content -replace '--radius-lg: 24px', '--radius-lg: 8px'
$content = $content -replace '--radius-xl: 32px', '--radius-xl: 12px'

# 3. Add New Variables
$content = $content -replace '--font-body: .*', "--font-body: 'Inter', system-ui, -apple-system, sans-serif;`n    --paper-shadow: 4px 4px 0px #3d342d;`n    --paper-shadow-hover: 6px 6px 0px #3d342d;"

# 4. Update body for notebook lines
$content = $content -replace 'background-color: var\(--bg-color\);', 'background-color: var(--bg-color);`n    background-image: linear-gradient(var(--bg-color) 24px, #f1ece1 25px);`n    background-size: 100% 25px;'

# 5. Overhaul Buttons & Cards
$content = $content -replace 'backdrop-filter: blur\(16px\);', '/* backdrop-filter removed for retro */'
$content = $content -replace 'border: 1px solid var\(--glass-border\);', 'border: 2px solid var(--border-color);'
$content = $content -replace 'box-shadow: var\(--card-shadow\);', 'box-shadow: var(--paper-shadow);'
$content = $content -replace 'box-shadow: var\(--card-shadow-hover\);', 'box-shadow: var(--paper-shadow-hover);'
$content = $content -replace 'transform: translateY\(-8px\);', 'transform: translate(-2px, -2px);'

# 6. Button Hover effect (0.5s transition and scale)
$content = $content -replace 'transition: all 0.3s ease;', 'transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);'
$content = $content -replace 'transform: translateY\(-2px\);', 'transform: scale(1.05) translate(-2px, -2px);'

Set-Content -Path $cssPath -Value $content -Encoding UTF8
