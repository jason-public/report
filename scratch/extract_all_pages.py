import pypdfium2 as pdfium
import os

pdf_path = "(8.3.) 중점사업 추진사업 점검 보고회 자료(교통국 수정)_최최종.pdf"
output_dir = "assets/pdf_pages"
os.makedirs(output_dir, exist_ok=True)

pdf = pdfium.PdfDocument(pdf_path)
print(f"Total PDF pages: {len(pdf)}")

for i, page in enumerate(pdf):
    page_num = i + 1
    image = page.render(scale=3).to_pil()
    file_path = os.path.join(output_dir, f"page_{page_num}.png")
    image.save(file_path)
    print(f"Saved {file_path}")

print("Extraction complete!")
