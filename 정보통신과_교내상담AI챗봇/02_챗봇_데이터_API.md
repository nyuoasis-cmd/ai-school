# 📊 교내 AI 상담 도우미 — 데이터 & API 스펙

## 1. 샘플 응답 데이터 (sampleResponses.js)

```javascript
// 6개 빠른 질문에 대한 하드코딩 응답
export const sampleResponses = {

  meal: {
    userText: "오늘 급식 뭐야?",
    botText: "오늘 급식 알려줄게냥! 🍚 맛있는 메뉴다냥~",
    card: {
      type: "meal",
      date: "2월 6일 (목)",
      items: [
        { emoji: "🍚", name: "잡곡밥", cal: 310 },
        { emoji: "🍲", name: "김치찌개", cal: 180 },
        { emoji: "🥩", name: "돈까스", cal: 350 },
        { emoji: "🥗", name: "콩나물무침", cal: 45 },
        { emoji: "🍊", name: "귤", cal: 40 },
        { emoji: "🥛", name: "딸기우유", cal: 120 },
      ],
      totalCal: 1045,
    },
    afterText: "오늘은 돈까스 나오는 날이다냥! 😻 맛있게 먹으라냥~",
  },

  timetable: {
    userText: "이번 주 시간표 알려줘",
    botText: "이번 주 시간표 보여줄게냥! 📅",
    card: {
      type: "timetable",
      className: "정보통신과 2-1",
      todayIndex: 3, // 0=월 ~ 4=금, 목요일
      periods: [
        ["국어",   "수학",     "영어",       "네트워크", "체육"],
        ["수학",   "프로그래밍", "국어",       "네트워크", "체육"],
        ["프로그래밍","프로그래밍","데이터베이스","정보보안",  "영어"],
        ["프로그래밍","영어",     "데이터베이스","정보보안",  "수학"],
        ["정보보안", "국어",     "프로그래밍",  "한국사",   "데이터베이스"],
        ["한국사",  "네트워크",  "프로그래밍",  "한국사",   "데이터베이스"],
        ["창체",   "네트워크",  "자율",       "동아리",   "자율"],
      ],
    },
    afterText: "오늘은 목요일이라 네트워크 수업이 있다냥! 💻 보라색으로 표시해뒀으니 확인해냥~",
  },

  calendar: {
    userText: "학사일정 알려줘",
    botText: "이번 달 주요 일정 정리해봤다냥! 📋",
    card: {
      type: "calendar",
      month: "2026년 2월",
      events: [
        { day: 10, dow: "월", title: "학년말고사 시작", desc: "2/10(월) ~ 2/13(목) 4일간", tag: "exam" },
        { day: 17, dow: "월", title: "진로체험의 날", desc: "IT 기업 현장 방문 (판교)", tag: "event" },
        { day: 21, dow: "금", title: "졸업식", desc: "3학년 졸업식 (오전 10시 체육관)", tag: "event" },
        { day: 24, dow: "월", title: "겨울방학 시작", desc: "2/24(월) ~ 3/1(일)", tag: "holiday" },
      ],
    },
    afterText: "시험이 다음 주라냥..! 📚 공부 열심히 해야 한다냥 화이팅이다냥! 💪🐾",
  },

  place: {
    userText: "교무실 어디야?",
    botText: "교무실 위치 알려줄게냥! 🏫",
    card: null,
    afterText: `교무실은 <b>본관 2층 201호</b>다냥! 🐾

🏢 <b>자주 찾는 장소</b>
• 교무실: 본관 2층 201호
• 행정실: 본관 1층 103호
• 진로상담실: 별관 3층 302호
• 컴퓨터실: 별관 2층 204호
• 보건실: 본관 1층 105호
• 도서관: 별관 4층

길 잃으면 또 물어봐냥~ 😸`,
  },

  wifi: {
    userText: "와이파이 비번 뭐야?",
    botText: null,
    card: null,
    afterText: `학교 와이파이 정보다냥! 📶

📡 <b>학생용 Wi-Fi</b>
• SSID: <b>SCHOOL-STUDENT</b>
• 비밀번호: <b>info2026!</b>

📡 <b>실습실 Wi-Fi</b>
• SSID: <b>LAB-NET</b>
• 비밀번호: <b>lab@2026</b>

접속 안 되면 전산실(별관 201)에 문의해냥! 🐱`,
  },

  club: {
    userText: "동아리 정보 알려줘",
    botText: null,
    card: null,
    afterText: `정보통신과 동아리 정보다냥! 🎮

💻 <b>코딩 동아리 (CodeCat)</b>
• 활동: 웹/앱 개발, 해커톤 참가
• 시간: 목요일 7교시
• 장소: 별관 204호

🔒 <b>정보보안 동아리 (WhiteHat)</b>
• 활동: CTF 대회 준비, 보안 실습
• 시간: 수요일 방과후
• 장소: 별관 205호

🤖 <b>AI 동아리 (NeuroNet)</b>
• 활동: 머신러닝, AI 프로젝트
• 시간: 금요일 방과후
• 장소: 별관 204호

관심 있는 동아리 있으면 담당 선생님한테 얘기해보라냥! 😺`,
  },
};

// 키워드 매칭 정의
export const keywordMap = {
  meal: /급식|점심|밥|메뉴|먹/,
  timetable: /시간표|수업|몇교시/,
  calendar: /시험|일정|행사|졸업|방학/,
  place: /교무실|어디|위치|장소|보건실|도서관/,
  wifi: /와이파이|wifi|비번|비밀번호|인터넷/,
  club: /동아리|클럽/,
};

// 매칭 안 될 때 기본 응답
export const defaultReplies = [
  "오호~ 그건 잘 모르겠다냥 😿 선생님께 직접 물어보는 게 좋을 것 같다냥!",
  "음... 그 정보는 아직 없다냥! 🙀 나중에 업데이트해줄게냥~",
  "냥냥! 그건 교무실(본관 2층)에 문의해보라냥~ 🐾",
];
```

---

## 2. 학교 정보 데이터 (schoolInfo.js)

AI 시스템 프롬프트에 주입할 학교 정보.

```javascript
export const schoolInfo = {
  name: "한국정보통신고등학교",
  department: "정보통신과",
  class: "2학년 1반",
  year: 2026,

  // 급식 정보 (일별 업데이트 가능)
  todayMeal: {
    date: "2026-02-06",
    menu: ["잡곡밥(310kcal)", "김치찌개(180kcal)", "돈까스(350kcal)", "콩나물무침(45kcal)", "귤(40kcal)", "딸기우유(120kcal)"],
    totalCal: 1045,
  },

  // 시간표
  timetable: {
    mon: ["국어","수학","프로그래밍","프로그래밍","정보보안","한국사","창체"],
    tue: ["수학","프로그래밍","프로그래밍","영어","국어","네트워크","네트워크"],
    wed: ["영어","국어","데이터베이스","데이터베이스","프로그래밍","프로그래밍","자율"],
    thu: ["네트워크","네트워크","정보보안","정보보안","한국사","한국사","동아리"],
    fri: ["체육","체육","영어","수학","데이터베이스","데이터베이스","자율"],
  },

  // 학사일정
  events: [
    { date: "2026-02-10", title: "학년말고사 시작", detail: "2/10~2/13 4일간" },
    { date: "2026-02-17", title: "진로체험의 날", detail: "IT 기업 현장 방문 (판교)" },
    { date: "2026-02-21", title: "졸업식", detail: "3학년 졸업식 (오전 10시 체육관)" },
    { date: "2026-02-24", title: "겨울방학 시작", detail: "2/24 ~ 3/1" },
  ],

  // 장소 정보
  locations: {
    "교무실": "본관 2층 201호",
    "행정실": "본관 1층 103호",
    "진로상담실": "별관 3층 302호",
    "컴퓨터실": "별관 2층 204호",
    "보건실": "본관 1층 105호",
    "도서관": "별관 4층",
    "전산실": "별관 2층 201호",
    "체육관": "운동장 옆 별도 건물",
  },

  // 와이파이
  wifi: {
    student: { ssid: "SCHOOL-STUDENT", password: "info2026!" },
    lab: { ssid: "LAB-NET", password: "lab@2026" },
  },

  // 동아리
  clubs: [
    { name: "CodeCat", emoji: "💻", desc: "코딩 동아리", activity: "웹/앱 개발, 해커톤", time: "목 7교시", room: "별관 204호" },
    { name: "WhiteHat", emoji: "🔒", desc: "정보보안 동아리", activity: "CTF 대회, 보안 실습", time: "수 방과후", room: "별관 205호" },
    { name: "NeuroNet", emoji: "🤖", desc: "AI 동아리", activity: "머신러닝, AI 프로젝트", time: "금 방과후", room: "별관 204호" },
  ],
};
```

---

## 3. OpenAI API 연동 (chat.js)

### 시스템 프롬프트

```javascript
import { schoolInfo } from '../data/schoolInfo';

export function buildSystemPrompt() {
  return `너는 "${schoolInfo.name}" ${schoolInfo.department}의 AI 도우미 "또리"야.
귀여운 고양이 캐릭터이고, 항상 "~다냥", "~냥" 말투를 써.
이모지도 적절히 사용해. 🐱🐾

학교 정보:
- 급식: ${JSON.stringify(schoolInfo.todayMeal)}
- 시간표: ${JSON.stringify(schoolInfo.timetable)}
- 학사일정: ${JSON.stringify(schoolInfo.events)}
- 장소: ${JSON.stringify(schoolInfo.locations)}
- 와이파이: ${JSON.stringify(schoolInfo.wifi)}
- 동아리: ${JSON.stringify(schoolInfo.clubs)}

규칙:
1. 위 학교 정보를 기반으로 정확하게 답변해.
2. 모르는 건 솔직하게 "잘 모르겠다냥" 하고 교무실 방문을 추천해.
3. 항상 친근하고 밝은 톤 유지.
4. 답변은 간결하게 (3~5문장).
5. 학교 정보와 관련 없는 질문에도 친절히 응대하되, 학교 관련 질문으로 유도해.`;
}
```

### API 호출 코드

```javascript
// /api/chat.js (서버 라우트)
import { buildSystemPrompt } from '../data/schoolInfo';

export async function POST(req) {
  const { message, history = [] } = await req.json();

  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`,
    },
    body: JSON.stringify({
      model: 'gpt-4o-mini',
      messages: [
        { role: 'system', content: buildSystemPrompt() },
        ...history,
        { role: 'user', content: message },
      ],
      max_tokens: 500,
      temperature: 0.7,
    }),
  });

  const data = await response.json();
  const reply = data.choices[0].message.content;

  return Response.json({ reply });
}
```

### 프론트에서 호출

```javascript
// hooks/useChat.js
import { sampleResponses, keywordMap, defaultReplies } from '../data/sampleResponses';

export function useChat() {
  const [messages, setMessages] = useState([]);
  const [isTyping, setIsTyping] = useState(false);
  const [showWelcome, setShowWelcome] = useState(true);

  // 키워드 매칭 시도
  function matchKeyword(text) {
    for (const [key, regex] of Object.entries(keywordMap)) {
      if (regex.test(text)) return key;
    }
    return null;
  }

  // 메시지 전송
  async function sendMessage(text, quickKey = null) {
    setShowWelcome(false);

    // 1. 유저 메시지 추가
    const userMsg = { role: 'user', text: quickKey ? sampleResponses[quickKey].userText : text };
    setMessages(prev => [...prev, userMsg]);

    // 2. 빠른 질문이면 하드코딩 응답
    const matched = quickKey || matchKeyword(text);
    if (matched && sampleResponses[matched]) {
      await showHardcodedResponse(sampleResponses[matched]);
      return;
    }

    // 3. 매칭 안 되면 AI API 호출
    setIsTyping(true);
    try {
      const res = await fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text, history: messages }),
      });
      const { reply } = await res.json();
      setIsTyping(false);
      setMessages(prev => [...prev, { role: 'bot', text: reply }]);
    } catch (err) {
      setIsTyping(false);
      const fallback = defaultReplies[Math.floor(Math.random() * defaultReplies.length)];
      setMessages(prev => [...prev, { role: 'bot', text: fallback }]);
    }
  }

  // 하드코딩 응답 순차 표시
  async function showHardcodedResponse(response) {
    const delay = (ms) => new Promise(r => setTimeout(r, ms));

    if (response.botText) {
      setIsTyping(true);
      await delay(600);
      setIsTyping(false);
      setMessages(prev => [...prev, { role: 'bot', text: response.botText }]);
    }

    if (response.card) {
      setIsTyping(true);
      await delay(600);
      setIsTyping(false);
      setMessages(prev => [...prev, { role: 'bot', card: response.card }]);
    }

    if (response.afterText) {
      setIsTyping(true);
      await delay(600);
      setIsTyping(false);
      setMessages(prev => [...prev, { role: 'bot', text: response.afterText }]);
    }
  }

  return { messages, isTyping, showWelcome, sendMessage };
}
```

---

## 4. 환경 변수

Replit Secrets에 설정:

```
OPENAI_API_KEY=sk-...
```

---

## 5. 핵심 로직 요약

### 메시지 분기 흐름

```
사용자 입력
  ├─ 빠른 질문 버튼 클릭 → 해당 quickKey로 하드코딩 응답
  ├─ 직접 입력 + 키워드 매칭 성공 → 하드코딩 응답
  └─ 직접 입력 + 키워드 매칭 실패 → OpenAI API 호출
```

### 카드 렌더링 분기

```javascript
// MessageBubble.jsx 내부
if (msg.card) {
  switch (msg.card.type) {
    case 'meal':     return <MealCard data={msg.card} />;
    case 'timetable': return <TimetableCard data={msg.card} />;
    case 'calendar':  return <CalendarCard data={msg.card} />;
  }
}
if (msg.text) {
  // dangerouslySetInnerHTML로 <b>, <br> 처리
  return <div dangerouslySetInnerHTML={{ __html: msg.text }} />;
}
```

### 태그 스타일 매핑

```javascript
const tagStyles = {
  exam:    { bg: '#FDF0F7', color: '#EC4899', label: '시험' },
  event:   { bg: '#EBF2FF', color: '#3B82F6', label: '행사' },
  holiday: { bg: '#E6FAF2', color: '#10B981', label: '방학' },
};
```

---

## 6. 구현 우선순위

| 순서 | 항목 | 상세 |
|------|------|------|
| 1 | 기본 레이아웃 | 헤더 + 채팅영역 + 입력창 |
| 2 | 웰컴 + 버튼 | 웰컴카드 + 6개 빠른 질문 (1열) |
| 3 | 메시지 버블 | 유저(우)/봇(좌) 버블 + 아바타 |
| 4 | 하드코딩 응답 | 6개 빠른 질문 답변 (텍스트만) |
| 5 | 카드 컴포넌트 | 급식/시간표/학사일정 카드 3종 |
| 6 | 타이핑 효과 | 인디케이터 + 순차 등장 |
| 7 | 키워드 매칭 | 직접 입력 시 자동 분류 |
| 8 | AI API 연동 | OpenAI 호출 (매칭 실패 시) |
| 9 | 데스크탑 프레임 | 390x844 폰 프레임 |
| 10 | 애니메이션 | fadeUp, slideIn 등 |
