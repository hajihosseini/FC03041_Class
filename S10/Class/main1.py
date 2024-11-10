

def fib1(n):
    f1 = 1
    f2 = 1
    fx = 1
    for _ in range(n-2):
        fx = f1 + f2
        f1 = f2
        f2 = fx
    return fx











def fib(n):
    a = 1
    b = 1
    count = int(n/2)
    while count > 0:
        a = a + b
        b = a + b
        count -= 1
    return b
n = fib(10)
print(n)


# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# n = factorial(7)
# print(n)
    



















def min2(a, b):
    if a<b:
        return a
    else:
        return b    

def min(a, b, c):
    if a > b and a > c:
        return min2(b,c)
    elif a > b:
        return b
    else:
        return a

    
# print(min(10, 5, 3))