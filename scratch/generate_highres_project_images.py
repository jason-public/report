import os
import pypdfium2 as pdfium
from PIL import Image

pdf_path = '(8.3.) 중점사업 추진사업 점검 보고회 자료(교통국 수정)_최최종.hwpx'
pdf_doc = pdfium.PdfDocument('(8.3.) 중점사업 추진사업 점검 보고회 자료(교통국 수정)_최최종.pdf')

# Map projects to PDF pages (1-indexed)
# Page 6: 별내선(8호선) 연장 (proj-1)
# Page 7: 생애주기별 대중교통비 지원 (proj-2)
# Page 8: 대광위 광역버스 준공영제 (proj-3)
# Page 9: 시내버스 공공관리제 (proj-4)
# Page 11: 공영주차장 조성사업 7개소 (proj-5)
# Page 15: 미금로(중로1-302호) 확장공사 (proj-6)
# Page 17: 시도5호선 도로확장 (proj-7)
# Page 19: 농어촌도로102호선 도로확장 (proj-8)
# Page 21: 진접 금곡리 바람골길 (proj-9)
# Page 23: 화도읍 가곡초 통학로 (proj-10)
# Page 25: 오남 양지리 대대울 (proj-11)
# Page 27: 묵현20리 연결도로 (proj-12)
# Page 29: 진접 금곡리 도시계획도로 (proj-13)

project_pages = {
    'proj-1': 6,
    'proj-2': 7,
    'proj-3': 8,
    'proj-4': 9,
    'proj-5': 11,
    'proj-6': 15,
    'proj-7': 17,
    'proj-8': 19,
    'proj-9': 21,
    'proj-10': 23,
    'proj-11': 25,
    'proj-12': 27,
    'proj-13': 29,
}

os.makedirs('assets/images', exist_ok=True)

# 1. Generate high-res rendered images for all projects from PDF pages
for proj_id, p_num in project_pages.items():
    page = pdf_doc[p_num - 1]
    # Render at 3x scale (approx 2500x1780)
    pil_image = page.render(scale=3.0).to_pil()
    
    # Save as project canonical image
    target_path = f"assets/images/{proj_id}.png"
    pil_image.save(target_path, "PNG", quality=95)
    print(f"Generated high-res PDF page render: {proj_id} <- Page {p_num} (size: {pil_image.size})")

# 2. Extract parking subproject images from PDF Page 12 & 13 extracted images
parking_images = {
    'park-1': 'scratch/pdf_images/page_12_img_1_Im25.jpg',
    'park-2': 'scratch/pdf_images/page_12_img_2_Im26.jpg',
    'park-3': 'scratch/pdf_images/page_12_img_3_Im27.jpg',
    'park-4': 'scratch/pdf_images/page_12_img_4_Im28.jpg',
    'park-5': 'scratch/pdf_images/page_13_img_1_Im29.jpg',
    'park-6': 'scratch/pdf_images/page_13_img_2_Im30.jpg',
    'park-7': 'scratch/pdf_images/page_13_img_3_Im31.jpg',
}

for park_id, src_path in parking_images.items():
    if os.path.exists(src_path):
        with Image.open(src_path) as img:
            img = img.convert('RGB')
            dst_path = f"assets/images/{park_id}.png"
            img.save(dst_path, "PNG", quality=95)
            print(f"Generated parking image: {park_id} <- {src_path} (size: {img.size})")

print("\nDone generating all high-res project and parking images!")
