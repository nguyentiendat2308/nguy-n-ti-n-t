original_string = input("Nhập chuỗi: ")
#Slicing để đảo ngược
# [:: -1] nghĩa là: "Lấy từ đầu đến cuối nhưng nhảy ngược lại 1 bước"
reversed_string = original_string[::-1]
print("Chuỗi sau khi đảo ngược là:", reversed_string)