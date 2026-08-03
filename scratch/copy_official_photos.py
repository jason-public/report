import os
from PIL import Image

src_dir = '사진자료(교통국 중점사업 보고회)'
dst_dir = 'assets/images'
os.makedirs(dst_dir, exist_ok=True)

photo_mapping = {
    'proj-1': '총괄1. 별내선(8호선) 연장(별내~별내별가람).png',
    'proj-2': '총괄2. 생애주기별 대중교통비 지원.png',
    'proj-3': '총괄3. 대광위 광역버스 준공영제.JPG',
    'proj-4': '총괄4. 시내버스 공공관리제.jpg',
    'proj-5': '총괄5. 공영주차장 조성사업.jpeg',
    'proj-6': '총괄6. 미금로 확장공사.png',
    'proj-7': '총괄7. 시도5호선(중말교차로~철마교차로).png',
    'proj-8': '총괄8. 농어촌도로102호선(녹촌~창현).png',
    'proj-9': '총괄9. 진접읍 금곡리 바람골길.png',
    'proj-10': '총괄10. 화도읍 가곡초 통학로 확장공사.png',
    'proj-11': '총괄11. 오남 양지리(대대울) 진입도로 개설공사.png',
    'proj-12': '총괄12. 묵현20리 연결도로 개설공사.png',
    'proj-13': '총괄13. 진접 금곡리 도시계획도로 개설공사.png',

    'park-1': '(주차) 2-5. 1. 퇴계원중학교 운동장 지하 공영주차장 건립(현장사진).jpeg',
    'park-2': '(주차) 2-5. 2. 다산진건지구(주9) 공영주차장 건립(현장사진).jpeg',
    'park-3': '(주차) 2-5. 3. 다산역 환승주차장 건립(현장사진).jpg',
    'park-4': '(주차) 2-5. 4. 와부읍 팔당2리 공영주차장 조성(위치도).png',
    'park-5': '(주차) 2-5. 5. 평내동 물놀이장 지하 공영주차장 건립(조감도).jpg',
    'park-6': '(주차) 2-5. 6. 다산지금지구(주2) 공영주차장 건립(조감도).jpg',
    'park-7': '(주차) 2-5. 7. 와부 빛터널 임시 공영주차장 조성(현장사진).jpg',
}

for key, fname in photo_mapping.items():
    full_src = os.path.join(src_dir, fname)
    full_dst = os.path.join(dst_dir, f"{key}.png")
    
    if not os.path.exists(full_src):
        print(f"MISSING FILE: {full_src}")
        continue
        
    with Image.open(full_src) as img:
        img = img.convert('RGB')
        img.save(full_dst, 'PNG', quality=95)
        print(f"Copied & Converted: {key}.png <- {fname} (Size: {img.size})")

print("\nAll 20 official photos mapped successfully!")
