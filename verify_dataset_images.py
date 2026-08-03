import json, os
from PIL import Image

with open('assets/projects_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for p in data:
    pid = p["id"]
    img_path = p.get("image")
    if img_path:
        exists = os.path.exists(img_path)
        sz = os.path.getsize(img_path) if exists else 0
        dim = '-'
        valid = False
        if exists:
            try:
                with Image.open(img_path) as im:
                    valid = True
                    dim = im.size
            except:
                valid = False
        print(f"{pid}: {img_path} -> Exists: {exists}, Valid: {valid}, Size: {sz/1024:.1f}KB, Dim: {dim}")

    for sp in p.get("subProjects", []):
        spid = sp["id"]
        sp_img = sp.get("image")
        if sp_img:
            exists = os.path.exists(sp_img)
            sz = os.path.getsize(sp_img) if exists else 0
            dim = '-'
            valid = False
            if exists:
                try:
                    with Image.open(sp_img) as im:
                        valid = True
                        dim = im.size
                except:
                    valid = False
            print(f"  sub {spid}: {sp_img} -> Exists: {exists}, Valid: {valid}, Size: {sz/1024:.1f}KB, Dim: {dim}")
