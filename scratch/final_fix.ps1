$htmlFiles = Get-ChildItem -Path "c:\Users\HP\Desktop\Projects Folder\world_of_tools" -Filter "*.html" -Recurse
foreach ($file in $htmlFiles) {
    if ($file.FullName -like "*node_modules*" -or $file.FullName -like "*\.git*") { continue }
    $content = Get-Content $file.FullName -Raw
    # Fix the doubled transition
    $content = $content -replace 'transition: all 0.5s cubic-bezier\(0.175, 0.885, 0.32, 1.275\) cubic-bezier\(0.4, 0, 0.2, 1\);', 'transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);'
    # Fix the encoding to UTF8 without BOM correctly
    [System.IO.File]::WriteAllText($file.FullName, $content, (New-Object System.Text.UTF8Encoding($false)))
}
