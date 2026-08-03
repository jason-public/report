import re

file_path = 'build_final_dataset.py'

page_mappings = {
    'proj-1': 6,
    'proj-2': 7,
    'proj-3': 8,
    'proj-4': 9,
    'proj-5': 11,
    'proj-6': 15,
    'proj-7': 17,
    'proj-8': 19,
    'proj-9': 21,
    'proj-10': 23,
    'proj-11': 25,
    'proj-12': 27,
    'proj-13': 29,
}

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

for proj_id, pdf_page in page_mappings.items():
    # Replace "id": "proj-X", with "id": "proj-X",\n        "pdfPage": X,
    pattern = f'("id": "{proj_id}",)'
    replacement = f'\\1\n        "pdfPage": {pdf_page},'
    content = re.sub(pattern, replacement, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Added pdfPage to all 13 projects in build_final_dataset.py!")
