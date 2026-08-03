import os
import json
import zipfile
import xml.etree.ElementTree as ET
from PIL import Image
import re

# Convert all .bmp in assets/images to .png / .jpg
images_dir = 'assets/images'
for filename in os.listdir(images_dir):
    if filename.lower().endswith('.bmp'):
        bmp_path = os.path.join(images_dir, filename)
        jpg_name = filename.rsplit('.', 1)[0] + '.jpg'
        jpg_path = os.path.join(images_dir, jpg_name)
        try:
            with Image.open(bmp_path) as img:
                rgb_img = img.convert('RGB')
                rgb_img.save(jpg_path, 'JPEG', quality=90)
            print(f"Converted {filename} -> {jpg_name}")
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")

# Now let's inspect section0.xml to verify image ordering for each project
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
pics_found = []

for elem in root.iter():
    tag = elem.tag.split('}')[-1]
    if tag == 'pic':
        bin_ref = elem.attrib.get('binRef', '')
        href = id_to_href.get(bin_ref, '')
        fname = os.path.basename(href)
        if fname.lower().endswith('.bmp'):
            fname = fname.rsplit('.', 1)[0] + '.jpg'
        pics_found.append((bin_ref, fname, elem.attrib.get('name', '')))

print(f"\nTotal picture elements in XML: {len(pics_found)}")
for i, p in enumerate(pics_found):
    print(f"Pic {i+1}: binRef={p[0]}, fname={p[1]}, name={p[2]}")
