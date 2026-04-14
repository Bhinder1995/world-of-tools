$files = Get-ChildItem -Path "c:\Users\HP\Desktop\Projects Folder\world_of_tools" -Filter "index.html" -Recurse

foreach ($file in $files) {
    if ($file.FullName -like "*guides*") { continue }
    $indexPath = $file.FullName
    $content = Get-Content $indexPath -Raw

# 1. Hero Section Cleanup
$content = $content -replace 'background: radial-gradient\(circle at 50% 0%, rgba\(79, 70, 229, 0.05\) 0%, #ffffff 60%\);', 'background: var(--bg-color);'
$content = $content -replace 'background-image: radial-gradient\(var\(--primary-color\) 0.5px, transparent 0.5px\);', 'background-image: linear-gradient(var(--bg-color) 24px, #f1ece1 25px);'
$content = $content -replace 'opacity: 0.03', 'opacity: 1'

# 2. Hero Subtitle & Badges
$content = $content -replace 'background: rgba\(79, 70, 229, 0.08\);', 'background: white; border: 2px solid var(--border-color);'
$content = $content -replace 'background: rgba\(16,185,129,0.08\);', 'background: white; border: 2px solid var(--border-color);'
$content = $content -replace 'border-radius: 99px;', 'border-radius: 4px;'
$content = $content -replace 'color: #059669;', 'color: var(--text-color);'

# 3. Search Wrapper
$content = $content -replace 'border-radius: 20px;', 'border-radius: 4px;'
$content = $content -replace 'box-shadow: 0 25px 50px -12px rgba\(0, 0, 0, 0.1\);', 'box-shadow: 6px 6px 0px var(--border-color);'

# 4. Tool Chips
$content = $content -replace 'border-radius: 12px;', 'border-radius: 4px;'
$content = $content -replace 'box-shadow: 0 4px 6px -1px rgba\(0, 0, 0, 0.05\);', 'box-shadow: 4px 4px 0px var(--border-color);'
$content = $content -replace 'background: #fef3c7;', 'background: white;'
$content = $content -replace 'color: #92400e;', 'color: var(--text-color);'

# 5. Recent Tools capsules
$content = $content -replace 'background: rgba\(79, 70, 229, 0.1\);', 'background: white; border: 2px solid var(--border-color);'
$content = $content -replace 'background: rgba\(16, 185, 129, 0.1\);', 'background: white; border: 2px solid var(--border-color);'

# 6. Buttons
$content = $content -replace 'border-radius: 16px;', 'border-radius: 4px;'

    Set-Content -Path $indexPath -Value $content -Encoding UTF8
}
