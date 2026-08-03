import zipfile
import xml.etree.ElementTree as ET
import os
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

log_lines = []
for elem in root.iter():
    tag = elem.tag.split('}')[-1]
    if tag == 'p':
        text = ''.join(elem.itertext()).strip()
        imgs = [e.attrib.get('binaryItemIDRef') for e in elem.iter() if e.tag.endswith('img') and 'binaryItemIDRef' in e.attrib]
        if imgs or any(kw in text for kw in ['2-①', '2-②', '2-③', '2-④', '2-⑤', '2-⑥', '2-⑦', '3-①', '3-②', '3-③', '3-④', '3-⑤', '3-⑥', '별내선', '대중교통비', '광역버스', '공공관리제', '공영주차장', '미금로', '시도5호선', '농어촌도로', '바람골길', '가곡초', '대대울', '묵현20리', '도시계획도로', '퇴계원중', '다산진건', '다산역', '팔당2리', '물놀이장', '다산지금', '빛터널']):
            img_paths = [id_to_href.get(r, r) for r in imgs]
            log_lines.append(f"TEXT: {text[:70]} | IMGS: {img_paths}")

with open('scratch/image_match_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log_lines))

print(f"Logged {len(log_lines)} lines to scratch/image_match_log.txt")
