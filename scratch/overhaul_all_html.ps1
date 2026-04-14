$rootPath = "c:\Users\HP\Desktop\Projects Folder\world_of_tools"
$htmlFiles = Get-ChildItem -Path $rootPath -Filter "*.html" -Recurse

foreach ($file in $htmlFiles) {
    if ($file.FullName -like "*node_modules*" -or $file.FullName -like "*\.git*") { continue }
    
    $path = $file.FullName
    $content = Get-Content $path -Raw
    
    # --- 1. Colors & Basic Theme ---
    $content = $content -replace '#4f46e5', '#e67e22' # Primary Blue -> Retro Orange
    $content = $content -replace 'rgba\(79, 70, 229,', 'rgba(230, 126, 34,' # Primary Alpha
    $content = $content -replace '#7c3aed', '#d35400' # Purple -> Dark Orange
    $content = $content -replace '#818cf8', '#e67e22' # Light Blue -> Orange
    $content = $content -replace '#06b6d4', '#d35400' # Cyan -> Dark Orange
    $content = $content -replace '#1A56DB', '#e67e22' # Royal Blue -> Orange
    $content = $content -replace '#1e293b', '#2c2520' # Slate -> Coffee
    $content = $content -replace '#0f172a', '#2c2520' # Dark Blue -> Coffee
    
    # --- 2. Radius Reduction ---
    $content = $content -replace 'border-radius:20px', 'border-radius:4px'
    $content = $content -replace 'border-radius:16px', 'border-radius:4px'
    $content = $content -replace 'border-radius:12px', 'border-radius:4px'
    $content = $content -replace 'border-radius:24px', 'border-radius:4px'
    $content = $content -replace 'border-radius:10px', 'border-radius:4px'
    $content = $content -replace 'border-radius:99px', 'border-radius:4px'
    
    # --- 3. Remove Glassmorphism & Modern Shadows ---
    $content = $content -replace 'backdrop-filter: blur\(.*\);', '/* blur removed */'
    $content = $content -replace '-webkit-backdrop-filter: blur\(.*\);', '/* blur removed */'
    $content = $content -replace 'box-shadow: 0 10px 30px -10px rgba\(0,0,0,0.05\);', 'box-shadow: 4px 4px 0px #3d342d;'
    $content = $content -replace 'box-shadow: 0 4px 6px rgba\(79, 70, 229, 0.2\);', 'box-shadow: 3px 3px 0px #3d342d;'
    $content = $content -replace 'box-shadow: 0 8px 20px -6px rgba\(79, 70, 229, 0.4\);', 'box-shadow: 4px 4px 0px #3d342d;'
    $content = $content -replace 'box-shadow:0 1px 4px rgba\(0,0,0,.1\)', 'box-shadow: 2px 2px 0px #3d342d'
    
    # --- 4. Borders ---
    $content = $content -replace 'border: 1px solid var\(--border-color\)', 'border: 2px solid var(--border-color)'
    $content = $content -replace 'border: 2px dashed var\(--border-color\)', 'border: 3px solid var(--border-color)'
    
    # --- 5. Transitions for "Alive" feel (0.5s as requested) ---
    $content = $content -replace 'transition: all 0.2s', 'transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275)'
    $content = $content -replace 'transition: all 0.3s', 'transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275)'
    $content = $content -replace 'transition: all 0.4s', 'transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275)'
    
    # --- 6. Hover effects (Scale and Offset Shadow) ---
    $content = $content -replace 'transform: translateY\(-2px\)', 'transform: scale(1.05) translate(-2px, -2px)'
    
    Set-Content -Path $path -Value $content -Encoding UTF8
}
