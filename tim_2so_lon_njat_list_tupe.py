def find_two_largest(list_numbers):

  # Sắp xếp list theo thứ tự tăng dần
  list_numbers.sort()

  # Lấy hai phần tử cuối cùng (có chỉ số -1 và -2)
  largest_1 = list_numbers[-1]
  largest_2 = list_numbers[-2]

  return largest_1, largest_2

# Ví dụ sử dụng
list_numbers = [10, 4, 2, 8, 7, 5, 9, 1, 6, 3]
largest_1, largest_2 = find_two_largest(list_numbers)

print(f"Hai số lớn nhất trong list là: {largest_1} và {largest_2}")