#!/usr/bin/env python3
"""
Script để chạy tất cả unit tests và tạo báo cáo.
"""
import unittest
import sys
import os

# Thêm thư mục src vào path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))


def run_all_tests():
    """Chạy tất cả unit tests."""
    print("=" * 80)
    print("CHẠY TẤT CẢ UNIT TESTS - HỆ THỐNG QUẢN LÝ NHÂN VIÊN")
    print("=" * 80)
    print()
    
    # Discover và chạy tests
    loader = unittest.TestLoader()
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Chạy với verbosity=2 để hiển thị chi tiết
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print()
    print("=" * 80)
    print("TỔNG KẾT")
    print("=" * 80)
    print(f"Tổng số tests: {result.testsRun}")
    print(f"Thành công: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Thất bại: {len(result.failures)}")
    print(f"Lỗi: {len(result.errors)}")
    print("=" * 80)
    
    # Return status
    if result.wasSuccessful():
        print("✅ TẤT CẢ TESTS ĐỀU PASS! SẴN SÀNG NỘP BÀI!")
        return 0
    else:
        print("❌ CÓ TESTS THẤT BẠI! VUI LÒNG KIỂM TRA LẠI!")
        return 1


if __name__ == '__main__':
    sys.exit(run_all_tests())
