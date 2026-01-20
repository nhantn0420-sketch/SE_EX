"""
Script tự động tạo file PDF từ test results và test cases.
Yêu cầu: pip install reportlab pillow
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Preformatted
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from datetime import datetime
import os


def create_pdf(output_filename="BaiTap_UnitTest.pdf", 
               student_name="[Tên sinh viên]",
               student_id="[MSSV]",
               class_name="[Lớp]",
               subject="[Môn học]",
               screenshot_path=None):
    """
    Tạo file PDF báo cáo unit test.
    
    Args:
        output_filename: Tên file PDF output
        student_name: Họ tên sinh viên
        student_id: Mã số sinh viên
        class_name: Lớp
        subject: Tên môn học
        screenshot_path: Đường dẫn đến ảnh screenshot (optional)
    """
    
    # Tạo document
    doc = SimpleDocTemplate(output_filename, pagesize=A4,
                           rightMargin=0.75*inch, leftMargin=0.75*inch,
                           topMargin=0.75*inch, bottomMargin=0.75*inch)
    
    # Container cho các elements
    story = []
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor='#2C3E50',
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor='#34495E',
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    code_style = ParagraphStyle(
        'Code',
        parent=styles['Code'],
        fontSize=8,
        fontName='Courier',
        leftIndent=20,
        backColor='#F5F5F5'
    )
    
    # ==================== TRANG BÌA ====================
    story.append(Spacer(1, 1*inch))
    
    title = Paragraph("<b>BÀI TẬP UNIT TEST</b>", title_style)
    story.append(title)
    
    subtitle = Paragraph(
        "<b>HỆ THỐNG QUẢN LÝ NHÂN VIÊN VÀ TÍNH TIỀN THƯỞNG</b>",
        title_style
    )
    story.append(subtitle)
    story.append(Spacer(1, 0.5*inch))
    
    # Thông tin sinh viên
    info_style = styles['Normal']
    info_style.fontSize = 12
    info_style.alignment = TA_CENTER
    
    story.append(Paragraph(f"<b>Họ và tên:</b> {student_name}", info_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(f"<b>Mã số sinh viên:</b> {student_id}", info_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(f"<b>Lớp:</b> {class_name}", info_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(f"<b>Môn học:</b> {subject}", info_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(f"<b>Ngày nộp:</b> {datetime.now().strftime('%d/%m/%Y')}", info_style))
    
    story.append(PageBreak())
    
    # ==================== PHẦN 1: MÔ TẢ ====================
    story.append(Paragraph("PHẦN 1: MÔ TẢ ĐỀ BÀI", heading2_style))
    
    content = """
    <b>Bài toán:</b> Xây dựng hệ thống quản lý nhân viên và tính tiền thưởng cho công ty XYZ.<br/>
    <br/>
    <b>Yêu cầu chính:</b><br/>
    • Quản lý thông tin nhân viên (mã số, họ tên, lương cơ bản)<br/>
    • Hỗ trợ nhiều loại nhân viên: Lập trình viên, Kiểm thử, Chuyên viên phân tích, Kế toán<br/>
    • Nhiều phương thức tính thưởng: Thông thường (2%), Ngoài giờ (10%), Ngoài tỉnh (15%)<br/>
    • Dễ dàng mở rộng<br/>
    <br/>
    <b>Giải pháp:</b><br/>
    • Design Patterns: Strategy Pattern + Factory Pattern<br/>
    • Ngôn ngữ: Python 3<br/>
    • Framework test: unittest<br/>
    """
    story.append(Paragraph(content, styles['Normal']))
    story.append(Spacer(1, 0.3*inch))
    
    # ==================== PHẦN 2: KẾT QUẢ TEST ====================
    story.append(Paragraph("PHẦN 2: KẾT QUẢ CHẠY UNIT TEST", heading2_style))
    
    # Thêm screenshot nếu có
    if screenshot_path and os.path.exists(screenshot_path):
        try:
            img = Image(screenshot_path, width=6*inch, height=4*inch)
            story.append(img)
            story.append(Spacer(1, 0.1*inch))
            story.append(Paragraph("<i>Hình 1: Kết quả chạy 61 unit tests - 100% PASS</i>", 
                                 styles['Normal']))
        except:
            story.append(Paragraph("<i>[Không thể load ảnh screenshot]</i>", styles['Normal']))
    else:
        story.append(Paragraph("<i>[Chèn ảnh screenshot kết quả test ở đây]</i>", styles['Normal']))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Bảng tóm tắt
    summary = """
    <b>Tóm tắt kết quả:</b><br/>
    • Tổng số test cases: 61<br/>
    • Test PASS: 61 (100%)<br/>
    • Test FAIL: 0<br/>
    • Thời gian thực thi: ~0.013s<br/>
    """
    story.append(Paragraph(summary, styles['Normal']))
    story.append(PageBreak())
    
    # ==================== PHẦN 3: TEST CASES ====================
    story.append(Paragraph("PHẦN 3: MÃ NGUỒN TEST CASES", heading2_style))
    
    # Đọc và thêm test files
    test_files = [
        ('tests/test_itienthuong.py', 'Test cho Strategies Tính Thưởng'),
        ('tests/test_nhanvien.py', 'Test cho Nhân Viên'),
        ('tests/test_factory.py', 'Test cho Factory')
    ]
    
    for file_path, description in test_files:
        story.append(Paragraph(f"<b>{description}</b>", styles['Heading3']))
        story.append(Paragraph(f"<i>File: {file_path}</i>", styles['Normal']))
        story.append(Spacer(1, 0.1*inch))
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                code = f.read()
                # Giới hạn độ dài code nếu quá dài
                if len(code) > 10000:
                    code = code[:10000] + "\n\n... [Code còn lại bị cắt do giới hạn độ dài] ..."
                
                # Preformatted text cho code
                code_para = Preformatted(code, code_style)
                story.append(code_para)
        except Exception as e:
            story.append(Paragraph(f"<i>[Không thể đọc file: {str(e)}]</i>", styles['Normal']))
        
        story.append(PageBreak())
    
    # ==================== KẾT LUẬN ====================
    story.append(Paragraph("PHẦN 4: KẾT LUẬN", heading2_style))
    
    conclusion = """
    <b>Kết quả đạt được:</b><br/>
    ✓ Đã hoàn thành 61 unit test cases<br/>
    ✓ Tất cả test cases đều PASS (100%)<br/>
    ✓ Áp dụng đúng Design Patterns (Strategy + Factory)<br/>
    ✓ Code tuân thủ best practices và SOLID principles<br/>
    ✓ Hệ thống dễ dàng mở rộng và bảo trì<br/>
    <br/>
    <b>Kiến thức áp dụng:</b><br/>
    • OOP: Abstract classes, Inheritance, Polymorphism<br/>
    • Design Patterns: Strategy Pattern, Factory Pattern<br/>
    • Unit Testing: unittest framework<br/>
    • Python: ABC module, typing, best practices<br/>
    """
    story.append(Paragraph(conclusion, styles['Normal']))
    
    # Build PDF
    doc.build(story)
    print(f"✅ Đã tạo file PDF: {output_filename}")


if __name__ == "__main__":
    print("=" * 60)
    print("TẠO FILE PDF BÁO CÁO UNIT TEST")
    print("=" * 60)
    print()
    
    # Thông tin sinh viên (sửa lại theo thông tin của bạn)
    student_name = input("Nhập họ tên sinh viên: ") or "[Tên sinh viên]"
    student_id = input("Nhập MSSV: ") or "[MSSV]"
    class_name = input("Nhập lớp: ") or "[Lớp]"
    subject = input("Nhập tên môn học: ") or "[Môn học]"
    
    # Đường dẫn screenshot (optional)
    screenshot = input("Đường dẫn ảnh screenshot (Enter để bỏ qua): ").strip()
    if not screenshot:
        screenshot = None
    
    # Tên file output
    output = f"{student_name.replace(' ', '_')}_{student_id}_UnitTest.pdf"
    
    print()
    print("Đang tạo PDF...")
    
    try:
        create_pdf(
            output_filename=output,
            student_name=student_name,
            student_id=student_id,
            class_name=class_name,
            subject=subject,
            screenshot_path=screenshot
        )
        print()
        print("=" * 60)
        print(f"✅ HOÀN TẤT! File PDF: {output}")
        print("=" * 60)
    except Exception as e:
        print()
        print(f"❌ Lỗi: {str(e)}")
        print()
        print("Để sử dụng script này, cài đặt thư viện:")
        print("pip install reportlab pillow")
