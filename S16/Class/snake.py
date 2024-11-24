import turtle
import math
import time
import random

step = 10

def change_up():
    if shead.dy == 0:
        shead.dx = 0
        shead.dy = +step

def change_down():
    if shead.dy == 0:
        shead.dx = 0
        shead.dy = -step

def change_right():
    if shead.dx == 0:
        shead.dx = step
        shead.dy = 0

def change_left():
    if shead.dx == 0:
        shead.dx = -step
        shead.dy = 0

def setup_screen():
    s = turtle.Screen()
    turtle.tracer(0)
    s.bgcolor("green")
    h = s.window_height()
    w = s.window_width()
    s.listen()
    s.onkey(change_up, "Up")
    s.onkey(change_right, "Right")
    s.onkey(change_down, "Down")
    s.onkey(change_left, "Left")
    return h,w

def create_snake():
    s = turtle.Turtle()
    s.penup()
    s.shape("square")
    s.color("white")
    s.dx = 0
    s.dy = step
    return s

def get_random_location(h,w):
    maxx = int(w/2)-50
    maxy = int(h/2)-50
    minx = -maxx
    miny = -maxy
    return random.randint(minx,maxx), random.randint(miny, maxy)

def make_food(h,w):
    f = turtle.Turtle()
    x,y = get_random_location(h,w)
    f.penup()
    f.color("red")
    f.shape("circle")
    f.shapesize(2)
    f.setpos(x,y)
    return f

def snake_move(s):
    x,y = s.pos()
    s.setpos(x + s.dx, y + s.dy)

def dist(t1,t2):
    x1,y1 = t1.pos()
    x2,y2 = t2.pos()
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def hit(s,f):
    return dist(s,f) < 10

def score_up():
    pass

def relocate(f,h,w):
    x,y = get_random_location(h,w)
    f.setpos(x,y)

def add_tail(head, tail):
    c = create_snake()
    c.dx = head.dx
    c.dy = head.dy
    c.setpos(head.pos())
    c.color("black")
    tail.append(c)

def move_tail(head, tail):
    for i in range(len(tail)-1,0,-1):
        pc = tail[i-1]
        cc = tail[i]
        cc.setpos(pc.pos())
    if len(tail)>0:
        tail[0].setpos(head.pos())

h,w = setup_screen()
shead = create_snake()
stail = []
food = make_food(h,w)

turtle.update()

while True:
    snake_move(shead)
    time.sleep(0.1)
    if hit(shead,food):
        score_up()
        relocate(food,h,w)
        add_tail(shead, stail)
        step = step + 5
    move_tail(shead, stail)
    
    turtle.update()

turtle.mainloop()
    