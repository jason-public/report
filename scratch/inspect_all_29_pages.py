import pypdf
import sys

sys.stdout.reconfigure(encoding='utf-8')

reader = pypdf.PdfReader('(8.3.) 중점사업 추진사업 점검 보고회 자료(교통국 수정)_최최종.pdf')

for idx, page in enumerate(reader.pages):
    text = page.extract_text()
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    first_few = " | ".join(lines[:4])
    print(f"PDF Page {idx + 1}: {first_few}")
