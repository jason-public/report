import zipfile
import xml.etree.ElementTree as ET
import os
import re
import json

hwpx_path = '(8.3.) 중점사업 추진사업 점검 보고회 자료(교통국 수정)_최최종.hwpx'

with zipfile.ZipFile(hwpx_path, 'r') as z:
    manifest_xml = z.read('Contents/content.hpf').decode('utf-8', errors='ignore')
    section_xml = z.read('Contents/section0.xml').decode('utf-8', errors='ignore')
    
    # Extract all binary files
    os.makedirs('assets/images', exist_ok=True)
    for name in z.namelist():
        if name.startswith('BinData/'):
            basename = os.path.basename(name)
            with open(os.path.join('assets/images', basename), 'wb') as out_f:
                out_f.write(z.read(name))
            print(f"Extracted: {name} -> assets/images/{basename}")

# Manifest mapping
id_to_href = {}
for line in manifest_xml.splitlines():
    if 'opf:item' in line and 'href=' in line:
        id_m = re.search(r'id="([^"]+)"', line)
        href_m = re.search(r'href="([^"]+)"', line)
        if id_m and href_m:
            id_to_href[id_m.group(1)] = href_m.group(1)

print("\nManifest ID to HREF:")
for k, v in id_to_href.items():
    print(f"  {k} -> {v}")
