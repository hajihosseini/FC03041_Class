def F(x):
    result = 1
    for i in range(1,x+1):
        result *= i
    return result

def C(n,r):
    return int(F(n)/(F(r)*F(n-r)))


n = 4
for j in range(n): 
    print((n-j)*"\t", end="")
    for i in range(j+1):
        print(C(j,i), end="\t\t")
    print()


print(2**(n))