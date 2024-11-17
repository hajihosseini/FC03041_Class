import turtle
import random
import time

def right_key():
    x = paddle.xcor()
    paddle.setx(x + 50)
    turtle.update()

def left_key():
    x = paddle.xcor()
    paddle.setx(x - 50)
    turtle.update()

def setup_screen():
    turtle.tracer(0)
    s = turtle.Screen()
    h = s.window_height()
    w = s.window_width()
    s.bgcolor("black")
    s.onkey(left_key, "Left")
    s.onkey(right_key, "Right")
    s.listen()
    return h,w

def get_color():
    my_fav_colors = ["red", "yellow", "pink", "blue", "green"]
    n = random.randint(0,len(my_fav_colors)-1)
    return my_fav_colors[n]

def create_block(h, w, row, col, color):
    t = turtle.Turtle()
    t.color(color)
    t.penup()
    t.shape("square")
    t.shapesize(stretch_wid=1, stretch_len=5)
    minx = -w/2+50
    maxy = h/2-30    
    t.setpos(minx + col * 120, maxy - row * 30)

def create_blocks(h, w):
    blocks = []
    for row in range(4):
        for col in range(8):
            c = get_color()
            b = create_block(h, w, row, col, c) 
            blocks.append(b)
    turtle.update()
    return blocks

def make_ball():
    b = turtle.Turtle()
    b.shape("circle")
    b.shapesize(2)
    b.color("white")
    b.penup()
    b.setpos(0,100)
    b.dx = 5
    b.dy = -5
    return b

def move_ball(b):
    x,y = b.pos()
    b.setpos(x+b.dx, y+b.dy)
    turtle.update()

def make_paddle():
    p = turtle.Turtle()
    p.setpos(0, -200)
    p.penup()
    p.color("white")
    p.shape("square")
    p.shapesize(stretch_len=5, stretch_wid=1)
    return p

h,w = setup_screen()

blocks = create_blocks(h,w)
ball = make_ball()
paddle = make_paddle()

while True:
    move_ball(ball)
    time.sleep(0.01)
#     if ball_hit_paddle(ball, paddle):
#         ball.vy = -ball.vy
    
#     if ball_hit_horizontal_wall():
#         ball.vx = -ball.vx
    
#     block = ball_hit_blocks(ball, blocks)
#     if block:
#         remove_block(block)
#         ball.vy = -ball.vy


turtle.mainloop()

