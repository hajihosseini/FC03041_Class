def is_prime(n):
    if n==1:
        return False
    elif n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True


def BMM(x,y):
    bmm = 1
    for i in range(1,x+1):
        if x%i==0 and y%i==0:
            bmm = i
    return bmm
 

def KMM(x,y):
    return (x*y)//BMM(x,y)

