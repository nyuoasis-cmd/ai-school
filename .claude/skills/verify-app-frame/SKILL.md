---
name: verify-app-frame
description: 학과 앱(v2.html)이 표준 프레임 패턴(app-frame, app-header, max-width:430px)을 따르는지 검증. 앱 추가/수정 후 사용.
---

# 앱 프레임 패턴 검증

## Purpose

모든 학과 앱(v2.html)이 프로젝트의 표준 앱 프레임 패턴을 따르는지 검증합니다:

1. **app-frame** — `<div class="app-frame">` 래퍼 사용
2. **max-width** — CSS에 `max-width:430px` 설정
3. **app-header** — `<header class="app-header">` 사용
4. **tab-bar** — 탭 네비게이션 (`class="tab-bar"`) 사용 (해당되는 경우)
5. **min-height** — `min-height:100dvh` 사용
6. **standalone** — 외부 CSS/JS 의존 없이 인라인으로 완결

## When to Run

- 새 학과 앱을 추가한 후
- 기존 앱의 레이아웃을 수정한 후
- 앱 프레임 공통 스타일을 변경한 후
- PR 전 앱 일관성 점검 시

## Related Files

| File | Purpose |
|------|---------|
| `조리과_칼로리계산기/calorie-app-v2.html` | 조리과 앱 |
| `전기과_스마트전력대시보드/power-dashboard-v2.html` | 전기과 앱 |
| `보건복지_노인돌봄/moodcare-v2.html` | 보건복지 앱 |
| `디자인미디어학과_인테리어디자인/room-glow-v2.html` | 디자인 앱 |
| `건설학과_안전점검/safecheck-v2.html` | 건설학과 앱 |
| `기계차량_부품도감/parts-guide-v2.html` | 기계차량 앱 |
| `경영금융_쇼핑몰경영/shop-simulator-v2.html` | 경영금융 앱 |
| `정보통신과_교내상담AI챗봇/school-chatbot-v2.html` | 정보통신 앱 |

## Workflow

### Step 1: v2.html 파일 목록 수집

**도구:** Glob

```bash
find . -name "*-v2.html" -not -path "./.git/*"
```

8개 v2.html 파일을 수집합니다.

### Step 2: app-frame 래퍼 검증

**도구:** Grep

각 v2.html에서 `class="app-frame"` 사용 여부를 확인합니다.

```bash
grep -L "app-frame" */*-v2.html
```

**PASS:** 결과 없음 (모든 파일이 app-frame 사용)
**FAIL:** app-frame 미사용 파일 발견

### Step 3: max-width:430px 검증

**도구:** Grep

각 v2.html CSS에서 `max-width` 설정을 확인합니다.

```bash
grep "max-width.*430" */*-v2.html
```

**PASS:** 8개 파일 모두 max-width:430px 설정
**FAIL:** max-width 미설정 파일 발견

### Step 4: app-header 검증

**도구:** Grep

```bash
grep -L "app-header" */*-v2.html
```

**PASS:** 결과 없음
**FAIL:** app-header 미사용 파일 발견

### Step 5: min-height:100dvh 검증

**도구:** Grep

```bash
grep "min-height.*100dvh" */*-v2.html
```

**PASS:** 8개 파일 모두 설정
**FAIL:** min-height 미설정 파일 발견

### Step 6: 외부 의존성 검증

**도구:** Grep

```bash
grep -E '<link.*rel="stylesheet".*href="http|<script.*src="http' */*-v2.html | grep -v "fonts.googleapis"
```

Google Fonts 외의 외부 CSS/JS 의존이 없는지 확인합니다.

**PASS:** 결과 없음 (Google Fonts만 사용)
**FAIL:** 외부 의존성 발견 — 인라인으로 변환 필요

### Step 7: 결과 보고

발견된 이슈를 테이블로 정리합니다.

## Output Format

```markdown
## 앱 프레임 검증 결과

### 검사 요약

| 검사 항목 | 대상 파일 수 | 통과 | 이슈 |
|-----------|-------------|------|------|
| app-frame 래퍼 | N | N | N |
| max-width:430px | N | N | N |
| app-header | N | N | N |
| min-height:100dvh | N | N | N |
| 외부 의존성 없음 | N | N | N |

### 이슈

| # | 검사 항목 | 파일 | 문제 | 수정 방법 |
|---|-----------|------|------|-----------|

### 결론: PASS / N개 이슈 발견
```

## Exceptions

다음은 **위반이 아닙니다**:

1. **tab-bar 미사용 앱** — 챗봇(school-chatbot-v2.html), 칼로리(calorie-app-v2.html) 등 앱 특성상 탭 네비게이션이 불필요한 경우 tab-bar 없이도 위반 아님
2. **design.html 파일** — `*-design.html`은 디자인 참고용이므로 앱 프레임 패턴을 따를 필요 없음
3. **Google Fonts CDN** — `fonts.googleapis.com`, `fonts.gstatic.com`은 허용되는 외부 의존성
4. **index.html** — 메인 사이트 페이지는 앱 프레임이 아니므로 검증 대상 아님
