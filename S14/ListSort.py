a = [3,5,1,8,2,9,2]

for j in range(len(a)):
    for i in range(j,len(a)):
        if a[j] > a[i]:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp

print(a)