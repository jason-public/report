import os
from PIL import Image

mapping = {
    'proj-1': 'assets/images/image8.jpg',
    'proj-2': 'assets/images/image9.bmp',
    'proj-3': 'assets/images/image10.bmp',
    'proj-4': 'assets/images/image11.bmp',
    'proj-5': 'assets/images/image12.bmp',
    'proj-6': 'assets/images/image13.png',
    'proj-7': 'assets/images/image14.png',
    'proj-8': 'assets/images/image15.png',
    'proj-9': 'assets/images/image28.bmp',
    'proj-10': 'assets/images/image29.bmp',
    'proj-11': 'assets/images/image30.bmp',
    'proj-12': 'assets/images/image31.png',
    'proj-13': 'assets/images/image32.bmp',

    'park-1': 'assets/images/image21.bmp',
    'park-2': 'assets/images/image22.bmp',
    'park-3': 'assets/images/image23.bmp',
    'park-4': 'assets/images/image24.bmp',
    'park-5': 'assets/images/image25.bmp',
    'park-6': 'assets/images/image26.bmp',
    'park-7': 'assets/images/image27.bmp',
}

for key, src_path in mapping.items():
    if not os.path.exists(src_path):
        print(f"ERROR: Source file {src_path} missing!")
        continue
    
    ext = os.path.splitext(src_path)[1].lower()
    target_path = f"assets/images/{key}.png"
    
    try:
        with Image.open(src_path) as img:
            # Convert RGBA/P to RGB if saving as JPEG, or save directly as PNG
            img = img.convert('RGB')
            img.save(target_path, 'PNG', quality=95)
            print(f"Successfully processed: {key} -> {target_path} (from {src_path})")
    except Exception as e:
        print(f"Failed to process {key} from {src_path}: {e}")

print("\nDone converting and saving project images!")
