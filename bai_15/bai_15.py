n = int(input(" Nhập n: "))
gt = 1
if n < 0:
    print("Không hợp lệ")
elif n == 0:
    print("Giai thừa của 0 là 1.")
else:
    for i in range(1, n + 1):
        gt= gt * i
    print("Kết quả:", n, "! =", gt)