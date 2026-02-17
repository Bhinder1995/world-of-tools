import openpyxl
import json

# Load the Excel file
wb = openpyxl.load_workbook('Keyword_Tracker_14_Tools.xlsx')
ws = wb.active

# Dictionary to store keywords for each tool
keywords_data = {}

# Read the Excel file
# Assuming first row is headers and first column is tool names
for row in ws.iter_rows(min_row=2, values_only=True):
    if row[0]:  # If tool name exists
        tool_name = row[0]
        keywords = [cell for cell in row[1:] if cell]  # Get all non-empty cells
        keywords_data[tool_name] = keywords

# Print the data in a readable format
print(json.dumps(keywords_data, indent=2))

# Save to a JSON file for easy access
with open('keywords_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(keywords_data, f, indent=2, ensure_ascii=False)

print("\n\nKeywords have been saved to keywords_extracted.json")
