
# import package and making object
import turtle
screen = turtle.Screen()
 
rad = float(input("nhập bán kính: "))

screen.setup(500,500)

screen.bgcolor('black')

col=['violet','blue','green','yellow',
     'orange','red']
 
val=10
ind=0
 
turtle.speed(100)
 
for i in range(36):
 
    turtle.seth(-val)

    turtle.color(col[ind])
     

    if ind==5:
        ind=0
    else:
        ind+=1
     
    # calling method
    for i in range(2):
        turtle.circle(rad,90)
        turtle.circle(rad//2,90)

    val+=10
 

turtle.hideturtle()