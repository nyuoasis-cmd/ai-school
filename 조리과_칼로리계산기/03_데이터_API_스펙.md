# 📦 데이터 구조 & AI API 연동

## 1. 샘플 음식 데이터 (sampleMeals.js)

샘플 음식은 하드코딩. 체험 그리드에서 탭하면 바로 결과 표시.

```javascript
export const sampleMeals = [
  {
    id: 0,
    name: "한식 정식",
    totalCal: 685,
    carb: 55,      // %
    protein: 25,   // %
    fat: 20,       // %
    img: "https://images.unsplash.com/photo-1580651315530-69c8e0026377?w=600&h=400&fit=crop",
    foods: [
      {
        name: "쌀밥",
        qty: "1공기 (200g)",
        cal: 310,
        img: "https://images.unsplash.com/photo-1536304993881-460e32f50dc2?w=100&h=100&fit=crop"
      },
      {
        name: "김치찌개",
        qty: "1인분",
        cal: 200,
        img: "https://images.unsplash.com/photo-1498654896293-37aacf113fd9?w=100&h=100&fit=crop"
      },
      {
        name: "겉절이",
        qty: "1접시",
        cal: 45,
        img: "https://images.unsplash.com/photo-1583224994076-0a3a25d57799?w=100&h=100&fit=crop"
      },
      {
        name: "계란말이",
        qty: "2조각",
        cal: 130,
        img: "https://images.unsplash.com/photo-1482049016688-2d3e1b311543?w=100&h=100&fit=crop"
      }
    ]
  },
  {
    id: 1,
    name: "크림 파스타",
    totalCal: 780,
    carb: 48,
    protein: 22,
    fat: 30,
    img: "https://images.unsplash.com/photo-1612874742237-6526221588e3?w=600&h=400&fit=crop",
    foods: [
      {
        name: "크림 파스타",
        qty: "1인분 (350g)",
        cal: 620,
        img: "https://images.unsplash.com/photo-1612874742237-6526221588e3?w=100&h=100&fit=crop"
      },
      {
        name: "마늘빵",
        qty: "2조각",
        cal: 120,
        img: "https://images.unsplash.com/photo-1549931319-a545dcf3bc73?w=100&h=100&fit=crop"
      },
      {
        name: "탄산음료",
        qty: "1잔",
        cal: 40,
        img: "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?w=100&h=100&fit=crop"
      }
    ]
  },
  {
    id: 2,
    name: "햄버거 세트",
    totalCal: 1050,
    carb: 42,
    protein: 28,
    fat: 30,
    img: "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600&h=400&fit=crop",
    foods: [
      {
        name: "치즈버거",
        qty: "1개",
        cal: 520,
        img: "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=100&h=100&fit=crop"
      },
      {
        name: "감자튀김",
        qty: "미디움",
        cal: 340,
        img: "https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=100&h=100&fit=crop"
      },
      {
        name: "콜라",
        qty: "미디움",
        cal: 190,
        img: "https://images.unsplash.com/photo-1629203851122-3726ecdf080e?w=100&h=100&fit=crop"
      }
    ]
  },
  {
    id: 3,
    name: "비빔밥",
    totalCal: 580,
    carb: 52,
    protein: 28,
    fat: 20,
    img: "https://images.unsplash.com/photo-1553163147-622ab57be1c7?w=600&h=400&fit=crop",
    foods: [
      {
        name: "잡곡밥",
        qty: "1공기",
        cal: 280,
        img: "https://images.unsplash.com/photo-1536304993881-460e32f50dc2?w=100&h=100&fit=crop"
      },
      {
        name: "나물",
        qty: "5종",
        cal: 120,
        img: "https://images.unsplash.com/photo-1583224994076-0a3a25d57799?w=100&h=100&fit=crop"
      },
      {
        name: "고추장소스",
        qty: "2T",
        cal: 60,
        img: "https://images.unsplash.com/photo-1635379771110-7ccaf3b04aed?w=100&h=100&fit=crop"
      },
      {
        name: "달걀프라이",
        qty: "1개",
        cal: 120,
        img: "https://images.unsplash.com/photo-1482049016688-2d3e1b311543?w=100&h=100&fit=crop"
      }
    ]
  },
  {
    id: 4,
    name: "샐러드 볼",
    totalCal: 320,
    carb: 35,
    protein: 38,
    fat: 27,
    img: "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600&h=400&fit=crop",
    foods: [
      {
        name: "믹스 채소",
        qty: "1볼",
        cal: 45,
        img: "https://images.unsplash.com/photo-1540420773420-3366772f4999?w=100&h=100&fit=crop"
      },
      {
        name: "그릴 치킨",
        qty: "100g",
        cal: 165,
        img: "https://images.unsplash.com/photo-1532550907401-a500c9a57435?w=100&h=100&fit=crop"
      },
      {
        name: "드레싱",
        qty: "2T",
        cal: 80,
        img: "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=100&h=100&fit=crop"
      },
      {
        name: "파마산",
        qty: "1T",
        cal: 30,
        img: "https://images.unsplash.com/photo-1486297678162-eb2a19b0a32d?w=100&h=100&fit=crop"
      }
    ]
  },
  {
    id: 5,
    name: "라면",
    totalCal: 550,
    carb: 58,
    protein: 18,
    fat: 24,
    img: "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=600&h=400&fit=crop",
    foods: [
      {
        name: "라면",
        qty: "1봉지",
        cal: 500,
        img: "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=100&h=100&fit=crop"
      },
      {
        name: "계란",
        qty: "1개",
        cal: 30,
        img: "https://images.unsplash.com/photo-1482049016688-2d3e1b311543?w=100&h=100&fit=crop"
      },
      {
        name: "대파·김치",
        qty: "약간",
        cal: 20,
        img: "https://images.unsplash.com/photo-1583224994076-0a3a25d57799?w=100&h=100&fit=crop"
      }
    ]
  }
];
```

---

## 2. 히스토리 상태 구조

```javascript
// useHistory.js (React state 또는 localStorage)
const [history, setHistory] = useState([]);

// 저장 시 추가되는 객체
{
  ...meal,               // sampleMeals 데이터 그대로
  slot: 0,               // 0=아침, 1=점심, 2=간식, 3=저녁
  timestamp: Date.now()   // 저장 시각
}

// 시간대 순환: 저장할 때마다 0→1→2→3→0→... (데모용 간편 로직)
// 또는 실제 시간 기반: 6-10시=아침, 11-14시=점심, 14-17시=간식, 17시~=저녁
```

### 시간대 메타데이터

```javascript
export const mealSlots = [
  { name: "아침", emoji: "🌅", bgClass: "yellow-light" },
  { name: "점심", emoji: "☀️", bgClass: "accent-light" },
  { name: "간식", emoji: "🍪", bgClass: "blue-light" },
  { name: "저녁", emoji: "🌙", bgClass: "green-light" },
];
```

---

## 3. AI API 연동 (실제 카메라 촬영 시)

### 3-1. 사진 → Base64 변환

```javascript
// 카메라 또는 갤러리에서 이미지 받기
const handleImageUpload = async (file) => {
  const base64 = await fileToBase64(file);
  const result = await analyzeFood(base64);
  showResult(result);
};

function fileToBase64(file) {
  return new Promise((resolve) => {
    const reader = new FileReader();
    reader.onload = () => resolve(reader.result.split(',')[1]);
    reader.readAsDataURL(file);
  });
}
```

### 3-2. OpenAI Vision API 호출

```javascript
// analyzeFood.js
export async function analyzeFood(base64Image) {
  const response = await fetch('https://api.openai.com/v1/chat/completions', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${process.env.OPENAI_API_KEY}`
    },
    body: JSON.stringify({
      model: "gpt-4o-mini",
      messages: [
        {
          role: "system",
          content: `당신은 음식 영양 분석 전문가입니다.
사진 속 음식을 분석하여 아래 JSON 형식으로만 응답하세요.
다른 텍스트 없이 JSON만 출력하세요.

{
  "name": "음식 전체 이름",
  "totalCal": 총칼로리(숫자),
  "carb": 탄수화물비율(숫자, %),
  "protein": 단백질비율(숫자, %),
  "fat": 지방비율(숫자, %),
  "foods": [
    {
      "name": "개별 음식명",
      "qty": "분량 설명",
      "cal": 칼로리(숫자)
    }
  ]
}`
        },
        {
          role: "user",
          content: [
            {
              type: "image_url",
              image_url: {
                url: `data:image/jpeg;base64,${base64Image}`,
                detail: "low"
              }
            },
            {
              type: "text",
              text: "이 음식의 칼로리와 영양소를 분석해주세요."
            }
          ]
        }
      ],
      max_tokens: 500,
      temperature: 0.3
    })
  });

  const data = await response.json();
  const content = data.choices[0].message.content;

  // JSON 파싱 (코드블록 제거)
  const cleaned = content.replace(/```json|```/g, '').trim();
  const result = JSON.parse(cleaned);

  // 실제 API 결과에는 이미지가 없으므로 기본 이미지 설정
  result.img = URL.createObjectURL(file);  // 촬영한 원본 사진
  result.foods = result.foods.map(f => ({
    ...f,
    img: result.img  // 또는 기본 placeholder
  }));

  return result;
}
```

### 3-3. 흐름 분기

```
사용자 액션
├─ 샘플 음식 탭 → sampleMeals[i] 데이터 즉시 사용 (로딩 연출만)
├─ 카메라 촬영  → 사진 → base64 → OpenAI API → 결과 (실제 로딩)
└─ 갤러리 선택  → 사진 → base64 → OpenAI API → 결과 (실제 로딩)
```

### 3-4. 환경변수

```
OPENAI_API_KEY=sk-...
```

Replit Secrets에 저장. 프론트엔드에서 직접 호출하지 않고 **서버 API 라우트를 통해 호출** 권장:

```
POST /api/analyze
Body: { image: base64string }
→ OpenAI API 호출
→ Response: meal 객체
```

---

## 4. 핵심 계산 로직

### 일일 섭취량 게이지
```javascript
const dailyTarget = 2000; // kcal
const totalToday = history.reduce((sum, h) => sum + h.totalCal, 0);
const percentage = Math.min(Math.round(totalToday / dailyTarget * 100), 100);

// 색상 분기
const gaugeColor = percentage > 90
  ? 'linear-gradient(90deg, var(--green), var(--accent))'  // 경고
  : 'var(--green)';  // 정상
```

### 히스토리 그룹핑
```javascript
const grouped = {};
history.forEach(h => {
  if (!grouped[h.slot]) grouped[h.slot] = [];
  grouped[h.slot].push(h);
});
// Object.keys(grouped).sort() 로 시간대 순서 보장
```
