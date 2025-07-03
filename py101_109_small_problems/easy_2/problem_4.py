def multiply(num1, num2):
    return num1 * num2

def square(number):
    return multiply(number, number)


#further exploration

def nth_power(number, to_the_n):
    total = 1
    count = 0
    if to_the_n % 2 != 0:
        while count < to_the_n:
            if count == to_the_n - 1:
                total *= multiply (number, 1)
                return total
            total *= multiply(number, number)
            count += 2
    else:
        while count < to_the_n:
            total *= multiply(number, number)
            count +=2 
    return total
        


print(nth_power(4, 5))