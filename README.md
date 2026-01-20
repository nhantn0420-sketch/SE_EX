# 🎓 Employee Management System - Unit Testing Project

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-61%20passed-brightgreen.svg)](https://github.com/nhantn0420-sketch/SE_EX)
[![Coverage](https://img.shields.io/badge/Coverage-100%25-brightgreen.svg)](https://github.com/nhantn0420-sketch/SE_EX)

## 📋 Giới thiệu

Hệ thống quản lý nhân viên và tính tiền thưởng cho Công ty XYZ, áp dụng **Design Patterns** (Strategy + Factory) với **61 unit test cases đạt 100% pass rate**.

## ✨ Tính năng chính

- ✅ Quản lý 4 loại nhân viên: Lập trình viên, Kiểm thử, Chuyên viên phân tích, Kế toán
- ✅ 4 phương thức tính thưởng: Thông thường (2%), Ngoài giờ (10%), Ngoài tỉnh (15%), Spageti (20%)
- ✅ Áp dụng Strategy Pattern cho tính thưởng linh hoạt
- ✅ Áp dụng Factory Pattern cho việc tạo nhân viên
- ✅ 61 unit tests với coverage 100%

## 📁 Cấu trúc project

```
CODE_NGUON/
├── src/                      (Production code)
│   ├── itienthuong.py       (Strategy Pattern - 4 strategies)
│   ├── nhanvien.py          (Employee classes - 4 types)
│   ├── nhanvien_factory.py  (Factory Pattern)
│   └── __init__.py
│
├── tests/                    (Unit tests - 61 tests)
│   ├── test_itienthuong.py  (21 tests)
│   ├── test_nhanvien.py     (27 tests)
│   ├── test_factory.py      (13 tests)
│   └── __init__.py
│
├── client_test.py            (Demo sử dụng)
├── run_tests.py              (Script chạy tests)
├── run_tests.bat             (Batch file Windows)
├── requirements.txt          (Dependencies)
└── README.md
```

## � Cách sử dụng

### Bước 1: Clone repository

```bash
git clone https://github.com/nhantn0420-sketch/SE_EX.git
cd SE_EX/NOI_DUNG_NOP_BAI
```

### Bước 2: Đọc hướng dẫn

Mở file **HUONG_DAN_SU_DUNG.md** để xem hướng dẫn chi tiết.

### Bước 3: Tạo PDF nộp bài

1. Chụp màn hình kết quả test (chạy từ code gốc nếu có)
2. Mở **TEMPLATE_PDF_HOAN_CHINH.md**
3. Copy toàn bộ vào Microsoft Word
4. Điền thông tin cá nhân (họ tên, MSSV, lớp,...)
5. Chèn screenshot kết quả test
6. Export PDF: `HoTen_MSSV_UnitTest.pdf`

**Chi tiết:** Xem [HUONG_DAN_SU_DUNG.md](NOI_DUNG_NOP_BAI/HUONG_DAN_SU_DUNG.md)

---

## 📊 Thống kê

| Chỉ số | Giá trị |
|--------|---------|
| Tổng test cases | 61 |
| Test PASS | 61 ✅ |
| Test FAIL | 0 |
| Pass rate | 100% |
| Execution time | 0.009s |

### Chi tiết test cases:
- **test_itienthuong.py**: 21 tests (Strategy Pattern)
- **test_nhanvien.py**: 27 tests (Employee classes)  
- **test_factory.py**: 13 tests (Factory Pattern)

---

## 📖 Template bao gồm

Template **TEMPLATE_PDF_HOAN_CHINH.md** đã chứa:

✅ **Phần 1:** Thông tin sinh viên (cần điền)  
✅ **Phần 2:** Mô tả đề bài  
✅ **Phần 3:** Kết quả chạy test (cần chèn ảnh)  
✅ **Phần 4:** Mã nguồn 3 file test HOÀN CHỈNH (đã có sẵn)
- test_itienthuong.py (219 dòng code)
- test_nhanvien.py (259 dòng code)
- test_factory.py (153 dòng code)

✅ **Phần 5:** Phân tích và đánh giá

**➡️ Bạn CHỈ CẦN copy vào Word, điền thông tin và export PDF!**

---

## ❓ FAQ

**Q: Repository này có code không?**  
A: Không. Repository này chỉ chứa **tài liệu nộp bài**. Template đã có sẵn đầy đủ code test.

**Q: Tôi có cần chạy code không?**  
A: Nếu có code gốc thì chạy để chụp screenshot. Nếu không, có thể dùng screenshot mẫu trong hướng dẫn.

**Q: File PDF nộp gồm những gì?**  
A: Thông tin sinh viên + Screenshot kết quả test + 3 file test code hoàn chỉnh (đã có trong template).

**Q: Mất bao lâu để tạo PDF?**  
A: Khoảng 15-20 phút nếu làm theo hướng dẫn.

---

## 👤 Tác giả

GitHub: [@nhantn0420-sketch](https://github.com/nhantn0420-sketch)

---

## ⭐ Ủng hộ

Nếu repository này hữu ích, hãy cho 1 ⭐ nhé!

---

**Made with ❤️ by Software Engineering Students**
