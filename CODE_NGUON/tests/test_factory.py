"""
Unit tests cho NhanvienFactory.
"""
import unittest
import sys
import os

# Thêm thư mục src vào path để import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from nhanvien_factory import NhanvienFactory, INhanvienFactory
from nhanvien import (
    ChuyenvienPhantich,
    Ketoanvien,
    Laptrinhvien,
    NhanvienKiemthu
)


class TestNhanvienFactory(unittest.TestCase):
    """Test cho NhanvienFactory."""
    
    def setUp(self):
        """Khởi tạo factory trước mỗi test."""
        self.factory = NhanvienFactory()
    
    def test_factory_la_instance_cua_interface(self):
        """Test factory implement INhanvienFactory."""
        self.assertIsInstance(self.factory, INhanvienFactory)
    
    def test_create_chuyenvien_phantich_day_du(self):
        """Test tạo chuyên viên phân tích với đầy đủ thông tin."""
        nv = self.factory.create_nhanvien("chuyenvienphantich", "CV001", "Nguyen A", 18000000)
        self.assertIsInstance(nv, ChuyenvienPhantich)
        self.assertEqual(nv.get_maso(), "CV001")
        self.assertEqual(nv.get_hoten(), "Nguyen A")
        self.assertEqual(nv.get_luong_cb(), 18000000)
    
    def test_create_ketoanvien_day_du(self):
        """Test tạo kế toán viên với đầy đủ thông tin."""
        nv = self.factory.create_nhanvien("ketoanvien", "KT001", "Tran B", 12000000)
        self.assertIsInstance(nv, Ketoanvien)
        self.assertEqual(nv.get_maso(), "KT001")
        self.assertEqual(nv.get_hoten(), "Tran B")
        self.assertEqual(nv.get_luong_cb(), 12000000)
    
    def test_create_laptrinhvien_day_du(self):
        """Test tạo lập trình viên với đầy đủ thông tin."""
        nv = self.factory.create_nhanvien("laptrinhvien", "LTV001", "Le C", 25000000)
        self.assertIsInstance(nv, Laptrinhvien)
        self.assertEqual(nv.get_maso(), "LTV001")
        self.assertEqual(nv.get_hoten(), "Le C")
        self.assertEqual(nv.get_luong_cb(), 25000000)
    
    def test_create_nhanvien_kiemthu_day_du(self):
        """Test tạo nhân viên kiểm thử với đầy đủ thông tin."""
        nv = self.factory.create_nhanvien("nhanvienkiemthu", "NVKT001", "Pham D", 16000000)
        self.assertIsInstance(nv, NhanvienKiemthu)
        self.assertEqual(nv.get_maso(), "NVKT001")
        self.assertEqual(nv.get_hoten(), "Pham D")
        self.assertEqual(nv.get_luong_cb(), 16000000)
    
    def test_create_nhanvien_chi_co_loai(self):
        """Test tạo nhân viên chỉ với loại (các tham số khác mặc định)."""
        nv = self.factory.create_nhanvien("laptrinhvien")
        self.assertIsInstance(nv, Laptrinhvien)
        self.assertEqual(nv.get_maso(), "")
        self.assertEqual(nv.get_hoten(), "")
        self.assertEqual(nv.get_luong_cb(), 0.0)
    
    def test_create_nhanvien_voi_tham_so_optional(self):
        """Test tạo nhân viên với một số tham số optional."""
        nv = self.factory.create_nhanvien("ketoanvien", "KT002")
        self.assertIsInstance(nv, Ketoanvien)
        self.assertEqual(nv.get_maso(), "KT002")
        self.assertEqual(nv.get_hoten(), "")
        self.assertEqual(nv.get_luong_cb(), 0.0)
    
    def test_create_nhanvien_loai_khong_hop_le(self):
        """Test tạo nhân viên với loại không hợp lệ."""
        nv = self.factory.create_nhanvien("nhanvienbaohanh", "NV001", "Test", 10000000)
        self.assertIsNone(nv)
    
    def test_create_nhanvien_loai_viet_hoa(self):
        """Test tạo nhân viên với loại viết hoa."""
        nv = self.factory.create_nhanvien("LAPTRINHVIEN", "LTV002", "Uppercase", 20000000)
        self.assertIsInstance(nv, Laptrinhvien)
    
    def test_create_nhanvien_loai_co_khoang_trang(self):
        """Test tạo nhân viên với loại có khoảng trắng."""
        nv = self.factory.create_nhanvien("  laptrinhvien  ", "LTV003", "Space", 20000000)
        self.assertIsInstance(nv, Laptrinhvien)
    
    def test_create_nhieu_nhanvien_khac_loai(self):
        """Test tạo nhiều nhân viên khác loại."""
        nv1 = self.factory.create_nhanvien("laptrinhvien", "LTV001", "A", 20000000)
        nv2 = self.factory.create_nhanvien("ketoanvien", "KT001", "B", 12000000)
        nv3 = self.factory.create_nhanvien("chuyenvienphantich", "CV001", "C", 18000000)
        nv4 = self.factory.create_nhanvien("nhanvienkiemthu", "NVKT001", "D", 16000000)
        
        self.assertIsInstance(nv1, Laptrinhvien)
        self.assertIsInstance(nv2, Ketoanvien)
        self.assertIsInstance(nv3, ChuyenvienPhantich)
        self.assertIsInstance(nv4, NhanvienKiemthu)
    
    def test_create_nhanvien_cung_loai_khac_thong_tin(self):
        """Test tạo nhiều nhân viên cùng loại nhưng khác thông tin."""
        nv1 = self.factory.create_nhanvien("laptrinhvien", "LTV001", "A", 20000000)
        nv2 = self.factory.create_nhanvien("laptrinhvien", "LTV002", "B", 25000000)
        
        self.assertIsInstance(nv1, Laptrinhvien)
        self.assertIsInstance(nv2, Laptrinhvien)
        self.assertNotEqual(nv1.get_maso(), nv2.get_maso())
        self.assertNotEqual(nv1.get_hoten(), nv2.get_hoten())
        self.assertNotEqual(nv1.get_luong_cb(), nv2.get_luong_cb())
    
    def test_factory_khong_luu_trang_thai(self):
        """Test factory không lưu trạng thái giữa các lần tạo."""
        nv1 = self.factory.create_nhanvien("laptrinhvien", "LTV001", "A", 20000000)
        nv2 = self.factory.create_nhanvien("laptrinhvien", "LTV002", "B", 25000000)
        
        # Thay đổi nv1 không ảnh hưởng đến nv2
        nv1.set_hoten("Modified")
        self.assertNotEqual(nv1.get_hoten(), nv2.get_hoten())


if __name__ == '__main__':
    unittest.main(verbosity=2)
