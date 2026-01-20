@echo off
REM Script chay tat ca unit tests

echo ================================================================================
echo           CHAY TAT CA UNIT TESTS - HE THONG QUAN LY NHAN VIEN
echo ================================================================================
echo.

echo [1/3] Dang chay tat ca tests...
echo.
python -m unittest discover tests -v

echo.
echo ================================================================================
echo.
echo [2/3] Thong ke ket qua:
python -m unittest discover tests 2>&1 | findstr "Ran OK"

echo.
echo ================================================================================
echo.
echo [3/3] Ban co the chup man hinh ket qua tren de nop bai!
echo.
echo Nhan phim bat ky de thoat...
pause > nul
