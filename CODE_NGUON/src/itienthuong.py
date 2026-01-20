"""
Module chứa interface ITienthuong và các implementation cụ thể.
Strategy Pattern cho việc tính tiền thưởng.
"""
from abc import ABC, abstractmethod


class ITienthuong(ABC):
    """Interface định nghĩa phương thức tính tiền thưởng."""
    
    @abstractmethod
    def tinh_tienthuong(self, luong_cb: float) -> float:
        """
        Tính tiền thưởng dựa trên lương cơ bản.
        
        Args:
            luong_cb: Lương cơ bản của nhân viên
            
        Returns:
            Số tiền thưởng
        """
        pass


class TienthuongThongthuong(ITienthuong):
    """Tiền thưởng thông thường: 2% lương cơ bản."""
    
    def tinh_tienthuong(self, luong_cb: float) -> float:
        """Tính 2% lương cơ bản."""
        return luong_cb * 0.02


class TienthuongNgoaigio(ITienthuong):
    """Tiền thưởng làm ngoài giờ: 10% lương cơ bản."""
    
    def tinh_tienthuong(self, luong_cb: float) -> float:
        """Tính 10% lương cơ bản."""
        return luong_cb * 0.10


class TienthuongNgoaitinh(ITienthuong):
    """Tiền thưởng làm việc ngoài tỉnh: 15% lương cơ bản."""
    
    def tinh_tienthuong(self, luong_cb: float) -> float:
        """Tính 15% lương cơ bản."""
        return luong_cb * 0.15


class TienthuongSpageti(ITienthuong):
    """Tiền thưởng đặc biệt Spageti: 20% lương cơ bản."""
    
    def tinh_tienthuong(self, luong_cb: float) -> float:
        """Tính 20% lương cơ bản (bonus đặc biệt)."""
        return luong_cb * 0.20
