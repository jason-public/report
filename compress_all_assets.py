import os
from PIL import Image

TARGET_FOLDERS = [
    r"g:\34_report_online\report-main",
    r"g:\31_중점사항 보고회 추진 자료"
]

def strict_compress_image(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext not in ['.png', '.jpg', '.jpeg']:
        return

    sz = os.path.getsize(filepath)
    if sz <= 600 * 1024:
        return

    try:
        with Image.open(filepath) as img:
            w, h = img.size
            max_dim = 1600
            if w > max_dim or h > max_dim:
                if w >= h:
                    new_w = max_dim
                    new_h = int(h * (max_dim / w))
                else:
                    new_h = max_dim
                    new_w = int(w * (max_dim / h))
                img = img.resize((new_w, new_h), Image.Resampling.LANCZOS)

            rgb_img = img.convert('RGB')
            # Save as JPEG with quality 80
            rgb_img.save(filepath, 'JPEG', quality=80, optimize=True)
            sz_after = os.path.getsize(filepath)
            print(f"Strict Compressed: {os.path.basename(filepath)}: {sz/1024:.0f}KB -> {sz_after/1024:.0f}KB")
    except Exception as e:
        print(f"Failed {filepath}: {e}")

if __name__ == '__main__':
    for folder in TARGET_FOLDERS:
        if os.path.exists(folder):
            for root, dirs, files in os.walk(folder):
                for f in files:
                    fp = os.path.join(root, f)
                    strict_compress_image(fp)
    print("Strict compression complete!")
