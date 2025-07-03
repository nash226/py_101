"""This program asks the user to enter an integer >0
    and it asks if they want a sum or product of all 
    the numbers between 1 and the entered integer"""


integer = int(input('Please enter an integer greater than 0: '))
while integer <= 0:
    print("Invalid input, please enter an integer larger than 0")
    integer = int(input())

sum_or_product = input('Enter "s" to compute the sum, or "p" to compute the product. ')
while sum_or_product.lower() not in ['s','p']:
    print('Invalid input please enter "s" or "p"')
    sum_or_product = input()

def sum_interval():
    """This function finds our sum of the interval"""
    sum = 0
    for x in range(1, integer + 1):
        sum += x
    return sum

def product_interval():
    """This function finds our product of the interval"""
    product = 1
    for x in range(1, integer + 1):
        product *= x
    return product

if sum_or_product == 's':
    print (f'The sum of the integers between 1 and {integer} is {sum_interval()}')
else:
    print (f'The product of the integers between 1 and {integer} is {product_interval()}')