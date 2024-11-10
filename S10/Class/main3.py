import turtle

x = 5
a = 20


def follow(s):
    for c in s:
        if c == 'f':
            turtle.forward(x)
        elif c == '-':
            turtle.left(a)
        elif c == '+':
            turtle.right(a)

            

def process_inst(s, n):
    inst = ""
    for _ in range(n):
        i = 0
        while i < len(s):
            if s[i] != 'f':
                inst += s[i]
            else:
                pass


x = 50
a = 20
F = "f-f+f"
follow(F)
turtle.mainloop()
# for c in F:
#     print(c)
# l = len(F)
# print(l)
# for i in range(l):
#     print(F[i])