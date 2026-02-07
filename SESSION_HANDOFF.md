# SESSION HANDOFF — 보건복지과 MoodCare(마음돌봄) 체험판 제작

## 프로젝트 개요
AI 위탁교육 프로그램 홍보용 데모 사이트. 8개 학과별 AI 앱 체험판을 제공하는 쇼케이스 페이지.
`index.html`이 메인 쇼케이스이며, 각 학과 카드 클릭 시 아이폰 폰프레임 모달 안에 iframe으로 체험판 HTML을 로드한다.

---

## 이번 세션 작업 목표 (3개)

### 1. `보건복지_노인돌봄/moodcare-v2.html` 제작
- 스펙 파일 3개 기반으로 standalone 모바일 체험판 제작
  - `마음돌봄_00_빠른시작_프롬프트.md` — 앱 개요, 대상자 데이터, 색상, 화면 흐름
  - `마음돌봄_01_화면별_스펙.md` — 픽셀 단위 UI 스펙 (아바타, 레이더차트, 바텀시트 등)
  - `마음돌봄_02_데이터_로직.md` — 대상자 데이터, 감정 분석 로직, AI 결과 생성
- **design.html은 없음** — 스펙 문서만으로 처음부터 v2 제작
- **반드시 app-frame 패턴을 따를 것** (아래 패턴 설명 참고)

### 2. 썸네일 생성
- Puppeteer로 `moodcare-v2.html` 스크린샷 (390x844 @2x)
- PIL로 400px 너비 JPEG 변환 → `image/moodcare-thumb.jpg`

### 3. index.html 카드 전환
- 보건복지과 카드를 `dept-card--thumb` 패턴으로 변경
- 데모 매핑 `file:` 값을 `보건복지_노인돌봄/moodcare-v2.html`로 변경

---

## app-frame 패턴 (필수 준수)

완성된 v2 파일 6개가 따르는 패턴:

```html
<!-- 폰 프레임 없음. index.html의 iframe에서 로드됨 -->
<div class="app-frame" style="max-width:430px; margin:0 auto; min-height:100dvh;">
  <header style="position:sticky; top:0;">헤더</header>
  <main style="flex:1;">컨텐츠</main>
</div>
```

핵심 규칙:
- **폰 프레임/상태바/노치 없음** — index.html이 iframe 안에 폰 프레임을 씌움
- **데스크탑 폰프레임 @media 블록 포함하지 않음**
- `max-width: 430px`, `margin: 0 auto`
- **390x844 뷰포트에서 첫 화면(초기 상태)이 스크롤 없이 완전히 보여야 함**
- 모든 CSS/JS/데이터 인라인 (standalone HTML 한 파일)
- 외부 의존: Google Fonts CDN만 사용 (Unsplash 이미지 OK)
- `user-select: none; -webkit-user-select: none;` body에 추가
- 입력 요소는 `user-select: auto` 재설정

### MoodCare 앱 구조 (3탭)
```
┌─────────────────────────┐
│  헤더 (Teal 그라디언트)    │  ← sticky top
├─────────────────────────┤
│  탭 바 (3탭)              │  ← 🏠 홈 | 🧠 분석 | 📈 추이
├─────────────────────────┤
│  콘텐츠 영역 (flex:1 스크롤)│
└─────────────────────────┘
```

**390x844 첫 화면 핏**: 헤더 + 탭 바 높이를 빼고 콘텐츠에 대상자 카드 최소 4개 보여야 함.
→ 헤더를 콤팩트하게, 카드를 압축적으로 배치.

---

## 디자인 토큰 (MoodCare)

```css
--bg: #F6F8FA;            /* 라이트 배경 */
--surface: #FFFFFF;        /* 카드 배경 */
--border: #E2E8F0;         /* 테두리 */
--text: #1A2332;           /* 본문 */
--text2: #5A6B7F;          /* 보조 */
--text3: #94A3B8;          /* 비활성 */
--teal: #0D9488;           /* 메인 (돌봄, 안정) */
--teal-dark: #0F766E;      /* 헤더 그라디언트 끝 */
--teal-light: #CCFBF1;     /* 메인 라이트 배경 */
--lavender: #7C3AED;       /* 보조 (심리, 전문성) */
--green: #10B981;          /* 기쁨 */
--blue: #3B82F6;           /* 슬픔 */
--amber: #F59E0B;          /* 불안 */
--coral: #F97066;          /* 분노/경고 */
--pink: #EC4899;           /* 보조 핑크 */
```

폰트: `Noto Sans KR` (본문) + `JetBrains Mono` (수치)
테마: **라이트 테마 + Teal(#0D9488) 포인트 + Lavender(#7C3AED) 보조**

---

## 핵심 기능

### 탭1: 홈 — 대상자 현황 대시보드
- 6명의 어르신 대상자 카드 (이름·나이·질환·감정상태·스파크라인)
- 한글 성씨 이니셜 아바타 (원형 52x52, 고유 색상, 흰색 텍스트)
- 상단에 통계 요약 (전체 대상자, 주의 필요, 안정 등)
- 카드 클릭 → 분석 탭 이동 + 해당 대상자 자동 선택

### 탭2: 분석 — AI 감정 분석
- 대상자 선택 드롭다운/칩
- 관찰 기록 입력 텍스트 영역
- 빠른 태그 10개 (눈물/식사거름/수면어려움/가족이야기/웃음/산책/TV시청/대화적극/말수줄어듦/짜증)
- AI 분석 시작 버튼 → 4단계 로딩 애니메이션 (2.8초)
- 결과 바텀시트 팝업:
  - **6축 레이더 차트 (SVG)**: 기쁨/평온/슬픔/불안/분노/외로움 (각 0~100)
  - 중앙에서 펼쳐지는 애니메이션
  - 감정 점수 + 위험도 3단계 (🟢안정/🟡관찰필요/🔴주의)
  - 추천 조치 텍스트

### 탭3: 추이 — 감정 변화 트렌드
- 주간 감정 추이 라인차트 (SVG)
- 최근 분석 타임라인 목록
- 대상자별 필터링

### 데이터
```javascript
clients = [
  { id:1, name:'김순자', age:78, condition:'경도 치매', mood:'sad', avatarColor:'#E57373', alert:true },
  { id:2, name:'이영호', age:82, condition:'우울증', mood:'lonely', avatarColor:'#7986CB', alert:true },
  { id:3, name:'박옥순', age:75, condition:'관절염', mood:'calm', avatarColor:'#81C784', alert:false },
  { id:4, name:'정대현', age:80, condition:'당뇨', mood:'anxious', avatarColor:'#FFB74D', alert:false },
  { id:5, name:'한미경', age:77, condition:'고혈압', mood:'happy', avatarColor:'#BA68C8', alert:false },
  { id:6, name:'최병수', age:85, condition:'파킨슨', mood:'angry', avatarColor:'#4FC3F7', alert:true }
]
```

---

## index.html 카드 전환 방법

### 현재 상태 (아이콘 기반, ~1296줄):
```html
<div class="dept-card" onclick="openDemo('moodcare')">
  <div class="dept-card-glow"></div>
  <div class="dept-card-visual">
    <div class="dept-card-visual-bg"></div>
    <div class="dept-card-icon">🩺</div>
  </div>
  <div class="dept-card-body">
    <div class="dept-card-dept">보건복지과</div>
    <div class="dept-card-app"><span class="dept-card-app-dot"></span>MoodCare 감정분석</div>
    <div class="dept-card-desc">AI로 돌봄 대상자의 감정 상태를 모니터링하고...</div>
  </div>
</div>
```

### 변경 후 (썸네일 기반):
```html
<div class="dept-card dept-card--thumb dept-card--thumb-moodcare" onclick="openDemo('moodcare')">
  <div class="dept-card-glow"></div>
  <div class="dept-card-thumb-bottom">
    <div class="dept-card-dept">보건복지과</div>
    <div class="dept-card-app">MoodCare 감정분석</div>
  </div>
</div>
```

### CSS 추가 (index.html ~504줄, 기존 thumb CSS 블록 뒤에):
```css
/* 보건복지과 썸네일 */
.dept-card--thumb-moodcare {
  background:
    linear-gradient(to top, #000 0%, rgba(0,0,0,0.9) 10%, rgba(0,0,0,0.5) 22%, transparent 35%),
    url('image/moodcare-thumb.jpg') center top / cover no-repeat !important;
}
```

### 데모 매핑 변경 (index.html ~1567줄):
```javascript
// Before:
moodcare:  { title: 'MOOD_CARE // 감정 모니터링', file: '보건복지_노인돌봄/moodcare-design.html' }
// After:
moodcare:  { title: 'MOOD_CARE // 감정 모니터링', file: '보건복지_노인돌봄/moodcare-v2.html' }
```

---

## Puppeteer 스크린샷 방법

```bash
cd /home/claude && node -e '
const puppeteer = require("puppeteer");
const path = require("path");
(async () => {
  const browser = await puppeteer.launch({ headless: "new", args: ["--no-sandbox","--disable-setuid-sandbox","--disable-dev-shm-usage"] });
  const page = await browser.newPage();
  await page.setViewport({ width: 390, height: 844, deviceScaleFactor: 2 });
  const filePath = path.resolve("ai-school/보건복지_노인돌봄/moodcare-v2.html");
  await page.goto("file://" + filePath, { waitUntil: "networkidle0", timeout: 20000 });
  await new Promise(r => setTimeout(r, 3000));
  await page.screenshot({ path: "ai-school/image/moodcare-thumb.png", clip: { x: 0, y: 0, width: 390, height: 844 } });
  await browser.close();
  console.log("Screenshot done");
  process.exit(0);
})().catch(e => { console.error(e.message); process.exit(1); });
'
```

PIL 압축:
```python
python3 -c "
from PIL import Image; import os
img = Image.open('ai-school/image/moodcare-thumb.png')
img = img.resize((400, int(400 * img.height / img.width)), Image.LANCZOS).convert('RGB')
img.save('ai-school/image/moodcare-thumb.jpg', 'JPEG', quality=80)
print(f'{img.size[0]}x{img.size[1]}, {os.path.getsize(\"ai-school/image/moodcare-thumb.jpg\")//1024}KB')
"
```

---

## 이전 세션들에서 겪은 이슈 & 해결책

1. **390x844 첫 화면 핏**: 헤더+탭+하단 높이를 빼고 콘텐츠 영역을 계산해야 함. 헤더를 콤팩트하게 설계하고, 카드도 압축적으로 배치.
2. **user-select: none** 필수 — 드래그/스와이프 가능한 요소에 반드시 추가 (파란 선택 방지). 단, 텍스트 입력(textarea)은 user-select 허용.
3. **`page.waitForTimeout` 사용 불가** — `await new Promise(r => setTimeout(r, ms))` 사용
4. **Puppeteer는 `/home/claude`에서 실행** — `node_modules`가 거기 있음
5. **v2에서는 `@media (min-width:500px)` 폰프레임 블록을 제거해야 함**. index.html이 iframe으로 폰프레임을 씌움.
6. **카드 높이**: `.dept-card--thumb`에 `min-height: 258px` 설정됨. 일반 카드와 높이 맞춤.
7. **Unsplash 이미지**: Puppeteer 스크린샷 시 외부 이미지 로딩 대기 필요. `waitUntil: "networkidle0"` + 추가 3초 대기.
8. **SVG 레이더차트**: 외부 차트 라이브러리 없이 SVG로 직접 그려야 함. 6각형 그리드 + 데이터 폴리곤 + 축 라벨 + 점수 표시. 중앙에서 펼쳐지는 애니메이션 포함.
9. **바텀시트**: backdrop-filter: blur(8px), 슬라이드업 애니메이션. 외부 팝업이 아닌 카드 내부 또는 오버레이 방식.

---

## MoodCare에서 주의할 기술적 포인트

### SVG 레이더 차트 (6축)
- 6각형 배경 그리드 (3단계 동심원)
- 데이터 폴리곤 (teal 색상, 반투명 fill)
- 각 꼭짓점에 축 라벨 (기쁨/평온/슬픔/불안/분노/외로움)
- 애니메이션: 중앙에서 펼쳐지는 효과 (scale 0→1 또는 polygon 점들이 중앙에서 이동)

### 4단계 로딩 애니메이션
- 프로그레스바 방식: 25% → 50% → 75% → 100%
- 각 단계별 텍스트: "대화 분석 중..." → "감정 패턴 탐색..." → "위험도 평가 중..." → "보고서 생성 중..."
- 총 2.8초 (각 단계 0.7초)

### 바텀시트 팝업
- 하단에서 슬라이드업
- 배경 블러 오버레이
- 닫기 버튼 또는 배경 클릭으로 닫기

### 감정 분석 결과 생성 (가상 AI)
- 입력된 관찰 기록의 키워드 매칭으로 감정 점수 조절
- 빠른 태그 기반 가중치 적용
- 위험도 판정: 슬픔+외로움+불안 합계 기반

---

## 완성된 v2 참고 파일 (패턴 참고용)

| 파일 | 학과 | 테마 | 특징 |
|------|------|------|------|
| `조리과_칼로리계산기/calorie-app-v2.html` | 조리과 | 라이트/오렌지 | 헤더+탭, 3탭 |
| `디자인미디어학과_인테리어디자인/room-glow-v2.html` | 디자인과 | 다크 | 헤더+탭, B/A슬라이더 |
| `기계차량_부품도감/parts-guide-v2.html` | 기계과 | 다크+레드 | 헤더+탭, 카드스크롤 |
| `정보통신과_교내상담AI챗봇/school-chatbot-v2.html` | 정보통신과 | 라이트/퍼플 | 탭없음, 채팅 |
| `전기과_스마트전력대시보드/power-dashboard-v2.html` | 전기과 | 다크/사이언 | 헤더+탭, 게이지+차트 |
| `경영금융_쇼핑몰경영/shop-simulator-v2.html` | 경영금융과 | 라이트/그린 | 헤더+3탭, 6슬라이더+시뮬레이션 |

**MoodCare는 라이트 테마 + 3탭 구조**. `calorie-app-v2.html`의 라이트 테마 레이아웃을 참고하되, 레이더 차트·바텀시트·로딩 애니메이션이 핵심 차이점.

---

## 파일 구조

```
ai-school/
├── index.html                          ← 메인 쇼케이스 (보건복지 카드 전환 필요)
├── SESSION_HANDOFF.md                  ← 이 문서
├── image/
│   ├── calorie-thumb.jpg               ← 조리과 썸네일 (완성)
│   ├── roomglow-thumb.jpg              ← 디자인과 썸네일 (완성)
│   ├── parts-thumb.jpg                 ← 기계과 썸네일 (완성)
│   ├── chatbot-thumb.jpg               ← 정보통신과 썸네일 (완성)
│   ├── power-thumb.jpg                 ← 전기전자과 썸네일 (완성)
│   ├── shop-thumb.jpg                  ← 경영금융과 썸네일 (완성)
│   └── moodcare-thumb.jpg              ← [생성 필요] 보건복지과 썸네일
├── 경영금융_쇼핑몰경영/
│   └── shop-simulator-v2.html          ← 완성 (6슬라이더 확장판)
├── 조리과_칼로리계산기/
│   └── calorie-app-v2.html             ← 완성 (라이트 테마 참고용)
├── 전기과_스마트전력대시보드/
│   └── power-dashboard-v2.html         ← 완성
├── 정보통신과_교내상담AI챗봇/
│   └── school-chatbot-v2.html          ← 완성
├── 디자인미디어학과_인테리어디자인/
│   └── room-glow-v2.html               ← 완성
├── 기계차량_부품도감/
│   └── parts-guide-v2.html             ← 완성
├── 보건복지_노인돌봄/                    ← [이번 작업 대상]
│   ├── moodcare-v2.html                ← [생성 필요] app-frame 체험판
│   ├── 마음돌봄_00_빠른시작_프롬프트.md ← 앱 개요
│   ├── 마음돌봄_01_화면별_스펙.md      ← UI 스펙
│   └── 마음돌봄_02_데이터_로직.md      ← 데이터, 감정분석 로직
└── 건설학과_안전점검/                    ← design만 있음 (미완성)
```

---

## 현재 index.html 카드 현황

| # | 학과 | 카드 타입 | 데모 파일 |
|---|------|-----------|-----------|
| 1 | 조리과 | thumb (완성) | calorie-app-v2.html |
| 2 | 디자인과 | thumb (완성) | room-glow-v2.html |
| 3 | 기계과 | thumb (완성) | parts-guide-v2.html |
| 4 | 정보통신과 | thumb (완성) | school-chatbot-v2.html |
| 5 | 전기전자과 | thumb (완성) | power-dashboard-v2.html |
| 6 | 경영금융과 | thumb (완성) | shop-simulator-v2.html |
| 7 | **보건복지과** | **아이콘 (미완성)** | **moodcare-design.html** |
| 8 | 건설과 | 아이콘 | safecheck-design.html |

---

## 참고: index 페이지 디자인 토큰

```css
배경: #08090D
카드: #12141C
악센트: #00E5A0 (민트 그린)
텍스트: #E8E9ED
```
