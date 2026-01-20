"""
Unit tests cho các class Nhanvien.
"""
import unittest
import sys
import os

# Thêm thư mục src vào path để import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from nhanvien import (
    Nhanvien,
    ChuyenvienPhantich,
    Ketoanvien,
    Laptrinhvien,
    NhanvienKiemthu
)
from itienthuong import (
    TienthuongThongthuong,
    TienthuongNgoaigio,
    TienthuongNgoaitinh,
    TienthuongSpageti
)


class TestNhanvienBase(unittest.TestCase):
    """Test các tính năng cơ bản của class Nhanvien."""
    
    def setUp(self):
        """Khởi tạo nhân viên trước mỗi test."""
        self.nhanvien = Laptrinhvien("NV001", "Nguyen Van A", 15000000)
    
    def test_constructor_day_du(self):
        """Test constructor với đầy đủ tham số."""
        nv = Laptrinhvien("NV002", "Tran Thi B", 20000000)
        self.assertEqual(nv.get_maso(), "NV002")
        self.assertEqual(nv.get_hoten(), "Tran Thi B")
        self.assertEqual(nv.get_luong_cb(), 20000000)
    
    def test_constructor_mac_dinh(self):
        """Test constructor mặc định."""
        nv = Laptrinhvien()
        self.assertEqual(nv.get_maso(), "")
        self.assertEqual(nv.get_hoten(), "")
        self.assertEqual(nv.get_luong_cb(), 0.0)
    
    def test_getter_maso(self):
        """Test getter cho mã số."""
        self.assertEqual(self.nhanvien.get_maso(), "NV001")
    
    def test_getter_hoten(self):
        """Test getter cho họ tên."""
        self.assertEqual(self.nhanvien.get_hoten(), "Nguyen Van A")
    
    def test_getter_luong_cb(self):
        """Test getter cho lương cơ bản."""
        self.assertEqual(self.nhanvien.get_luong_cb(), 15000000)
    
    def test_setter_maso(self):
        """Test setter cho mã số."""
        self.nhanvien.set_maso("NV999")
        self.assertEqual(self.nhanvien.get_maso(), "NV999")
    
    def test_setter_hoten(self):
        """Test setter cho họ tên."""
        self.nhanvien.set_hoten("Le Van C")
        self.assertEqual(self.nhanvien.get_hoten(), "Le Van C")
    
    def test_setter_luong_cb(self):
        """Test setter cho lương cơ bản."""
        self.nhanvien.set_luong_cb(25000000)
        self.assertEqual(self.nhanvien.get_luong_cb(), 25000000)
    
    def test_get_tien_thuong_chua_co_strategy(self):
        """Test lấy tiền thưởng khi chưa có strategy."""
        self.assertEqual(self.nhanvien.get_tien_thuong(), 0.0)
    
    def test_set_phuongthuc_tinhthuong(self):
        """Test thiết lập phương thức tính thưởng."""
        strategy = TienthuongThongthuong()
        self.nhanvien.set_phuongthuc_tinhthuong(strategy)
        self.assertIsNotNone(self.nhanvien.get_phuongthuc_tinhthuong())
    
    def test_get_tien_thuong_voi_strategy(self):
        """Test lấy tiền thưởng khi đã có strategy."""
        strategy = TienthuongThongthuong()
        self.nhanvien.set_phuongthuc_tinhthuong(strategy)
        expected = 15000000 * 0.02  # 2% của 15 triệu = 300k
        self.assertEqual(self.nhanvien.get_tien_thuong(), expected)
    
    def test_thay_doi_strategy_runtime(self):
        """Test thay đổi strategy trong runtime."""
        # Ban đầu dùng thưởng thông thường
        strategy1 = TienthuongThongthuong()
        self.nhanvien.set_phuongthuc_tinhthuong(strategy1)
        thuong1 = self.nhanvien.get_tien_thuong()
        
        # Thay đổi sang thưởng ngoài giờ
        strategy2 = TienthuongNgoaigio()
        self.nhanvien.set_phuongthuc_tinhthuong(strategy2)
        thuong2 = self.nhanvien.get_tien_thuong()
        
        # Kiểm tra thưởng ngoài giờ cao hơn
        self.assertGreater(thuong2, thuong1)
    
    def test_to_string(self):
        """Test phương thức toString."""
        strategy = TienthuongThongthuong()
        self.nhanvien.set_phuongthuc_tinhthuong(strategy)
        result = str(self.nhanvien)
        
        self.assertIn("NV001", result)
        self.assertIn("Nguyen Van A", result)
        self.assertIn("15,000,000", result)


class TestChuyenvienPhantich(unittest.TestCase):
    """Test cho class ChuyenvienPhantich."""
    
    def test_tao_chuyenvien_day_du(self):
        """Test tạo chuyên viên phân tích với đầy đủ thông tin."""
        cv = ChuyenvienPhantich("CV001", "Pham Van D", 18000000)
        self.assertEqual(cv.get_maso(), "CV001")
        self.assertEqual(cv.get_hoten(), "Pham Van D")
        self.assertEqual(cv.get_luong_cb(), 18000000)
    
    def test_tao_chuyenvien_mac_dinh(self):
        """Test tạo chuyên viên phân tích mặc định."""
        cv = ChuyenvienPhantich()
        self.assertIsInstance(cv, ChuyenvienPhantich)
        self.assertIsInstance(cv, Nhanvien)
    
    def test_chuyenvien_voi_cac_strategy(self):
        """Test chuyên viên với các strategy khác nhau."""
        cv = ChuyenvienPhantich("CV002", "Hoang Thi E", 20000000)
        
        # Test với thưởng ngoài tỉnh
        cv.set_phuongthuc_tinhthuong(TienthuongNgoaitinh())
        expected = 20000000 * 0.15  # 15% = 3 triệu
        self.assertEqual(cv.get_tien_thuong(), expected)


class TestKetoanvien(unittest.TestCase):
    """Test cho class Ketoanvien."""
    
    def test_tao_ketoanvien_day_du(self):
        """Test tạo kế toán viên với đầy đủ thông tin."""
        kt = Ketoanvien("KT001", "Nguyen Thi F", 12000000)
        self.assertEqual(kt.get_maso(), "KT001")
        self.assertEqual(kt.get_hoten(), "Nguyen Thi F")
        self.assertEqual(kt.get_luong_cb(), 12000000)
    
    def test_tao_ketoanvien_mac_dinh(self):
        """Test tạo kế toán viên mặc định."""
        kt = Ketoanvien()
        self.assertIsInstance(kt, Ketoanvien)
        self.assertIsInstance(kt, Nhanvien)
    
    def test_ketoanvien_voi_thuong_thongthuong(self):
        """Test kế toán viên với thưởng thông thường."""
        kt = Ketoanvien("KT002", "Vo Van G", 10000000)
        kt.set_phuongthuc_tinhthuong(TienthuongThongthuong())
        expected = 10000000 * 0.02  # 2% = 200k
        self.assertEqual(kt.get_tien_thuong(), expected)


class TestLaptrinhvien(unittest.TestCase):
    """Test cho class Laptrinhvien."""
    
    def test_tao_laptrinhvien_day_du(self):
        """Test tạo lập trình viên với đầy đủ thông tin."""
        ltv = Laptrinhvien("LTV001", "Tran Van H", 22000000)
        self.assertEqual(ltv.get_maso(), "LTV001")
        self.assertEqual(ltv.get_hoten(), "Tran Van H")
        self.assertEqual(ltv.get_luong_cb(), 22000000)
    
    def test_tao_laptrinhvien_mac_dinh(self):
        """Test tạo lập trình viên mặc định."""
        ltv = Laptrinhvien()
        self.assertIsInstance(ltv, Laptrinhvien)
        self.assertIsInstance(ltv, Nhanvien)
    
    def test_laptrinhvien_voi_thuong_ngoaigio(self):
        """Test lập trình viên với thưởng ngoài giờ."""
        ltv = Laptrinhvien("LTV002", "Le Thi I", 25000000)
        ltv.set_phuongthuc_tinhthuong(TienthuongNgoaigio())
        expected = 25000000 * 0.10  # 10% = 2.5 triệu
        self.assertEqual(ltv.get_tien_thuong(), expected)


class TestNhanvienKiemthu(unittest.TestCase):
    """Test cho class NhanvienKiemthu."""
    
    def test_tao_nhanvien_kiemthu_day_du(self):
        """Test tạo nhân viên kiểm thử với đầy đủ thông tin."""
        nvkt = NhanvienKiemthu("NVKT001", "Phan Van K", 16000000)
        self.assertEqual(nvkt.get_maso(), "NVKT001")
        self.assertEqual(nvkt.get_hoten(), "Phan Van K")
        self.assertEqual(nvkt.get_luong_cb(), 16000000)
    
    def test_tao_nhanvien_kiemthu_mac_dinh(self):
        """Test tạo nhân viên kiểm thử mặc định."""
        nvkt = NhanvienKiemthu()
        self.assertIsInstance(nvkt, NhanvienKiemthu)
        self.assertIsInstance(nvkt, Nhanvien)
    
    def test_nhanvien_kiemthu_voi_thuong_spageti(self):
        """Test nhân viên kiểm thử với thưởng spageti."""
        nvkt = NhanvienKiemthu("NVKT002", "Dang Thi L", 14000000)
        nvkt.set_phuongthuc_tinhthuong(TienthuongSpageti())
        expected = 14000000 * 0.20  # 20% = 2.8 triệu
        self.assertEqual(nvkt.get_tien_thuong(), expected)


class TestTichHopNhanvienStrategy(unittest.TestCase):
    """Test tích hợp giữa nhân viên và strategy."""
    
    def test_nhieu_nhanvien_nhieu_strategy(self):
        """Test nhiều nhân viên với nhiều strategy khác nhau."""
        # Lập trình viên với thưởng ngoài giờ
        ltv = Laptrinhvien("LTV001", "A", 20000000)
        ltv.set_phuongthuc_tinhthuong(TienthuongNgoaigio())
        
        # Chuyên viên với thưởng ngoài tỉnh
        cv = ChuyenvienPhantich("CV001", "B", 18000000)
        cv.set_phuongthuc_tinhthuong(TienthuongNgoaitinh())
        
        # Kế toán viên với thưởng thông thường
        kt = Ketoanvien("KT001", "C", 12000000)
        kt.set_phuongthuc_tinhthuong(TienthuongThongthuong())
        
        # Kiểm tra tiền thưởng
        self.assertEqual(ltv.get_tien_thuong(), 2000000)  # 10%
        self.assertEqual(cv.get_tien_thuong(), 2700000)  # 15%
        self.assertEqual(kt.get_tien_thuong(), 240000)  # 2%
    
    def test_thay_doi_strategy_dong(self):
        """Test thay đổi strategy động trong runtime."""
        nv = Laptrinhvien("NV001", "Test", 10000000)
        
        # Chu kỳ 1: Thưởng thông thường
        nv.set_phuongthuc_tinhthuong(TienthuongThongthuong())
        thuong1 = nv.get_tien_thuong()
        self.assertEqual(thuong1, 200000)
        
        # Chu kỳ 2: Thưởng ngoài giờ
        nv.set_phuongthuc_tinhthuong(TienthuongNgoaigio())
        thuong2 = nv.get_tien_thuong()
        self.assertEqual(thuong2, 1000000)
        
        # Chu kỳ 3: Thưởng ngoài tỉnh
        nv.set_phuongthuc_tinhthuong(TienthuongNgoaitinh())
        thuong3 = nv.get_tien_thuong()
        self.assertEqual(thuong3, 1500000)


if __name__ == '__main__':
    unittest.main(verbosity=2)
