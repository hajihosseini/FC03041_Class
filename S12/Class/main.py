import turtle


t0 = 0
dt = 0.1
v0 = 20
x0 = 0
t = t0
x = x0
turtle.penup()
turtle.shapesize(3)


while t < 30:
    x = v0 * t + x0
    t = t + dt    
    turtle.setpos(x, 0)

turtle.mainloop()
    