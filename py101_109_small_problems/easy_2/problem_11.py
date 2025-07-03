def center_of(string1):
    x = len(string1)
    if x % 2 == 1:
        return string1[x // 2]
    else:
        middle_1 = string1[x // 2 - 1]
        middle_2 = string1[(x // 2)]
        return middle_1 + middle_2
        





# print(center_of('bob'))

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True