# SESSION HANDOFF — 기계자동차과 파츠피디아 데모 제작

## 프로젝트 개요
AI 위탁교육 프로그램 홍보용 데모 사이트. 8개 학과별 AI 앱 체험판을 제공하는 쇼케이스 페이지.
`index.html`이 메인 쇼케이스이며, 각 학과 카드 클릭 시 아이폰 폰프레임 모달 안에 iframe으로 체험판 HTML을 로드한다.

---

## 이번 세션 작업 목표 (3개)

### 1. `기계차량_부품도감/parts-guide-v2.html` 제작
- 스펙 파일 3개 기반으로 standalone 모바일 체험판 제작
  - `부품도감_00_빠른시작_프롬프트.md` — 앱 개요, 핵심 기능 3탭
  - `부품도감_01_화면스펙.md` — 픽셀 단위 UI 스펙
  - `부품도감_02_데이터_로직.md` — 부품 8종, 핫스팟 5개, 퀴즈 10문항 JSON 데이터
- 기존 `parts-guide-design.html`은 폰프레임 래퍼 포함 버전 → **수정하지 말 것**
- **반드시 app-frame 패턴을 따를 것** (아래 패턴 설명 참고)

### 2. 썸네일 생성
- Puppeteer로 `parts-guide-v2.html` 스크린샷 (390x844 @2x)
- PIL로 400px 너비 JPEG 변환 → `image/parts-thumb.jpg`

### 3. index.html 카드 전환
- 기계자동차과 카드를 `dept-card--thumb` 패턴으로 변경
- 데모 매핑 `file:` 값을 `parts-guide-v2.html`로 변경

---

## app-frame 패턴 (필수 준수)

`calorie-app-v2.html`, `room-glow-v2.html`이 따르는 패턴:

```html
<!-- 폰 프레임 없음. index.html의 iframe에서 로드됨 -->
<div class="app-frame" style="max-width:430px; margin:0 auto; min-height:100dvh;">
  <header style="height:46px; position:sticky; top:0;">로고 + 학과 배지</header>
  <nav style="height:38px; position:sticky; top:46px;">탭 바</nav>
  <main>컨텐츠</main>
</div>
```

핵심 규칙:
- **폰 프레임/상태바 없음** — index.html이 iframe 안에 폰 프레임을 씌움
- `max-width: 430px`, `margin: 0 auto`
- 헤더 46px + 탭바 38px (sticky)
- **390x844 뷰포트에서 스크롤 없이 첫 화면(탭1 기본 뷰)이 완전히 보여야 함**
- 모든 CSS/JS/데이터 인라인 (standalone HTML 한 파일)
- 외부 의존: Google Fonts CDN만 사용

---

## 디자인 토큰 (파츠피디아)

```css
--red: #EF4444;
--red-dark: #DC2626;
--red-glow: rgba(239, 68, 68, 0.3);
--bg-primary: #0A0A0A;
--bg-secondary: #141414;
--bg-card: #1A1A1A;
--border: #2A2A2A;
--text-primary: #F5F5F5;
--text-secondary: #A3A3A3;
--text-muted: #666666;
--success: #22C55E;
--warning: #F59E0B;
```

폰트: `Rajdhani` (영문 타이틀/수치) + `Noto Sans KR` (한국어)
테마: **다크 테마 + 레드(#EF4444) 포인트**

---

## index.html 카드 전환 방법

### 기존 아이콘 카드 → 썸네일 카드 변환

**Before (기존 아이콘 기반):**
```html
<div class="dept-card" onclick="openDemo('parts')">
  <div class="dept-card-glow"></div>
  <div class="dept-card-visual"><div class="dept-card-icon">🔧</div></div>
  <div class="dept-card-body">
    <div class="dept-card-dept">기계자동차과</div>
    <div class="dept-card-app"><span class="dept-card-app-dot"></span>파츠피디아 부품 도감</div>
    <div class="dept-card-desc">...</div>
  </div>
</div>
```

**After (썸네일 기반):**
```html
<div class="dept-card dept-card--thumb dept-card--thumb-parts" onclick="openDemo('parts')">
  <div class="dept-card-glow"></div>
  <div class="dept-card-thumb-bottom">
    <div class="dept-card-dept">기계자동차과</div>
    <div class="dept-card-app">파츠피디아 부품 도감</div>
  </div>
</div>
```

**CSS 추가:**
```css
.dept-card--thumb-parts {
  background:
    linear-gradient(to top, #000 0%, rgba(0,0,0,0.9) 10%, rgba(0,0,0,0.5) 22%, transparent 35%),
    url('image/parts-thumb.jpg') center top / cover no-repeat !important;
}
```

**데모 매핑 변경:**
```javascript
parts: { title: 'PARTS_PEDIA // 부품 도감', file: '기계차량_부품도감/parts-guide-v2.html' },
```

---

## 기존 썸네일 카드 CSS (index.html에 이미 존재)

```css
.dept-card--thumb { display:flex; flex-direction:column; justify-content:flex-end; border:none !important; background-size:cover !important; background-position:center top !important; }
.dept-card-thumb-bottom { padding:16px 18px 14px; }
.dept-card--thumb .dept-card-dept, .dept-card--thumb .dept-card-app { color:#fff; text-shadow:0 1px 6px rgba(0,0,0,0.7); }
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
  const filePath = path.resolve("ai-school/기계차량_부품도감/parts-guide-v2.html");
  await page.goto("file://" + filePath, { waitUntil: "networkidle0", timeout: 20000 });
  await new Promise(r => setTimeout(r, 3000));
  await page.screenshot({ path: "ai-school/image/parts-thumb.png", clip: { x: 0, y: 0, width: 390, height: 844 } });
  await browser.close();
  process.exit(0);
})().catch(e => { console.error(e.message); process.exit(1); });
'
```

PIL 압축:
```python
python3 -c "
from PIL import Image; import os
img = Image.open('ai-school/image/parts-thumb.png')
img = img.resize((400, int(400 * img.height / img.width)), Image.LANCZOS).convert('RGB')
img.save('ai-school/image/parts-thumb.jpg', 'JPEG', quality=80)
print(f'{img.size[0]}x{img.size[1]}, {os.path.getsize(\"ai-school/image/parts-thumb.jpg\")//1024}KB')
"
```

---

## 이전 세션에서 겪은 이슈 & 해결책

1. **BA 슬라이더 clip-path 방향**: `inset(0 0 0 X%)` = after가 오른쪽. `inset(0 X% 0 0)`은 after가 왼쪽으로 나와 before/after가 뒤바뀜.
2. **user-select: none** 필수 — 드래그/스와이프 가능한 요소에 반드시 추가 (파란 선택 방지)
3. **390x844 첫 화면 핏**: 헤더 46px + 탭 38px = 84px. 컨텐츠 영역 약 760px에 맞춰야 함.
4. **`page.waitForTimeout` 사용 불가** — `await new Promise(r => setTimeout(r, ms))` 사용
5. **Puppeteer는 `/home/claude`에서 실행** — `node_modules`가 거기 있음
6. **Unsplash 이미지 검색**: WebFetch로 `unsplash.com/napi/search/photos?query=...&per_page=6&orientation=landscape` 사용. `premium_photo-` URL은 로드 안 됨.

---

## 파일 구조

```
ai-school/
├── index.html                          ← 메인 쇼케이스 (카드 전환 필요)
├── SESSION_HANDOFF.md                  ← 이 문서
├── image/
│   ├── calorie-thumb.jpg               ← 조리과 썸네일
│   ├── roomglow-thumb.jpg              ← 디자인과 썸네일
│   └── parts-thumb.jpg                 ← [생성 필요] 기계과 썸네일
├── 기계차량_부품도감/
│   ├── parts-guide-design.html         ← 기존 폰프레임 디자인 (수정 금지)
│   ├── parts-guide-v2.html             ← [생성 필요] app-frame 체험판
│   ├── 부품도감_00_빠른시작_프롬프트.md  ← 앱 개요
│   ├── 부품도감_01_화면스펙.md          ← UI 스펙
│   └── 부품도감_02_데이터_로직.md       ← 데이터/로직
├── 조리과_칼로리계산기/
│   └── calorie-app-v2.html             ← app-frame 패턴 참고용
└── 디자인미디어학과_인테리어디자인/
    └── room-glow-v2.html               ← app-frame 패턴 참고용
```

---

## 참고: index 페이지 디자인 토큰

```css
배경: #08090D
카드: #12141C
악센트: #00E5A0 (민트 그린)
텍스트: #E8E9ED
```
