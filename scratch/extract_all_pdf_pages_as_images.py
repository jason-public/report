import os
import pypdfium2 as pdfium

pdf_path = '(8.3.) 중점사업 추진사업 점검 보고회 자료(교통국 수정)_최최종.pdf'
out_dir = 'assets/pdf_pages'
os.makedirs(out_dir, exist_ok=True)

doc = pdfium.PdfDocument(pdf_path)
print(f"Total PDF pages: {len(doc)}")

for i in range(len(doc)):
    page_num = i + 1
    page = doc[i]
    # Render at 3x scale (~2523x1785 resolution) for ultra high clarity
    img = page.render(scale=3.0).to_pil()
    file_path = os.path.join(out_dir, f"page_{page_num}.png")
    img.save(file_path, "PNG", quality=95)
    print(f"Extracted Page {page_num}: {file_path} (size: {img.size})")

print("\nSuccessfully extracted all PDF pages as PNG images!")
