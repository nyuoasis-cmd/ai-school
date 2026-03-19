# AI School

직업계고/특성화고 대상 AI 교육 쇼케이스 사이트 (ai.teachermate.co.kr)

## Tech Stack

- **Frontend**: 순수 HTML/CSS/JS (프레임워크 없음)
- **배포**: GitHub Pages
- **폰트**: Google Fonts (Noto Sans KR, JetBrains Mono, Sora)

## 구조

- `index.html` — AI 중점학교 랜딩페이지 (공문 유입용, 폼→운영자 대시보드)
- `showcase.html` — 기존 메인 쇼케이스 (학과 카드, 커리큘럼 카드, 비즈쿨 카드) — UI에서 숨김
- `404.html` — SPA 라우팅 (`/ai-school/{학교코드}` → `/?school={학교코드}`)
- `{학과명}/*-v2.html` — 8개 학과별 앱 데모
- `class-detail*.html` — 커리큘럼 상세 (2h/4h/6h/8h)
- `bizcool-detail*.html` — 비즈쿨 상세 (4h/8h/12h)
- `image/*-thumb.png` — 8개 앱 썸네일 이미지
- `mockup/06.*/*.jpg` — 수업 현장 사진

## 랜딩페이지 (index.html)

- **URL**: `ai.teachermate.co.kr/ai-school/{학교코드}?utm_source=gongmun&...`
- **폼 제출**: `POST https://teachermate.co.kr/api/contact` (source: "ai-school-landing")
- **GA4**: GTM-PKXBMKWW, 이벤트: page_view, sample_app_click, modal_open, form_submit
- **학교코드**: 404.html이 `/ai-school/{code}` → `/?school={code}`로 리다이렉트, index.html이 읽음

## Skills

| 스킬 | 설명 |
|------|------|
| `verify-demo-registry` | 데모/커리큘럼 등록 일관성 검증 (demos 객체, curFiles, bizFiles ↔ 카드 ↔ 파일) |
| `verify-app-frame` | 앱 프레임 패턴 검증 (app-frame, app-header, max-width:430px) |
