import math

# Nhập bán kính từ người dùng
r = float(input("Nhập bán kính của hình tròn: "))

# Tính chu vi
chu_vi = 2 * 3.14 * r

# Tính diện tích
dien_tich = 3.14 * r**2

# In kết quả
print("Chu vi của hình tròn là:", chu_vi)
print("Diện tích của hình tròn là:", dien_tich)






#vẽ hình tròn có bán kính s và tô màu cho hình tròn đó
import turtle

# Nhập bán kính từ người dùng
R = float(input("Nhập bán kính của hình tròn R : "))

# Tạo đối tượng Turtle
t = turtle.Turtle()

# Vẽ hình tròn
t.circle(R)

# Tô màu cho hình tròn
t.begin_fill()
t.fillcolor('green')  # Màu tô fill
t.circle(R)
t.end_fill()

# Hiển thị cửa sổ vẽ
turtle.done()