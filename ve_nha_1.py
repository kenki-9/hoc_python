#Bước 1: Lấy Công cụ vẽ
import turtle

#Bước 2: lấy viết
t = turtle.Turtle()

#nhấc ngòi viết lên
t.penup()

#di chuyển đến bước cần vẽ

t.goto(-200,-200)

#để ngòi viết lên
t.pendown()

#vẽ tầng 1

t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)

#vẽ tầng 2

t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)


# vẽ mái nhà
t.penup()
t.goto(-50,-50)
t.pendown()

t.right(45)
t.forward(120)

t.left(98)
t.forward(110)


# vẽ cửa nhà
t.penup()
t.goto(-170, -350)
t.pendown()
t.goto(-170, -300)
t.goto(-140, -300)
t.goto(-140, -350)
t.goto(-170, -350)


#vẽ  mặt trời
t.penup()
t.goto(200,200)
t.pendown()
t.circle(50)


turtle.done()

