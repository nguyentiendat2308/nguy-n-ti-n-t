input_string = input("Nhập vào một câu tiếng Anh bất kỳ: ")
# Chuyển tất cả về chữ thường để dễ đếm
input_string = input_string.lower()
vowels = "aeiou"
# Tạo biến đếm, ban đầu bằng 0
vowel_count = 0
# Dùng vòng lặp đi qua từng chữ cái trong câu
for char in input_string:
    if char in vowels:
        vowel_count = vowel_count + 1
print("Số lượng nguyên âm trong câu là:", vowel_count)