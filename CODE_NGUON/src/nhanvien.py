"""
Module chứa abstract class Nhanvien và các loại nhân viên cụ thể.
"""
from abc import ABC
from typing import Optional
from itienthuong import ITienthuong


class Nhanvien(ABC):
    """
    Abstract class đại diện cho nhân viên.
    
    Attributes:
        maso: Mã số nhân viên
        hoten: Họ tên nhân viên
        luong_cb: Lương cơ bản
        phuongthuc_tinhthuong: Phương thức tính tiền thưởng (Strategy)
    """
    
    def __init__(self, maso: str = "", hoten: str = "", luong_cb: float = 0.0):
        """
        Khởi tạo nhân viên.
        
        Args:
            maso: Mã số nhân viên
            hoten: Họ tên nhân viên
            luong_cb: Lương cơ bản
        """
        self._maso = maso
        self._hoten = hoten
        self._luong_cb = luong_cb
        self._phuongthuc_tinhthuong: Optional[ITienthuong] = None
    
    # Getter methods
    def get_maso(self) -> str:
        """Lấy mã số nhân viên."""
        return self._maso
    
    def get_hoten(self) -> str:
        """Lấy họ tên nhân viên."""
        return self._hoten
    
    def get_luong_cb(self) -> float:
        """Lấy lương cơ bản."""
        return self._luong_cb
    
    def get_phuongthuc_tinhthuong(self) -> Optional[ITienthuong]:
        """Lấy phương thức tính thưởng."""
        return self._phuongthuc_tinhthuong
    
    # Setter methods
    def set_maso(self, maso: str) -> None:
        """Thiết lập mã số nhân viên."""
        self._maso = maso
    
    def set_hoten(self, hoten: str) -> None:
        """Thiết lập họ tên nhân viên."""
        self._hoten = hoten
    
    def set_luong_cb(self, luong_cb: float) -> None:
        """Thiết lập lương cơ bản."""
        self._luong_cb = luong_cb
    
    def set_phuongthuc_tinhthuong(self, phuongthuc: ITienthuong) -> None:
        """Thiết lập phương thức tính thưởng."""
        self._phuongthuc_tinhthuong = phuongthuc
    
    def get_tien_thuong(self) -> float:
        """
        Lấy số tiền thưởng dựa trên phương thức tính thưởng hiện tại.
        
        Returns:
            Số tiền thưởng, hoặc 0 nếu chưa có phương thức tính thưởng
        """
        if self._phuongthuc_tinhthuong is None:
            return 0.0
        return self._phuongthuc_tinhthuong.tinh_tienthuong(self._luong_cb)
    
    def __str__(self) -> str:
        """Trả về chuỗi mô tả nhân viên."""
        tien_thuong = self.get_tien_thuong()
        return (f"{self.__class__.__name__}[Mã số: {self._maso}, "
                f"Họ tên: {self._hoten}, Lương CB: {self._luong_cb:,.0f}, "
                f"Tiền thưởng: {tien_thuong:,.0f}]")


class ChuyenvienPhantich(Nhanvien):
    """Chuyên viên phân tích dữ liệu."""
    
    def __init__(self, maso: str = "", hoten: str = "", luong_cb: float = 0.0):
        super().__init__(maso, hoten, luong_cb)


class Ketoanvien(Nhanvien):
    """Nhân viên kế toán."""
    
    def __init__(self, maso: str = "", hoten: str = "", luong_cb: float = 0.0):
        super().__init__(maso, hoten, luong_cb)


class Laptrinhvien(Nhanvien):
    """Lập trình viên."""
    
    def __init__(self, maso: str = "", hoten: str = "", luong_cb: float = 0.0):
        super().__init__(maso, hoten, luong_cb)


class NhanvienKiemthu(Nhanvien):
    """Nhân viên kiểm thử phần mềm."""
    
    def __init__(self, maso: str = "", hoten: str = "", luong_cb: float = 0.0):
        super().__init__(maso, hoten, luong_cb)
