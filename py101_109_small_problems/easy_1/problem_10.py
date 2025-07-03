def multisum(number):
    total_sum = 0
    for current_number in range(1, number + 1):
        if current_number % 3 == 0 or current_number % 5 == 0:
            total_sum += current_number
    return total_sum


# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)