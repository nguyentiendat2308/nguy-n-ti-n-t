input_str = input("Nhập chuỗi ")
# Chuyển về chữ thường
clean_str = input_str.lower()
# Đảo ngược chuỗi (Dùng kỹ thuật [::-1])
reversed_str = clean_str[::-1]
#So sánh chuỗi gốc và chuỗi đảo ngược
if clean_str == reversed_str:
    print(f"'{input_str}' là chuỗi Palindrome ")
else:
    print(f"'{input_str}' không phải là chuỗi Palindrome.")