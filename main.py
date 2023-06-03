import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle instance
t = turtle.Turtle()
t.speed(5)  # Set the turtle's speed (1 = slowest, 10 = fastest)

# Function to draw a branch
def draw_branch(length, thickness):
    if length < 5:
        return
    else:
        t.pensize(thickness)
        t.forward(length)
        t.right(20)
        draw_branch(length - 15, thickness - 1)
        t.left(40)
        draw_branch(length - 15, thickness - 1)
        t.right(20)
        t.backward(length)

# Function to draw a leaf
def draw_leaf():
    t.fillcolor("green")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

# Draw the trunk
t.penup()
t.goto(0, -200)
t.pendown()
t.setheading(90)
t.pensize(20)
t.pencolor("brown")
t.forward(100)

# Draw the branches
t.penup()
t.goto(0, -100)
t.pendown()
t.pensize(10)
t.pencolor("brown")
draw_branch(80, 7)

# Draw the leaves
t.penup()
t.goto(0, -20)
t.pendown()
draw_leaf()

t.penup()
t.goto(-20, 0)
t.pendown()
draw_leaf()

t.penup()
t.goto(20, 0)
t.pendown()
draw_leaf()

t.penup()
t.goto(0, 20)
t.pendown()
draw_leaf()

t.penup()
t.goto(-30, 20)
t.pendown()
draw_leaf()

t.penup()
t.goto(30, 20)
t.pendown()
draw_leaf()

# Hide the turtle
t.hideturtle()

# Exit on click
turtle.done()
