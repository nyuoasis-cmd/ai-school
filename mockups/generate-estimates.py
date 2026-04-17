#!/usr/bin/env python3
"""
AI교육 운영견적서 4차시/6차시/8차시 HWPX 생성기
기존 12차시 견적서를 base로 차시/금액만 치환
"""
import zipfile, io, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_HWPX = os.path.join(SCRIPT_DIR, "AI 교육_운영견적서_티처메이트.hwpx")
OUTPUT_DIR = SCRIPT_DIR

# 단가 (차시당)
RATE_LECTURER = 70_000   # 강사비
RATE_TOOLS = 10_000      # 티처메이트 수업도구
RATE_SPRINT = 15_000     # 티처메이트 스프린트 스튜디오


def fmt(n):
    """Format number with commas"""
    return f"{n:,}"


def generate_estimate(num_hours, output_path):
    """Generate estimate HWPX by replacing values in base file"""

    # Calculate amounts
    lecturer = RATE_LECTURER * num_hours
    tools = RATE_TOOLS * num_hours
    sprint = RATE_SPRINT * num_hours
    subtotal = lecturer + tools + sprint
    vat = int(subtotal * 0.1)
    total = subtotal + vat

    with zipfile.ZipFile(BASE_HWPX, 'r') as zin:
        section0 = zin.read('Contents/section0.xml').decode('utf-8')

        # 1. Replace title
        section0 = section0.replace(
            'AI 동아리 교육 운영 견적서',
            f'AI 동아리 교육 운영 견적서 ({num_hours}차시)'
        )

        # 2. Replace 기본정보 표 - 교육 차시
        # "12차시" in info table (교육 차시 value cell)
        # Be careful: "12차시" appears in multiple places
        # Info table value: just "12차시" as cell text
        # Estimate table: "× 12차시" patterns
        # Budget label: "1~12차시"

        # Replace "12차시" standalone in info table (between tags)
        section0 = section0.replace(
            '<hp:t>12차시</hp:t>',
            f'<hp:t>{num_hours}차시</hp:t>'
        )

        # 3. Replace 예산 총액 in info table
        section0 = section0.replace(
            '<hp:t>1,254,000 원</hp:t>',
            f'<hp:t>{fmt(total)} 원</hp:t>'
        )

        # 4. Replace estimate table - 산출근거 (unit × hours)
        section0 = section0.replace(
            f'70,000원 × 12차시',
            f'70,000원 × {num_hours}차시'
        )
        section0 = section0.replace(
            f'10,000원 × 12차시',
            f'10,000원 × {num_hours}차시'
        )
        section0 = section0.replace(
            f'15,000원 × 12차시',
            f'15,000원 × {num_hours}차시'
        )

        # 5. Replace estimate table - 금액
        section0 = section0.replace(
            '<hp:t>840,000</hp:t>',
            f'<hp:t>{fmt(lecturer)}</hp:t>'
        )
        section0 = section0.replace(
            '<hp:t>120,000</hp:t>',
            f'<hp:t>{fmt(tools)}</hp:t>'
        )
        section0 = section0.replace(
            '<hp:t>180,000</hp:t>',
            f'<hp:t>{fmt(sprint)}</hp:t>'
        )
        section0 = section0.replace(
            '<hp:t>1,140,000</hp:t>',
            f'<hp:t>{fmt(subtotal)}</hp:t>'
        )
        section0 = section0.replace(
            '<hp:t>114,000</hp:t>',
            f'<hp:t>{fmt(vat)}</hp:t>'
        )
        section0 = section0.replace(
            '<hp:t>1,254,000</hp:t>',
            f'<hp:t>{fmt(total)}</hp:t>'
        )

        # 6. Replace budget subtitle "1~12차시"
        section0 = section0.replace(
            '1~12차시',
            f'1~{num_hours}차시'
        )

        # Write output
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as zout:
            for item in zin.namelist():
                if item == 'Contents/section0.xml':
                    zout.writestr(item, section0.encode('utf-8'))
                elif item == 'Preview/PrvText.txt':
                    prv = f"AI 동아리 교육 운영 견적서 ({num_hours}차시)\n{num_hours}차시, {fmt(total)}원"
                    zout.writestr(item, prv.encode('utf-8'))
                else:
                    zout.writestr(item, zin.read(item))

    with open(output_path, 'wb') as f:
        f.write(buf.getvalue())

    print(f"Generated: {output_path}")
    print(f"  {num_hours}차시: 강사비 {fmt(lecturer)} + 수업도구 {fmt(tools)} + 스프린트 {fmt(sprint)} = {fmt(subtotal)} + VAT {fmt(vat)} = {fmt(total)}원")


if __name__ == '__main__':
    for n in [4, 6, 8]:
        output = os.path.join(OUTPUT_DIR, f"AI교육_운영견적서_{n}차시.hwpx")
        generate_estimate(n, output)

    print("\nDone! Generated 3 estimate HWPX files.")
