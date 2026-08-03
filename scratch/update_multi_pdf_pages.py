import re

file_path = 'build_final_dataset.py'

# Page range mapping: proj_id -> (pdfPage, pdfPages, pdfPageLabel)
project_page_map = {
    'proj-1': (6, [6], "P.6"),
    'proj-2': (7, [7], "P.7"),
    'proj-3': (8, [8], "P.8"),
    'proj-4': (9, [9, 10], "P.9~10"),
    'proj-5': (11, [11, 12, 13, 14], "P.11~14"),
    'proj-6': (15, [15], "P.15"),
    'proj-7': (17, [17], "P.17"),
    'proj-8': (19, [19], "P.19"),
    'proj-9': (21, [21], "P.21"),
    'proj-10': (23, [23], "P.23"),
    'proj-11': (25, [25], "P.25"),
    'proj-12': (27, [27], "P.27"),
    'proj-13': (29, [29], "P.29"),
}

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

for proj_id, (pdfPage, pdfPages, pdfPageLabel) in project_page_map.items():
    # Replace `"pdfPage": X,` with `"pdfPage": X,\n        "pdfPages": pdfPages,\n        "pdfPageLabel": "label",`
    pattern = f'("id": "{proj_id}",\n\\s*"pdfPage": \\d+,)'
    replacement = f'\\1\n        "pdfPages": {pdfPages},\n        "pdfPageLabel": "{pdfPageLabel}",'
    content = re.sub(pattern, replacement, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated build_final_dataset.py with pdfPages and pdfPageLabel!")
