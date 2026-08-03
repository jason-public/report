import os
from PIL import Image

pdf_dir = 'scratch/pdf_images'
os.makedirs('scratch/preview_all', exist_ok=True)

# Save cropped or labeled previews of all extracted images from pdf and assets/images
asset_files = [f for f in os.listdir('assets/images') if f.endswith(('.jpg', '.png', '.bmp'))]

print("--- Asset files ---")
for f in asset_files:
    path = os.path.join('assets/images', f)
    with Image.open(path) as img:
        print(f"{f}: size={img.size}, mode={img.mode}")
