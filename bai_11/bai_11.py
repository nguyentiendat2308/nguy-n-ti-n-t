import random
so_can_doan = random.randint(1, 100)
so_lan_thu = 0
da_doan_dung = False
while da_doan_dung == False:
    doan = int(input("Đoán số (1-100): "))
    so_lan_thu = so_lan_thu + 1
    if doan < so_can_doan:
        print("Số cần tìm lớn hơn")
    elif doan > so_can_doan:
        print("Số cần tìm bé hơn")
    else:
        print(" Bạn đã đoán đúng sau", so_lan_thu, "lần thử.")
        da_doan_dung = True

