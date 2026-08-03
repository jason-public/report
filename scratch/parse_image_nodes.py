import zipfile
import xml.etree.ElementTree as ET

hwpx_path = '(8.3.) 중점사업 추진사업 점검 보고회 자료(교통국 수정)_최최종.hwpx'

with zipfile.ZipFile(hwpx_path, 'r') as z:
    section_xml = z.read('Contents/section0.xml').decode('utf-8', errors='ignore')

root = ET.fromstring(section_xml.encode('utf-8'))

current_heading = "HEADER"

for elem in root.iter():
    tag = elem.tag.split('}')[-1]
    if tag == 'p':
        text = ''.join(elem.itertext()).strip()
        if any(no in text for no in ['2-①', '2-②', '2-③', '2-④', '2-⑤', '2-⑥', '2-⑦', '3-①', '3-②', '3-③', '3-④', '3-⑤', '3-⑥', '별내선', '생애주기', '광역버스', '공공관리제', '공영주차장', '미금로', '시도5호선', '농어촌도로', '바람골길', '가곡초', '대대울', '묵현20리', '도시계획도로', '퇴계원중', '다산진건', '다산역', '팔당2리', '물놀이장', '다산지금', '빛터널']):
            print(f"\n--- HEADING/TEXT: {text[:80]} ---")
            current_heading = text[:40]
        
        imgs = [e.attrib.get('binaryItemIDRef') for e in elem.iter() if e.tag.endswith('img') and 'binaryItemIDRef' in e.attrib]
        if imgs:
            print(f"   [IMG IN {current_heading}]: {imgs}")
