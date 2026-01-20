"""
Client Test - Demo hệ thống quản lý nhân viên và tính tiền thưởng.
"""
import sys
import os

# Thêm thư mục src vào path để import
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from nhanvien_factory import NhanvienFactory
from itienthuong import (
    TienthuongThongthuong,
    TienthuongNgoaigio,
    TienthuongNgoaitinh,
    TienthuongSpageti
)


def main():
    """Hàm main để demo hệ thống."""
    print("=" * 80)
    print("HỆ THỐNG QUẢN LÝ NHÂN VIÊN VÀ TÍNH TIỀN THƯỞNG")
    print("Công ty XYZ - Phần mềm máy tính")
    print("=" * 80)
    print()
    
    # Khởi tạo factory
    factory = NhanvienFactory()
    
    # Tạo các nhân viên
    print(">>> TẠO CÁC NHÂN VIÊN <<<")
    print("-" * 80)
    
    ltv1 = factory.create_nhanvien("laptrinhvien", "LTV001", "Nguyen Van A", 25000000)
    print(f"✓ Đã tạo: {ltv1}")
    
    ltv2 = factory.create_nhanvien("laptrinhvien", "LTV002", "Tran Thi B", 22000000)
    print(f"✓ Đã tạo: {ltv2}")
    
    kt = factory.create_nhanvien("ketoanvien", "KT001", "Le Van C", 12000000)
    print(f"✓ Đã tạo: {kt}")
    
    cv = factory.create_nhanvien("chuyenvienphantich", "CV001", "Pham Thi D", 18000000)
    print(f"✓ Đã tạo: {cv}")
    
    nvkt = factory.create_nhanvien("nhanvienkiemthu", "NVKT001", "Hoang Van E", 16000000)
    print(f"✓ Đã tạo: {nvkt}")
    
    print()
    print("=" * 80)
    print(">>> ÁP DỤNG CÁC PHƯƠNG THỨC TÍNH THƯỞNG <<<")
    print("-" * 80)
    
    # Áp dụng thưởng thông thường cho LTV001
    print("\n1. Lập trình viên A - Thưởng thông thường (2%)")
    ltv1.set_phuongthuc_tinhthuong(TienthuongThongthuong())
    print(f"   Lương CB: {ltv1.get_luong_cb():,.0f} VNĐ")
    print(f"   Tiền thưởng: {ltv1.get_tien_thuong():,.0f} VNĐ")
    print(f"   Tổng: {ltv1.get_luong_cb() + ltv1.get_tien_thuong():,.0f} VNĐ")
    
    # Áp dụng thưởng ngoài giờ cho LTV002
    print("\n2. Lập trình viên B - Làm ngoài giờ (10%)")
    ltv2.set_phuongthuc_tinhthuong(TienthuongNgoaigio())
    print(f"   Lương CB: {ltv2.get_luong_cb():,.0f} VNĐ")
    print(f"   Tiền thưởng: {ltv2.get_tien_thuong():,.0f} VNĐ")
    print(f"   Tổng: {ltv2.get_luong_cb() + ltv2.get_tien_thuong():,.0f} VNĐ")
    
    # Áp dụng thưởng ngoài tỉnh cho CV
    print("\n3. Chuyên viên phân tích D - Dự án ngoài tỉnh (15%)")
    cv.set_phuongthuc_tinhthuong(TienthuongNgoaitinh())
    print(f"   Lương CB: {cv.get_luong_cb():,.0f} VNĐ")
    print(f"   Tiền thưởng: {cv.get_tien_thuong():,.0f} VNĐ")
    print(f"   Tổng: {cv.get_luong_cb() + cv.get_tien_thuong():,.0f} VNĐ")
    
    # Áp dụng thưởng Spageti cho NVKT
    print("\n4. Nhân viên kiểm thử E - Thưởng đặc biệt Spageti (20%)")
    nvkt.set_phuongthuc_tinhthuong(TienthuongSpageti())
    print(f"   Lương CB: {nvkt.get_luong_cb():,.0f} VNĐ")
    print(f"   Tiền thưởng: {nvkt.get_tien_thuong():,.0f} VNĐ")
    print(f"   Tổng: {nvkt.get_luong_cb() + nvkt.get_tien_thuong():,.0f} VNĐ")
    
    # Áp dụng thưởng thông thường cho KT
    print("\n5. Kế toán viên C - Thưởng thông thường (2%)")
    kt.set_phuongthuc_tinhthuong(TienthuongThongthuong())
    print(f"   Lương CB: {kt.get_luong_cb():,.0f} VNĐ")
    print(f"   Tiền thưởng: {kt.get_tien_thuong():,.0f} VNĐ")
    print(f"   Tổng: {kt.get_luong_cb() + kt.get_tien_thuong():,.0f} VNĐ")
    
    print()
    print("=" * 80)
    print(">>> DEMO THAY ĐỔI PHƯƠNG THỨC TÍNH THƯỞNG ĐỘNG <<<")
    print("-" * 80)
    print("\nLập trình viên A thay đổi phương thức tính thưởng:")
    
    # Thay đổi từ thưởng thông thường sang ngoài giờ
    print(f"- Ban đầu (Thưởng thông thường): {ltv1.get_tien_thuong():,.0f} VNĐ")
    
    ltv1.set_phuongthuc_tinhthuong(TienthuongNgoaigio())
    print(f"- Sau khi chuyển sang Ngoài giờ: {ltv1.get_tien_thuong():,.0f} VNĐ")
    
    ltv1.set_phuongthuc_tinhthuong(TienthuongNgoaitinh())
    print(f"- Sau khi chuyển sang Ngoài tỉnh: {ltv1.get_tien_thuong():,.0f} VNĐ")
    
    print()
    print("=" * 80)
    print("✅ DEMO HOÀN TẤT - Strategy Pattern hoạt động tốt!")
    print("=" * 80)


if __name__ == "__main__":
    main()
