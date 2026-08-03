import os
from PIL import Image

pdf_dir = 'scratch/pdf_images'
files = sorted(os.listdir(pdf_dir))

for f in files:
    path = os.path.join(pdf_dir, f)
    with Image.open(path) as img:
        print(f"{f}: size={img.size}, mode={img.mode}")
