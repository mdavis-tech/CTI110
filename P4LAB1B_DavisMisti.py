import turtle

# setup
win = turtle.Screen()
t = turtle.Turtle()

t.pensize(5)
t.shape("turtle")

# ----- DRAW M (PURPLE, UPRIGHT) -----
t.pencolor("purple")

t.left(90)
t.forward(100)        # left vertical

t.right(150)
t.forward(60)         # down diagonal

t.left(120)
t.forward(60)         # up diagonal

t.right(150)
t.forward(100)        # right vertical

# ----- MOVE TO DRAW D -----
t.penup()
t.goto(120, 0)
t.setheading(90)      # IMPORTANT: reset direction so it's upright
t.pendown()

# ----- DRAW D (BLUE, UPRIGHT) -----
t.pencolor("blue")

t.forward(100)        # vertical line

t.right(90)
t.circle(-50, 180)    # curved part

win.mainloop()