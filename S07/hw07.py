    # "\033[91m",  # Red
    # "\033[92m",  # Green
    # "\033[93m",  # Yellow
    # "\033[94m",  # Blue
    # "\033[95m",  # Magenta
    # "\033[96m",  # Cyan
    # "\033[97m",  # White
def calc_dist(x, y):
    return (x**2 + y**2)**0.5

def get_color(x, y):
    d = int(calc_dist(x, y)) % 8
    return "\033[" + str(d+98) + "m"

def inside_circle(x, y, r):
    if calc_dist(x,y) <= r:
        return True
    else:
        return False
    
def inside_circle2(x, y, r):
    return calc_dist(x,y) <= r

def print_one_line(r, y):
    for x in range(-r ,r + 1):
        c = get_color(x, y)
        if inside_circle(x, y, r):
            print(c + '**', end='')
        else:
            print('  ', end='')
    print()

def print_circle(r):
    for y in range(-r ,r + 1):
        print_one_line(r, y)

        

print_circle(10)



# print_one_line(15,7)
# print_one_line(15,8)

def minimum(a, b):
    if a < b :
        return a
    else:
        return b

def minimum1(a, b):
    min = a
    if b < a:
        min = b
    return min

# m = minimum(5, 4)

# for i in range(m):
#     print('*')
