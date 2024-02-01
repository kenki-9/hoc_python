import turtle

t = turtle.Turtle()
for i in range(240):
    t.forward(2+i/4)
    t.left(30-i/12)

turtle.done()