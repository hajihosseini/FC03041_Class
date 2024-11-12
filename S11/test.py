a = [1,2,3,4,5]

print(a[0])
a[0] = 10

print(a)

a[1] = a[2]
print(a)

a[2] = a[4]
print(a)

a.append(16)
print(a)

a.pop()
print(a)

q = a.pop(1)
print(a)
print(q)