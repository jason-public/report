import pypdfium2 as pdfium

pdf_path = '(8.3.) 중점사업 추진사업 점검 보고회 자료(교통국 수정)_최최종.pdf'
doc = pdfium.PdfDocument(pdf_path)

for i in range(len(doc)):
    page_num = i + 1
    page = doc[i]
    textpage = page.get_textpage()
    text = textpage.get_text_range()
    first_line = text.split('\n')[0] if text else ''
    print(f"Page {page_num}: {first_line[:80]} | Total text len: {len(text)}")
