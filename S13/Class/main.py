import turtle
import math

s = math.sqrt(10)

n = 5
w = 1.2
s = "lkdfjsld"

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.setpos(-200,0)
t2.setpos(200,0)

while True:
    x,y = t1.pos()
    t1.setpos(x+1,y)
    x,y = t2.pos()
    t2.setpos(x-1,y)
