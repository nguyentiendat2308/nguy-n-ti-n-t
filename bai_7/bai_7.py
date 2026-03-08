st1 = float(input("Nhập số thứ nhất: "))
st2 = float(input("Nhập số thứ hai: "))
st3 = float(input("Nhập số thứ ba: "))
so_lon_nhat = st1
if st2 > so_lon_nhat:
    so_lon_nhat = st2
if st3 > so_lon_nhat:
    so_lon_nhat = st3
print("Số lớn nhất trong 3 số là:", so_lon_nhat)