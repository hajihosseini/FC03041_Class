    # "\033[91m",  # Red
    # "\033[92m",  # Green
    # "\033[93m",  # Yellow
    # "\033[94m",  # Blue
    # "\033[95m",  # Magenta
    # "\033[96m",  # Cyan
    # "\033[97m",  # White

def get_color(x, y, r):
    d = 0
    return "\033[" + d+91 + "m"

def inside_circle(x, y, r):
    d = 0;
    if d < r:
        return True
    else:
        return False

def print_circle(r):
    for y in range(-r ,r + 1):
        for x in range(-r ,r + 1):
            c = get_color(x, y, r)
            if inside_circle(x, y, r):
                print('*', end='')
            else:
                print(' ', end='')
    pass


print_circle(10)