import turtle
import time

# Function to draw the clock face
def draw_clock_face(radius, h, m, s):
    # Clear everything to redraw
    clock_turtle.clear()
    
   
    # Draw the hour marks
    for hour_mark in range(12):
        angle = hour_mark * 30  # Each hour mark is 30 degrees apart
        clock_turtle.penup()
        clock_turtle.goto(0, 0)
        clock_turtle.setheading(90)  # North
        clock_turtle.right(angle)
        clock_turtle.forward(radius - 10)
        clock_turtle.pendown()
        clock_turtle.forward(10)
        clock_turtle.penup()
        clock_turtle.goto(0, 0)

    draw_hand(h, radius*0.5, 6) # Hour hand
    draw_hand(m, radius*0.8, 4) # Minute hand
    draw_hand(s, radius*0.9, 2) # Second hand

# Function to draw the hands
def draw_hand(position, length, width):
    angle = (position % 60) * 6  # Each minute (or second) is 6 degrees
    clock_turtle.penup()
    clock_turtle.goto(0, 0)
    clock_turtle.setheading(90)
    clock_turtle.right(angle)
    clock_turtle.pendown()
    clock_turtle.pensize(width)
    clock_turtle.forward(length)
    clock_turtle.penup()
    clock_turtle.goto(0, 0)
    clock_turtle.pensize(1)

# Function to update the clock continuously
def update_clock():
    while True:
        # Get current time
        now = time.localtime()
        hour = now.tm_hour
        minute = now.tm_min
        second = now.tm_sec
        
        # Draw the clock face with updated time
        draw_clock_face(clock_radius, hour, minute, second)
        
        # Update the screen
        screen.update()
        
        # Wait a second before the next update
        time.sleep(1)

# Setting up the screen
screen = turtle.Screen()
screen.title("Continuous Clock - ChatGPT's Turtle Academy")
screen.tracer(0)  # Turn off auto update

# Setting up the turtle
clock_turtle = turtle.Turtle()
clock_turtle.speed(0)  # Fastest drawing speed

# Drawing the clock face
clock_radius = 200
# Initial draw (the time will be set inside the loop)
draw_clock_face(clock_radius, 0, 0, 0)

# Hide the turtle pointer
clock_turtle.hideturtle()

# Start the clock update loop
update_clock()

# This line is no longer needed as the window will now update in the loop
screen.mainloop()  # This keeps the window open
