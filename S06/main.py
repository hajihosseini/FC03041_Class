def Head(w):
    k = (w//2)+1
    print(
       k * " "+
       "^"
    )
    for i in range(1,k):
        print(
            " "*(k-i)+
            "/"*i +
            "|" +
            "\\"*i
        )


def Line(w):
    print(
          "+" + 
          "-" * w +
          "+"
        )

def Body(w , h):
    for _ in range(h):
        print(
            "+" +
            "*"*w +
            "+"
            )


def make_roket(n, w ,h):
    Head(w)
    Line(w)

    for _ in range(n):
        Body(w,h)
        Line(w)

    Head(w)

make_roket(3, 9,10)

