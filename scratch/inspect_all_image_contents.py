import os
from PIL import Image

image_dir = 'assets/images'
files = sorted([f for f in os.listdir(image_dir) if f.startswith('image')])

for f in files:
    path = os.path.join(image_dir, f)
    try:
        with Image.open(path) as img:
            print(f"{f}: format={img.format}, size={img.size}, mode={img.mode}")
    except Exception as e:
        print(f"{f}: Error {e}")
