"""
Module chứa Factory Pattern để tạo nhân viên.
"""
from abc import ABC, abstractmethod
from typing import Optional
from nhanvien import (
    Nhanvien, 
    ChuyenvienPhantich, 
    Ketoanvien, 
    Laptrinhvien, 
    NhanvienKiemthu
)


class INhanvienFactory(ABC):
    """Interface định nghĩa Factory để tạo nhân viên."""
    
    @abstractmethod
    def create_nhanvien(self, loai: str, maso: str = "", 
                       hoten: str = "", luong_cb: float = 0.0) -> Optional[Nhanvien]:
        """
        Tạo nhân viên với đầy đủ thông tin.
        
        Args:
            loai: Loại nhân viên (ChuyenvienPhantich, Ketoanvien, Laptrinhvien, NhanvienKiemthu)
            maso: Mã số nhân viên
            hoten: Họ tên nhân viên
            luong_cb: Lương cơ bản
            
        Returns:
            Instance của nhân viên hoặc None nếu loại không hợp lệ
        """
        pass


class NhanvienFactory(INhanvienFactory):
    """Factory cụ thể để tạo các loại nhân viên."""
    
    def create_nhanvien(self, loai: str, maso: str = "", 
                       hoten: str = "", luong_cb: float = 0.0) -> Optional[Nhanvien]:
        """
        Tạo nhân viên dựa trên loại.
        
        Args:
            loai: Loại nhân viên
            maso: Mã số nhân viên (optional)
            hoten: Họ tên nhân viên (optional)
            luong_cb: Lương cơ bản (optional)
            
        Returns:
            Instance của nhân viên tương ứng hoặc None nếu loại không hợp lệ
        """
        loai = loai.lower().strip()
        
        if loai == "chuyenvienphantich":
            return ChuyenvienPhantich(maso, hoten, luong_cb)
        elif loai == "ketoanvien":
            return Ketoanvien(maso, hoten, luong_cb)
        elif loai == "laptrinhvien":
            return Laptrinhvien(maso, hoten, luong_cb)
        elif loai == "nhanvienkiemthu":
            return NhanvienKiemthu(maso, hoten, luong_cb)
        else:
            return None
