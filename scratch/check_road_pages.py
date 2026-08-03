import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = "(8.3.) 중점사업 추진사업 점검 보고회 자료(교통국 수정)_최최종.pdf"
doc = fitz.open(pdf_path)

print(f"Total pages: {len(doc)}")

for page_num in range(15, 31):
    text = doc[page_num - 1].get_text()
    first_line = text.split('\n')[0] if text else ''
    lines = [line.strip() for line in text.split('\n') if line.strip()][:4]
    print(f"PDF Page {page_num}: {lines}")
