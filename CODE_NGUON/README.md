# Hệ Thống Quản Lý Nhân Viên và Tính Tiền Thưởng

## Mô tả
Dự án implement hệ thống quản lý nhân viên và tính tiền thưởng cho công ty XYZ chuyên về phần mềm máy tính.

## Design Patterns
- **Factory Pattern**: Tạo các loại nhân viên khác nhau
- **Strategy Pattern**: Linh hoạt trong việc tính tiền thưởng

## Cấu trúc thư mục
```
BT_TEST/
├── src/                          # Code production
│   ├── itienthuong.py           # Interface và strategies tính thưởng
│   ├── nhanvien.py              # Abstract class Nhanvien và các loại nhân viên
│   ├── nhanvien_factory.py      # Factory pattern
│   └── __init__.py
├── tests/                        # Unit tests
│   ├── test_itienthuong.py      # Test cho strategies
│   ├── test_nhanvien.py         # Test cho nhân viên
│   ├── test_factory.py          # Test cho factory
│   └── __init__.py
├── client_test.py                # Demo hệ thống
├── DeBai.md                      # Đề bài
├── MoTaDiagram.md                # Mô tả class diagram
├── requirements.txt              # Dependencies
└── README.md                     # File này
```

## Các loại nhân viên
1. **Lập trình viên** (Laptrinhvien)
2. **Nhân viên kiểm thử** (NhanvienKiemthu)
3. **Chuyên viên phân tích dữ liệu** (ChuyenvienPhantich)
4. **Nhân viên kế toán** (Ketoanvien)

## Các phương thức tính thưởng
1. **Thưởng thông thường**: 2% lương cơ bản
2. **Thưởng ngoài giờ**: 10% lương cơ bản
3. **Thưởng ngoài tỉnh**: 15% lương cơ bản
4. **Thưởng đặc biệt Spageti**: 20% lương cơ bản

## Cài đặt

### 1. Clone/Download project
```bash
cd BT_TEST
```

### 2. (Optional) Cài đặt pytest
```bash
pip install -r requirements.txt
```

## Chạy chương trình

### 1. Chạy demo
```bash
python client_test.py
```

### 2. Chạy unit tests

#### Cách 1: Dùng unittest (built-in)
```bash
# Chạy tất cả tests
python -m unittest discover tests -v

# Chạy test cụ thể
python -m unittest tests.test_itienthuong -v
python -m unittest tests.test_nhanvien -v
python -m unittest tests.test_factory -v
```

#### Cách 2: Dùng pytest (nếu đã cài)
```bash
# Chạy tất cả tests
pytest tests/ -v

# Chạy test cụ thể
pytest tests/test_itienthuong.py -v
pytest tests/test_nhanvien.py -v
pytest tests/test_factory.py -v

# Chạy với coverage
pytest tests/ -v --cov=src
```

#### Cách 3: Chạy từng file test trực tiếp
```bash
python tests/test_itienthuong.py
python tests/test_nhanvien.py
python tests/test_factory.py
```

## Test Coverage

### Test cho ITienthuong (Strategies)
- ✅ Test tính thưởng với các mức lương khác nhau
- ✅ Test tính thưởng với lương = 0
- ✅ Test độ chính xác tỷ lệ phần trăm
- ✅ Test so sánh các strategy với nhau

### Test cho Nhanvien
- ✅ Test constructor (đầy đủ và mặc định)
- ✅ Test getter/setter cho tất cả thuộc tính
- ✅ Test get_tien_thuong() với/không strategy
- ✅ Test thay đổi strategy trong runtime
- ✅ Test toString()
- ✅ Test cho từng loại nhân viên cụ thể
- ✅ Test tích hợp nhân viên với strategy

### Test cho Factory
- ✅ Test tạo từng loại nhân viên
- ✅ Test với tham số đầy đủ/optional
- ✅ Test với loại không hợp lệ
- ✅ Test case-insensitive và trim spaces
- ✅ Test tạo nhiều nhân viên
- ✅ Test factory không lưu trạng thái

## Nộp bài
1. ✅ Chạy unit tests và đảm bảo tất cả pass
2. ✅ Chụp màn hình kết quả test
3. ✅ Nộp file hình ảnh + test cases (mã nguồn)

## Tác giả
Sinh viên - Bài tập thiết kế hệ thống quản lý nhân viên

## License
MIT
