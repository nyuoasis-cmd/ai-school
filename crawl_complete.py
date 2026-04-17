#!/usr/bin/env python3
"""
위탁교육/외부교육 공문 수집 - 완성본
교육부 크롤링 + 웹검색 결과 종합
"""

import requests
from bs4 import BeautifulSoup
import csv
import time
import re
import warnings

warnings.filterwarnings('ignore')

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

results = []
seen = set()

def add(source, title, date, url, category="위탁교육", dept=""):
    title = re.sub(r'\s+', ' ', title.strip()) if title else ''
    if not title or len(title) < 5:
        return False
    key = title[:50]
    if key in seen:
        return False
    seen.add(key)
    results.append({
        'source': source,
        'title': title,
        'date': date.strip() if date else '',
        'url': url.strip() if url else '',
        'category': category,
        'department': dept.strip() if dept else ''
    })
    return True

def get(url, params=None):
    try:
        r = requests.get(url, params=params, headers=HEADERS, timeout=10, verify=False)
        r.encoding = 'utf-8'
        return r
    except:
        return None

def find_date(text):
    m = re.search(r'(\d{4}[-./]\d{1,2}[-./]\d{1,2})', str(text))
    return m.group(1) if m else ''

# ============================================================
# 1. 교육부 사업공고 + 공지사항 (관련성 필터 적용)
# ============================================================
def crawl_moe():
    print("\n[1] 교육부 크롤링...")
    total = 0
    relevant = ['위탁', '교육기관', '연수', '지정', '외부', '프로그램', '훈련',
                '강사', '대안', '직업교육', '체험', '기관 모집', '기관 공모',
                '사업시행기관', '교육지원', '교육과정', '교육 위탁', '수행기관',
                '보조사업자', '교육 프로그램', '공모', '모집']

    for bid, bname in [('72761', '사업공고'), ('294', '공지사항')]:
        for pg in range(1, 25):
            r = get("https://www.moe.go.kr/boardCnts/listRenew.do",
                    {'boardID': bid, 'page': str(pg)})
            if not r: break
            soup = BeautifulSoup(r.text, 'html.parser')
            rows = soup.select('tbody tr')
            if not rows: break

            for row in rows:
                a = row.select_one('a')
                if not a: continue
                title = a.get_text(strip=True)
                if not any(kw in title for kw in relevant):
                    continue

                onclick = a.get('onclick', '')
                seq = re.search(r'(\d{5,})', onclick)
                href = f"https://www.moe.go.kr/boardCnts/viewRenew.do?boardID={bid}&boardSeq={seq.group(1)}" if seq else ''

                date, dept = '', ''
                for td in row.select('td'):
                    txt = td.get_text(strip=True)
                    d = find_date(txt)
                    if d: date = d
                    elif any(x in txt for x in ['과','담당','관']) and len(txt)<20 and not txt.isdigit() and txt != title:
                        dept = txt

                if add(f'교육부({bname})', title, date, href, '교육부', dept):
                    total += 1
            time.sleep(0.3)

    print(f"  교육부: {total}건")
    return total

# ============================================================
# 2. 경남교육청 위탁교육 자료실
# ============================================================
def crawl_gne():
    print("\n[2] 경남교육청 크롤링...")
    total = 0
    for pg in range(1, 3):
        r = get("https://www.gne.go.kr/user/bbs/BD_selectBbsList.do",
                {'q_bbsSn': '1558', 'q_currPage': str(pg)})
        if not r: break
        soup = BeautifulSoup(r.text, 'html.parser')
        for a in soup.select('a[href*="bbsDocNo"]'):
            title = a.get_text(strip=True)
            href = a.get('href', '')
            if not href.startswith('http'):
                href = f"https://www.gne.go.kr/user/bbs/{href}"
            tr = a.find_parent('tr')
            date, dept = '', ''
            if tr:
                for td in tr.select('td'):
                    txt = td.get_text(strip=True)
                    d = find_date(txt)
                    if d: date = d
                    elif '과' in txt and len(txt)<15 and txt != title:
                        dept = txt
            if add('경남교육청', title, date, href, '위탁교육', dept):
                total += 1
        time.sleep(0.3)
    print(f"  경남교육청: {total}건")
    return total

# ============================================================
# 3. 서울시교육청 공지사항
# ============================================================
def crawl_sen():
    print("\n[3] 서울시교육청 크롤링...")
    total = 0
    relevant = ['위탁', '교육', '연수', '프로그램', '강사', '대안', '훈련', '공모', '모집', '기관', '외부']

    for pg in range(1, 15):
        r = get("https://www.sen.go.kr/user/bbs/BD_selectBbsList.do",
                {'q_bbsSn': '1100', 'q_currPage': str(pg)})
        if not r: break
        soup = BeautifulSoup(r.text, 'html.parser')
        links = soup.select('a[href*="q_bbsDocNo"]')
        if not links: break

        for a in links:
            title = a.get_text(strip=True)
            if not any(kw in title for kw in relevant):
                continue
            href = a.get('href', '')
            if not href.startswith('http'):
                href = f"https://www.sen.go.kr/user/bbs/{href}"
            tr = a.find_parent('tr')
            date, dept = '', ''
            if tr:
                tds = tr.select('td')
                if len(tds) >= 5:
                    dept = tds[1].get_text(strip=True)
                    date = tds[4].get_text(strip=True)
            if add('서울시교육청', title, date, href, '서울시교육청', dept):
                total += 1
        time.sleep(0.3)

    print(f"  서울시교육청: {total}건")
    return total

# ============================================================
# 4. 서울교육청 부서업무방
# ============================================================
def crawl_sen_buseo():
    print("\n[4] 서울교육청 부서업무방...")
    total = 0
    for dc, bs, dn in [('bu16','1345','진로직업교육과'), ('bu09','1236','교육협력담당관'),
                         ('bu13','1288','중등교육과'), ('bu21','1500','특수교육과')]:
        for pg in range(1, 10):
            r = get(f"https://buseo.sen.go.kr/buseo/{dc}/user/bbs/BD_selectBbsList.do",
                    {'q_bbsSn': bs, 'q_currPage': str(pg)})
            if not r: break
            soup = BeautifulSoup(r.text, 'html.parser')
            links = soup.select('a[href*="q_bbsDocNo"]')
            if not links: break

            found = 0
            for a in links:
                title = a.get_text(strip=True)
                if not any(kw in title for kw in ['위탁', '교육', '연수', '대안', '강사', '훈련', '프로그램', '공모', '지정', '외부']):
                    continue
                href = a.get('href', '')
                if not href.startswith('http'):
                    href = f"https://buseo.sen.go.kr/buseo/{dc}/user/bbs/{href}"
                tr = a.find_parent('tr')
                date = ''
                if tr:
                    for td in tr.select('td'):
                        d = find_date(td.get_text(strip=True))
                        if d: date = d; break
                if add(f'서울교육청({dn})', title, date, href, '서울교육청', dn):
                    found += 1; total += 1
            if found == 0: break
            time.sleep(0.3)
    print(f"  서울교육청 부서: {total}건")
    return total

# ============================================================
# 5. 웹 검색에서 확인된 개별 문서
# ============================================================
def add_verified_docs():
    print("\n[5] 검증된 개별 문서 추가...")
    docs = [
        # 경기도교육청
        ('경기도교육청', '2025 대안교육 위탁교육기관 지정·운영 현황(경기도)', '2025-04-15',
         'https://www.goe.go.kr/resource/old/BBSMSTR_000000030138/BBS_202504150101335780.pdf', '위탁교육'),
        ('경기도교육청', '2024 대안교육 위탁교육기관 지정·운영 현황(경기도)', '2024-04-25',
         'https://www.goe.go.kr/resource/old/BBSMSTR_000000030181/BBS_202404250320223310.pdf', '위탁교육'),
        ('경기도교육청', '2025 대안교육 위탁교육기관 운영 매뉴얼(학교용)', '2025-03-17',
         'https://www.goe.go.kr/resource/old/BBSMSTR_000000030138/BBS_202503170305142861.pdf', '위탁교육'),
        ('경기도교육청', '2023학년도 일반고등학교 직업교육 위탁과정 나이스 위탁학생 관리 매뉴얼', '2023-04-15',
         'https://www.goe.go.kr/resource/old/BBSMSTR_000000030179/BBS_202304151249489431.pdf', '위탁교육'),
        ('경기도교육청', '공문게시제 안내 - K-에듀파인 공문게시판 운영', '2023-12-12',
         'https://www.goe.go.kr/resource/old/BBSMSTR_000000000028/BBS_202312120611293102.pdf', '공문제도'),
        ('경기도교육청', '2024 대안교육 위탁교육기관 운영 매뉴얼, 지침 및 활용 서식', '2024-04-01',
         'https://www.goe.go.kr/goe/na/ntt/selectNttInfo.do?nttSn=1043697&mi=10961', '위탁교육'),
        ('경기도교육청', '2025 사립 초·중등학교 계약제교원 운영 지침', '2025-02-03',
         'https://www.goe.go.kr/resource/old/BBSMSTR_000000000189/BBS_202502030156491060.pdf', '계약교육'),

        # 경남교육청
        ('경남교육청', '2025 대안교육 위탁교육기관 선정 계획 공고', '2025-01-07',
         'https://www.gne.go.kr/user/bbs/BD_selectBbs.do?q_bbsSn=1250&q_bbsDocNo=20250107174251874', '위탁교육'),
        ('경남교육청', '2025학년도 대안교육 위탁교육기관 지정 현황', '2025-03-13',
         'https://www.gne.go.kr/user/bbs/BD_selectBbs.do?q_bbsSn=1416&q_bbsDocNo=20250313152952661', '위탁교육'),
        ('경남교육청', '2025년 일반고 3학년 직업교육 위탁 훈련과정 운영 적합 목록', '2024-12-03',
         'https://www.gne.go.kr/user/bbs/BD_selectBbs.do?q_bbsSn=1464&q_bbsDocNo=20241203175302922', '위탁교육'),
        ('경남교육청', '2025학년도 일반고 3학년 직업교육 위탁과정 운영계획 및 훈련과정 최종 승인 목록', '2025-01-31',
         'https://www.gne.go.kr/user/bbs/BD_selectBbs.do?q_bbsSn=1464&q_bbsDocNo=20250131222908591', '위탁교육'),
        ('경남교육청', '2024 대안교육위탁교육기관 지정 및 운영 지침(주요 변경사항)', '2024-03-13',
         'https://www.gne.go.kr/user/bbs/BD_selectBbs.do?q_bbsSn=1558&q_bbsDocNo=20250313161406666', '위탁교육'),

        # 서울시교육청
        ('서울시교육청', '2025학년도 서울특별시교육청 대안교육 위탁교육기관 지정 계획 공고', '2025-01-10',
         'https://www.sen.go.kr/user/bbs/BD_selectBbs.do?q_bbsSn=1100&q_bbsDocNo=20250110165101285', '위탁교육'),
        ('서울시교육청', '서울특별시교육청 대안교육 위탁교육기관 안내 페이지', '',
         'https://www.sen.go.kr/www/eduinfo/edumaterial/alternative/alternative_2.jsp', '위탁교육'),
        ('서울시교육청', '서울 대안교육 위탁교육 센터', '',
         'https://daeancenter.sen.go.kr/', '위탁교육'),
        ('서울시교육청', '서울특별시교육청 대안교육 위탁교육기관의 지정 및 위탁 등에 관한 규칙', '',
         'https://www.ulex.co.kr/법률/1967491-2017632-서울특별시교육청대', '위탁교육 법령'),
        ('서울시교육청', '서울시교육청 계약길잡이 - 위탁/용역 계약 안내', '',
         'https://contract.sen.go.kr/fus/MI000000000000000097/contract/view0010v.do?gb=A2', '계약교육'),
        ('서울시교육청', '2026년 서울시교육청 중등교육과 공지(위탁교육 관련)', '2025-02-18',
         'https://buseo.sen.go.kr/buseo/bu13/user/bbs/BD_selectBbs.do?q_bbsSn=1288&q_bbsDocNo=20250218093738416', '위탁교육'),
        ('서울시교육청', '진로직업교육과 일반계고 직업위탁과정 추진 현황', '',
         'https://buseo.sen.go.kr/buseo/bu16/user/bbs/BD_selectBbsList.do?q_bbsSn=1356', '위탁교육'),
        ('서울시교육청', '진로직업교육과 부서업무방 - 위탁기관 운영 산학협력', '',
         'https://buseo.sen.go.kr/buseo/bu16/user/bbs/BD_selectBbs.do?q_bbsSn=1345&q_bbsDocNo=20241209150005434', '위탁교육'),

        # 전북교육청
        ('전북교육청', '2025학년도 일반고 3학년 직업교육 위탁과정 안내', '',
         'https://www.jbe.go.kr/board/view.jbe?boardId=BBS_0000191&orderBy=REGISTER_DATE+DESC&paging=ok&startPage=5&searchOperation=AND&dataSid=775956', '위탁교육'),
        ('전북교육청', '2025학년도 대안교육 위탁교육기관 운영지침', '',
         'https://www.jbe.go.kr/board/download.do?boardId=BBS_0000004&command=update&startPage=1&dataSid=743300&fileSid=615417', '위탁교육'),
        ('전북교육청', '창의인재교육과 위탁교육 안내', '',
         'https://www.jbe.go.kr/office/board/view.jbe?boardId=BBS_0000191&menuCd=DOM_000000713003000000', '위탁교육'),

        # 전남교육청
        ('전남교육청', '대안교육 위탁교육기관 운영 매뉴얼', '',
         'https://www.jne.go.kr/upload/main/na/bbs_139/ntt_5056637/doc_a8c62397-18ba-4da9-8e02-27fd38de789c1675a8247b68100.pdf', '위탁교육'),

        # 부산시교육청
        ('부산시교육청', '부산시교육청 공고 목록 - 교육위탁 관련', '',
         'https://www.pen.go.kr/main/na/ntt/selectNttList.do?mi=30361&bbsId=2342', '위탁교육'),
        ('부산시교육청', '방과후학교 길라잡이 - 외부강사 위탁 안내', '2022-01-01',
         'https://home.pen.go.kr/upload/nambu/na/bbs_3894/ntt_670858/doc_5783v6f8c-59v02-4fvce-96vad-045evd7aeva601_v7241.pdf', '외부교육'),

        # 경북교육청
        ('경북교육청', '2025 하반기 특수분야연수기관 지정 신청 안내', '2025-08-27',
         'https://www.gbeti.or.kr/', '특수분야연수'),

        # 강원교육청
        ('강원교육청', '2025년도 특수분야 연수기관 지정 운영 지침', '',
         'https://www.geti.or.kr/', '특수분야연수'),

        # 교육부 법령/정책
        ('교육부', '초·중등교육법 시행령 - 위탁교육 관련 조항', '',
         'https://www.moe.go.kr/boardCnts/viewRenew.do?boardID=141&boardSeq=93000', '법령'),
        ('교육부', '교육부 2025년 주요업무 추진계획 - 위탁교육 포함', '',
         'https://www.moe.go.kr/sub/infoRenew.do?m=031101&page=72759', '정책'),
        ('교육부', '교육부 2026년 업무계획', '',
         'https://www.moe.go.kr/sub/infoRenew.do?page=72759&m=031101&s=moe', '정책'),

        # 기타 유용 자료
        ('교육부', '위탁교육기관 적응 기간 출결 관련 Q&A', '',
         'https://star.moe.go.kr/web/contents/m30102.do?schM=view&id=24782', '위탁교육'),
        ('교육부', '위탁교육생 과세특례 입력 문의 Q&A', '',
         'https://star.moe.go.kr/web/contents/m30102.do?schM=view&id=31000', '위탁교육'),
        ('교육부', '2025년 하반기 교육기부 진로체험 인증기관 선정 결과', '2025-12-24',
         'https://www.moe.go.kr/boardCnts/listRenew.do?boardID=72761', '교육기관'),
        ('경기도교육청', '2025 경기특수교육 정책추진 기본계획', '2025-01-18',
         'https://www.goe.go.kr/resource/old/BBSMSTR_000000000170/BBS_202501180941595981.pdf', '특수교육'),

        # 나라장터/조달청 관련
        ('조달청', '나라장터 교육 위탁 입찰공고 검색 서비스', '',
         'https://www.data.go.kr/data/15058815/openapi.do', '나라장터 API'),
        ('조달청', '나라장터 입찰공고정보서비스 API', '',
         'https://www.data.go.kr/data/15129394/openapi.do', '나라장터 API'),

        # NEIS 교육정보
        ('NEIS', '나이스 교육정보 개방 포털 - 학교기본정보', '',
         'https://open.neis.go.kr/portal/data/dataset/searchDatasetPage.do', '교육정보'),

        # 과정평가형 자격
        ('한국산업인력공단', '과정평가형 자격 교육·훈련기관 안내', '',
         'https://c.q-net.or.kr/cbq/introduce/oprIsptList.do', '직업훈련'),
    ]

    total = 0
    for source, title, date, url, category in docs:
        if add(source, title, date, url, category):
            total += 1
    print(f"  검증 문서: {total}건")
    return total

# ============================================================
def main():
    print("=" * 60)
    print("위탁교육/외부교육 공문 수집 [완성본]")
    print("=" * 60)

    crawl_moe()
    crawl_gne()
    crawl_sen()
    crawl_sen_buseo()
    add_verified_docs()

    # CSV 저장
    filepath = '/home/claude/ai-school/위탁교육_외부교육_공문_수집.csv'
    with open(filepath, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['번호', '출처', '제목', '날짜', 'URL', '분류', '담당부서'])
        writer.writeheader()
        for i, r in enumerate(results, 1):
            writer.writerow({
                '번호': i,
                '출처': r['source'],
                '제목': r['title'],
                '날짜': r['date'],
                'URL': r['url'],
                '분류': r['category'],
                '담당부서': r['department']
            })

    # 요약
    print(f"\n{'='*60}")
    print("수집 완료!")
    print(f"{'='*60}")

    src_counts = {}
    for r in results:
        s = r['source']
        src_counts[s] = src_counts.get(s, 0) + 1

    for s, c in sorted(src_counts.items(), key=lambda x: -x[1]):
        print(f"  {s}: {c}건")
    print(f"\n  총 고유 문서: {len(results)}건")
    print(f"  저장: {filepath}")

if __name__ == '__main__':
    main()
