import random
import turtle

n = 50
height = 600
width = 800

def setup_nightsky(h, w):
    turtle.bgcolor("black")
    turtle.screensize(w, h)
    turtle.fillcolor("white")

def draw_star(x, y, s, n):
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(n):
        turtle.forward(s)
        turtle.right(180-180/n)
    turtle.end_fill()


def draw_stars(n, h, w):
    for _ in range(n):
        x = random.randint(int(-w/2), int(w/2))
        y = random.randint(int(-h/2), int(h/2))
        s = 25 + random.randint(-15,15)
        draw_star(x, y, s, 5)

setup_nightsky(height, width)

turtle.tracer(0)
draw_stars(n, height, width)
turtle.update()

turtle.mainloop()