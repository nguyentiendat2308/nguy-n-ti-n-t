st1 = float(input("Nhập số thứ nhất: "))
st2 = float(input("Nhập số thứ hai: "))
tong = st1 + st2
hieu = st1 - st2
tich = st1 * st2
print("Kết quả cộng là:", tong)
print("Kết quả trừ là:", hieu)
print("Kết quả nhân là:", tich)
if st1 != 0:
    thuong = st1 / st2
    print("Kết quả chia là:", thuong)
else:
    print("Không thể chia cho số 0")