/* ==========================================================================
   교통국 중점 추진사업 총괄보고 대시보드 - JavaScript Logic
   ========================================================================== */

// Embedded full dataset to ensure 100% offline & file:// protocol compatibility
const EMBEDDED_PROJECTS_DATA = [
    {
        "id": "proj-1",
        "pdfPage": 6,
        "pdfPages": [
            6
        ],
        "pdfPageLabel": "P.6",
        "no": "2-①",
        "title": "별내선(8호선) 연장(별내~별내별가람)",
        "dept": "교통정책과",
        "phone": "2420",
        "category": "지속추진",
        "tags": [
            "지속추진"
        ],
        "location": "별내역 ~ 별내별가람역",
        "scope": "3.437km (정거장 1개소)",
        "budgetTotal": "4,196억원",
        "budgetNum": 4196,
        "budgetUnit": "억원",
        "budgetBreakdown": {
            "국비(70%)": "2,307억원",
            "도비(15%)": "494.5억원",
            "시비(15%)": "494.5억원",
            "LH분담금": "900억원"
        },
        "period": "2021년 ~ 2033년",
        "beneficiaries": "별내동 및 북부권 주민 (수혜인원 : 약 15만명)",
        "purpose": "8호선 별내역과 4호선 별내별가람역 연계를 통한 수도권 동북부 광역교통망 구축 및 주민 통행 편의 증진",
        "achievements": [
            {
                "text": "2026. 6. : 2026년 제2차 예비타당성조사 대상 사업 제출(시→도→대광위→국토부→기획예산처)",
                "children": [
                    "2025. 5. : 별내선 연장 재기획 연구용역 추진",
                    "2026. 6. : 국토부 투자심사위원회 통과",
                    "2026. 6. ~ 7. : 국토부 제1차관 및 기획예산처 장관 정책 건의"
                ]
            }
        ],
        "schedule": [
            "2026. 8. : 제2차 예비타당성조사 대상 사업 선정 (기획예산처)"
        ],
        "image": "assets/images/proj-1.png",
        "imageCaption": "별내선(8호선) 연장 노선도"
    },
    {
        "id": "proj-2",
        "pdfPage": 7,
        "pdfPages": [
            7
        ],
        "pdfPageLabel": "P.7",
        "no": "2-②",
        "title": "생애주기별 대중교통비 지원",
        "dept": "대중교통과",
        "phone": "2290",
        "category": "지속추진",
        "tags": [
            "지속추진",
            "2회추경"
        ],
        "location": "남양주시 전역",
        "scope": "K패스, 어르신(만 65세 이상), 어린이·청소년(만 6~18세)",
        "budgetTotal": "33,603백만원",
        "budgetNum": 336.03,
        "budgetUnit": "억원",
        "budgetBreakdown": {
            "기 확보액": "23,760백만원",
            "2회 추경 요구액": "9,843백만원",
            "K패스 지원": "25,924백만원 (국 50%, 도 15%, 시 35%)",
            "어르신 교통비 지원": "6,420백만원 (시 100%)",
            "어린이·청소년 교통비 지원": "1,259백만원 (도 50%, 시 50%)"
        },
        "period": "연중 계속",
        "beneficiaries": "약 193,000명 지원 (K패스 10.3만명, 어르신 6.7만명, 어린이·청소년 2.3만명)",
        "purpose": "시민의 대중교통 이용 활성화와 교통비 부담 완화를 위해 일반 시민부터 어르신, 어린이·청소년까지 생애주기별 맞춤형 교통비 지원",
        "achievements": [
            "K패스 : 2026년 보조금 1·2차 총 11,659백만원 지급(이용자 103,216명)",
            "어르신 교통비 : 2026년 1분기 1,405백만원 지급(이용자 66,767명)",
            "어린이·청소년 교통비 : 2026년 1차분 804백만원 지급(이용자 약 23,000명)"
        ],
        "schedule": [
            "2026. 7. ~ 12. : 교통비 지원 및 이용현황 지속 관리"
        ],
        "image": "assets/images/proj-2.png",
        "imageCaption": "생애주기별 대중교통비 지원 홍보물"
    },
    {
        "id": "proj-3",
        "pdfPage": 8,
        "pdfPages": [
            8
        ],
        "pdfPageLabel": "P.8",
        "no": "2-③",
        "title": "대광위 광역버스 준공영제",
        "dept": "대중교통과",
        "phone": "2290",
        "category": "지속추진",
        "tags": [
            "지속추진",
            "2회추경"
        ],
        "location": "관내 및 경유 광역버스 노선 전역",
        "scope": "관할 28개 노선 229대 / 경유 4개 노선 16대",
        "budgetTotal": "12,624백만원",
        "budgetNum": 126.24,
        "budgetUnit": "억원",
        "budgetBreakdown": {
            "기 확보액": "10,856백만원",
            "2회 추경 요구액": "1,768백만원",
            "재원 분담": "국비 50%, 도비 15%, 시비 35%"
        },
        "period": "2020년 ~ 계속",
        "beneficiaries": "일평균 약 40,000명 이용 시민",
        "purpose": "대광위 광역버스 준공영제 운영 지원을 통한 안정적인 광역버스 이용 환경 제공",
        "achievements": [
            "2024. 12. 전체 광역버스 노선 전환 완료(경기도 공공버스 → 대광위 준공영제)",
            "국비 지원 확보(50%)로 시비 부담 절감",
            "안정적 운행으로 시민 출·퇴근 및 통학 광역교통 이용 편의 증진"
        ],
        "schedule": [
            "대광위 광역버스 준공영제 노선 확충 및 안정적 운영 추진"
        ],
        "image": "assets/images/proj-3.png",
        "imageCaption": "대광위 광역버스 준공영제 차량"
    },
    {
        "id": "proj-4",
        "pdfPage": 9,
        "pdfPages": [
            9,
            10
        ],
        "pdfPageLabel": "P.9~10",
        "no": "2-④",
        "title": "시내버스 공공관리제",
        "dept": "대중교통과",
        "phone": "2290",
        "category": "지속추진",
        "tags": [
            "지속추진",
            "2회추경"
        ],
        "location": "남양주시 시내버스 전체 노선",
        "scope": "시·군간 23개 노선 264대 / 시·군내 36개 노선 123대",
        "budgetTotal": "23,033백만원",
        "budgetNum": 230.33,
        "budgetUnit": "억원",
        "budgetBreakdown": {
            "기 확보액": "16,540백만원",
            "2회 추경 요구액": "6,492백만원",
            "시·군간 노선": "15,427백만원 (시비 100%)",
            "시·군내 노선": "7,606백만원 (도비 30%, 시비 70%)"
        },
        "period": "2024. 1. ~ 2027. 12.",
        "beneficiaries": "시내버스 이용 전체 시민",
        "purpose": "시내버스 운영의 공공성 강화와 교통편의 증진을 위하여 경기도 시내버스 준공영제 시행",
        "achievements": [
            "시·군간 9개 노선 121대 전환 완료 (전환율 : 45.8%)",
            "시·군내 12개 노선 28대 전환 완료 (전환율 : 22.8%)"
        ],
        "schedule": [
            "2026. 10. : 시·군간 7개 노선 66대 전환 예정",
            "2026. 11. : 시·군내 8개 노선 9대 전환 예정",
            "2027년 : 시·군간 7개 노선 77대, 시·군내 16개 노선 86대 전환 예정"
        ],
        "image": "assets/images/proj-4.png",
        "imageCaption": "시내버스 공공관리제 현장 사진"
    },
    {
        "id": "proj-5",
        "pdfPage": 11,
        "pdfPages": [
            11,
            12,
            13
        ],
        "pdfPageLabel": "P.11~13",
        "no": "2-⑤",
        "title": "공영주차장 조성사업 (7개소)",
        "dept": "주차관리과",
        "phone": "8921",
        "category": "지속추진",
        "tags": [
            "지속추진",
            "2회추경"
        ],
        "location": "퇴계원, 다산, 와부, 평내 등 7개소",
        "scope": "1,003면 조성 / 연면적 39,783㎡",
        "budgetTotal": "124,184백만원",
        "budgetNum": 1241.84,
        "budgetUnit": "억원",
        "budgetBreakdown": {
            "기 확보액": "67,844백만원",
            "2회 추경 요구액": "14,930백만원",
            "자체 재원": "79,696백만원",
            "외부 재원": "44,488백만원"
        },
        "period": "2023년 ~ 2028년",
        "beneficiaries": "남양주시 주요 도심지 주차 이용 시민",
        "purpose": "도심지 주차난 해소 및 주민 편의증진을 위한 공영주차장 7개소 건립",
        "achievements": [
            "7개 사업지 중 공사중 3개소, 실시설계중 3개소, 행정절차 1개소 정상 추진",
            "퇴계원중 지하(174면, 공정률 65%), 다산진건 주9(94면, 공정률 60%), 다산역 환승(308면, 공정률 27%)"
        ],
        "schedule": [
            "2026. 10. : 다산진건지구(주9) 주차장 운영 개시",
            "2026. 12. : 퇴계원중학교 지하 주차장 운영 개시",
            "2027. 03. : 다산역 환승주차장 공사 준공"
        ],
        "image": "assets/images/proj-5.png",
        "imageCaption": "공영주차장 조성 대표 현장/조감도",
        "subProjects": [
            {
                "id": "park-1",
                "name": "퇴계원중학교 운동장 지하 공영주차장 건립",
                "budget": "21,000백만원",
                "capacity": "174면",
                "area": "6,301㎡",
                "status": "공사중 (공정률 65%)",
                "plan": "2026.12 운영개시 / 2027.04 준공",
                "image": "assets/images/park-1.png"
            },
            {
                "id": "park-2",
                "name": "다산진건지구(주9) 공영주차장 건립",
                "budget": "11,549백만원",
                "capacity": "94면",
                "area": "2,932㎡",
                "status": "공사중 (공정률 60%)",
                "plan": "2026.10 운영개시 / 2026.12 준공",
                "image": "assets/images/park-2.png"
            },
            {
                "id": "park-3",
                "name": "다산역 환승주차장 건립",
                "budget": "43,900백만원",
                "capacity": "308면",
                "area": "16,206㎡",
                "status": "공사중 (공정률 27%)",
                "plan": "2027.03 공사 준공",
                "image": "assets/images/park-3.png"
            },
            {
                "id": "park-4",
                "name": "와부읍 팔당2리 공영주차장 조성",
                "budget": "2,995백만원",
                "capacity": "26면",
                "area": "2,154㎡",
                "status": "실시설계중 (공정률 30%)",
                "plan": "2026.11 착공 / 2026.12 준공",
                "image": "assets/images/park-4.png"
            },
            {
                "id": "park-5",
                "name": "평내동 물놀이장 지하 공영주차장 건립",
                "budget": "10,900백만원",
                "capacity": "68면",
                "area": "2,893㎡",
                "status": "실시설계중 (공정률 83%)",
                "plan": "2026.10 착공 / 2028.04 준공",
                "image": "assets/images/park-5.png"
            },
            {
                "id": "park-6",
                "name": "다산지금지구(주2) 공영주차장 건립",
                "budget": "33,800백만원",
                "capacity": "318면",
                "area": "8,526㎡",
                "status": "실시설계중 (공정률 82%)",
                "plan": "2026.12 착공 / 2028.10 준공",
                "image": "assets/images/park-6.png"
            },
            {
                "id": "park-7",
                "name": "와부 빛터널 임시 공영주차장 조성",
                "budget": "40백만원",
                "capacity": "15면",
                "area": "771㎡",
                "status": "사전행정절차 이행중",
                "plan": "2026.09 공사 착공 및 준공",
                "image": "assets/images/park-7.png"
            }
        ]
    },
    {
        "id": "proj-6",
        "pdfPage": 14,
        "pdfPages": [
            14,
            15
        ],
        "pdfPageLabel": "P.14~15",
        "no": "2-⑥",
        "title": "미금로(중로1-302호) 확장공사",
        "dept": "도로건설과",
        "phone": "2430",
        "category": "지속추진",
        "tags": [
            "지속추진",
            "2회추경"
        ],
        "location": "다산동 4302-48번지 일원",
        "scope": "L=385m, B=20m (4차선 도로확장)",
        "budgetTotal": "760억원",
        "budgetNum": 760,
        "budgetUnit": "억원",
        "budgetBreakdown": {
            "GH 부담금(90%)": "684억원",
            "시비(10%)": "76억원",
            "기 확보액": "11.5억원"
        },
        "period": "2027. 6. ~ 2029. 12.",
        "beneficiaries": "다산1동, 다산2동 인구 약 140,000명",
        "purpose": "미금로 도로 확장에 따라 다산1동, 다산2동 인구 14만 명 교통 편익 증진 및 도로 병목 현구 해소",
        "achievements": [
            "2025. 5. : 실시설계용역 착수(공정률 90%, 2026.10 준공 예정)",
            "2025. 7. : GH 재원분담 협약 체결 [GH 684억(90%), 남양주시 76억(10%)]",
            "2026. 6. : 도시관리계획 변경 및 실시계획인가 신청"
        ],
        "schedule": [
            "2026. 11. : 보상절차 추진 (건축물 18개동, 사유지 31필지)",
            "2027. 6. ~ 2029. 12. : 공사 추진"
        ],
        "image": "assets/images/proj-6.png",
        "imageCaption": "미금로(중로1-302호) 확장공사 위치도"
    },
    {
        "id": "proj-7",
        "pdfPage": 16,
        "pdfPages": [
            16,
            17
        ],
        "pdfPageLabel": "P.16~17",
        "no": "2-⑦",
        "title": "시도5호선(중말교차로~철마교차로) 도로확장",
        "dept": "도로건설과",
        "phone": "2430",
        "category": "지속추진",
        "tags": [
            "지속추진",
            "2회추경"
        ],
        "location": "진접읍 진벌리 521-1 ~ 팔야리 757-5번지 일원",
        "scope": "L=1.0km, B=20m (4차로 도로확장)",
        "budgetTotal": "350억원",
        "budgetNum": 350,
        "budgetUnit": "억원",
        "budgetBreakdown": {
            "설계비": "6억원",
            "보상비": "200억원",
            "공사비": "144억원",
            "기 확보액": "16억원",
            "2회 추경 요구액": "25억원"
        },
        "period": "2027. 9. ~ 2029. 9.",
        "beneficiaries": "진접읍 인구 약 39,000명 (진벌리 기업인회, 팔야 기업인회 중점 건의)",
        "purpose": "진접읍 현장 시장실 건의사항 해결, 산단 접근성 향원 및 정체 해소",
        "achievements": [
            "2022. 4. 25. : 실시설계용역 착수 (공정률 95%)",
            "2024. 4. 30. : 도로구역 결정(변경) 및 지형도면 고시",
            "2026. 5. 12. : 경관심의(조건부 의결) 완료"
        ],
        "schedule": [
            "2026. 11. : 보상계획 공고 (200필지 보상 예정)",
            "2027. 9. ~ 2029. 9. : 공사 추진"
        ],
        "image": "assets/images/proj-7.png",
        "imageCaption": "시도5호선(중말교차로~철마교차로) 도로확장 공사 위치도"
    },
    {
        "id": "proj-8",
        "pdfPage": 18,
        "pdfPages": [
            18,
            19
        ],
        "pdfPageLabel": "P.18~19",
        "no": "3-①",
        "title": "농어촌도로102호선(녹촌~창현) 도로확장",
        "dept": "도로건설과",
        "phone": "2430",
        "category": "2회추경 사업",
        "tags": [
            "2회추경"
        ],
        "location": "화도읍 녹촌리 303-13 ~ 창현리 577-7(녹촌교)",
        "scope": "L=914m, B=20m (4차로 도로확장)",
        "budgetTotal": "174억원",
        "budgetNum": 174,
        "budgetUnit": "억원",
        "budgetBreakdown": {
            "설계비": "4억원",
            "보상비": "100억원",
            "공사비": "70억원",
            "기 확보액": "24억원",
            "2회 추경 요구액": "25억원"
        },
        "period": "2027. 9. ~ 2029. 9.",
        "beneficiaries": "화도읍 주민 약 28,000명 이상",
        "purpose": "2026년 10월 국도46호선 녹촌IC 개통 예정에 맞춰 2차선에서 4차선으로 확장하여 교통정체 해소",
        "achievements": [
            "설계 공정율 95% 달성",
            "국도 46호선 녹촌IC 체계 연계"
        ],
        "schedule": [
            "2026. 11. : 농어촌도로 노선지정(변경) 고시",
            "2026. 12. : 보상계획 공고 (189필지 보상 예정)",
            "2027. 9. ~ 2029. 9. : 공사 추진"
        ],
        "image": "assets/images/proj-8.png",
        "imageCaption": "농어촌도로102호선(녹촌~창현) 도로확장 공사 위치도"
    },
    {
        "id": "proj-9",
        "pdfPage": 20,
        "pdfPages": [
            20,
            21
        ],
        "pdfPageLabel": "P.20~21",
        "no": "3-②",
        "title": "진접 금곡리 바람골길 도로개설(소1-107호)",
        "dept": "도로건설과",
        "phone": "2430",
        "category": "2회추경 사업",
        "tags": [
            "2회추경"
        ],
        "location": "진접읍 금곡리 115-2번지 ~ 성관사 앞",
        "scope": "L=750m, B=10m (1차수 L=320m, 2차수 L=430m)",
        "budgetTotal": "143억원",
        "budgetNum": 143,
        "budgetUnit": "억원",
        "budgetBreakdown": {
            "설계비": "3억원",
            "보상비": "105억원",
            "공사비": "35억원",
            "시비": "135억원",
            "외부 재원": "8억원 (특교세 5억, 특조금 3억)",
            "2회 추경 요구액": "26억원 (편성 시 전액확보)"
        },
        "period": "2020. 3. ~ 2027. 12.",
        "beneficiaries": "진접읍 금곡리 주민 및 바람골 기업인회 등 약 37,321명 이상",
        "purpose": "현황도로의 차량교행 어려움 해소 및 대형차량 진입 민원 해결",
        "achievements": [
            "1차수 구간 통행 여건 개선",
            "2회 추경 편성 시 사업비 전액 확보"
        ],
        "schedule": [
            "2027. 5. : 준공 (전체 구간)"
        ],
        "image": "assets/images/proj-9.png",
        "imageCaption": "진접 금곡리 바람골길 도로개설 위치도"
    },
    {
        "id": "proj-10",
        "pdfPage": 22,
        "pdfPages": [
            22,
            23
        ],
        "pdfPageLabel": "P.22~23",
        "no": "3-③",
        "title": "화도읍 가곡초 통학로 확장공사",
        "dept": "도로건설과",
        "phone": "2430",
        "category": "2회추경 사업",
        "tags": [
            "2회추경"
        ],
        "location": "화도읍 가곡리 279-15번지 ~ 284-127번지 일원",
        "scope": "L=470m, B=10m",
        "budgetTotal": "79억원",
        "budgetNum": 79,
        "budgetUnit": "억원",
        "budgetBreakdown": {
            "설계비": "2억원",
            "보상비": "65억원",
            "공사비": "12억원",
            "시비": "73억원",
            "외부 재원": "6억원 (특교세)",
            "2회 추경 요구액": "11.9억원 (보상률 63%)"
        },
        "period": "2021. 10. ~ 2027. 12.",
        "beneficiaries": "가곡초 학생 및 주민 6,257명 이상",
        "purpose": "가곡초 정문 앞 차량·보행자 혼재로 인한 교통안전 민원 해소 및 안전한 통학로 조성",
        "achievements": [
            "보상률 63% 달성 (전체 60필지 중 38필지 보상 완료)",
            "2회 추경 편성 시 사업비 전액 확보"
        ],
        "schedule": [
            "2026. 12. : 잔여지(22필지) 보상 완료",
            "2027. 3. ~ 12. : 착공 및 준공"
        ],
        "image": "assets/images/proj-10.png",
        "imageCaption": "화도읍 가곡초 통학로 확장공사 위치도"
    },
    {
        "id": "proj-11",
        "pdfPage": 24,
        "pdfPages": [
            24,
            25
        ],
        "pdfPageLabel": "P.24~25",
        "no": "3-④",
        "title": "오남 양지리(대대울)진입도로 개설공사",
        "dept": "도로건설과",
        "phone": "2430",
        "category": "2회추경 사업",
        "tags": [
            "2회추경"
        ],
        "location": "오남읍 양지리 777-18번지 ~ 794-5번지 일원(대대울)",
        "scope": "L=930m, B=8m [2구간 L=785m, 3구간 L=145m] ※ 1구간 준공 L=331m",
        "budgetTotal": "62.4억원",
        "budgetNum": 62.4,
        "budgetUnit": "억원",
        "budgetBreakdown": {
            "설계비": "2.5억원",
            "보상비": "37.9억원",
            "공사비": "22억원",
            "기 확보액": "26.4억원",
            "2회 추경 요구액": "17억원",
            "2027년 이후": "19억원"
        },
        "period": "2018. 10. ~ 2028. 12.",
        "beneficiaries": "오남읍 양지리 주민 및 대대울 기업인회 약 16,226명 이상",
        "purpose": "공장밀집지역 진입도로 확장을 통해 대형차량 진입 및 통행불편 민원 해소",
        "achievements": [
            "1구간 L=331m 준공 완료",
            "2구간 보상률 53% 달성"
        ],
        "schedule": [
            "2026. 7. : 실시설계용역 착수(3구간)",
            "2026. 12. : 도시관리계획 결정(3구간)",
            "2027. 3. : 실시계획인가 고시(3구간)",
            "2027. 4. ~ 2028. 2. : 보상협의(2,3구간)",
            "2028. 3. ~ 12. : 착공 및 준공(2,3구간)"
        ],
        "image": "assets/images/proj-11.png",
        "imageCaption": "오남 양지리(대대울) 진입도로 현장 및 위치도"
    },
    {
        "id": "proj-12",
        "pdfPage": 26,
        "pdfPages": [
            26,
            27
        ],
        "pdfPageLabel": "P.26~27",
        "no": "3-⑤",
        "title": "묵현20리 연결도로 개설공사",
        "dept": "도로건설과",
        "phone": "2430",
        "category": "2회추경 사업",
        "tags": [
            "2회추경"
        ],
        "location": "화도읍 묵현리 40-1번지 ~ 36-16번지 일원 (마석역신도브래뉴, 삼익A 진입구간)",
        "scope": "L=189m, B=10m",
        "budgetTotal": "84억원",
        "budgetNum": 84,
        "budgetUnit": "억원",
        "budgetBreakdown": {
            "설계비": "2억원",
            "보상비": "70억원",
            "공사비": "12억원",
            "기 확보액": "2억원",
            "2회 추경 요구액": "35억원",
            "2027년 이후": "47억원"
        },
        "period": "2023. 7. ~ 2027. 12.",
        "beneficiaries": "화도읍 묵현20리 주민 약 34,189명 이상",
        "purpose": "지방도 387호선 단절 도로 연결로 주민 숙원 통행 불편 해소",
        "achievements": [
            "실시설계 및 행정절차 수행 완료"
        ],
        "schedule": [
            "2026. 9. : 실시계획인가 변경 고시",
            "2026. 10. : 보상 협의 (9필지 보상 예정)",
            "2027. 6. : 공사 착공"
        ],
        "image": "assets/images/proj-12.png",
        "imageCaption": "묵현20리 연결도로 개설공사 위치도"
    },
    {
        "id": "proj-13",
        "pdfPage": 28,
        "pdfPages": [
            28,
            29
        ],
        "pdfPageLabel": "P.28~29",
        "no": "3-⑥",
        "title": "진접 금곡리 도시계획도로 개설공사",
        "dept": "도로건설과",
        "phone": "2430",
        "category": "2회추경 사업",
        "tags": [
            "2회추경"
        ],
        "location": "진접읍 금곡리 841-3번지 ~ 227-3번지 일원 (금곡천 옆)",
        "scope": "L=710m, B=10m",
        "budgetTotal": "103.7억원",
        "budgetNum": 103.7,
        "budgetUnit": "억원",
        "budgetBreakdown": {
            "설계비": "2.4억원",
            "보상비": "72억원",
            "공사비": "29.3억원",
            "기 확보액": "3억원",
            "2회 추경 요구액": "36억원",
            "2027년 이후": "64.7억원"
        },
        "period": "2018. 5. ~ 2028. 6.",
        "beneficiaries": "진접읍 금곡리 주민 약 37,321명 이상",
        "purpose": "진접선 차량기지 이전공사에 대한 다수인민원 보상차원으로 마을안길 협소 도로 개선",
        "achievements": [
            "도시계획 도로 지정 및 용역 완료"
        ],
        "schedule": [
            "2026. 10. ~ 2028. 2. : 보상협의 (89필지 보상 예정)",
            "2028. 3. ~ 2028. 12. : 착공 및 준공"
        ],
        "image": "assets/images/proj-13.png",
        "imageCaption": "진접 금곡리 도시계획도로 개설공사 위치도"
    }
];

let projectsData = [];
let activeDept = 'all';
let activeTag = 'all';
let currentSearch = '';
let currentSelectedProject = null;
const RAW_PDF_FILENAME = "(8.3.) 중점사업 추진사업 점검 보고회 자료(교통국 수정)_최최종.pdf";

// Initialize Dashboard when DOM is ready
document.addEventListener('DOMContentLoaded', async () => {
    initTheme();
    await loadProjectsData();
    initEventListeners();
    initLightboxInteractions();
});

// Load Dataset
async function loadProjectsData() {
    try {
        const response = await fetch('assets/projects_data.json');
        if (!response.ok) throw new Error('Failed to load JSON data');
        const data = await response.json();
        if (data && data.length > 0) {
            projectsData = data;
        } else {
            projectsData = EMBEDDED_PROJECTS_DATA;
        }
    } catch (err) {
        console.warn('Fetch fallback to embedded 13 projects dataset:', err);
        projectsData = EMBEDDED_PROJECTS_DATA;
    }

    renderKPI();
    renderDeptBar();
    renderProjects();
}

// Render KPI Summary Section
function renderKPI() {
    const totalCount = projectsData.length;
    const checkCount = projectsData.filter(p => p.tags.includes('지속추진') || p.tags.includes('점검사업')).length;
    const suppCount = projectsData.filter(p => p.tags.includes('2회추경')).length;

    let totalBudget = 0;
    projectsData.forEach(p => {
        if (p.budgetNum) {
            totalBudget += p.budgetNum;
        }
    });

    document.getElementById('kpi-total-count').textContent = totalCount;
    document.getElementById('kpi-check-count').textContent = checkCount;
    document.getElementById('kpi-supp-count').textContent = suppCount;
    document.getElementById('kpi-budget-total').textContent = Math.round(totalBudget).toLocaleString();

    // Update pill counts
    document.getElementById('count-all').textContent = totalCount;
    document.getElementById('count-policy').textContent = projectsData.filter(p => p.dept === '교통정책과').length;
    document.getElementById('count-transit').textContent = projectsData.filter(p => p.dept === '대중교통과').length;
    document.getElementById('count-parking').textContent = projectsData.filter(p => p.dept === '주차관리과').length;
    document.getElementById('count-road').textContent = projectsData.filter(p => p.dept === '도로건설과').length;
}

// Render Department Analytics Bar
function renderDeptBar() {
    const container = document.getElementById('dept-bar-container');
    if (!container) return;

    const depts = [
        { name: '교통정책과', key: 'dept-policy', color: '#2563eb' },
        { name: '대중교통과', key: 'dept-transit', color: '#059669' },
        { name: '주차관리과', key: 'dept-parking', color: '#7c3aed' },
        { name: '도로건설과', key: 'dept-road', color: '#d97706' }
    ];

    const total = projectsData.length;
    let barHTML = `<div class="dept-bar-group">`;
    let legendHTML = `<div class="dept-legend-row">`;

    depts.forEach(d => {
        const count = projectsData.filter(p => p.dept === d.name).length;
        const pct = ((count / total) * 100).toFixed(1);
        if (count > 0) {
            barHTML += `
                <div class="dept-segment ${d.key}" style="width: ${pct}%;" 
                     title="${d.name}: ${count}건 (${pct}%)"
                     onclick="filterByDept('${d.name}')">
                    ${d.name} ${count}건
                </div>
            `;
        }
        legendHTML += `
            <div class="legend-item">
                <span class="legend-dot" style="background-color: ${d.color};"></span>
                <span>${d.name} (${count}건)</span>
            </div>
        `;
    });

    barHTML += `</div>`;
    legendHTML += `</div>`;
    container.innerHTML = barHTML + legendHTML;
}

// Dynamic update for type filter pill counts based on active department & search
function updateDynamicTagCounts() {
    const deptProjects = projectsData.filter(p => {
        if (activeDept !== 'all' && p.dept !== activeDept) return false;
        if (currentSearch.trim() !== '') {
            const query = currentSearch.toLowerCase();
            const matchTitle = p.title.toLowerCase().includes(query);
            const matchLocation = (p.location || '').toLowerCase().includes(query);
            const matchDept = p.dept.toLowerCase().includes(query);
            const matchPurpose = (p.purpose || '').toLowerCase().includes(query);
            if (!matchTitle && !matchLocation && !matchDept && !matchPurpose) return false;
        }
        return true;
    });

    const countCheck = deptProjects.filter(p => p.tags.includes('지속추진') || p.tags.includes('점검사업')).length;
    const countSupp = deptProjects.filter(p => p.tags.includes('2회추경')).length;

    const checkSpan = document.getElementById('count-tag-check');
    const suppSpan = document.getElementById('count-tag-supp');

    if (checkSpan) checkSpan.textContent = countCheck;
    if (suppSpan) suppSpan.textContent = countSupp;
}

// Render Project Cards Grid or Table View based on currentView
function renderProjects() {
    updateDynamicTagCounts();
    const cardContainer = document.getElementById('project-cards-container');
    const tableContainer = document.getElementById('project-table-container');
    const emptyState = document.getElementById('empty-state');

    // Filter Logic
    const filtered = projectsData.filter(p => {
        if (activeDept !== 'all' && p.dept !== activeDept) return false;

        if (activeTag !== 'all') {
            if (!p.tags.includes(activeTag)) return false;
        }

        if (currentSearch.trim() !== '') {
            const query = currentSearch.toLowerCase();
            const matchTitle = p.title.toLowerCase().includes(query);
            const matchLocation = (p.location || '').toLowerCase().includes(query);
            const matchDept = p.dept.toLowerCase().includes(query);
            const matchPurpose = (p.purpose || '').toLowerCase().includes(query);
            const matchScope = (p.scope || '').toLowerCase().includes(query);
            const matchNo = (p.no || '').toLowerCase().includes(query);
            if (!matchTitle && !matchLocation && !matchDept && !matchPurpose && !matchScope && !matchNo) return false;
        }

        return true;
    });

    if (filtered.length === 0) {
        if (cardContainer) cardContainer.innerHTML = '';
        if (tableContainer) tableContainer.innerHTML = '';
        if (emptyState) emptyState.style.display = 'flex';
        return;
    }

    if (emptyState) emptyState.style.display = 'none';

    if (currentView === 'card') {
        if (cardContainer) cardContainer.style.display = '';
        if (tableContainer) tableContainer.style.display = 'none';

        cardContainer.innerHTML = filtered.map(p => {
            const tagsHTML = p.tags.map(t => `<span class="tag-badge badge-${t}">${t}</span>`).join('');
            const pdfLabel = p.pdfPageLabel || `P.${p.pdfPage || 1}`;
            const pdfUrl = `${RAW_PDF_FILENAME}#page=${p.pdfPage || 1}`;

            return `
                <article class="project-card">
                    <div class="card-header-bar">
                        <div class="card-no-group">
                            <span class="card-no-badge">${p.no}</span>
                        </div>
                        <div class="card-tags">${tagsHTML}</div>
                    </div>

                    <div class="card-body">
                        <!-- Project Title Clickable -> Triggers Detail Modal -->
                        <a class="card-title-link" onclick="openDetailModal('${p.id}')" title="사업 상세 정보 보기">
                            <span>${p.title}</span>
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                        </a>

                        <div class="card-meta-list">
                            <div class="meta-row">
                                <span class="meta-label">담당부서</span>
                                <span class="meta-val">${p.dept} (☎${p.phone})</span>
                            </div>
                            <div class="meta-row">
                                <span class="meta-label">사업위치</span>
                                <span class="meta-val">${p.location}</span>
                            </div>
                            <div class="meta-row">
                                <span class="meta-label">총사업비</span>
                                <span class="meta-val highlight-budget">${p.budgetTotal}</span>
                            </div>
                            <div class="meta-row">
                                <span class="meta-label">사업규모</span>
                                <span class="meta-val">${p.scope}</span>
                            </div>
                        </div>

                        <!-- Reference Photo Thumbnail Clickable -> Triggers Image Lightbox -->
                        <div class="card-image-box" onclick="openLightbox('${p.image}', '${escapeHtml(p.title)} - 참고사진')" title="클릭하면 큰 사진으로 확대합니다">
                            <img src="${p.image}" alt="${p.imageCaption || p.title}" loading="lazy">
                            <div class="card-image-overlay">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/><line x1="11" y1="8" x2="11" y2="14"/><line x1="8" y1="11" x2="14" y2="11"/></svg>
                                <span>참고사진 확대보기</span>
                            </div>
                        </div>
                    </div>

                    <div class="card-footer">
                        <button class="btn btn-outline" onclick="openDetailModal('${p.id}')">
                            상세 현황 보기
                        </button>
                        <button class="btn btn-pdf-pill" onclick="openProjectPdfInLightbox('${p.id}')" title="${escapeHtml(p.title)} 원본 PDF 확대보기">
                            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/>
                                <polyline points="14 2 14 8 20 8"/>
                                <line x1="16" y1="13" x2="8" y2="13"/>
                                <line x1="16" y1="17" x2="8" y2="17"/>
                            </svg>
                            <span>원본 PDF (${p.pdfPageLabel || ('P.' + (p.pdfPage || 1))})</span>
                        </button>
                    </div>
                </article>
            `;
        }).join('');
    } else {
        if (cardContainer) cardContainer.style.display = 'none';
        if (tableContainer) tableContainer.style.display = '';
        renderTableView(filtered);
    }
}

// View Mode State
let currentView = 'card';

// Switch between Card and Table view
function switchView(mode) {
    currentView = mode;
    const cardBtn = document.getElementById('view-card-btn');
    const tableBtn = document.getElementById('view-table-btn');

    if (cardBtn) cardBtn.classList.toggle('active', mode === 'card');
    if (tableBtn) tableBtn.classList.toggle('active', mode === 'table');

    renderProjects();
}

// Render Table View — 보고서 형식 (사업유형 / 주요내용 / 참고사진)
function renderTableView(filtered) {
    const tableContainer = document.getElementById('project-table-container');
    if (!tableContainer) return;

    if (!filtered || filtered.length === 0) {
        tableContainer.innerHTML = '<p style="text-align:center;padding:2rem;color:var(--text-muted);">조건에 맞는 사업이 없습니다.</p>';
        return;
    }

    const ALL_TAG_TYPES = ['지속추진', '2회추경'];

    const rows = filtered.map(p => {
        // 사업유형 열: 각 유형별 체크박스 표시
        const typeChecks = ALL_TAG_TYPES
            .filter(t => p.tags.includes(t))
            .map(t => {
                const color = t === '지속추진' ? '#2563eb' : t === '점검사업' ? '#059669' : '#d97706';
                return `<div style="display:flex;align-items:center;gap:0.35rem;margin-bottom:0.3rem;font-size:0.8rem;color:${color};font-weight:700;">
                    <span style="display:inline-flex;align-items:center;justify-content:center;width:15px;height:15px;border:1.5px solid ${color};border-radius:3px;background:${color};color:#fff;font-size:0.6rem;">✓</span>
                    ${t}
                </div>`;
            }).join('');

        // 주요내용: 사업명, 총사업비, 사업내용(scope), 추진실적(achievements) 일부
        const achHTML = (() => {
            if (!p.achievements || p.achievements.length === 0) return '';
            const items = p.achievements.slice(0, 3).map(item => {
                const text = typeof item === 'object' ? (item.text || '') : item;
                return `<div style="display:flex;gap:0.4rem;align-items:flex-start;margin-top:0.25rem;">
                    <span style="color:var(--primary-color);font-weight:700;flex-shrink:0;margin-top:1px;">○</span>
                    <span style="color:var(--text-main);font-size:0.82rem;line-height:1.5;">${text}</span>
                </div>`;
            }).join('');
            return `<div style="margin-top:0.5rem;padding-top:0.4rem;border-top:1px dashed var(--border-color);">
                <div style="font-size:0.75rem;font-weight:700;color:var(--text-muted);margin-bottom:0.2rem;">▣ 추진실적</div>
                ${items}
            </div>`;
        })();

        const scheduleHTML = (() => {
            if (!p.schedule || p.schedule.length === 0) return '';
            const items = p.schedule.slice(0, 2).map(s =>
                `<div style="display:flex;gap:0.4rem;align-items:flex-start;margin-top:0.2rem;">
                    <span style="color:#d97706;font-weight:700;flex-shrink:0;">○</span>
                    <span style="color:var(--text-muted);font-size:0.8rem;line-height:1.5;">${s}</span>
                </div>`
            ).join('');
            return `<div style="margin-top:0.4rem;">
                <div style="font-size:0.75rem;font-weight:700;color:var(--text-muted);margin-bottom:0.2rem;">▣ 향후계획</div>
                ${items}
            </div>`;
        })();

        return `<tr onclick="openDetailModal('${p.id}')" style="cursor:pointer;border-bottom:1px solid var(--border-color);transition:background 0.15s;"
                    onmouseover="this.style.background='rgba(99,102,241,0.07)'"
                    onmouseout="this.style.background=''">
            <td style="padding:1rem 1rem;vertical-align:top;width:130px;min-width:130px;border-right:1px solid var(--border-color);">
                ${typeChecks}
            </td>
            <td style="padding:1rem 1.4rem;vertical-align:top;">
                <div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:0.5rem;">
                    <span style="background:var(--primary-color);color:#fff;font-size:0.75rem;font-weight:700;padding:0.15rem 0.55rem;border-radius:999px;white-space:nowrap;">${p.no}</span>
                    <span style="font-size:1.05rem;font-weight:800;color:var(--text-main);">사 업 명 : ${p.title}</span>
                </div>
                <div style="font-size:0.9rem;color:var(--text-muted);margin-bottom:0.25rem;">
                    <span style="font-weight:700;color:var(--text-main);">○ 총사업비 : </span><span style="font-weight:700;color:#d97706;">${p.budgetTotal}</span>
                </div>
                <div style="font-size:0.9rem;color:var(--text-muted);margin-bottom:0.25rem;">
                    <span style="font-weight:700;color:var(--text-main);">○ 사업내용 : </span>${p.scope}
                </div>
                ${achHTML}
                ${scheduleHTML}
            </td>
            <td style="padding:1rem 0.8rem;vertical-align:top;width:170px;min-width:170px;border-left:1px solid var(--border-color);text-align:center;">
                <img src="${p.image}" alt="${p.title}"
                     style="width:155px;height:105px;object-fit:cover;border-radius:var(--radius-sm);border:1px solid var(--border-color);cursor:pointer;"
                     onclick="event.stopPropagation(); openLightbox('${p.image}', '${escapeHtml(p.title)} - 참고사진')"
                     title="클릭하여 사진 확대보기">
                <div style="font-size:0.75rem;color:var(--text-muted);margin-top:0.4rem;line-height:1.4;">${p.imageCaption || p.title}</div>
            </td>
        </tr>`;
    }).join('');

    tableContainer.innerHTML = `
        <div style="overflow-x:auto;border-radius:var(--radius-md);box-shadow:var(--shadow-md);border:1.5px solid var(--border-color);">
            <table style="width:100%;border-collapse:collapse;font-size:0.9rem;">
                <thead>
                    <tr style="background:#f8f9fa;color:var(--text-main);border-bottom:2px solid #333;">
                        <th style="padding:0.7rem 1rem;text-align:center;width:130px;min-width:130px;font-size:0.9rem;font-weight:700;border-right:1px solid #ccc;border-left:1px solid #ccc;">사업유형</th>
                        <th style="padding:0.7rem 1.4rem;text-align:center;font-size:0.9rem;font-weight:700;border-right:1px solid #ccc;">주요내용</th>
                        <th style="padding:0.7rem 0.8rem;text-align:center;width:170px;min-width:170px;font-size:0.9rem;font-weight:700;border-right:1px solid #ccc;">참고사진</th>
                    </tr>
                </thead>
                <tbody>${rows}</tbody>
            </table>
        </div>
        <p style="text-align:right;font-size:0.75rem;color:var(--text-muted);margin-top:0.5rem;padding-right:0.5rem;">
            ※ 항목 클릭 시 상세 정보를 확인할 수 있습니다.
        </p>`;
}

function openDetailModal(projId) {
    const project = projectsData.find(p => p.id === projId);
    if (!project) return;

    currentSelectedProject = project;

    document.getElementById('modal-no').textContent = project.no;
    document.getElementById('modal-title').textContent = project.title;
    document.getElementById('modal-dept').textContent = `${project.dept} (☎${project.phone})`;
    document.getElementById('modal-location').textContent = project.location || '-';
    document.getElementById('modal-budget').textContent = project.budgetTotal;
    document.getElementById('modal-beneficiaries').textContent = project.beneficiaries || '-';

    // PDF page image & links inside modal
    const pdfPage = project.pdfPage || 1;
    const pdfLabel = project.pdfPageLabel || `P.${pdfPage}`;
    const pdfPages = project.pdfPages || [pdfPage];
    const pdfUrl = `${RAW_PDF_FILENAME}#page=${pdfPage}`;
    
    const pdfText = document.getElementById('modal-pdf-btn-text');
    const pdfExternalLink = document.getElementById('pdf-external-link');
    const pdfIndicator = document.getElementById('pdf-page-indicator');
    const modalFooterPdfPageNum = document.getElementById('modal-footer-pdf-page-num');

    if (pdfText) pdfText.textContent = `원본 PDF (${pdfLabel})`;
    if (pdfExternalLink) pdfExternalLink.href = pdfUrl;
    if (pdfIndicator) pdfIndicator.textContent = `원본 PDF 보고서 (${pdfLabel})`;
    if (modalFooterPdfPageNum) modalFooterPdfPageNum.textContent = pdfLabel;

    // Render Tab 2 Pages
    const pagesContainer = document.getElementById('modal-pdf-pages-container');
    if (pagesContainer) {
        pagesContainer.innerHTML = pdfPages.map((pg, idx) => `
            <div class="pdf-page-card" style="margin-bottom: 1.5rem; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-md); padding: 1.25rem; text-align: center; box-shadow: var(--shadow-sm);">
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 0.75rem; padding-bottom: 0.5rem; border-bottom: 1px dashed var(--border-color);">
                    <span style="font-weight: 700; color: var(--primary-color); font-size: 0.95rem;">📄 페이지 ${idx + 1} / ${pdfPages.length} (PDF Page ${pg})</span>
                    <div style="display:flex; gap:0.5rem;">
                        <button type="button" class="btn btn-sm btn-primary" onclick="openPdfPage(${pg}, '${escapeHtml(project.title)} - P.${pg}')">
                            🔍 확대보기 (P.${pg})
                        </button>
                        <a href="assets/pdf_pages/page_${pg}.png" download="${escapeHtml(project.title)}_PDF_Page_${pg}.png" class="btn btn-sm btn-outline">
                            💾 다운로드
                        </a>
                    </div>
                </div>
                <img src="assets/pdf_pages/page_${pg}.png" alt="${escapeHtml(project.title)} Page ${pg}" 
                     onclick="openPdfPage(${pg}, '${escapeHtml(project.title)} - P.${pg}')"
                     title="클릭 시 라이트박스 뷰어로 확대보기"
                     style="max-width:100%; max-height:650px; object-fit:contain; cursor:pointer; border-radius:var(--radius-sm); border:1px solid var(--border-color); box-shadow:var(--shadow-md);">
                <div style="margin-top:0.5rem; font-size:0.8rem; color:var(--text-muted);">🔍 이미지를 클릭하면 자유로운 확대/축소/이동(Lightbox) 뷰어로 크게 열립니다.</div>
            </div>
        `).join('');
    }

    // Reset Modal Tab to Info
    switchModalTab('info');

    // Tags
    const tagsContainer = document.getElementById('modal-tags');
    tagsContainer.innerHTML = project.tags.map(t => `<span class="tag-badge badge-${t}">${t}</span>`).join('');

    // Purpose & Scope
    document.getElementById('modal-purpose').textContent = project.purpose || '중점추진사업 지속점검 및 시민 교통편의 증진';
    document.getElementById('modal-scope').textContent = project.scope || '-';

    // Budget Table
    const budgetWrap = document.getElementById('modal-budget-table-wrap');
    if (project.budgetBreakdown) {
        let rows = '';
        for (const [key, val] of Object.entries(project.budgetBreakdown)) {
            rows += `<tr><th>${key}</th><td>${val}</td></tr>`;
        }
        budgetWrap.innerHTML = `
            <table class="budget-table">
                <thead>
                    <tr><th>구분 / 재원</th><th>금액 및 비율</th></tr>
                </thead>
                <tbody>${rows}</tbody>
            </table>
        `;
    } else {
        budgetWrap.innerHTML = `<div class="detail-desc-box">총사업비: ${project.budgetTotal}</div>`;
    }

    // Achievements
    const achList = document.getElementById('modal-achievements');
    achList.innerHTML = renderAchievementItems(project.achievements);

    // Schedule
    const schList = document.getElementById('modal-schedule');
    schList.innerHTML = (project.schedule || []).map(s => `<li>${s}</li>`).join('');

    // Sub-Projects for Parking (proj-5)
    const subSection = document.getElementById('modal-subprojects-section');
    const subContainer = document.getElementById('modal-subprojects-container');
    if (project.subProjects && project.subProjects.length > 0) {
        subSection.style.display = 'block';
        subContainer.innerHTML = project.subProjects.map(sp => `
            <div class="subproject-item-card">
                <div class="subproject-thumb" onclick="openLightbox('${sp.image}', '${escapeHtml(sp.name)}')">
                    <img src="${sp.image}" alt="${sp.name}">
                    <div class="card-image-overlay"><span>확대</span></div>
                </div>
                <div class="subproject-info">
                    <div class="subproject-name">${sp.name}</div>
                    <div><b>사업비:</b> ${sp.budget} (${sp.capacity})</div>
                    <div><b>상태:</b> <span class="tag-badge badge-지속추진">${sp.status}</span></div>
                    <div><b>계획:</b> ${sp.plan}</div>
                </div>
            </div>
        `).join('');
    } else {
        subSection.style.display = 'none';
    }

    // Image
    const modalImg = document.getElementById('modal-img');
    modalImg.src = project.image;
    document.getElementById('modal-img-caption').textContent = project.imageCaption || `${project.title} 참고사진`;

    // Show Modal
    const modal = document.getElementById('detail-modal');
    modal.classList.add('active');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
}

function switchModalTab(tabName) {
    const infoTab = document.getElementById('modal-tab-content-info');
    const pdfTab = document.getElementById('modal-tab-content-pdf');
    const infoBtn = document.getElementById('tab-info-btn');
    const pdfBtn = document.getElementById('tab-pdf-btn');

    if (tabName === 'info') {
        infoTab.style.display = 'block';
        pdfTab.style.display = 'none';
        infoBtn.classList.add('active');
        pdfBtn.classList.remove('active');
    } else if (tabName === 'pdf') {
        infoTab.style.display = 'none';
        pdfTab.style.display = 'block';
        infoBtn.classList.remove('active');
        pdfBtn.classList.add('active');
    }
}

function closeDetailModal() {
    const modal = document.getElementById('detail-modal');
    modal.classList.remove('active');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
}

function openLightboxFromModal() {
    if (currentSelectedProject) {
        openLightbox(currentSelectedProject.image, `${currentSelectedProject.title} - ${currentSelectedProject.imageCaption || '참고사진'}`);
    }
}

// Lightbox Zoom & Pan State Variables
let currentZoom = 1.0;
let currentTranslateX = 0;
let currentTranslateY = 0;
let isDragging = false;
let startX = 0;
let startY = 0;

function updateZoomTransform() {
    const wrapper = document.getElementById('lightbox-img-wrapper');
    const badge = document.getElementById('zoom-level-badge');
    const lightbox = document.getElementById('lightbox-modal');
    if (wrapper) {
        wrapper.style.transform = `translate(${currentTranslateX}px, ${currentTranslateY}px) scale(${currentZoom})`;
    }
    if (badge) {
        badge.textContent = `${Math.round(currentZoom * 100)}%`;
    }
    if (lightbox) {
        if (Math.abs(currentZoom - 1.0) > 0.05) {
            lightbox.classList.add('is-zoomed');
        } else {
            lightbox.classList.remove('is-zoomed');
        }
    }
}

function zoomIn() {
    currentZoom = Math.min(currentZoom + 0.25, 4.0);
    updateZoomTransform();
}

function zoomOut() {
    currentZoom = Math.max(currentZoom - 0.25, 0.5);
    updateZoomTransform();
}

function resetZoom() {
    currentZoom = 1.0;
    currentTranslateX = 0;
    currentTranslateY = 0;
    updateZoomTransform();
}

function toggleNativeFullscreen() {
    const modal = document.getElementById('lightbox-modal');
    if (!document.fullscreenElement) {
        if (modal.requestFullscreen) {
            modal.requestFullscreen();
        } else if (modal.webkitRequestFullscreen) {
            modal.webkitRequestFullscreen();
        }
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        } else if (document.webkitExitFullscreen) {
            document.webkitExitFullscreen();
        }
    }
}

// Summary Slides Dataset (요약_1-1.jpg ~ 요약_8.jpg)
const SUMMARY_SLIDES = [
    { src: "요약/요약_1-1.jpg", title: "교통국 중점 추진사업 요약", caption: "사업 요약 (1/9 페이지)", label: "1페이지" },
    { src: "요약/요약_1-2.jpg", title: "교통국 중점 추진사업 요약", caption: "사업 요약 (2/9 페이지)", label: "2페이지" },
    { src: "요약/요약_2.jpg", title: "교통국 중점 추진사업 요약", caption: "사업 요약 (3/9 페이지)", label: "3페이지" },
    { src: "요약/요약_3.jpg", title: "교통국 중점 추진사업 요약", caption: "사업 요약 (4/9 페이지)", label: "4페이지" },
    { src: "요약/요약_4.jpg", title: "교통국 중점 추진사업 요약", caption: "사업 요약 (5/9 페이지)", label: "5페이지" },
    { src: "요약/요약_5.jpg", title: "교통국 중점 추진사업 요약", caption: "사업 요약 (6/9 페이지)", label: "6페이지" },
    { src: "요약/요약_6.jpg", title: "교통국 중점 추진사업 요약", caption: "사업 요약 (7/9 페이지)", label: "7페이지" },
    { src: "요약/요약_7.jpg", title: "교통국 중점 추진사업 요약", caption: "사업 요약 (8/9 페이지)", label: "8페이지" },
    { src: "요약/요약_8.jpg", title: "교통국 중점 추진사업 요약", caption: "사업 요약 (9/9 페이지)", label: "9페이지" }
];

let lightboxItemsList = [];
let lightboxPageIndex = 0;
let lightboxBaseTitle = "";

function openGalleryLightbox(items, startIndex = 0, baseTitle = "") {
    lightboxItemsList = items || [];
    lightboxPageIndex = Math.min(Math.max(startIndex, 0), Math.max(0, lightboxItemsList.length - 1));
    lightboxBaseTitle = baseTitle || "";

    const lightbox = document.getElementById('lightbox-modal');
    const wrap = document.getElementById('lightbox-bottom-controls-wrap');

    if (wrap) wrap.classList.remove('hover-active');

    if (lightbox) {
        lightbox.classList.add('active');
        lightbox.classList.add('is-fullscreen-active');
        lightbox.setAttribute('aria-hidden', 'false');

        if (!document.fullscreenElement) {
            if (lightbox.requestFullscreen) {
                lightbox.requestFullscreen().catch(() => {});
            } else if (lightbox.webkitRequestFullscreen) {
                lightbox.webkitRequestFullscreen();
            }
        }
    }
    document.body.style.overflow = 'hidden';

    renderCurrentLightboxSlide();
}

function openSummarySlidesModal(startIndex = 0) {
    openGalleryLightbox(SUMMARY_SLIDES, startIndex, "교통국 중점사업 요약");
}

function openLightbox(imgSrc, caption, pagesList = null, pageIndex = 0, baseTitle = "") {
    if (pagesList && Array.isArray(pagesList) && pagesList.length > 0) {
        const items = pagesList.map((pg, idx) => ({
            src: `assets/pdf_pages/page_${pg}.png`,
            title: baseTitle || caption || '원본 PDF',
            caption: `${baseTitle || caption} - 원본 PDF 보고서 (P.${pg}) (${idx + 1}/${pagesList.length})`,
            label: `P.${pg}`
        }));
        openGalleryLightbox(items, pageIndex, baseTitle || caption);
    } else {
        const items = [{
            src: imgSrc,
            title: baseTitle || caption || '참고사진',
            caption: caption || '참고사진',
            label: '1'
        }];
        openGalleryLightbox(items, 0, baseTitle || caption);
    }
}

function renderCurrentLightboxSlide() {
    if (!lightboxItemsList || lightboxItemsList.length === 0) return;

    const currentItem = lightboxItemsList[lightboxPageIndex];
    const imgSrc = typeof currentItem === 'string' ? currentItem : currentItem.src;
    const captionText = typeof currentItem === 'object' && currentItem.caption ? currentItem.caption : `${lightboxBaseTitle} (${lightboxPageIndex + 1}/${lightboxItemsList.length})`;
    const titleText = typeof currentItem === 'object' && currentItem.title ? currentItem.title : (lightboxBaseTitle || '확대보기');

    const imgEl = document.getElementById('lightbox-img');
    const captionEl = document.getElementById('lightbox-caption');
    const downloadLink = document.getElementById('lightbox-download-link');
    const titleEl = document.getElementById('lightbox-title');
    const prevBtn = document.getElementById('lightbox-prev-btn');
    const nextBtn = document.getElementById('lightbox-next-btn');
    const paginationDots = document.getElementById('lightbox-pagination-dots');

    imgEl.src = imgSrc;
    captionEl.textContent = captionText;
    titleEl.textContent = titleText.includes('(') ? titleText : `${titleText} (${lightboxPageIndex + 1}/${lightboxItemsList.length})`;
    downloadLink.href = imgSrc;
    downloadLink.setAttribute('download', `${titleText}_slide_${lightboxPageIndex + 1}.png`.replace(/[\/\?%*:|"<>]/g, '_'));

    if (lightboxItemsList.length > 1) {
        if (prevBtn) {
            prevBtn.style.display = 'flex';
            prevBtn.disabled = (lightboxPageIndex <= 0);
        }
        if (nextBtn) {
            nextBtn.style.display = 'flex';
            nextBtn.disabled = (lightboxPageIndex >= lightboxItemsList.length - 1);
        }

        if (paginationDots) {
            paginationDots.style.display = 'flex';
            paginationDots.innerHTML = lightboxItemsList.map((item, idx) => {
                const label = item.label || `슬라이드 ${idx + 1}`;
                const isActive = (idx === lightboxPageIndex) ? 'active' : '';
                return `<button type="button" class="lightbox-dot-pill ${isActive}" onclick="event.stopPropagation(); goToLightboxSlide(${idx});">${label}</button>`;
            }).join('');
        }
    } else {
        if (prevBtn) prevBtn.style.display = 'none';
        if (nextBtn) nextBtn.style.display = 'none';
        if (paginationDots) paginationDots.style.display = 'none';
    }

    resetZoom();
}

function goToLightboxSlide(index) {
    if (!lightboxItemsList || index < 0 || index >= lightboxItemsList.length) return;
    lightboxPageIndex = index;
    renderCurrentLightboxSlide();
}

function navigateLightboxPage(delta) {
    if (!lightboxItemsList || lightboxItemsList.length <= 1) return;
    const newIdx = lightboxPageIndex + delta;
    if (newIdx < 0 || newIdx >= lightboxItemsList.length) return;
    goToLightboxSlide(newIdx);
}

function closeLightbox() {
    const lightbox = document.getElementById('lightbox-modal');
    lightbox.classList.remove('active');
    lightbox.classList.remove('is-fullscreen-active');
    lightbox.setAttribute('aria-hidden', 'true');
    resetZoom();

    const wrap = document.getElementById('lightbox-bottom-controls-wrap');
    if (wrap) wrap.classList.remove('hover-active');

    if (document.fullscreenElement) {
        if (document.exitFullscreen) document.exitFullscreen();
    }

    const detailModal = document.getElementById('detail-modal');
    if (!detailModal || !detailModal.classList.contains('active')) {
        document.body.style.overflow = '';
    }
}

function initLightboxInteractions() {
    const stage = document.getElementById('lightbox-stage');
    if (!stage) return;

    // Wheel zoom
    stage.addEventListener('wheel', (e) => {
        e.preventDefault();
        const delta = e.deltaY < 0 ? 0.15 : -0.15;
        currentZoom = Math.min(Math.max(currentZoom + delta, 0.5), 4.0);
        updateZoomTransform();
    }, { passive: false });

    // Drag to pan
    stage.addEventListener('mousedown', (e) => {
        if (e.target.closest('.lightbox-toolbar') || e.target.closest('.lightbox-fullscreen-bar') || e.target.closest('.lightbox-nav-btn') || e.target.closest('.lightbox-pagination-dots')) return;
        isDragging = true;
        startX = e.clientX - currentTranslateX;
        startY = e.clientY - currentTranslateY;
        stage.classList.add('dragging');
    });

    window.addEventListener('mousemove', (e) => {
        if (!isDragging) return;
        currentTranslateX = e.clientX - startX;
        currentTranslateY = e.clientY - startY;
        updateZoomTransform();
    });

    window.addEventListener('mouseup', () => {
        if (isDragging) {
            isDragging = false;
            stage.classList.remove('dragging');
        }
    });

    // Double click toggle zoom
    stage.addEventListener('dblclick', (e) => {
        if (e.target.closest('.lightbox-toolbar') || e.target.closest('.lightbox-fullscreen-bar') || e.target.closest('.lightbox-nav-btn') || e.target.closest('.lightbox-pagination-dots')) return;
        if (currentZoom === 1.0) {
            currentZoom = 2.0;
        } else {
            resetZoom();
            return;
        }
        updateZoomTransform();
    });

    const lightboxModal = document.getElementById('lightbox-modal');
    const bottomControlsWrap = document.getElementById('lightbox-bottom-controls-wrap');

    if (lightboxModal && bottomControlsWrap) {
        window.addEventListener('mousemove', (e) => {
            if (!lightboxModal.classList.contains('active')) return;
            // Check if mouse is in the bottom area (bottom 140px of screen)
            const isBottomArea = e.clientY >= (window.innerHeight - 140);
            if (isBottomArea) {
                bottomControlsWrap.classList.add('hover-active');
            } else {
                bottomControlsWrap.classList.remove('hover-active');
            }
        });

        document.addEventListener('fullscreenchange', () => {
            if (document.fullscreenElement) {
                lightboxModal.classList.add('is-fullscreen-active');
            } else {
                lightboxModal.classList.remove('is-fullscreen-active');
            }
            bottomControlsWrap.classList.remove('hover-active');
        });
    }

    // Keyboard navigation (Arrow keys & Escape)
    window.addEventListener('keydown', (e) => {
        const lightbox = document.getElementById('lightbox-modal');
        if (!lightbox || !lightbox.classList.contains('active')) return;

        if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
            e.preventDefault();
            navigateLightboxPage(-1);
        } else if (e.key === 'ArrowRight' || e.key === 'PageDown') {
            e.preventDefault();
            navigateLightboxPage(1);
        } else if (e.key === 'Escape') {
            e.preventDefault();
            closeLightbox();
        }
    });

function openPdfPage(pageNum, title, pagesList = null, pageIndex = 0) {
    const pageImgSrc = `assets/pdf_pages/page_${pageNum}.png`;
    const totalCount = (pagesList && pagesList.length > 1) ? ` (${pageIndex + 1}/${pagesList.length})` : '';
    const caption = title ? `${title} - 원본 PDF 보고서 (P.${pageNum})${totalCount}` : `원본 PDF 보고서 (P.${pageNum})${totalCount}`;
    openLightbox(pageImgSrc, caption, pagesList, pageIndex, title);
}

function openProjectPdfInLightbox(projId, startPageIndex = 0) {
    const project = projectsData.find(p => p.id === projId);
    if (!project) return;
    const pages = project.pdfPages || [project.pdfPage || 1];
    const pageIndex = Math.min(Math.max(startPageIndex, 0), pages.length - 1);
    openLightbox('', project.title, pages, pageIndex, project.title);
}

function openCurrentPdfPageInLightbox() {
    if (currentSelectedProject) {
        openProjectPdfInLightbox(currentSelectedProject.id, 0);
    }
}

function openPdfPagesForProject(projId) {
    openDetailModal(projId);
    switchModalTab('pdf');
}

function openRoadMapModal() {
    openLightbox('road_map/road_map.jpg', '교통국 중점 도로 사업 지도');
}

    window.zoomIn = zoomIn;
    window.zoomOut = zoomOut;
    window.resetZoom = resetZoom;
    window.toggleNativeFullscreen = toggleNativeFullscreen;
    window.openLightbox = openLightbox;
    window.openGalleryLightbox = openGalleryLightbox;
    window.openSummarySlidesModal = openSummarySlidesModal;
    window.openRoadMapModal = openRoadMapModal;
    window.goToLightboxSlide = goToLightboxSlide;
    window.closeLightbox = closeLightbox;
    window.navigateLightboxPage = navigateLightboxPage;
    window.openLightboxFromModal = openLightboxFromModal;
    window.openPdfPage = openPdfPage;
    window.openProjectPdfInLightbox = openProjectPdfInLightbox;
    window.openCurrentPdfPageInLightbox = openCurrentPdfPageInLightbox;
    window.openPdfPagesForProject = openPdfPagesForProject;
}

// Filter Event Listeners
function initEventListeners() {
    const searchInput = document.getElementById('search-input');
    const clearBtn = document.getElementById('clear-search-btn');

    searchInput.addEventListener('input', (e) => {
        currentSearch = e.target.value;
        clearBtn.style.display = currentSearch ? 'block' : 'none';
        renderProjects();
    });

    clearBtn.addEventListener('click', () => {
        searchInput.value = '';
        currentSearch = '';
        clearBtn.style.display = 'none';
        renderProjects();
    });

    // Dept Pills
    const deptPills = document.querySelectorAll('#dept-pills .pill-btn');
    deptPills.forEach(pill => {
        pill.addEventListener('click', () => {
            deptPills.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
            activeDept = pill.dataset.dept;
            renderProjects();
        });
    });

    // Tag Pills
    const tagPills = document.querySelectorAll('#tag-pills .pill-btn');
    tagPills.forEach(pill => {
        pill.addEventListener('click', () => {
            tagPills.forEach(p => p.classList.remove('active'));
            pill.classList.add('active');
            activeTag = pill.dataset.tag;
            renderProjects();
        });
    });

    // Close Modals on ESC Key or Backdrop Click
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            closeLightbox();
            closeDetailModal();
        }
    });

    document.getElementById('detail-modal').addEventListener('click', (e) => {
        if (e.target.id === 'detail-modal') closeDetailModal();
    });

    document.getElementById('lightbox-modal').addEventListener('click', (e) => {
        if (e.target.id === 'lightbox-modal') closeLightbox();
    });

    // Theme Toggle
    document.getElementById('theme-toggle-btn').addEventListener('click', toggleTheme);
}

function filterByDept(deptName) {
    activeDept = deptName;
    const deptPills = document.querySelectorAll('#dept-pills .pill-btn');
    deptPills.forEach(pill => {
        if (pill.dataset.dept === deptName) {
            pill.classList.add('active');
        } else {
            pill.classList.remove('active');
        }
    });
    renderProjects();
    document.getElementById('cards-section').scrollIntoView({ behavior: 'smooth' });
}

function resetFilters() {
    activeDept = 'all';
    activeTag = 'all';
    currentSearch = '';

    document.getElementById('search-input').value = '';
    document.getElementById('clear-search-btn').style.display = 'none';

    document.querySelectorAll('#dept-pills .pill-btn').forEach(p => {
        p.classList.toggle('active', p.dataset.dept === 'all');
    });
    document.querySelectorAll('#tag-pills .pill-btn').forEach(p => {
        p.classList.toggle('active', p.dataset.tag === 'all');
    });

    renderProjects();
}

// Dark Mode Theme Handler
function initTheme() {
    const savedTheme = localStorage.getItem('transport_dashboard_theme') || 'light';
    document.body.className = `theme-${savedTheme}`;
}

function toggleTheme() {
    const currentTheme = document.body.classList.contains('theme-dark') ? 'dark' : 'light';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.body.className = `theme-${newTheme}`;
    localStorage.setItem('transport_dashboard_theme', newTheme);
}

// Utility
function escapeHtml(str) {
    if (!str) return '';
    return str.replace(/'/g, "\'").replace(/"/g, '&quot;');
}

function renderAchievementItems(achievements) {
    if (!achievements || achievements.length === 0) return '';
    return achievements.map(item => {
        if (typeof item === 'object' && item !== null) {
            const parentText = item.text || item.title || '';
            const childrenHTML = (item.children || item.items || []).map(child => `<li class="sub-item">${child}</li>`).join('');
            return `<li class="parent-item">
                <div class="parent-text">${parentText}</div>
                ${childrenHTML ? `<ul class="sub-detail-list">${childrenHTML}</ul>` : ''}
            </li>`;
        } else if (typeof item === 'string') {
            if (item.startsWith('○ ') || item.startsWith('O ')) {
                return `<li class="parent-item"><div class="parent-text">${item.replace(/^[○O]\s*/, '')}</div></li>`;
            } else if (item.startsWith('  - ') || item.startsWith('- ')) {
                return `<li class="sub-item">${item.replace(/^(\s*-\s*)/, '')}</li>`;
            }
            return `<li>${item}</li>`;
        }
        return `<li>${item}</li>`;
    }).join('');
}
