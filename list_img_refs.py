import zipfile
import xml.etree.ElementTree as ET
import re
import json

hwpx_path = '(8.3.) 중점사업 추진사업 점검 보고회 자료(교통국 수정)_최최종.hwpx'
with zipfile.ZipFile(hwpx_path, 'r') as z:
    manifest_xml = z.read('Contents/content.hpf').decode('utf-8', errors='ignore')
    section_xml = z.read('Contents/section0.xml').decode('utf-8', errors='ignore')

id_to_href = {}
for line in manifest_xml.splitlines():
    if 'opf:item' in line and 'href=' in line:
        id_m = re.search(r'id="([^"]+)"', line)
        href_m = re.search(r'href="([^"]+)"', line)
        if id_m and href_m:
            id_to_href[id_m.group(1)] = href_m.group(1)

root = ET.fromstring(section_xml.encode('utf-8'))
img_refs = []

for elem in root.iter():
    if elem.tag.endswith('img') and 'binaryItemIDRef' in elem.attrib:
        ref = elem.attrib['binaryItemIDRef']
        href = id_to_href.get(ref, '')
        img_refs.append((ref, href))

print(f"Total image refs: {len(img_refs)}")
for idx, (ref, href) in enumerate(img_refs):
    print(f"#{idx+1}: {ref} -> {href}")
