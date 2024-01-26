import turtle
import random

number = random.uniform(0, 3)
intNumber=int(number)



ball=turtle.Turtle()
ball.shape("circle")

wn=turtle.Screen()
wn.bgcolor("black")
wn.title("circle")

if intNumber < 1:
    ball.color("green")
elif intNumber < 2:
    ball.color("yellow")
elif intNumber < 3 :
    ball.color("red")



turtle.done()
