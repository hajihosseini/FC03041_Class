def Head():
    print(r"     ^      ")
    print(r"    /|\     ")
    print(r"   //|\\    ")
    print(r"  ///|\\\   ")

def Body():
    print(r" +*******+  ")
    print(r" +*******+  ")
    print(r" +*******+  ")
    print(r" +*******+  ")

def Line():
    print(r" +-------+  ")

Head()
Line()
for _ in range(6):
    Body()
    Line()
Head()

