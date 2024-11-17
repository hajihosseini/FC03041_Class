def calc_sum(nums):
    s = 0
    for i in range(len(nums)):
        s = s + nums[i]
    return s


nums = []
for i in range(1,6):
    nums.append(i)

s = calc_sum(nums)
print(s)