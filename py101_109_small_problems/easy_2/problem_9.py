import random

name = input("Enter your name: ")
if name == '':
    name = 'Teddy'

print(f'{name} is {random.choice(range(20,101))} years old!')