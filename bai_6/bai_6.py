diem = float(input("Nhập điểm của học sinh (từ 0 đến 10): "))
#  Kiểm tra xem điểm có hợp lệ không (phải từ 0 đến 10)
if diem < 0 or diem > 10:
    print("Lỗi rồi! Điểm số phải nằm trong khoảng từ 0 đến 10 bạn nhé.")
# Nếu điểm hợp lệ, mới bắt đầu xếp loại
elif diem >= 9:
    print("Xếp loại: Xuất sắc")
elif diem >= 8:
    print("Xếp loại: Giỏi")
elif diem >= 6.5:
    print("Xếp loại: Khá")
elif diem >= 5:
    print("Xếp loại: Trung bình")
else:
# Trường hợp này giờ chỉ còn từ 0 đến dưới 5 thôi
    print("Xếp loại: Yếu/Kém")