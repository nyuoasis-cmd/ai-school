---
name: verify-demo-registry
description: 데모/커리큘럼 등록 일관성 검증 (demos 객체, curFiles, bizFiles ↔ 카드 ↔ 파일). 학과 앱 추가/수정 후 사용.
---

# 데모 등록 일관성 검증

## Purpose

index.html의 3개 등록 객체가 카드 요소 및 실제 파일과 일관되게 연결되어 있는지 검증합니다:

1. **demos 객체** — 8개 학과 앱 키 ↔ dept-card 카드 ↔ v2.html 파일
2. **curFiles 객체** — 4개 커리큘럼 키 ↔ cur-card 카드 ↔ class-detail 파일
3. **bizFiles 객체** — 3개 비즈쿨 키 ↔ cur-card 카드 ↔ bizcool-detail 파일

## When to Run

- 새 학과 앱을 추가한 후
- 기존 학과 앱의 파일 경로를 변경한 후
- 커리큘럼/비즈쿨 상세 페이지를 추가/삭제한 후
- index.html의 카드 섹션을 수정한 후
- PR 전 등록 일관성 점검 시

## Related Files

| File | Purpose |
|------|---------|
| `index.html` | 메인 페이지 (demos, curFiles, bizFiles 객체 + 카드 HTML) |
| `조리과_칼로리계산기/calorie-app-v2.html` | 조리과 앱 |
| `전기과_스마트전력대시보드/power-dashboard-v2.html` | 전기과 앱 |
| `보건복지_노인돌봄/moodcare-v2.html` | 보건복지 앱 |
| `디자인미디어학과_인테리어디자인/room-glow-v2.html` | 디자인 앱 |
| `건설학과_안전점검/safecheck-v2.html` | 건설학과 앱 |
| `기계차량_부품도감/parts-guide-v2.html` | 기계차량 앱 |
| `경영금융_쇼핑몰경영/shop-simulator-v2.html` | 경영금융 앱 |
| `정보통신과_교내상담AI챗봇/school-chatbot-v2.html` | 정보통신 앱 |
| `class-detail.html` | 1회차(2h) 커리큘럼 |
| `class-detail-4h.html` | 2회차(4h) 커리큘럼 |
| `class-detail-6h.html` | 3회차(6h) 커리큘럼 |
| `class-detail-8h.html` | 4회차(8h) 커리큘럼 |
| `bizcool-detail-4h.html` | 비즈쿨 4차시 |
| `bizcool-detail-8h.html` | 비즈쿨 8차시 |
| `bizcool-detail-12h.html` | 비즈쿨 12차시 |

## Workflow

### Step 1: demos 객체 키 수집

**도구:** Grep

```bash
grep "file:" index.html
```

demos 객체에서 키와 file 경로를 추출합니다 (8개 기대).

### Step 2: dept-card 카드 수집

**도구:** Grep

```bash
grep "openDemo(" index.html
```

dept-card의 onclick에서 사용하는 키를 추출합니다 (8개 기대).

**PASS:** demos 객체의 키 8개와 카드의 openDemo 키 8개가 동일
**FAIL:** 키 불일치 — demos 객체 또는 카드 추가/수정 필요

### Step 3: dept-card CSS 클래스 수집

**도구:** Grep

```bash
grep "dept-card--thumb-" index.html
```

CSS 정의(`.dept-card--thumb-{key}`)와 HTML 사용(`dept-card--thumb-{key}`)의 키를 대조합니다.

**PASS:** 모든 demos 키에 대해 CSS 클래스와 HTML 사용이 존재
**FAIL:** CSS 또는 HTML에서 누락된 키 — 썸네일 CSS 또는 카드 추가 필요

### Step 4: demos 파일 존재 검증

**도구:** Glob

demos 객체의 각 `file` 경로가 실제로 존재하는지 확인합니다.

```bash
ls {file-path} 2>/dev/null || echo "MISSING: {file-path}"
```

**PASS:** 8개 파일 모두 존재
**FAIL:** 누락 파일 발견 — 파일 생성 또는 경로 수정 필요

### Step 5: curFiles 검증

**도구:** Grep, Glob

```bash
grep "openCurriculum(" index.html
```

curFiles 객체의 키(4개)와 카드의 openCurriculum 키를 대조하고, 각 파일이 존재하는지 확인합니다.

**PASS:** 4개 키 일치 + 4개 파일 모두 존재
**FAIL:** 키 불일치 또는 파일 누락

### Step 6: bizFiles 검증

**도구:** Grep, Glob

```bash
grep "openBizcool(" index.html
```

bizFiles 객체의 키(3개)와 카드의 openBizcool 키를 대조하고, 각 파일이 존재하는지 확인합니다.

**PASS:** 3개 키 일치 + 3개 파일 모두 존재
**FAIL:** 키 불일치 또는 파일 누락

### Step 7: 결과 보고

발견된 이슈를 테이블로 정리합니다.

## Output Format

```markdown
## 데모 등록 검증 결과

### 등록 현황

| 등록 객체 | 키 수 | 카드 수 | 파일 존재 |
|-----------|-------|---------|-----------|
| demos | N | N | N/N |
| curFiles | N | N | N/N |
| bizFiles | N | N | N/N |

### 이슈

| # | 유형 | 키/파일 | 문제 | 수정 방법 |
|---|------|---------|------|-----------|

### 결론: PASS / N개 이슈 발견
```

## Exceptions

다음은 **위반이 아닙니다**:

1. **mockup/ 디렉토리의 파일** — mockup/class-detail-*.html은 참고용 사본이므로 등록 대상이 아님
2. **design.html 파일** — `*-design.html` 파일은 디자인 참고용이며 demos 등록 대상이 아님
3. **education-showcase-v4.html** — 레거시 참고 페이지로 현재 등록 체계에 포함되지 않음
