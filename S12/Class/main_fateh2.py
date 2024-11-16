import turtle
import math


def start_attack(dt, v0, x0, y0, t, theta, g):
    v0x = math.cos(theta) * v0
    v0y = math.sin(theta) * v0


    while t < 30:
        x = v0x * t + x0
        y = 0.5 * g * t**2 + v0y*t + y0
        t = t + dt    
        vy = g * t + v0y 
        theta = math.degrees(math.atan(vy/v0x))
        turtle.setheading(theta)
        turtle.setpos(x, y)
        if y < 0:
            turtle.shape("circle")
            turtle.color("red")
            for i in range(1,5):
                turtle.shapesize(i)
            break

def setup_attack():
    t0 = 0
    dt = 0.05
    v0 = 50
    x0 = -300
    y0 = 0
    t = t0
    x = x0
    theta = 45
    g = -9.8
    turtle.penup()
    turtle.shapesize(3)
    return dt,v0,x0,y0,t,theta,g

def silo(x, y, w, h):
    turtle.setheading(90)
    turtle.forward(h)
    turtle.right(90)
    turtle.forward(w)
    turtle.right(90)
    turtle.forward(h)
    turtle.right(90)
    turtle.forward(w)

def setup_farzi_ahdaf():
    x = 300
    y = 0
    x0, y0 = turtle.pos()
    silo(x,y, 70, 30)
    turtle.setpos(x0, y0)

setup_farzi_ahdaf()

dt, v0, x0, y0, t, theta, g = setup_attack()

start_attack(dt, v0, x0, y0, t, theta, g)
turtle.mainloop()
    