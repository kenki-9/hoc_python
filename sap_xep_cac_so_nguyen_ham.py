def sort_numbers(num1, num2, num3):
  temp = 0

  # Xác định số bé nhất
  if num2 < num1 and num2 < num3:
    temp = num1
    num1 = num2
    num2 = temp
  elif num3 < num1 and num3 < num2:
    temp = num1
    num1 = num3
    num3 = temp

  # Xác định số bé thứ hai
  if num3 < num2:
    temp = num2
    num2 = num3
    num3 = temp

  return (num1, num2, num3)

# Nhận đầu vào từ người dùng
x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))
z = int(input("Nhập số thứ ba: "))

# Gọi hàm sắp xếp và in ra kết quả
a, b, c = sort_numbers(x, y, z)

print("Số ban đầu:", x, y, z)
print("Số sau khi sắp xếp:", a, b, c)