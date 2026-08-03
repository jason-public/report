import pypdfium2 as pdfium

doc = pdfium.PdfDocument('(8.3.) 중점사업 추진사업 점검 보고회 자료(교통국 수정)_최최종.pdf')
print("--- PAGE 9 ---")
print(doc[8].get_textpage().get_text_range())
print("--- PAGE 10 ---")
print(doc[9].get_textpage().get_text_range())
