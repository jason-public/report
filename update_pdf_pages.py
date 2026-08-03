import json

with open('assets/projects_data.json', 'r', encoding='utf-8') as f:
    projects = json.load(f)

# Page mapping dictionary
pdf_page_map = {
    "proj-1": 6,   # 별내선 연장
    "proj-2": 7,   # 생애주기별 대중교통비
    "proj-3": 8,   # 대광위 광역버스 준공영제
    "proj-4": 9,   # 시내버스 공공관리제
    "proj-5": 11,  # 공영주차장 조성사업
    "proj-6": 14,  # 미금로 확장
    "proj-7": 16,  # 시도5호선 확장
    "proj-8": 18,  # 농어촌도로102호선 확장
    "proj-9": 20,  # 진접 금곡리 바람골길
    "proj-10": 22, # 화도읍 가곡초 통학로
    "proj-11": 24, # 오남 양지리(대대울)
    "proj-12": 26, # 묵현20리 연결도로
    "proj-13": 28  # 진접 금곡리 도시계획도로
}

pdf_file_name = "(8.3.) 중점사업 추진사업 점검 보고회 자료(교통국 수정)_최최종.pdf"

for p in projects:
    page_num = pdf_page_map.get(p["id"], 1)
    p["pdfPage"] = page_num
    p["pdfUrl"] = f"{pdf_file_name}#page={page_num}"

with open('assets/projects_data.json', 'w', encoding='utf-8') as f:
    json.dump(projects, f, ensure_ascii=False, indent=2)

print("Updated projects_data.json with pdfPage and pdfUrl for all 13 projects!")
