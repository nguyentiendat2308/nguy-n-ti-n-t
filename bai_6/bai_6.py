diem = float(input("Nhập điểm của học sinh (từ 0 đến 10): "))
if diem >= 9:
    print("Xếp loại: Xuất sắc")
elif diem >= 8:
    print("Xếp loại: Giỏi")
elif diem >= 6.5:
    print("Xếp loại: Khá")
elif diem >= 5:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu/Kém")