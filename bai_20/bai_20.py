numbers_list = [12, 7, 34, 23, 10, 55, 8, 19]
# Tạo một danh sách trống để chứa các số chẵn lọc được
even_numbers = []
#Dùng vòng lặp đi qua từng số trong danh sách ban đầu
for num in numbers_list:
    # Kiểm tra nếu số đó chia hết cho 2 (số chẵn)
    if num % 2 == 0:
        # Thêm số đó vào danh sách even_numbers
        even_numbers.append(num)
print("Danh sách gốc:", numbers_list)
print("Danh sách các số chẵn sau khi lọc:", even_numbers)