def q0_check_is_triangle(a,b,c):
    pass

def q1_Divisors_of_a_number(n):
    pass

def q2_nth_prime_number(n):
    pass

def q3_insert_value_to_lis(MyList, value, index):
    pass

def q4_uinque_value_in_list(Mylist):
    pass

def q5_count_substring(Mystr, substr):
    pass

def get_pos(nums):
    list = []
    for i in range(len(nums)):
        list.append(i)
    return list

def is_prime(n):
    if n == 0 or n == 1:
        return False
    
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def filter_prime(nums):
    list = []
    for n in nums:
        if is_prime(n):
            list.append(n)
    return list

def reverse(list):
    nums = []
    for i in range(len(list)-1, -1, -1):
        nums.append(list[i])
    return nums

def q6_reverse_prime_positions(Mylist):
    pos = get_pos(Mylist)  # 0 1 2 3 4 
    prim_pos = filter_prime(pos)  # 2 3
    rev_prim_pos = reverse(prim_pos) # 3 2
    for i in range(int(len(prim_pos)/2)):
        t = Mylist[prim_pos[i]] 
        Mylist[prim_pos[i]]  = Mylist[rev_prim_pos[i]]
        Mylist[rev_prim_pos[i]] = t
        
    return Mylist

def q7_is_symmetry(MyStr):
    pass

def is_in(list, key):
    for item in list:
        if item == key:
            return True
    return False

def q8_count_chrs(Mylist):
    dic = {}
    for word in Mylist:
        for c in word:
            n = 0
            if is_in(dic.keys(), c):
                n = dic[c]
            n += 1
            dic[c] = n
    return dic 
            



def main(a):
    pass