import math

def q1_add_if_odd(a,b):
    pass

def q2_average(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return round(sum/len(arr),2)

def q3_is_closest_to_average(arr):
    avg = q2_average(arr)

    diff = abs(avg-arr[0])
    number = arr[0]

    for i in range(len(arr)):
        if abs(avg-arr[i]) < diff :
            diff = abs(avg-arr[i])
            number = arr[i]

    return number

def q4_split_word_to_characters(s):
    pass

def q5_average_all(arr):
    all = []
    
    for i in range(len(arr)):
        avg = q2_average(arr[i])
        all.append(avg)
    
    avg_all = q2_average(all)
    all.append(avg_all)
    return all

def q6_Check_Arithmetic_or_Geometric(arr, n):
    if arr[2]-arr[1] == arr[1]-arr[0]:
        d = arr[2]-arr[1]
        nth = arr[0] + (n-1)*d
        return nth
    
    elif arr[2]/arr[1] == arr[1]/arr[0]:
        q = arr[2]/arr[1]
        nth = arr[0] * (q**(n-1))
        return nth
    return 0

def q7_determinant_2_2(arr):
    return arr[0][0]*arr[1][1] - arr[0][1]*arr[1][0]