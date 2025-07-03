"""This is a simple tip calculator"""

print("Welcome to tip calculator!")
def get_bill():
    while True:
        try:
            global bill 
            bill = float(input("What is the bill? "))
            if bill > 0:
                return bill
            else:
                print('Value must be positive')
        except ValueError:
            print('Not valid try again')

def get_tip_pcent():
    while True:
        try:
            global tip_pcent
            tip_pcent= float(input('What is the tip percentage? '))
            if tip_pcent > 0:
                return tip_pcent
            else:
                print('Value must be positive')
        except ValueError:
            print('Not valid try again')

get_bill()
get_tip_pcent()

tip = bill * (tip_pcent /100)
total = tip + bill
print(f'The tip is {round(tip,2)}')
print(f'The total is {round(total,2)}')
