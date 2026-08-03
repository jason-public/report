import zipfile
import xml.etree.ElementTree as ET
import re

hwpx_path = '(8.3.) 중점사업 추진사업 점검 보고회 자료(교통국 수정)_최최종.hwpx'

with zipfile.ZipFile(hwpx_path, 'r') as z:
    manifest_xml = z.read('Contents/content.hpf').decode('utf-8', errors='ignore')
    section_xml = z.read('Contents/section0.xml').decode('utf-8', errors='ignore')

# Extract id to href and original filename if present
lines = manifest_xml.splitlines()
for line in lines:
    if 'opf:item' in line:
        print(line)
