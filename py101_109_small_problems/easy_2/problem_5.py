num_1 = float(input('Enter the first number: '))
num_2 = float(input('Enter the second number: '))

def prompt(message):
    print(f'==> {message}')

prompt(f'{num_1} + {num_2} = {num_1 + num_2}')
prompt(f'{num_1} - {num_2} = {num_1 - num_2}')
prompt(f'{num_1} * {num_2} = {num_1 * num_2}')
prompt(f'{num_1} / {num_2} = {num_1 / num_2}')
prompt(f'{num_1} // {num_2} = {num_1 // num_2}')
prompt(f'{num_1} % {num_2} = {num_1 % num_2}')
prompt(f'{num_1} ** {num_2} = {num_1 ** num_2}')