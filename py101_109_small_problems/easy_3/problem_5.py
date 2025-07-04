def triangle (integer):
    space = " "
    n = integer
    for x in range(1, integer + 1):
        print(f'{space * (n - x)} {"*" * x}')

        
#space logic
# n - (n-1)
# n - (n-2)
# n - (n-3)
# n - (n-n)

triangle(12)