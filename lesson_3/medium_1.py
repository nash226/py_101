"""Question 1"""
# Let's do some "ASCII Art": a stone-age form of nerd artwork from 
# back in the days before computers had video screens.
# For this practice problem, write a program that outputs The 
# Flintstones Rock! 10 times, with each line prefixed by one more 
# hyphen than the line above it. The output should start out like 
# # this:
# -The Flintstones Rock!
# --The Flintstones Rock!
# ---The Flintstones Rock!
# #     ...

# for x in range(10):
#     print((x + 1) * '-' + "The Flintstones Rock!") # solution 1

# for x in range(1, 11):
#     print(f'{"-" * x }The Flintstones Rock!') # solution 2

"""Question 2"""
# Alan wrote the following function, which was intended to 
# return all of the factors of number:
def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

