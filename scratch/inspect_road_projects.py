import json

with open('assets/projects_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

projects = data['projects'] if isinstance(data, dict) and 'projects' in data else data

for p in projects:
    print(f"ID: {p['id']} | No: {p['no']} | Title: {p['title']} | Page: {p.get('pdfPage')} | Pages: {p.get('pdfPages')} | Label: {p.get('pdfPageLabel')}")
