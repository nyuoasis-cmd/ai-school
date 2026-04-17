#!/usr/bin/env python3
"""
AI교육 강의계획서 4차시/6차시/8차시 HWPX 생성기
기존 HWPX를 base로 section0.xml만 교체하는 방식
"""
import zipfile, copy, io, os, re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_HWPX = os.path.join(SCRIPT_DIR, "AI교육_강의계획서_티처메이트.hwpx")
OUTPUT_DIR = SCRIPT_DIR

# ============================================================
# 강의 커리큘럼 데이터 (티처메이트 도구 기반)
# ============================================================
# 도구: Sprint(기획) / Block Design(디자인) / App Maker(앱 생성)

LESSONS_8 = [
    {
        "chapter": "1차시",
        "topic": "AI와 만나다",
        "content": [
            "AI의 역사와 발전 과정",
            "생성형 AI란?\n(텍스트·이미지·코드 생성)",
            "일상 속 AI 활용 사례",
        ],
        "practice": [
            "생활 속 AI 찾기 활동",
            "모둠별 AI 서비스 조사",
            "AI 서바이벌 퀴즈(티처메이트)",
            "ChatGPT/Claude 첫 대화 체험",
        ],
    },
    {
        "chapter": "2차시",
        "topic": "불편함을\n아이디어로",
        "content": [
            "'불편함'이 곧 기회:\n문제 발견의 중요성",
            "사용자 페르소나 개념",
            "AI 페르소나 인터뷰 기법",
        ],
        "practice": [
            "주변 불편함 브레인스토밍\n(Sprint: 문제 발견)",
            "AI 페르소나 인터뷰 실습",
            "AI에게 사용자 역할 부여 후\n질문하기",
        ],
    },
    {
        "chapter": "3차시",
        "topic": "핵심 기능\n선정",
        "content": [
            "MVP(최소 기능 제품)란?",
            "기능 우선순위 정하기\n(Must / Should / Could)",
            "좋은 앱의 조건",
        ],
        "practice": [
            "기능 브레인스토밍\n(Sprint: 앱 주문서 작성)",
            "Must/Should/Could 분류",
            "앱 한 줄 소개 작성\n\"○○를 위한 ○○ 앱\"",
        ],
    },
    {
        "chapter": "4차시",
        "topic": "화면 스케치 &\nAI 분석",
        "content": [
            "화면 구성도(와이어프레임)란?",
            "스케치 기본 요소:\n헤더, 버튼, 입력창, 리스트",
            "AI 스케치 분석 활용법",
        ],
        "practice": [
            "화면 스케치 실습\n(Sprint: 화면 디자인)",
            "AI 스케치 분석 실습",
            "프롬프트 → 스케치 분석서",
        ],
    },
    {
        "chapter": "5차시",
        "topic": "UI 디자인\n기초",
        "content": [
            "UI/UX 디자인 기본 용어\n(여백, 정렬, 계층 등)",
            "디자인 원리 4가지:\n대비, 반복, 정렬, 근접성",
            "색상 코드(HEX) 기초",
        ],
        "practice": [
            "디자인 용어 카드 학습\n(Block Design: 배우기)",
            "따라하기 실습\n(Block Design: 실습)",
            "디자인 챌린지\n(Block Design: 챌린지)",
        ],
    },
    {
        "chapter": "6차시",
        "topic": "UI 디자인\n실전",
        "content": [
            "좋은 UI의 3원칙:\n일관성, 가시성, 피드백",
            "색상 조합과 타이포그래피",
            "벤치마킹 결과 활용법",
        ],
        "practice": [
            "자유 디자인 제작\n(Block Design: 만들기)",
            "우리 앱 디자인 방향 결정",
            "디자인 갤러리 공유 및 피드백",
        ],
    },
    {
        "chapter": "7차시",
        "topic": "바이브코딩\n입문",
        "content": [
            "바이브코딩이란?\n(프롬프트로 앱 만들기)",
            "프로젝트 생성 및\n프롬프트 입력법",
            "실시간 미리보기와 수정",
        ],
        "practice": [
            "앱 카테고리 선택 및\n스타일 설정 (App Maker)",
            "첫 프롬프트 입력 및 빌드",
            "첫 결과물 점검 및\n화면별 체크",
        ],
    },
    {
        "chapter": "8차시",
        "topic": "앱 완성 &\n발표",
        "content": [
            "버튼 링크 연결과\n화면 간 이동",
            "반복 수정의 요령:\n구체적 피드백 작성법",
            "발표(피칭) 구성법",
        ],
        "practice": [
            "화면 수정 및 기능 검수\n(App Maker: 수정 프롬프트)",
            "교차 테스트 및 피드백 교환",
            "3분 앱 피칭 발표\n+ 학급 투표",
        ],
    },
]

LESSONS_6 = [
    {
        "chapter": "1차시",
        "topic": "AI와 만나다",
        "content": [
            "생성형 AI란?\n(텍스트·이미지·코드 생성)",
            "일상 속 AI 활용 사례",
            "AI의 강점과 한계",
        ],
        "practice": [
            "AI 서바이벌 퀴즈(티처메이트)",
            "ChatGPT/Claude 첫 대화 체험",
            "AI 강점/한계 발견 카드 작성",
        ],
    },
    {
        "chapter": "2차시",
        "topic": "문제 발견 &\n앱 기획",
        "content": [
            "'불편함'이 곧 기회:\n문제 발견의 중요성",
            "MVP(최소 기능 제품)란?",
            "기능 우선순위 정하기\n(Must / Should / Could)",
        ],
        "practice": [
            "주변 불편함 브레인스토밍\n(Sprint: 문제 발견)",
            "앱 주문서 작성\n(Sprint: 앱 주문)",
            "앱 한 줄 소개 작성\n\"○○를 위한 ○○ 앱\"",
        ],
    },
    {
        "chapter": "3차시",
        "topic": "화면 스케치 &\nUI 기초",
        "content": [
            "화면 구성도(와이어프레임)란?",
            "UI 디자인 기본 용어\n(여백, 정렬, 계층)",
            "디자인 원리 4가지:\n대비, 반복, 정렬, 근접성",
        ],
        "practice": [
            "화면 스케치 실습\n(Sprint: 화면 디자인)",
            "디자인 용어 카드 학습\n(Block Design: 배우기)",
            "따라하기 실습\n(Block Design: 실습)",
        ],
    },
    {
        "chapter": "4차시",
        "topic": "UI 디자인\n실전",
        "content": [
            "좋은 UI의 3원칙:\n일관성, 가시성, 피드백",
            "색상 조합과 타이포그래피",
            "벤치마킹과 디자인 참고",
        ],
        "practice": [
            "디자인 챌린지\n(Block Design: 챌린지)",
            "자유 디자인 제작\n(Block Design: 만들기)",
            "디자인 갤러리 공유 및 피드백",
        ],
    },
    {
        "chapter": "5차시",
        "topic": "바이브코딩으로\n앱 만들기",
        "content": [
            "바이브코딩이란?\n(프롬프트로 앱 만들기)",
            "프로젝트 생성 및\n프롬프트 입력법",
            "실시간 미리보기와\n수정 프롬프트",
        ],
        "practice": [
            "앱 카테고리 선택 및\n스타일 설정 (App Maker)",
            "첫 프롬프트 입력 및 빌드",
            "화면 수정 실습\n(수정 프롬프트 작성)",
        ],
    },
    {
        "chapter": "6차시",
        "topic": "앱 완성 &\n발표",
        "content": [
            "기능 검수(QA)란?\n체크리스트 작성법",
            "반복 수정의 요령:\n구체적 피드백 작성법",
            "발표(피칭) 구성법",
        ],
        "practice": [
            "기능 검수 및 수정\n(App Maker: 수정 프롬프트)",
            "교차 테스트 및 피드백 교환",
            "3분 앱 피칭 발표\n+ 학급 투표",
        ],
    },
]

LESSONS_4 = [
    {
        "chapter": "1차시",
        "topic": "AI 이해 &\n문제 발견",
        "content": [
            "생성형 AI란?\n(텍스트·이미지·코드 생성)",
            "'불편함'이 곧 기회:\n문제 발견의 중요성",
            "MVP와 기능 우선순위",
        ],
        "practice": [
            "AI 서바이벌 퀴즈(티처메이트)",
            "주변 불편함 브레인스토밍\n(Sprint: 문제 발견)",
            "앱 주문서 작성\n(Sprint: 앱 주문)",
        ],
    },
    {
        "chapter": "2차시",
        "topic": "화면 설계 &\nUI 디자인",
        "content": [
            "화면 구성도(와이어프레임)란?",
            "UI 디자인 기본 용어와 원리",
            "좋은 UI의 3원칙:\n일관성, 가시성, 피드백",
        ],
        "practice": [
            "화면 스케치 실습\n(Sprint: 화면 디자인)",
            "디자인 용어 카드 학습\n(Block Design: 배우기)",
            "따라하기 + 자유 디자인\n(Block Design: 실습/만들기)",
        ],
    },
    {
        "chapter": "3차시",
        "topic": "바이브코딩으로\n앱 만들기",
        "content": [
            "바이브코딩이란?\n(프롬프트로 앱 만들기)",
            "프로젝트 생성 및\n프롬프트 입력법",
            "실시간 미리보기와\n수정 프롬프트",
        ],
        "practice": [
            "앱 카테고리 선택 및\n스타일 설정 (App Maker)",
            "첫 프롬프트 입력 및 빌드",
            "화면 수정 및 기능 추가",
        ],
    },
    {
        "chapter": "4차시",
        "topic": "앱 완성 &\n발표",
        "content": [
            "기능 검수(QA) 체크리스트",
            "반복 수정의 요령:\n구체적 피드백 작성법",
            "발표(피칭) 구성법",
        ],
        "practice": [
            "기능 검수 및 최종 수정\n(App Maker: 수정 프롬프트)",
            "교차 테스트 및 피드백 교환",
            "3분 앱 피칭 발표\n+ 학급 투표",
        ],
    },
]

# ============================================================
# 강의목표 / 기대효과 / 산출물 (차시별 조정)
# ============================================================
INFO = {
    4: {
        "title": "AI 동아리 교육 (4차시)",
        "time": "4차시 (45분×4 = 180분)",
        "outputs": "문제정의서, 앱 주문서, UI 디자인, 앱 프로토타입",
        "objective": "AI의 기본 개념을 이해하고, 사용자 문제를 발견하여 AI와 협업하는 바이브코딩으로 앱을 기획·디자인·개발하는 핵심 과정을 경험한다.",
        "effects": [
            "AI의 원리와 활용법을 이해하여 디지털 리터러시를 향상한다.",
            "사용자 관점에서 문제를 발견하고 해결책을 기획하는 문제 해결 역량을 기른다.",
            "바이브코딩을 통해 비전공자도 아이디어를 앱으로 구현할 수 있다는 자신감을 갖는다.",
            "팀 협업과 발표를 통해 소통 역량을 강화한다.",
        ],
    },
    6: {
        "title": "AI 동아리 교육 (6차시)",
        "time": "6차시 (45분×6 = 270분)",
        "outputs": "문제정의서, 앱 주문서, 화면 스케치, UI 디자인, 앱 프로토타입",
        "objective": "AI의 기본 개념을 이해하고, 사용자 문제를 발견·정의하여 AI와 협업하는 바이브코딩으로 앱을 기획·디자인·개발하는 전 과정을 경험한다.",
        "effects": [
            "AI의 원리와 활용법을 이해하여 디지털 리터러시를 향상한다.",
            "사용자 관점에서 문제를 발견하고 해결책을 기획하는 문제 해결 역량을 기른다.",
            "바이브코딩을 통해 비전공자도 아이디어를 앱으로 구현할 수 있다는 자신감을 갖는다.",
            "팀 협업, 피드백, 발표를 통해 소통 및 협력 역량을 강화한다.",
        ],
    },
    8: {
        "title": "AI 동아리 교육 (8차시)",
        "time": "8차시 (45분×8 = 360분)",
        "outputs": "문제정의서, 앱 주문서, 화면 스케치, UI 디자인, 앱 프로토타입, 발표자료",
        "objective": "AI의 기본 개념을 이해하고, 사용자 문제를 발견·정의하여 AI와 협업하는 바이브코딩으로 앱을 기획·개발·배포하는 전 과정을 경험한다.",
        "effects": [
            "AI의 원리와 활용법을 이해하여 디지털 리터러시를 향상한다.",
            "사용자 관점에서 문제를 발견하고 해결책을 기획하는 문제 해결 역량을 기른다.",
            "바이브코딩을 통해 비전공자도 아이디어를 앱으로 구현할 수 있다는 자신감을 갖는다.",
            "팀 협업, 피드백, 발표를 통해 소통 및 협력 역량을 강화한다.",
        ],
    },
}

# ============================================================
# XML Builder helpers
# ============================================================

NS = 'xmlns:ha="http://www.hancom.co.kr/hwpml/2011/app" xmlns:hp="http://www.hancom.co.kr/hwpml/2011/paragraph" xmlns:hp10="http://www.hancom.co.kr/hwpml/2016/paragraph" xmlns:hs="http://www.hancom.co.kr/hwpml/2011/section" xmlns:hc="http://www.hancom.co.kr/hwpml/2011/core" xmlns:hh="http://www.hancom.co.kr/hwpml/2011/head" xmlns:hhs="http://www.hancom.co.kr/hwpml/2011/history" xmlns:hm="http://www.hancom.co.kr/hwpml/2011/master-page" xmlns:hpf="http://www.hancom.co.kr/schema/2011/hpf" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf/" xmlns:ooxmlchart="http://www.hancom.co.kr/hwpml/2016/ooxmlchart" xmlns:epub="http://www.idpf.org/2007/ops" xmlns:config="urn:oasis:names:tc:opendocument:xmlns:config:1.0"'


def lineseg(vertpos=0, vertsize=1000, textheight=1000, baseline=850, spacing=300, horzsize=13636, flags=393216):
    return f'<hp:lineseg textpos="0" vertpos="{vertpos}" vertsize="{vertsize}" textheight="{textheight}" baseline="{baseline}" spacing="{spacing}" horzpos="0" horzsize="{horzsize}" flags="{flags}"/>'


def xml_escape(text):
    """Escape XML special characters"""
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace('"', "&quot;")
    return text


def make_text_para(text, paraPrIDRef="29", styleIDRef="23", charPrIDRef="16", horzsize=13636):
    """Create a paragraph with text, handling lineBreak for \n"""
    # Handle newlines
    if "\n" in text:
        parts = text.split("\n")
        inner = '<hp:lineBreak/>'.join(xml_escape(p) for p in parts)
    else:
        inner = xml_escape(text)

    return (
        f'<hp:p id="0" paraPrIDRef="{paraPrIDRef}" styleIDRef="{styleIDRef}" pageBreak="0" columnBreak="0" merged="0">'
        f'<hp:run charPrIDRef="{charPrIDRef}"><hp:t>{inner}</hp:t></hp:run>'
        f'<hp:linesegarray>{lineseg(horzsize=horzsize)}</hp:linesegarray>'
        f'</hp:p>'
    )


def make_cell(col_addr, row_addr, col_span, row_span, width, height, paras_xml, border_fill="3", vert_align="CENTER"):
    return (
        f'<hp:tc name="" header="0" hasMargin="0" protect="0" editable="0" dirty="0" borderFillIDRef="{border_fill}">'
        f'<hp:subList id="" textDirection="HORIZONTAL" lineWrap="BREAK" vertAlign="{vert_align}" '
        f'linkListIDRef="0" linkListNextIDRef="0" textWidth="0" textHeight="0" hasTextRef="0" hasNumRef="0">'
        f'{paras_xml}'
        f'</hp:subList>'
        f'<hp:cellAddr colAddr="{col_addr}" rowAddr="{row_addr}"/>'
        f'<hp:cellSpan colSpan="{col_span}" rowSpan="{row_span}"/>'
        f'<hp:cellSz width="{width}" height="{height}"/>'
        f'<hp:cellMargin left="510" right="510" top="283" bottom="283"/>'
        f'</hp:tc>'
    )


def make_lesson_row(lesson, row_idx):
    """Build a single lesson <hp:tr>"""
    row_height = 7383  # Same as original

    # Cell 1: 차시 (col 0, span 1)
    chapter_para = (
        f'<hp:p id="0" paraPrIDRef="28" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">'
        f'<hp:run charPrIDRef="11"><hp:t>{xml_escape(lesson["chapter"])}</hp:t></hp:run>'
        f'<hp:linesegarray>{lineseg(vertsize=1200, textheight=1200, baseline=1020, spacing=360, horzsize=3868)}</hp:linesegarray>'
        f'</hp:p>'
    )
    cell_chapter = make_cell(0, row_idx, 1, 1, 4891, row_height, chapter_para, border_fill="4")

    # Cell 2: 학습주제 (col 1, span 2)
    topic_text = lesson["topic"]
    if "\n" in topic_text:
        parts = topic_text.split("\n")
        inner = '<hp:lineBreak/>'.join(xml_escape(p) for p in parts)
    else:
        inner = xml_escape(topic_text)
    topic_para = (
        f'<hp:p id="0" paraPrIDRef="30" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">'
        f'<hp:run charPrIDRef="17"><hp:t>{inner}</hp:t></hp:run>'
        f'<hp:linesegarray>{lineseg(vertsize=1200, textheight=1200, baseline=1020, spacing=720, horzsize=10660)}</hp:linesegarray>'
        f'</hp:p>'
    )
    cell_topic = make_cell(1, row_idx, 2, 1, 11683, row_height, topic_para)

    # Cell 3: 학습내용 (col 3, span 3)
    content_paras = ""
    for item in lesson["content"]:
        content_paras += make_text_para(item, horzsize=13636)
    cell_content = make_cell(3, row_idx, 3, 1, 14659, row_height, content_paras)

    # Cell 4: 실습내용 (col 6, span 3)
    practice_paras = ""
    for item in lesson["practice"]:
        practice_paras += make_text_para(item, horzsize=15613)
    cell_practice = make_cell(6, row_idx, 3, 1, 16636, row_height, practice_paras)

    return f'<hp:tr>{cell_chapter}{cell_topic}{cell_content}{cell_practice}</hp:tr>'


def make_info_rows(info, num_lessons):
    """Build the info rows (rows 0-6) of the table"""
    rows = []

    # Row 0: 강의명
    rows.append('<hp:tr>' +
        make_cell(0, 0, 2, 1, 4891+6792, 1701,
            f'<hp:p id="0" paraPrIDRef="28" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="11"><hp:t>강의명</hp:t></hp:run><hp:linesegarray>{lineseg(vertsize=1200, textheight=1200, baseline=1020, spacing=360, horzsize=10660)}</hp:linesegarray></hp:p>',
            border_fill="4") +
        make_cell(2, 0, 7, 1, 11683+14659+16636-11683, 1701,
            f'<hp:p id="0" paraPrIDRef="28" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="15"><hp:t>{info["title"]}</hp:t></hp:run><hp:linesegarray>{lineseg(vertsize=1200, textheight=1200, baseline=1020, spacing=360, horzsize=36295)}</hp:linesegarray></hp:p>',
            border_fill="3") +
    '</hp:tr>')

    # Row 1: 강사명 / 강의 대상
    rows.append('<hp:tr>' +
        make_cell(0, 1, 2, 1, 4891+6792-6792, 1701,
            f'<hp:p id="0" paraPrIDRef="28" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="11"><hp:t>강사명 </hp:t></hp:run><hp:linesegarray>{lineseg(vertsize=1200, textheight=1200, baseline=1020, spacing=360, horzsize=3868)}</hp:linesegarray></hp:p>',
            border_fill="4") +
        make_cell(2, 1, 2, 1, 11683, 1701,
            f'<hp:p id="0" paraPrIDRef="21" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="0"><hp:t>-</hp:t></hp:run><hp:linesegarray>{lineseg(horzsize=10660)}</hp:linesegarray></hp:p>',
            border_fill="3") +
        make_cell(4, 1, 3, 1, 14659, 1701,
            f'<hp:p id="0" paraPrIDRef="28" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="11"><hp:t>강의 대상</hp:t></hp:run><hp:linesegarray>{lineseg(vertsize=1200, textheight=1200, baseline=1020, spacing=360, horzsize=13636)}</hp:linesegarray></hp:p>',
            border_fill="4") +
        make_cell(7, 1, 2, 1, 16636-14659+14659-11683, 1701,
            f'<hp:p id="0" paraPrIDRef="21" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="0"><hp:t>-</hp:t></hp:run><hp:linesegarray>{lineseg(horzsize=15613)}</hp:linesegarray></hp:p>',
            border_fill="3") +
    '</hp:tr>')

    # Row 2: 강의 일시
    rows.append('<hp:tr>' +
        make_cell(0, 2, 2, 1, 4891+6792-6792, 1701,
            f'<hp:p id="0" paraPrIDRef="28" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="11"><hp:t>강의 일시 </hp:t></hp:run><hp:linesegarray>{lineseg(vertsize=1200, textheight=1200, baseline=1020, spacing=360, horzsize=3868)}</hp:linesegarray></hp:p>',
            border_fill="4") +
        make_cell(2, 2, 7, 1, 11683+14659+16636-11683, 1701,
            f'<hp:p id="0" paraPrIDRef="21" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="0"><hp:t>-</hp:t></hp:run><hp:linesegarray>{lineseg(horzsize=36295)}</hp:linesegarray></hp:p>',
            border_fill="3") +
    '</hp:tr>')

    # Row 3: 교육 도구 / 강의 시간
    rows.append('<hp:tr>' +
        make_cell(0, 3, 2, 1, 4891+6792-6792, 1701,
            f'<hp:p id="0" paraPrIDRef="28" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="11"><hp:t>교육 도구</hp:t></hp:run><hp:linesegarray>{lineseg(vertsize=1200, textheight=1200, baseline=1020, spacing=360, horzsize=3868)}</hp:linesegarray></hp:p>',
            border_fill="4") +
        make_cell(2, 3, 3, 1, 11683+14659-11683, 1701,
            f'<hp:p id="0" paraPrIDRef="21" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="0"><hp:t>티처메이트(강사)</hp:t></hp:run><hp:linesegarray>{lineseg(horzsize=13636)}</hp:linesegarray></hp:p>',
            border_fill="3") +
        make_cell(5, 3, 3, 1, 14659, 1701,
            f'<hp:p id="0" paraPrIDRef="28" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="11"><hp:t>강의 시간</hp:t></hp:run><hp:linesegarray>{lineseg(vertsize=1200, textheight=1200, baseline=1020, spacing=360, horzsize=13636)}</hp:linesegarray></hp:p>',
            border_fill="4") +
        make_cell(8, 3, 1, 1, 16636-14659, 1701,
            f'<hp:p id="0" paraPrIDRef="21" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="0"><hp:t>{info["time"]}</hp:t></hp:run><hp:linesegarray>{lineseg(horzsize=15613)}</hp:linesegarray></hp:p>',
            border_fill="3") +
    '</hp:tr>')

    # Row 4: 산출물
    rows.append('<hp:tr>' +
        make_cell(0, 4, 2, 1, 4891+6792-6792, 1701,
            f'<hp:p id="0" paraPrIDRef="28" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="11"><hp:t>산출물</hp:t></hp:run><hp:linesegarray>{lineseg(vertsize=1200, textheight=1200, baseline=1020, spacing=360, horzsize=3868)}</hp:linesegarray></hp:p>',
            border_fill="4") +
        make_cell(2, 4, 7, 1, 11683+14659+16636-11683, 1701,
            f'<hp:p id="0" paraPrIDRef="21" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="0"><hp:t>{info["outputs"]}</hp:t></hp:run><hp:linesegarray>{lineseg(horzsize=36295)}</hp:linesegarray></hp:p>',
            border_fill="3") +
    '</hp:tr>')

    # Row 5: 강의목표
    rows.append('<hp:tr>' +
        make_cell(0, 5, 2, 1, 4891+6792-6792, 2400,
            f'<hp:p id="0" paraPrIDRef="28" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="11"><hp:t>강의목표</hp:t></hp:run><hp:linesegarray>{lineseg(vertsize=1200, textheight=1200, baseline=1020, spacing=360, horzsize=3868)}</hp:linesegarray></hp:p>',
            border_fill="4") +
        make_cell(2, 5, 7, 1, 11683+14659+16636-11683, 2400,
            f'<hp:p id="0" paraPrIDRef="29" styleIDRef="23" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="16"><hp:t>{info["objective"]}</hp:t></hp:run><hp:linesegarray>{lineseg(horzsize=36295)}</hp:linesegarray></hp:p>',
            border_fill="3") +
    '</hp:tr>')

    # Row 6: 기대효과
    effects_paras = ""
    for eff in info["effects"]:
        effects_paras += make_text_para(eff, horzsize=36295)
    rows.append('<hp:tr>' +
        make_cell(0, 6, 2, 1, 4891+6792-6792, 4800,
            f'<hp:p id="0" paraPrIDRef="28" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="11"><hp:t>기대효과</hp:t></hp:run><hp:linesegarray>{lineseg(vertsize=1200, textheight=1200, baseline=1020, spacing=360, horzsize=3868)}</hp:linesegarray></hp:p>',
            border_fill="4") +
        make_cell(2, 6, 7, 1, 11683+14659+16636-11683, 4800,
            effects_paras,
            border_fill="3") +
    '</hp:tr>')

    return rows


def make_header_row(row_idx):
    """Build the column header row (챕터/학습주제/학습내용/실습내용)"""
    return ('<hp:tr>' +
        make_cell(0, row_idx, 1, 1, 4891, 1701,
            f'<hp:p id="0" paraPrIDRef="28" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="11"><hp:t>챕터</hp:t></hp:run><hp:linesegarray>{lineseg(vertsize=1200, textheight=1200, baseline=1020, spacing=360, horzsize=3868)}</hp:linesegarray></hp:p>',
            border_fill="4") +
        make_cell(1, row_idx, 2, 1, 11683, 1701,
            f'<hp:p id="0" paraPrIDRef="28" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="11"><hp:t>학습주제</hp:t></hp:run><hp:linesegarray>{lineseg(vertsize=1200, textheight=1200, baseline=1020, spacing=360, horzsize=10660)}</hp:linesegarray></hp:p>',
            border_fill="4") +
        make_cell(3, row_idx, 3, 1, 14659, 1701,
            f'<hp:p id="0" paraPrIDRef="28" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="11"><hp:t>학습내용</hp:t></hp:run><hp:linesegarray>{lineseg(vertsize=1200, textheight=1200, baseline=1020, spacing=360, horzsize=13636)}</hp:linesegarray></hp:p>',
            border_fill="4") +
        make_cell(6, row_idx, 3, 1, 16636, 1701,
            f'<hp:p id="0" paraPrIDRef="28" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="11"><hp:t>실습내용</hp:t></hp:run><hp:linesegarray>{lineseg(vertsize=1200, textheight=1200, baseline=1020, spacing=360, horzsize=15613)}</hp:linesegarray></hp:p>',
            border_fill="4") +
    '</hp:tr>')


def build_section0(lessons, info, num_lessons):
    """Build complete section0.xml"""

    total_rows = 7 + 1 + num_lessons  # info rows + header row + lesson rows

    # Calculate table height
    info_height = 1701 * 5 + 2400 + 4800  # rows 0-6
    header_height = 1701
    lesson_height = 7383 * num_lessons
    total_height = info_height + header_height + lesson_height

    # Build rows
    all_rows = ""

    # Info rows (0-6)
    info_rows = make_info_rows(info, num_lessons)
    all_rows += "\n".join(info_rows)

    # Header row (7)
    all_rows += make_header_row(7)

    # Lesson rows (8+)
    for i, lesson in enumerate(lessons):
        all_rows += make_lesson_row(lesson, 8 + i)

    # Build the section
    section = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><hs:sec {NS}><hp:p id="3121190098" paraPrIDRef="20" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="0"><hp:secPr id="" textDirection="HORIZONTAL" spaceColumns="1134" tabStop="8000" outlineShapeIDRef="1" memoShapeIDRef="0" textVerticalWidthHead="0" masterPageCnt="0"><hp:grid lineGrid="0" charGrid="0" wonggojiFormat="0"/><hp:startNum pageStartsOn="BOTH" page="0" pic="0" tbl="0" equation="0"/><hp:visibility hideFirstHeader="0" hideFirstFooter="0" hideFirstMasterPage="0" border="SHOW_ALL" fill="SHOW_ALL" hideFirstPageNum="0" hideFirstEmptyLine="0" showLineNumber="0"/><hp:lineNumberShape restartType="0" countBy="0" distance="0" startNumber="0"/><hp:pagePr landscape="WIDELY" width="59528" height="84186" gutterType="LEFT_ONLY"><hp:margin header="2835" footer="2835" gutter="0" left="5669" right="5669" top="4252" bottom="4252"/></hp:pagePr><hp:footNotePr><hp:autoNumFormat type="DIGIT" userChar="" prefixChar="" suffixChar=")" supscript="0"/><hp:noteLine length="-1" type="SOLID" width="0.12 mm" color="#000000"/><hp:noteSpacing betweenNotes="283" belowLine="567" aboveLine="850"/><hp:numbering type="CONTINUOUS" newNum="1"/><hp:placement place="EACH_COLUMN" beneathText="0"/></hp:footNotePr><hp:endNotePr><hp:autoNumFormat type="DIGIT" userChar="" prefixChar="" suffixChar=")" supscript="0"/><hp:noteLine length="14692344" type="SOLID" width="0.12 mm" color="#000000"/><hp:noteSpacing betweenNotes="0" belowLine="567" aboveLine="850"/><hp:numbering type="CONTINUOUS" newNum="1"/><hp:placement place="END_OF_DOCUMENT" beneathText="0"/></hp:endNotePr><hp:pageBorderFill type="BOTH" borderFillIDRef="1" textBorder="PAPER" headerInside="0" footerInside="0" fillArea="PAPER"><hp:offset left="1417" right="1417" top="1417" bottom="1417"/></hp:pageBorderFill><hp:pageBorderFill type="EVEN" borderFillIDRef="1" textBorder="PAPER" headerInside="0" footerInside="0" fillArea="PAPER"><hp:offset left="1417" right="1417" top="1417" bottom="1417"/></hp:pageBorderFill><hp:pageBorderFill type="ODD" borderFillIDRef="1" textBorder="PAPER" headerInside="0" footerInside="0" fillArea="PAPER"><hp:offset left="1417" right="1417" top="1417" bottom="1417"/></hp:pageBorderFill></hp:secPr><hp:ctrl><hp:colPr id="" type="NEWSPAPER" layout="LEFT" colCount="1" sameSz="1" sameGap="0"/></hp:ctrl></hp:run><hp:run charPrIDRef="0"><hp:t/></hp:run><hp:linesegarray><hp:lineseg textpos="0" vertpos="0" vertsize="1000" textheight="1000" baseline="850" spacing="600" horzpos="0" horzsize="48188" flags="393216"/></hp:linesegarray></hp:p><hp:p id="0" paraPrIDRef="20" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="0"><hp:tbl id="2114307326" zOrder="1" numberingType="TABLE" textWrap="TOP_AND_BOTTOM" textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" pageBreak="CELL" repeatHeader="1" rowCnt="1" colCnt="1" cellSpacing="0" borderFillIDRef="3" noAdjust="0"><hp:sz width="23286" widthRelTo="ABSOLUTE" height="2682" heightRelTo="ABSOLUTE" protect="0"/><hp:pos treatAsChar="1" affectLSpacing="0" flowWithText="1" allowOverlap="0" holdAnchorAndSO="0" vertRelTo="PARA" horzRelTo="PARA" vertAlign="TOP" horzAlign="LEFT" vertOffset="0" horzOffset="0"/><hp:outMargin left="283" right="283" top="283" bottom="283"/><hp:inMargin left="510" right="510" top="141" bottom="141"/><hp:tr><hp:tc name="" header="0" hasMargin="0" protect="0" editable="0" dirty="0" borderFillIDRef="8"><hp:subList id="" textDirection="HORIZONTAL" lineWrap="BREAK" vertAlign="CENTER" linkListIDRef="0" linkListNextIDRef="0" textWidth="0" textHeight="0" hasTextRef="0" hasNumRef="0"><hp:p id="3197523146" paraPrIDRef="20" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="10"><hp:t>강 의 계 획 서(안)</hp:t></hp:run><hp:linesegarray><hp:lineseg textpos="0" vertpos="0" vertsize="2400" textheight="2400" baseline="2040" spacing="1440" horzpos="0" horzsize="22264" flags="393216"/></hp:linesegarray></hp:p></hp:subList><hp:cellAddr colAddr="0" rowAddr="0"/><hp:cellSpan colSpan="1" rowSpan="1"/><hp:cellSz width="23286" height="282"/><hp:cellMargin left="510" right="510" top="283" bottom="283"/></hp:tc></hp:tr></hp:tbl><hp:t/></hp:run><hp:linesegarray><hp:lineseg textpos="0" vertpos="1600" vertsize="3282" textheight="1000" baseline="850" spacing="600" horzpos="0" horzsize="48188" flags="393216"/></hp:linesegarray></hp:p><hp:p id="0" paraPrIDRef="0" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="0"><hp:tbl id="0" zOrder="2" numberingType="TABLE" textWrap="TOP_AND_BOTTOM" textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" pageBreak="TABLE" repeatHeader="1" rowCnt="{total_rows}" colCnt="9" cellSpacing="0" borderFillIDRef="3" noAdjust="0"><hp:sz width="47869" widthRelTo="ABSOLUTE" height="{total_height}" heightRelTo="ABSOLUTE" protect="0"/><hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="1" allowOverlap="0" holdAnchorAndSO="0" vertRelTo="PARA" horzRelTo="PARA" vertAlign="TOP" horzAlign="LEFT" vertOffset="0" horzOffset="0"/><hp:outMargin left="283" right="283" top="0" bottom="0"/><hp:inMargin left="510" right="510" top="141" bottom="141"/>{all_rows}</hp:tbl><hp:t/></hp:run><hp:linesegarray><hp:lineseg textpos="0" vertpos="0" vertsize="1000" textheight="1000" baseline="850" spacing="600" horzpos="0" horzsize="48188" flags="393216"/></hp:linesegarray></hp:p></hs:sec>'''

    return section


def generate_hwpx(lessons, info, num_lessons, output_path):
    """Generate HWPX file by replacing section0.xml in base file"""

    section0 = build_section0(lessons, info, num_lessons)

    # Read base HWPX and replace section0.xml
    buf = io.BytesIO()
    with zipfile.ZipFile(BASE_HWPX, 'r') as zin:
        with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zout:
            for item in zin.namelist():
                if item == 'Contents/section0.xml':
                    zout.writestr(item, section0.encode('utf-8'))
                elif item == 'Preview/PrvText.txt':
                    # Update preview text
                    prv = f"강 의 계 획 서(안)\n{info['title']}\n{info['time']}"
                    zout.writestr(item, prv.encode('utf-8'))
                elif item == 'Contents/content.hpf':
                    # Update content.hpf with correct section count
                    data = zin.read(item)
                    zout.writestr(item, data)
                else:
                    zout.writestr(item, zin.read(item))

    with open(output_path, 'wb') as f:
        f.write(buf.getvalue())

    print(f"Generated: {output_path} ({os.path.getsize(output_path):,} bytes)")


# ============================================================
# Main
# ============================================================
if __name__ == '__main__':
    configs = [
        (LESSONS_4, INFO[4], 4, "AI교육_강의계획서_4차시.hwpx"),
        (LESSONS_6, INFO[6], 6, "AI교육_강의계획서_6차시.hwpx"),
        (LESSONS_8, INFO[8], 8, "AI교육_강의계획서_8차시.hwpx"),
    ]

    for lessons, info, num, filename in configs:
        output = os.path.join(OUTPUT_DIR, filename)
        generate_hwpx(lessons, info, num, output)

    print("\nDone! Generated 3 HWPX files.")
