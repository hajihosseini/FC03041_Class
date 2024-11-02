def Head(w):
    k = (w//2) + 1
    print(k * " " + "^")
    for i in range(1,k):
        print(
            (k-i)*" " +
              i * "/" +
              "|" +
              i * "\\"
        )


def Line(w):
    print("+"+w*"-"+"+")

def Body(w,h):
    for _ in range(h):
        print("+"+
            w*"*"+
            "+")

def make_rocket(n,w,h):
    Head(w)
    Line(w)
    for i in range(n):
        Body(w,h)
        Line(w)
    Head(w)
    Line(w)

make_rocket(3,7,4)