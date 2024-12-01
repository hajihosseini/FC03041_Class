

# f = open("test_nums.txt")
# lines = f.readlines()
# sum = 0
# for l in lines:
#     n = int(l)
#     sum += n
# print(sum)
# f.close()

# f = open("test_nums.txt", "w")
# for i in range(1000):
#     f.write(str(i)+"\n")
# f.close()


f = open("test_nums.txt", "r+")
lines = f.readlines()
f.writelines(lines)
f.close()
