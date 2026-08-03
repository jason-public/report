import re

content = open('embed_data_in_app.py', encoding='utf-8').read()
lines = content.split('\n')

for i, line in enumerate(lines):
    if 'body = """' in line:
        print(f"body starts: line {i+1}")
    if line.strip() == '"""' or ('"""' in line and i > 10):
        print(f"Triple-quote at line {i+1}: {repr(line[:60])}")
