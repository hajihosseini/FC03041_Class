def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i

    return result


x = factorial(6)
y = factorial(8)

print(x)
print(x+y)

print(factorial(6) + factorial(8))

