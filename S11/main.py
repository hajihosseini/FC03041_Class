XList = [10, 14.5, 17, 16]

# for i in range(len(XList)):
#     print(XList[i])

def F(Temp):
    sum = 0
    for i in range(len(Temp)):
        sum += Temp[i]

    return sum/len(Temp)

print(F(XList))

def WAVG(Scores, Weights):
    sum = 0
    total_w = 0
    for i in range(len(Scores)):
        sum += Scores[i]*Weights[i]
        total_w += Weights[i]
    
    return sum/total_w


s = [14, 16.5, 17, 19]
w = [3, 2, 3 , 1]

print(WAVG(s,w))
print(F(s))

def CountValue(AList, value):
    count = 0
    for i in range(len(AList)):
        if AList[i] == value:
            count += 1
    return count


def CountValue2(AList, value):
    count = 0
    i = 0
    while(i <len(AList)):
        if AList[i] == value:
            count += 1
        i += 1
    return count


x = [1,2,3,1,2,1,2,1,2,3,4,5]
y = 2
print(CountValue(x,y))