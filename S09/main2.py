def SUM(n):
    if n == 1:
        return 1
    return n+SUM(n-1)

print(SUM(5))


def Factorial(n):
    if n<=1:
        return 1
    return n*Factorial(n-1)

print(Factorial(5))
    