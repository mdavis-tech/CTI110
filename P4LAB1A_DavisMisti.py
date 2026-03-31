import turtle

# setup
win = turtle.Screen()
t = turtle.Turtle()

t.pensize(4)
t.shape("turtle")

# ----- DRAW SQUARE (PURPLE) -----
t.pencolor("purple")

for i in range(4):
    t.forward(120)
    t.left(90)

# ----- MOVE TO TOP OF SQUARE -----
t.left(90)
t.forward(120)
t.right(90)

# ----- DRAW TRIANGLE (BLUE) -----
t.pencolor("blue")

for i in range(3):
    t.forward(120)
    t.left(120)

win.mainloop()