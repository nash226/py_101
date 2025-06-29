"""
This is a calculator that takes 2 numbers and outputs an operation
on the numbers
 """
LANGUAGE = 'en'

import json

with open('calculator_messages.json', 'r') as file:
    Messages = json.load(file)

def prompt (key):
        message = messages(key, LANGUAGE)
        print(f'==> {message}')

def invalid_number(number_str):
        try:
            float(number_str)
        except ValueError:
            return True

        return False

def messages(message, lang = 'en'):
     return Messages[lang][message]


english_or_spanish = 0

while english_or_spanish == 0:

    language = input('==> English or Spanish?: ')
    if language[0].lower() == 'e':
        LANGUAGE = 'en'
        break
        
    elif language[0].lower() == 's':
        LANGUAGE = 'es'
        break

while True:

    prompt('welcome')

    prompt('first_number')
    number1 = input()

    while invalid_number(number1):
        prompt('invalid_number')
        number1 = input()

    prompt('second_number')
    number2 = input()

    while invalid_number(number2):
        prompt('invalid_number')
        number2 = input()

    prompt('operation')
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt('not_in')
        operation = input()

    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) / float(number2)
            

    prompt('result')

    print(f'==> {output}')

    prompt('another_one')
    yes_or_no = input()

    if yes_or_no[0].lower() != 'y':
        break