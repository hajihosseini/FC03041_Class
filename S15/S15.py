def q0_only_one_is_odd(a,b):
    return (a+b)%2 == 1

def q1_is_substring(s,s1):
    for i in range(len(s)-len(s1)+1):
        flag = True
        for j in range(len(s1)):
            if s[i+j] != s1[j]:
                flag = False
                break
        if flag == True:
            return True
    return False

    #return s1 in s


def q2_BMM(a,b):
    pass

def q3_KMM(a,b):
    pass

def q4_remove_vowel_chr(s):
    pass

def q5_is_sum_of_squares(a):
    newstr = ""
    pass

def q6_nth_prime_number(n):
    pass

def q7_interpolate_strings(arr):
    pass

def q8_Caesar_encoder(s):
    pass