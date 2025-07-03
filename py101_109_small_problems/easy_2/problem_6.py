def penultimate(string):
    # print (string.split())
    x = len(string.split())
    y = string.split()
    if x == 1:
        return y[0] 
    elif x % 2 == 0:
        return y[ x // 2 - 1]
    elif x % 2 != 0:
        return y[ x // 2]
    else:
        return "Invalid Input"


# These examples should print True
print(penultimate("last word"))
print(penultimate("Launch School is great!"))

#edge cases :
#if the phrase its even or odd length
#if its one word or zero words