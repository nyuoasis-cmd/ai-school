# 세션 핸드오프 - 2026.02.07

## 오늘 완료한 작업

### 1. ai-school GitHub 연동 및 배포
- GitHub repo: https://github.com/nyuoasis-cmd/ai-school (public)
- GitHub Pages 배포 완료: https://ai.teachermate.co.kr
- 예스닉 DNS CNAME: `ai` → `nyuoasis-cmd.github.io`
- TODO: GitHub Pages Settings에서 **Enforce HTTPS** 체크 필요

### 2. 3개 서비스 네비바 연동
| 사이트 | 로컬 포트 | 프로덕션 URL |
|--------|-----------|-------------|
| youthschool (문서행정) | 5000 | teachermate.co.kr |
| teacher-toolkit (수업도구) | 5001 | tools.teachermate.co.kr |
| ai-school (AI교육) | 5002 | ai.teachermate.co.kr |

- 세 사이트 네비바에서 서로 이동 가능 (로컬/프로덕션 URL 자동 분기)
- '위탁교육' → 'AI교육'으로 버튼명 변경 완료

### 3. UI 수정사항
- ai-school 네비바 보더라인 밝은 회색으로 변경
- ai-school 히어로 제목: "모바일 기기로 배우는 / 청소년 AI 스쿨"
- teacher-toolkit 네비바 배경색 #F8F7F4
- 안전점검 비계작업 카드 unsplash 이미지로 복원

### 4. youthschool 회원가입 개선
- '담당' → '소속' 변경 (계급 → 부서 기반)
  - 행정실, 교무실, 급식실, 도서관, 상담실, 방과후/돌봄, 시설관리, 전산실, 기타
- '담당 업무' 섹션 제거

### 5. 전체 push 완료
- ai-school → nyuoasis-cmd/ai-school
- youthschool → nyuoasis-cmd/youthschool-mvp-complete
- teacher-toolkit → nyuoasis-cmd/Teacher-Toolkit

---

## 내일 할 일: 학교 영업 및 홍보

### 문서24 공문 발송
- 문서24를 통해 학교에 AI 위탁교육 프로그램 공문 보내기
- 공문 내용 작성 필요 (대상: 직업계고, 특성화고)
- 공문 발송 절차 및 자격 요건 확인

### 논의할 주제
1. **타겟 학교 선정** - 어떤 학교/학과에 먼저 영업할 것인가?
2. **공문 내용 작성** - 학교 담당자가 관심 가질 만한 포인트는?
3. **체험판 활용 전략** - ai.teachermate.co.kr 링크를 공문에 포함?
4. **후속 영업 프로세스** - 공문 발송 후 전화/방문 등 다음 단계
5. **가격 정책** - 위탁교육 단가 설정

### Render 관련
- ai-school은 GitHub Pages로 이전 완료
- Render의 ai-school Static Site는 삭제 가능 (Custom Domain 슬롯 회수)
