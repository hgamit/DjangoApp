def upside_down_asterisk_triangle(n):
     """
     takes an integer n and then returns a backwards
     asterisk triangle consisting of (n) many lines
     """
     x = 0
     while (x < n):
         print(" " * x,end='')
         print("*" * (n-x))
         x = x + 1
     return

def hollow_box(n):
    for i in range(n):
        for j in range(n):
            print('*' if i in [0, n-1] or j in [0, n-1] else ' ', end='')
        print()

def solid_diamond(n):
    for idx in range(n-1):
        print((n-idx) * ' ' + (2*idx+1) * '*')
    for idx in range(n-1, -1, -1):
        print((n-idx) * ' ' + (2*idx+1) * '*')

def hollow_diamond(N):
    # The top part (includes the middle row)
    print((N // 2) * " " + '*')
    i = 1
    while i < N // 2 + 1:
        print((N // 2 - i) * " " + '*' + (2 * i - 1) * " " + '*')
        i += 1

    # The bottom part
    i = 0
    while i < N // 2 - 1:
        print(" " * (i + 1) + '*' + " " * (N - 4 - 2 * i) + '*')
        i += 1
    print((N // 2) * " " + '*')


n = int(input("Number please: "))
upside_down_asterisk_triangle(n)
hollow_box(n)
solid_diamond(n)
hollow_diamond(n)