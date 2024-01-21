import turtle

t=turtle.Turtle()
# chọn kích cỡ nét vẽ

t.pensize(5)

#chọn màu vẽ 
t.pencolor("green")

# vẽ mặt 
face_size=200
    
t.penup()
t.goto(0,-200)
t.pendown()
t.circle(face_size)

# vẽ mắt trái
eye_size=17.5
t.penup()
t.goto(-100,50)
t.pendown()
t.circle(eye_size)

# vẽ mắt phải
t.penup()
t.goto(100,50)
t.pendown()
t.circle(eye_size)


#vẽ mũi
t.penup ()
t.goto(0,50)
t.pendown()
t.circle(-70, steps=3)

#vẽ mồm
t.penup()
t.goto(-100,-70)
t.pendown()
t.right(90)
t.circle(100,180)
turtle.mainloop()

turtle.done()
