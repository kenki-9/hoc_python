import turtle
import math

#input CD, CR

CD = float(input("Nhap chieu dai: "))
CR = float(input("Nhap chieu rong: "))

# tính Chu vi , D tích HCN
Cvi = 2 * (CD + CR)
DT = CD * CR

print("Chu vi hình chũ nhật là : ", Cvi)
print("Diện tích hình chũ nhật là : ", DT)


t = turtle.Turtle()
t.color("green")
t.begin_fill()

#ve hinh chu nhật
t.forward(CD)
t.right(90)
t.forward(CR)
t.right(90)
t.forward(CD)
t.right(90)
t.forward(CR)

turtle.done()






