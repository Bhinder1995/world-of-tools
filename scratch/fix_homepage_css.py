with open('index.html', encoding='utf-8') as f:
    content = f.read()

# The old CSS starts after the new </style> block at ~line 672
# and ends before the <meta name="theme-color"> line
# Let's find and remove the orphaned CSS block

old_css_start_marker = '</style>\r\n.hero-badge {\r\n  display: inline-flex;'
# Try different line endings
if old_css_start_marker not in content:
    old_css_start_marker = '</style>\n.hero-badge {\n  display: inline-flex;'

idx = content.find(old_css_start_marker)
print('Marker found at:', idx)

if idx >= 0:
    # The orphaned CSS block ends at a second </style> tag or before a <meta> tag
    # Search for the next <meta name="theme-color" after this position
    meta_pos = content.find('<meta name="theme-color"', idx)
    print('meta found at:', meta_pos)
    
    # The old block runs from idx+8 (after first </style>) to just before meta_pos
    # But there may be a closing </style> before it too
    # Find second </style> after idx+8
    second_close = content.find('</style>', idx + 8)
    print('Second </style> at:', second_close)
    
    # Remove from after the first </style> up to the meta tag
    end_of_deletion = meta_pos if meta_pos >= 0 else (second_close + len('</style>'))
    start_of_deletion = idx + len('</style>')
    
    print(f'Will remove chars [{start_of_deletion}:{end_of_deletion}]')
    print('Preview of what gets removed (first 100 chars):', repr(content[start_of_deletion:start_of_deletion+100]))
    
    new_content = content[:start_of_deletion] + '\n' + content[end_of_deletion:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Done! File saved.')
else:
    print('ERROR: marker not found in file')
    # Try to find the leak another way
    lines = content.split('\n')
    for i, line in enumerate(lines[650:700], start=650):
        print(i, repr(line[:80]))
