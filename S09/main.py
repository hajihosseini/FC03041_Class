def F(X):
    sum = 0
    i = 0
    while(sum<=X):
        i += 1
        sum += i
    return i-1

print(F(15))