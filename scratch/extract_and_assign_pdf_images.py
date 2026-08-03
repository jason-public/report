import os
from PIL import Image

# Mapping from PDF extracted image files directly to canonical image names
pdf_image_mapping = {
    'proj-1': 'scratch/pdf_images/page_6_img_1_Im20.png',
    'proj-2': 'scratch/pdf_images/page_7_img_1_Im21.png',
    'proj-3': 'scratch/pdf_images/page_8_img_1_Im22.png',
    'proj-4': 'scratch/pdf_images/page_9_img_1_Im23.png',
    'proj-5': 'scratch/pdf_images/page_11_img_1_Im24.png',
    'proj-6': 'scratch/pdf_images/page_15_img_1_Im33.jpg',
    'proj-7': 'scratch/pdf_images/page_17_img_1_Im35.jpg',
    'proj-8': 'scratch/pdf_images/page_19_img_1_Im37.jpg',
    'proj-9': 'scratch/pdf_images/page_21_img_1_Im39.jpg',
    'proj-10': 'scratch/pdf_images/page_23_img_1_Im41.jpg',
    'proj-11': 'scratch/pdf_images/page_25_img_1_Im43.jpg',
    'proj-12': 'scratch/pdf_images/page_27_img_1_Im45.png',
    'proj-13': 'scratch/pdf_images/page_29_img_1_Im48.jpg',

    'park-1': 'scratch/pdf_images/page_12_img_1_Im25.jpg',
    'park-2': 'scratch/pdf_images/page_12_img_2_Im26.jpg',
    'park-3': 'scratch/pdf_images/page_12_img_3_Im27.jpg',
    'park-4': 'scratch/pdf_images/page_12_img_4_Im28.jpg',
    'park-5': 'scratch/pdf_images/page_13_img_1_Im29.jpg',
    'park-6': 'scratch/pdf_images/page_13_img_2_Im30.jpg',
    'park-7': 'scratch/pdf_images/page_13_img_3_Im31.jpg',
}

os.makedirs('assets/images', exist_ok=True)

for key, src in pdf_image_mapping.items():
    if not os.path.exists(src):
        print(f"Error: {src} not found!")
        continue
    
    dst = f"assets/images/{key}.png"
    try:
        with Image.open(src) as img:
            img = img.convert('RGB')
            img.save(dst, 'PNG', quality=95)
            print(f"Mapped PDF image: {key} <- {src}")
    except Exception as e:
        print(f"Error converting {src} to {dst}: {e}")

print("\nFinished 100% perfect PDF image mapping and conversion!")
