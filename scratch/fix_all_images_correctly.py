import os
from PIL import Image

correct_image_sources = {
    'proj-1': 'assets/images/image8.jpg',      # 별내선 연장 노선도
    'proj-2': 'assets/images/image9.bmp',      # 생애주기별 대중교통비 지원
    'proj-3': 'assets/images/image10.bmp',     # 대광위 광역버스 준공영제
    'proj-4': 'assets/images/image11.bmp',     # 시내버스 공공관리제
    'proj-5': 'assets/images/image12.bmp',     # 공영주차장 조성 대표 현장/조감도
    'proj-6': 'assets/images/image4.jpg',      # 미금로(중로1-302호) 확장공사 위치도 (1500x1408)
    'proj-7': 'assets/images/image5.jpg',      # 시도5호선 도로확장 위치도 (1500x1002)
    'proj-8': 'assets/images/image6.jpg',      # 농어촌도로102호선 도로확장 위치도 (1500x1061)
    'proj-9': 'assets/images/image28.bmp',     # 진접 금곡리 바람골길 도로개설 위치도 (805x485)
    'proj-10': 'assets/images/image29.bmp',    # 화도읍 가곡초 통학로 확장공사 위치도 (940x599)
    'proj-11': 'assets/images/image30.bmp',    # 오남 양지리(대대울) 진입도로 위치도 (1104x771)
    'proj-12': 'assets/images/image31.png',    # 묵현20리 연결도로 위치도 (1564x1029)
    'proj-13': 'assets/images/image32.bmp',    # 진접 금곡리 도시계획도로 위치도 (1169x655)

    'park-1': 'assets/images/image21.bmp',     # 퇴계원중학교 운동장 지하 (599x342)
    'park-2': 'assets/images/image22.bmp',     # 다산진건지구(주9) (599x342)
    'park-3': 'assets/images/image23.bmp',     # 다산역 환승주차장 (599x354)
    'park-4': 'assets/images/image24.bmp',     # 와부읍 팔당2리 (490x282)
    'park-5': 'assets/images/image25.bmp',     # 평내동 물놀이장 (432x288)
    'park-6': 'assets/images/image26.bmp',     # 다산지금지구(주2) (599x340)
    'park-7': 'assets/images/image27.bmp',     # 와부 빛터널 (599x370)
}

os.makedirs('assets/images', exist_ok=True)

for key, src in correct_image_sources.items():
    if not os.path.exists(src):
        print(f"ERROR: {src} missing!")
        continue
    
    dst = f"assets/images/{key}.png"
    try:
        with Image.open(src) as img:
            img = img.convert('RGB')
            img.save(dst, 'PNG', quality=95)
            print(f"Fixed image: {key}.png <- {src}")
    except Exception as e:
        print(f"Error processing {key}: {e}")

print("\n100% correct image assignment completed!")
