# AI School

직업계고/특성화고 대상 AI 교육 쇼케이스 사이트 (ai.teachermate.co.kr)

## Tech Stack

- **Frontend**: 순수 HTML/CSS/JS (프레임워크 없음)
- **배포**: GitHub Pages
- **폰트**: Google Fonts (Noto Sans KR, JetBrains Mono, Sora)

## 구조

- `index.html` — 메인 페이지 (학과 카드, 커리큘럼 카드, 비즈쿨 카드)
- `{학과명}/*-v2.html` — 8개 학과별 앱 데모
- `class-detail*.html` — 커리큘럼 상세 (2h/4h/6h/8h)
- `bizcool-detail*.html` — 비즈쿨 상세 (4h/8h/12h)

## Skills

| 스킬 | 설명 |
|------|------|
| `verify-demo-registry` | 데모/커리큘럼 등록 일관성 검증 (demos 객체, curFiles, bizFiles ↔ 카드 ↔ 파일) |
| `verify-app-frame` | 앱 프레임 패턴 검증 (app-frame, app-header, max-width:430px) |
