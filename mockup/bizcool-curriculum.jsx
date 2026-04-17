import { useState, useEffect } from "react";

/* ═══════════════════════════════════════════════
   DATA — 4 / 8 / 12차시
   각 블록은 독립 판매 가능 · 이전 블록 위에 확장
   ═══════════════════════════════════════════════ */
const C = [
{
  id:"s4", tier:"스타터", hours:"4차시", meta:"50분 × 4교시 · 2회 방문",
  visits:["1회차","2회차"],
  title:"AI 창업 아이디어 스프린트",
  desc:"스타트업 바이블 핵심 프레임워크로 시장을 분석하고, AI 도구를 활용해 창업 아이디어를 비즈니스 모델로 완성하는 단기 집중 과정입니다.",
  tags:["시장세분화","AI 리서치","BMC","SCAMPER"],
  hl:{icon:"🔥",text:"AI로 시장분석부터 피칭까지 2회 완성!"},
  col:"#00d68f", dim:"#00d68f15",
  prereq: null,
  grad:"🎓 아이디어 제안서 + 1분 피칭 영상",
  flow:"발견하고 → 고객 찾고 → 모델 만들고 → 다듬어서 발표",
  detail:[
    {visit:"1회차",vt:"아이디어 발굴 & AI 시장분석",classes:[
      {n:"1",t:"창업 마인드셋 & 시장세분화",step:"STEP 01",ref:"스타트업 바이블 1단계",min:50,type:"이론+실습",
       desc:"「사업에 필요한 단 하나의 필요충분조건은 돈을 지불하는 실고객이다」 — 고객 중심 사고를 배우고, 브레인스토밍으로 6~12개 잠재시장을 탐색합니다.",
       act:["일상 속 불편함 발견 워크숍","시장 기회 매트릭스 작성 (7가지 평가 기준)","'모두가 내 고객' 함정 & '차이나 신드롬' 토론"],
       tools:["ChatGPT","Perplexity"],out:"시장 기회 매트릭스"},
      {n:"2",t:"AI 고객 리서치 & 페르소나",step:"STEP 02",ref:"스타트업 바이블 5단계",min:50,type:"실습",
       desc:"AI로 목표고객 페르소나를 설계하고 모의 고객 인터뷰를 진행합니다. 최종사용자와 의사결정권자를 구분하고 선도고객을 식별합니다.",
       act:["AI로 페르소나 카드 자동 생성","ChatGPT 역할극: 고객 인터뷰 시뮬레이션","거점시장 선정 & 발표"],
       tools:["ChatGPT","Claude"],out:"페르소나 카드 + 거점시장"}
    ]},
    {visit:"2회차",vt:"비즈니스 모델 & 피칭대회",classes:[
      {n:"3",t:"비즈니스 모델 캔버스 설계",step:"STEP 03",ref:"스타트업 바이블 15단계",min:50,type:"실습",
       desc:"고객이 왜 돈을 지불하는지 정의하고, BMC 9블록을 AI 도구로 작성합니다. 수익모델과 가치제안을 구체화합니다.",
       act:["가치제안 캔버스 작성","AI 기반 BMC 9블록 자동 완성","수익모델 시뮬레이션"],
       tools:["ChatGPT","Canva"],out:"BMC + 수익모델"},
      {n:"4",t:"SCAMPER 아이디어 고도화 & 피칭대회",step:"STEP 04",ref:"비즈쿨 융합교안 + 데모데이",min:50,type:"발표",
       desc:"SCAMPER 7가지 발상법으로 아이디어를 한 단계 더 확장합니다. 1분 엘리베이터 피칭 대회로 Block 1을 마무리하고, 동료 투표와 시상으로 최고의 아이디어를 선정합니다.",
       act:["SCAMPER 발상법 워크숍 (대체·결합·응용·변형·용도전환·제거·재배열)","AI로 피칭 스크립트 초안 생성 & 1분 피칭대회","동료 투표 & 우수 아이디어 시상"],
       tools:["ChatGPT","Google Slides"],out:"아이디어 제안서 + 피칭 영상"}
    ]}
  ]
},
{
  id:"s8", tier:"빌더", hours:"8차시", meta:"50분 × 8교시 · 4회 방문",
  visits:["3회차","4회차"],
  title:"AI 앱 스타트업 빌딩",
  desc:"검증된 아이디어를 바이브코딩으로 실제 AI 앱으로 구현합니다. 기업가정신 사례로 영감을 충전하고, MVP 런칭 쇼케이스로 세상에 공개합니다.",
  tags:["바이브코딩","MVP 개발","기업가정신","사회적 가치"],
  hl:{icon:"💻",text:"프롬프트로 만드는 AI 앱 스타트업 체험"},
  col:"#4e8cff", dim:"#4e8cff15",
  prereq:"4차시 포함",
  grad:"🎓 작동하는 AI 앱 + 데모 영상",
  flow:"만들고 → 고치고 → 의미 입히고 → 세상에 보여주고",
  detail:[
    {visit:"3회차",vt:"바이브코딩 MVP 개발",classes:[
      {n:"5",t:"바이브코딩 입문 & 프로토타입",step:"STEP 05",ref:"스타트업 바이블 18단계",min:50,type:"실습",
       desc:"프롬프트로 앱을 만드는 바이브코딩 실습. 기획서를 AI에게 전달하여 작동하는 프로토타입을 제작합니다.",
       act:["바이브코딩 기초: 프롬프트 → 코드","기획서 기반 AI 앱 프로토타입 제작","라이브 코딩 시연"],
       tools:["Replit","Bolt.new"],out:"AI 앱 프로토타입 v1"},
      {n:"6",t:"UI/UX 개선 & 기능 고도화",step:"STEP 06",ref:"스타트업 바이블 23단계",min:50,type:"실습",
       desc:"동료 테스트로 사용성 피드백 수집. UI 개선과 핵심 기능을 추가하여 앱을 고도화합니다.",
       act:["동료 사용자 테스트 (3명 이상)","피드백 기반 UI/UX 개선","핵심 기능 추가 & 버그 수정"],
       tools:["Replit","ChatGPT"],out:"AI 앱 v2 (고도화)"}
    ]},
    {visit:"4회차",vt:"기업가정신 & MVP 런칭",classes:[
      {n:"7",t:"기업가정신 & 사회적 가치 설계",step:"STEP 07",ref:"비즈쿨 융합교안 7차시",min:50,type:"이론+실습",
       desc:"구글·아마존의 창업 스토리와 사회적기업 사례를 통해 기업가정신을 이해합니다. 우리 앱에 사회적 가치를 입히는 워크숍으로 제품의 의미를 확장합니다.",
       act:["구글·아마존 창업 스토리 & 기업가정신 핵심 역량","사회적기업 사례 분석 (쿠키아·CSV 등)","우리 AI 앱에 사회적 가치 입히기 워크숍"],
       tools:["ChatGPT","영상 자료"],out:"가치선언문 + 앱 v2 보완"},
      {n:"8",t:"MVP 런칭 쇼케이스",step:"STEP 08",ref:"데모데이",min:50,type:"발표",
       desc:"완성된 AI 앱을 동료들에게 라이브로 시연합니다. 실제 사용자 체험 → 피드백 수집 → 회고로 Block 2를 마무리합니다.",
       act:["AI 앱 라이브 시연 & 동료 체험","사용자 피드백 수집 (3가지 개선점 + 1가지 칭찬)","Block 2 회고 & 다음 단계 액션플랜"],
       tools:["라이브 시연","Google Forms"],out:"데모 영상 + 피드백 리포트"}
    ]}
  ]
},
{
  id:"s12", tier:"프로",hours:"12차시", meta:"50분 × 12교시 · 6회 방문",
  visits:["5회차","6회차"],
  title:"고객검증 & 실전 마케팅",
  desc:"실제 사용자 테스트로 앱을 검증하고, 피드백을 반영해 최종 버전을 완성합니다. STP 마케팅 전략과 AI 콘텐츠 제작으로 실전 마케팅을 경험하고, 최종 데모데이로 마무리합니다.",
  tags:["사용자 테스트","앱 고도화","STP 마케팅","데모데이"],
  hl:{icon:"📊",text:"테스트 → 개선 → 마케팅 → 최종 발표"},
  col:"#a855f7", dim:"#a855f715",
  prereq:"8차시 포함",
  grad:"🎓 최종 AI 앱 + 마케팅 키트 + 사업계획서",
  flow:"테스트하고 → 고치고 → 알리고 → 보여주고",
  detail:[
    {visit:"5회차",vt:"고객검증 & 앱 고도화",classes:[
      {n:"9",t:"사용자 테스트 & 데이터 수집",step:"STEP 09",ref:"스타트업 바이블 23단계",min:50,type:"실습",
       desc:"우리 앱을 실제로 쓸 사람에게 직접 보여주고 반응을 확인합니다. 5명 이상의 사용자에게 MVP를 테스트하고, 정량/정성 피드백 데이터를 체계적으로 수집합니다.",
       act:["사용자 테스트 프로토콜 설계 (과제·관찰·질문)","최소 5명 대상 MVP 테스트 진행","피드백 데이터 정리 & 핵심 인사이트 도출"],
       tools:["Google Forms","ChatGPT"],out:"테스트 결과 보고서"},
      {n:"10",t:"피드백 반영 & 앱 고도화",step:"STEP 10",ref:"스타트업 바이블 23단계",min:50,type:"실습",
       desc:"수집된 피드백을 우선순위로 정리하고, 핵심 개선점을 반영하여 앱을 최종 버전으로 업데이트합니다. '가장 많이 나온 불만 1순위'부터 해결합니다.",
       act:["피드백 우선순위 매트릭스 작성 (임팩트 × 난이도)","핵심 개선점 Top 3 반영 & 앱 v3 업데이트","개선 전후 비교 시연"],
       tools:["Replit","ChatGPT"],out:"AI 앱 v3 (최종 버전)"}
    ]},
    {visit:"6회차",vt:"실전 마케팅 & 최종 데모데이",classes:[
      {n:"11",t:"STP 마케팅 전략 & AI 콘텐츠 제작",step:"STEP 11",ref:"창업실무 마케팅 전략",min:50,type:"실습",
       desc:"STP(시장세분화-타겟팅-포지셔닝) 전략을 수립하고 4P 마케팅 믹스를 설계합니다. AI 도구로 로고, SNS 콘텐츠, 홍보 영상을 직접 제작합니다.",
       act:["STP 전략 수립 워크숍 (세분화 → 타겟 → 포지셔닝맵)","4P 마케팅 믹스 설계 (제품·가격·유통·촉진)","AI로 로고 · SNS 콘텐츠 · 30초 홍보영상 제작"],
       tools:["ChatGPT","Canva","미리캔버스"],out:"마케팅 키트 (전략서 + 콘텐츠)"},
      {n:"12",t:"최종 쇼케이스: 데모데이",step:"STEP 12",ref:"데모데이",min:50,type:"발표",
       desc:"전 과정의 집대성. AI 앱 라이브 시연과 3분 사업발표를 진행하고, 심사위원 Q&A와 카테고리별 시상으로 전체 교육을 마무리합니다.",
       act:["AI 앱 라이브 시연 + 3분 사업발표 (앱·마케팅·BM 종합)","심사위원 Q&A & 동료 피드백","카테고리별 시상 & 최종 포트폴리오 전달"],
       tools:["Google Slides","라이브 시연"],out:"사업계획서 + 최종 포트폴리오"}
    ]}
  ]
}
];

/* ═══════════════════════════════════════════════
   TYPE BADGE
   ═══════════════════════════════════════════════ */
const TC = {
  "이론+실습":{bg:"#4e8cff18",c:"#4e8cff",i:"📖"},
  "실습":{bg:"#00d68f18",c:"#00d68f",i:"⚡"},
  "발표":{bg:"#fbbf2418",c:"#fbbf24",i:"🎤"},
};

/* ═══════════════════════════════════════════════
   CLASS CARD (inside modal)
   ═══════════════════════════════════════════════ */
function ClassCard({cls, col}){
  const tc = TC[cls.type]||TC["실습"];
  return(
    <div style={{background:"#1a1a28",border:"1px solid #ffffff08",borderRadius:14,overflow:"hidden"}}>
      <div style={{padding:"20px 22px 14px",display:"flex",alignItems:"flex-start",justifyContent:"space-between",gap:12}}>
        <div style={{flex:1}}>
          <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:8,flexWrap:"wrap"}}>
            <span style={{fontFamily:"'JetBrains Mono',monospace",fontSize:11,fontWeight:700,color:col,letterSpacing:1}}>{cls.step}</span>
            <span style={{fontSize:10,color:"#555",fontFamily:"'JetBrains Mono',monospace"}}>· {cls.ref}</span>
          </div>
          <h3 style={{fontSize:16,fontWeight:700,color:"#e8e8f0",margin:0}}>{cls.t}</h3>
        </div>
        <div style={{display:"flex",gap:6,flexShrink:0,alignItems:"center"}}>
          <span style={{fontFamily:"'JetBrains Mono',monospace",fontSize:10,fontWeight:600,color:tc.c,background:tc.bg,padding:"4px 8px",borderRadius:5}}>{tc.i} {cls.type}</span>
          <span style={{fontFamily:"'JetBrains Mono',monospace",fontSize:10,color:"#555",background:"#ffffff06",padding:"4px 8px",borderRadius:5}}>{cls.min}분</span>
        </div>
      </div>
      <div style={{padding:"0 22px 14px"}}>
        <p style={{fontSize:13.5,color:"#999",lineHeight:1.75,fontWeight:300,margin:0}}>{cls.desc}</p>
      </div>
      <div style={{padding:"0 22px 14px"}}>
        <div style={{fontFamily:"'JetBrains Mono',monospace",fontSize:10,color:"#555",fontWeight:600,letterSpacing:1.5,marginBottom:10}}>ACTIVITIES</div>
        <div style={{display:"flex",flexDirection:"column",gap:6}}>
          {cls.act.map((a,i)=>(
            <div key={i} style={{display:"flex",alignItems:"flex-start",gap:10,fontSize:13,color:"#bbb",fontWeight:400}}>
              <span style={{color:col,fontSize:8,marginTop:6,flexShrink:0}}>●</span>{a}
            </div>
          ))}
        </div>
      </div>
      <div style={{padding:"14px 22px",borderTop:"1px solid #ffffff06",display:"flex",alignItems:"center",justifyContent:"space-between",flexWrap:"wrap",gap:10,background:"#ffffff02"}}>
        <div style={{display:"flex",gap:5,flexWrap:"wrap"}}>
          {cls.tools.map((tl,i)=>(
            <span key={i} style={{fontFamily:"'JetBrains Mono',monospace",fontSize:10,padding:"3px 8px",borderRadius:4,background:"#ffffff06",border:"1px solid #ffffff08",color:"#777"}}>{tl}</span>
          ))}
        </div>
        <div style={{display:"flex",alignItems:"center",gap:6}}>
          <span style={{fontSize:12}}>📦</span>
          <span style={{fontFamily:"'JetBrains Mono',monospace",fontSize:11,color:col,fontWeight:500}}>{cls.out}</span>
        </div>
      </div>
    </div>
  );
}

/* ═══════════════════════════════════════════════
   MODAL
   ═══════════════════════════════════════════════ */
function Modal({course:c, onClose}){
  const [av, setAv] = useState(0);
  useEffect(()=>{
    document.body.style.overflow="hidden";
    const esc=e=>{if(e.key==="Escape")onClose();};
    window.addEventListener("keydown",esc);
    return()=>{document.body.style.overflow="";window.removeEventListener("keydown",esc);};
  },[onClose]);

  const cv = c.detail[av];
  return(
    <div onClick={onClose} style={{
      position:"fixed",inset:0,zIndex:9999,
      background:"rgba(0,0,0,0.72)",backdropFilter:"blur(10px)",
      display:"flex",alignItems:"center",justifyContent:"center",
      padding:24,animation:"mbIn .25s ease-out",
    }}>
      <div onClick={e=>e.stopPropagation()} style={{
        background:"#111119",border:`1px solid ${c.col}25`,borderRadius:20,
        width:"100%",maxWidth:820,maxHeight:"90vh",
        display:"flex",flexDirection:"column",overflow:"hidden",
        animation:"mdIn .3s cubic-bezier(.22,1,.36,1)",
        boxShadow:`0 40px 100px rgba(0,0,0,.55), 0 0 0 1px ${c.col}12`,
      }}>
        {/* header */}
        <div style={{padding:"24px 28px 20px",borderBottom:"1px solid #ffffff08",display:"flex",alignItems:"flex-start",justifyContent:"space-between",flexShrink:0}}>
          <div>
            <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:8,flexWrap:"wrap"}}>
              <span style={{fontFamily:"'JetBrains Mono',monospace",fontSize:11,fontWeight:700,color:c.col,background:c.dim,padding:"4px 10px",borderRadius:5,letterSpacing:1.5}}>{c.tier.toUpperCase()}</span>
              <span style={{fontFamily:"'JetBrains Mono',monospace",fontSize:11,color:"#666"}}>{c.meta}</span>
              {c.prereq && <span style={{fontFamily:"'JetBrains Mono',monospace",fontSize:10,color:"#555",background:"#ffffff06",padding:"3px 8px",borderRadius:4,border:"1px solid #ffffff08"}}>⬆ {c.prereq}</span>}
            </div>
            <h2 style={{fontSize:22,fontWeight:800,color:"#e8e8f0",margin:0}}>{c.title}</h2>
            {c.flow && <p style={{fontSize:12,color:"#666",margin:"8px 0 0",fontFamily:"'JetBrains Mono',monospace"}}>{c.flow}</p>}
          </div>
          <button onClick={onClose} style={{background:"#ffffff08",border:"1px solid #ffffff10",borderRadius:8,width:36,height:36,display:"flex",alignItems:"center",justifyContent:"center",cursor:"pointer",color:"#888",fontSize:18,fontFamily:"'JetBrains Mono',monospace",flexShrink:0}}>✕</button>
        </div>
        {/* graduation badge */}
        {c.grad && (
          <div style={{margin:"16px 28px 0",padding:"10px 16px",borderRadius:10,background:c.dim,border:`1px solid ${c.col}20`,display:"flex",alignItems:"center",gap:10,flexShrink:0}}>
            <span style={{fontSize:16}}>🎓</span>
            <span style={{fontSize:13,fontWeight:600,color:c.col}}>{c.grad.replace("🎓 ","")}</span>
          </div>
        )}
        {/* visit tabs */}
        <div style={{display:"flex",gap:4,padding:"16px 28px 0",flexShrink:0,overflowX:"auto"}}>
          {c.detail.map((v,i)=>(
            <button key={i} onClick={()=>setAv(i)} style={{
              fontFamily:"'JetBrains Mono',monospace",fontSize:12,
              fontWeight:av===i?700:400,
              color:av===i?c.col:"#666",
              background:av===i?c.dim:"transparent",
              border:av===i?`1px solid ${c.col}30`:"1px solid transparent",
              borderRadius:8,padding:"8px 16px",cursor:"pointer",
              transition:"all .2s",whiteSpace:"nowrap",
            }}>{v.visit}</button>
          ))}
        </div>
        {/* visit title */}
        <div style={{padding:"16px 28px 12px",display:"flex",alignItems:"center",gap:12,flexShrink:0}}>
          <div style={{width:4,height:20,borderRadius:2,background:c.col}}/>
          <span style={{fontSize:16,fontWeight:700,color:"#e8e8f0"}}>{cv.vt}</span>
        </div>
        {/* scrollable classes */}
        <div style={{flex:1,overflowY:"auto",padding:"0 28px 28px",display:"flex",flexDirection:"column",gap:16}}>
          {cv.classes.map((cls,i)=><ClassCard key={i} cls={cls} col={c.col}/>)}
        </div>
      </div>
    </div>
  );
}

/* ═══════════════════════════════════════════════
   COURSE CARD
   ═══════════════════════════════════════════════ */
function CourseCard({course:c, idx}){
  const [h, setH] = useState(false);
  const [m, setM] = useState(false);
  return(
    <>
      <div
        onClick={()=>setM(true)}
        onMouseEnter={()=>setH(true)}
        onMouseLeave={()=>setH(false)}
        style={{
          background:h?"#1e1e2e":"#16161f",
          border:h?`1px solid ${c.col}40`:"1px solid #ffffff0a",
          borderRadius:18,padding:"32px 28px",cursor:"pointer",
          transition:"all .3s cubic-bezier(.22,1,.36,1)",
          display:"flex",flexDirection:"column",position:"relative",overflow:"hidden",
          animation:`cdIn .6s cubic-bezier(.22,1,.36,1) ${idx*.12}s both`,
          transform:h?"translateY(-4px)":"translateY(0)",
          boxShadow:h?`0 20px 50px ${c.col}12`:"none",
        }}
      >
        {/* tier + prereq */}
        <div style={{display:"flex",alignItems:"center",gap:10,marginBottom:16}}>
          <span style={{fontFamily:"'JetBrains Mono',monospace",fontSize:11,fontWeight:700,letterSpacing:2,color:c.col,textTransform:"uppercase"}}>{c.tier}</span>
          {c.prereq && <span style={{fontFamily:"'JetBrains Mono',monospace",fontSize:9,color:"#555",background:"#ffffff06",padding:"2px 8px",borderRadius:4,border:"1px solid #ffffff08"}}>⬆ {c.prereq}</span>}
        </div>
        {/* hours */}
        <div style={{fontSize:42,fontWeight:900,color:"#e8e8f0",lineHeight:1,marginBottom:6}}>{c.hours}</div>
        {/* meta */}
        <div style={{fontFamily:"'JetBrains Mono',monospace",fontSize:12,color:"#666",marginBottom:20}}>{c.meta}</div>
        {/* visit pills */}
        <div style={{display:"flex",gap:6,marginBottom:24,flexWrap:"wrap"}}>
          {c.visits.map((v,i)=>(
            <span key={i} style={{fontFamily:"'JetBrains Mono',monospace",fontSize:10,fontWeight:500,padding:"4px 10px",borderRadius:5,background:c.dim,color:c.col,border:`1px solid ${c.col}20`}}>{v}</span>
          ))}
        </div>
        {/* title */}
        <h3 style={{fontSize:19,fontWeight:800,color:"#e8e8f0",lineHeight:1.4,margin:"0 0 10px"}}>{c.title}</h3>
        {/* desc */}
        <p style={{fontSize:13.5,color:"#888",lineHeight:1.7,fontWeight:300,margin:"0 0 20px"}}>{c.desc}</p>
        {/* tags */}
        <div style={{display:"flex",gap:6,flexWrap:"wrap",marginBottom:20}}>
          {c.tags.map((tg,i)=>(
            <span key={i} style={{fontFamily:"'JetBrains Mono',monospace",fontSize:10,fontWeight:500,padding:"3px 9px",borderRadius:4,background:"#ffffff06",color:"#777"}}>{tg}</span>
          ))}
        </div>
        {/* highlight */}
        <div style={{display:"flex",alignItems:"center",gap:10,padding:"12px 14px",borderRadius:10,background:c.dim,border:`1px solid ${c.col}15`,marginBottom:12}}>
          <span style={{fontSize:20}}>{c.hl.icon}</span>
          <span style={{fontSize:13,fontWeight:600,color:c.col}}>{c.hl.text}</span>
        </div>
        {/* graduation */}
        {c.grad && (
          <div style={{display:"flex",alignItems:"center",gap:8,padding:"10px 14px",borderRadius:10,background:"#ffffff04",border:"1px solid #ffffff08",marginBottom:20}}>
            <span style={{fontSize:14}}>🎓</span>
            <span style={{fontSize:12,fontWeight:500,color:"#999"}}>{c.grad.replace("🎓 ","")}</span>
          </div>
        )}
        {/* CTA */}
        <div style={{display:"flex",alignItems:"center",gap:10,marginTop:"auto",paddingTop:4}}>
          <span style={{fontSize:16}}>📋</span>
          <span style={{fontSize:14,fontWeight:600,color:"#ccc"}}>상세 커리큘럼 보기</span>
          <span style={{marginLeft:"auto",fontFamily:"'JetBrains Mono',monospace",fontSize:16,color:c.col,transition:"transform .2s",transform:h?"translateX(4px)":"translateX(0)"}}>→</span>
        </div>
      </div>
      {m && <Modal course={c} onClose={()=>setM(false)}/>}
    </>
  );
}

/* ═══════════════════════════════════════════════
   MAIN
   ═══════════════════════════════════════════════ */
export default function BizcoolCurriculum(){
  useEffect(()=>{
    const s=document.createElement("style");
    s.textContent=`
      @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Noto+Sans+KR:wght@300;400;500;600;700;800;900&display=swap');
      *{margin:0;padding:0;box-sizing:border-box}
      body{background:#0a0a0f;font-family:'Noto Sans KR',sans-serif;-webkit-font-smoothing:antialiased}
      ::-webkit-scrollbar{width:5px}::-webkit-scrollbar-track{background:transparent}::-webkit-scrollbar-thumb{background:#333;border-radius:3px}
      @keyframes cdIn{from{opacity:0;transform:translateY(32px)}to{opacity:1;transform:translateY(0)}}
      @keyframes mbIn{from{opacity:0}to{opacity:1}}
      @keyframes mdIn{from{opacity:0;transform:scale(.95) translateY(20px)}to{opacity:1;transform:scale(1) translateY(0)}}
    `;
    document.head.appendChild(s);
    return()=>s.remove();
  },[]);

  return(
    <div style={{background:"#0a0a0f",minHeight:"100vh",color:"#e8e8f0"}}>
      <div style={{maxWidth:1200,margin:"0 auto",padding:"80px 24px 16px"}}>
        <div style={{fontFamily:"'JetBrains Mono',monospace",fontSize:12,fontWeight:600,letterSpacing:3,color:"#ff6b2b",marginBottom:14}}>BIZCOOL AI CURRICULUM</div>
        <h2 style={{fontSize:"clamp(28px,4vw,40px)",fontWeight:900,lineHeight:1.35,marginBottom:14,color:"#e8e8f0"}}>비즈쿨 AI 창업교육 커리큘럼</h2>
        <p style={{fontSize:16,color:"#888",lineHeight:1.75,maxWidth:600,fontWeight:300,marginBottom:8}}>
          학교 일정에 딱 맞는 차시를 선택하세요. 각 블록은 독립 운영 가능하며, 연결하면 점점 깊어지는 구조입니다.<br/>클릭하면 상세 커리큘럼을 확인할 수 있습니다.
        </p>

        {/* Progress bar */}
        <div style={{display:"flex",alignItems:"center",gap:0,marginTop:28,marginBottom:8,maxWidth:600}}>
          {C.map((c,i)=>(
            <div key={i} style={{flex:1,display:"flex",alignItems:"center"}}>
              <div style={{display:"flex",flexDirection:"column",alignItems:"center",gap:6}}>
                <div style={{width:32,height:32,borderRadius:8,background:c.dim,border:`2px solid ${c.col}`,display:"flex",alignItems:"center",justifyContent:"center",fontFamily:"'JetBrains Mono',monospace",fontSize:11,fontWeight:700,color:c.col}}>
                  {c.hours.replace("차시","")}
                </div>
                <span style={{fontFamily:"'JetBrains Mono',monospace",fontSize:9,color:"#555",whiteSpace:"nowrap"}}>{c.visits.join("~")}</span>
              </div>
              {i<C.length-1 && <div style={{flex:1,height:2,background:"linear-gradient(to right, "+c.col+"40, "+C[i+1].col+"40)",margin:"0 8px",marginBottom:18}}/>}
            </div>
          ))}
        </div>
      </div>

      <div style={{maxWidth:1200,margin:"0 auto",padding:"24px 24px 100px",display:"grid",gridTemplateColumns:"repeat(auto-fit,minmax(300px,1fr))",gap:20,alignItems:"start"}}>
        {C.map((c,i)=><CourseCard key={c.id} course={c} idx={i}/>)}
      </div>
    </div>
  );
}
