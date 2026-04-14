$cssPath = "c:\Users\HP\Desktop\Projects Folder\world_of_tools\css\style.css"
$content = Get-Content $cssPath -Raw

# Fix the `n issue
$content = $content -replace '`n', "`n"

# Fix the malformed backdrop-filter comments
$content = $content -replace '(?s)/\* backdrop-filter removed for retro \*/.*?-webkit-/\* backdrop-filter removed for retro \*/', ''

# Fix hero-title text fill
$content = $content -replace '-webkit-text-fill-color: transparent;', '-webkit-text-fill-color: var(--text-color);'
$content = $content -replace 'background: linear-gradient\(135deg, var\(--primary-color\), #818cf8, #06b6d4\);', 'background: none;'

Set-Content -Path $cssPath -Value $content -Encoding UTF8

# Fix Encoding for HTML files
$htmlFiles = Get-ChildItem -Path "c:\Users\HP\Desktop\Projects Folder\world_of_tools" -Filter "*.html" -Recurse
foreach ($file in $htmlFiles) {
    $c = Get-Content $file.FullName -Raw
    Set-Content -Path $file.FullName -Value $c -Encoding UTF8
}
