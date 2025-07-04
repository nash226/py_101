def stringy(number):
    char = ''
    for x in range(number):
        digit = '1' if x % 2 == 0 else '0'
        char = char + digit
    return char

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True