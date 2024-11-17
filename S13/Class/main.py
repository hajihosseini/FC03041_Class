import turtle
import math

def distance(t1, t2):
    x1,y1 = t1.pos()
    x2,y2 = t2.pos()
    return math.sqrt(
        (y2-y1)**2 + (x2-x1)**2
    )

s = math.sqrt(10)

n = 5
w = 1.2
s = "lkdfjsld"

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.penup()
t2.penup()
t1.setpos(-200,100)
t2.setpos(200,100)
t2.setheading(180)
turtle.speed(0)
explosion = False

while not explosion:
    x,_ = t1.pos()
    t1.setx(x+1)
    x,_ = t2.pos()
    t2.setx(x-1)
    if distance(t1,t2) <5:
        for i in range(1,8):
            turtle.color("red")
            turtle.shape("circle")
            turtle.shapesize(i)
        explosion = True

turtle.mainloop()
