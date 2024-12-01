def q6_contains_pattern(nums, pattern):
    for s in range(len(nums)-len(pattern)+1):
        if cont_pat_atr(nums, pattern, s,0):
            return True
    return False

def cont_pat_at(nums, pattern, s):
    for i in range(len(pattern)):
        if nums[i+s] != pattern[i]:
            return False
    return True

def cont_pat_atr(nums, pattern, s, n):
    if n == len(pattern)-1:
        return nums[s+n]== pattern[n]    
    if nums[s+n] == pattern[n]:
        return cont_pat_atr(nums, pattern, s, n+1)
    return False



# def q6_contains_pattern(nums, pattern):
