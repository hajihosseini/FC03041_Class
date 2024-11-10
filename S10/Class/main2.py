import turtle

def tj(n):
    if n < 20:
        turtle.forward(n)
        return
    
    n = n/3
    tj(n)
    turtle.left(60)
    tj(n)
    turtle.right(120)
    tj(n)
    turtle.left(60)
    tj(n)



turtle.penup()
turtle.speed(0)
turtle.backward(200)
turtle.pendown()
tj(400)
turtle.mainloop()