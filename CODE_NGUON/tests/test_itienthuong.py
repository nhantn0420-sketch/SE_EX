"""
Unit tests cho các strategy tính tiền thưởng (ITienthuong).
"""
import unittest
import sys
import os

# Thêm thư mục src vào path để import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from itienthuong import (
    ITienthuong,
    TienthuongThongthuong,
    TienthuongNgoaigio,
    TienthuongNgoaitinh,
    TienthuongSpageti
)


class TestTienthuongThongthuong(unittest.TestCase):
    """Test cho TienthuongThongthuong (2% lương)."""
    
    def setUp(self):
        """Khởi tạo strategy trước mỗi test."""
        self.strategy = TienthuongThongthuong()
    
    def test_tinh_tienthuong_luong_chuan(self):
        """Test tính thưởng với lương chuẩn."""
        luong = 10000000  # 10 triệu
        expected = 200000  # 2% = 200k
        self.assertEqual(self.strategy.tinh_tienthuong(luong), expected)
    
    def test_tinh_tienthuong_luong_cao(self):
        """Test tính thưởng với lương cao."""
        luong = 50000000  # 50 triệu
        expected = 1000000  # 2% = 1 triệu
        self.assertEqual(self.strategy.tinh_tienthuong(luong), expected)
    
    def test_tinh_tienthuong_luong_thap(self):
        """Test tính thưởng với lương thấp."""
        luong = 5000000  # 5 triệu
        expected = 100000  # 2% = 100k
        self.assertEqual(self.strategy.tinh_tienthuong(luong), expected)
    
    def test_tinh_tienthuong_luong_zero(self):
        """Test tính thưởng với lương bằng 0."""
        luong = 0
        expected = 0
        self.assertEqual(self.strategy.tinh_tienthuong(luong), expected)
    
    def test_tinh_tienthuong_ti_le_chinh_xac(self):
        """Test tỷ lệ tính thưởng chính xác là 2%."""
        luong = 12345678
        expected = luong * 0.02
        self.assertAlmostEqual(self.strategy.tinh_tienthuong(luong), expected, places=2)


class TestTienthuongNgoaigio(unittest.TestCase):
    """Test cho TienthuongNgoaigio (10% lương)."""
    
    def setUp(self):
        """Khởi tạo strategy trước mỗi test."""
        self.strategy = TienthuongNgoaigio()
    
    def test_tinh_tienthuong_luong_chuan(self):
        """Test tính thưởng với lương chuẩn."""
        luong = 10000000  # 10 triệu
        expected = 1000000  # 10% = 1 triệu
        self.assertEqual(self.strategy.tinh_tienthuong(luong), expected)
    
    def test_tinh_tienthuong_luong_cao(self):
        """Test tính thưởng với lương cao."""
        luong = 50000000  # 50 triệu
        expected = 5000000  # 10% = 5 triệu
        self.assertEqual(self.strategy.tinh_tienthuong(luong), expected)
    
    def test_tinh_tienthuong_luong_thap(self):
        """Test tính thưởng với lương thấp."""
        luong = 5000000  # 5 triệu
        expected = 500000  # 10% = 500k
        self.assertEqual(self.strategy.tinh_tienthuong(luong), expected)
    
    def test_tinh_tienthuong_luong_zero(self):
        """Test tính thưởng với lương bằng 0."""
        luong = 0
        expected = 0
        self.assertEqual(self.strategy.tinh_tienthuong(luong), expected)
    
    def test_tinh_tienthuong_ti_le_chinh_xac(self):
        """Test tỷ lệ tính thưởng chính xác là 10%."""
        luong = 12345678
        expected = luong * 0.10
        self.assertAlmostEqual(self.strategy.tinh_tienthuong(luong), expected, places=2)


class TestTienthuongNgoaitinh(unittest.TestCase):
    """Test cho TienthuongNgoaitinh (15% lương)."""
    
    def setUp(self):
        """Khởi tạo strategy trước mỗi test."""
        self.strategy = TienthuongNgoaitinh()
    
    def test_tinh_tienthuong_luong_chuan(self):
        """Test tính thưởng với lương chuẩn."""
        luong = 10000000  # 10 triệu
        expected = 1500000  # 15% = 1.5 triệu
        self.assertEqual(self.strategy.tinh_tienthuong(luong), expected)
    
    def test_tinh_tienthuong_luong_cao(self):
        """Test tính thưởng với lương cao."""
        luong = 50000000  # 50 triệu
        expected = 7500000  # 15% = 7.5 triệu
        self.assertEqual(self.strategy.tinh_tienthuong(luong), expected)
    
    def test_tinh_tienthuong_luong_thap(self):
        """Test tính thưởng với lương thấp."""
        luong = 5000000  # 5 triệu
        expected = 750000  # 15% = 750k
        self.assertEqual(self.strategy.tinh_tienthuong(luong), expected)
    
    def test_tinh_tienthuong_luong_zero(self):
        """Test tính thưởng với lương bằng 0."""
        luong = 0
        expected = 0
        self.assertEqual(self.strategy.tinh_tienthuong(luong), expected)
    
    def test_tinh_tienthuong_ti_le_chinh_xac(self):
        """Test tỷ lệ tính thưởng chính xác là 15%."""
        luong = 12345678
        expected = luong * 0.15
        self.assertAlmostEqual(self.strategy.tinh_tienthuong(luong), expected, places=2)


class TestTienthuongSpageti(unittest.TestCase):
    """Test cho TienthuongSpageti (20% lương)."""
    
    def setUp(self):
        """Khởi tạo strategy trước mỗi test."""
        self.strategy = TienthuongSpageti()
    
    def test_tinh_tienthuong_luong_chuan(self):
        """Test tính thưởng với lương chuẩn."""
        luong = 10000000  # 10 triệu
        expected = 2000000  # 20% = 2 triệu
        self.assertEqual(self.strategy.tinh_tienthuong(luong), expected)
    
    def test_tinh_tienthuong_luong_cao(self):
        """Test tính thưởng với lương cao."""
        luong = 50000000  # 50 triệu
        expected = 10000000  # 20% = 10 triệu
        self.assertEqual(self.strategy.tinh_tienthuong(luong), expected)
    
    def test_tinh_tienthuong_luong_thap(self):
        """Test tính thưởng với lương thấp."""
        luong = 5000000  # 5 triệu
        expected = 1000000  # 20% = 1 triệu
        self.assertEqual(self.strategy.tinh_tienthuong(luong), expected)
    
    def test_tinh_tienthuong_luong_zero(self):
        """Test tính thưởng với lương bằng 0."""
        luong = 0
        expected = 0
        self.assertEqual(self.strategy.tinh_tienthuong(luong), expected)
    
    def test_tinh_tienthuong_ti_le_chinh_xac(self):
        """Test tỷ lệ tính thưởng chính xác là 20%."""
        luong = 12345678
        expected = luong * 0.20
        self.assertAlmostEqual(self.strategy.tinh_tienthuong(luong), expected, places=2)


class TestSoSanhCacStrategy(unittest.TestCase):
    """Test so sánh các strategy với nhau."""
    
    def test_so_sanh_ti_le_thuong(self):
        """Test so sánh tỷ lệ thưởng giữa các strategy."""
        luong = 10000000
        
        thuong_thongthuong = TienthuongThongthuong().tinh_tienthuong(luong)
        thuong_ngoaigio = TienthuongNgoaigio().tinh_tienthuong(luong)
        thuong_ngoaitinh = TienthuongNgoaitinh().tinh_tienthuong(luong)
        thuong_spageti = TienthuongSpageti().tinh_tienthuong(luong)
        
        # Kiểm tra thứ tự tăng dần
        self.assertLess(thuong_thongthuong, thuong_ngoaigio)
        self.assertLess(thuong_ngoaigio, thuong_ngoaitinh)
        self.assertLess(thuong_ngoaitinh, thuong_spageti)


if __name__ == '__main__':
    unittest.main(verbosity=2)
