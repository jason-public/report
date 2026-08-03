import zipfile
import xml.etree.ElementTree as ET
import os
import json
import re

hwpx_path = '(8.3.) 중점사업 추진사업 점검 보고회 자료(교통국 수정)_최최종.hwpx'
os.makedirs('assets/images', exist_ok=True)

with zipfile.ZipFile(hwpx_path, 'r') as z:
    manifest_xml = z.read('Contents/content.hpf').decode('utf-8', errors='ignore')
    section_xml = z.read('Contents/section0.xml').decode('utf-8', errors='ignore')

    for item in z.namelist():
        if 'BinData/' in item:
            filename = os.path.basename(item)
            if filename:
                with open(os.path.join('assets/images', filename), 'wb') as f:
                    f.write(z.read(item))

# Parse manifest: id -> href
id_to_href = {}
for line in manifest_xml.splitlines():
    if 'opf:item' in line and 'href=' in line:
        id_m = re.search(r'id="([^"]+)"', line)
        href_m = re.search(r'href="([^"]+)"', line)
        if id_m and href_m:
            id_to_href[id_m.group(1)] = href_m.group(1)

root = ET.fromstring(section_xml.encode('utf-8'))

# Map pictures
image_map = []
for elem in root.iter():
    tag = elem.tag.split('}')[-1]
    if tag == 'pic':
        bin_ref = elem.attrib.get('binRef', '')
        href = id_to_href.get(bin_ref, '')
        filename = os.path.basename(href)
        image_map.append({
            'binRef': bin_ref,
            'filename': filename,
            'rel_path': f'assets/images/{filename}'
        })

print(f"Extracted {len(image_map)} image tags, saved to assets/images/")
with open('image_map.json', 'w', encoding='utf-8') as f:
    json.dump(image_map, f, ensure_ascii=False, indent=2)
