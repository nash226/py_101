"""This is a simple tip calculator"""

print("Welcome to tip calculator!")
def get_bill():
    while True:
        bill = float(input("What is the bill? "))
        if bill > 0:
            return bill
        else:
            print('Not valid try again')

def get_tip_pcent():
    while True:
        tip_pcent = float(input('What is the tip percentage?'))
        if tip_pcent > 0:
            return tip_pcent
        else:
            print('Not valid try again')

def total_and_tip(bill, tip_pcent):
    tip = bill * tip_pcent
    total = tip + bill
    print(f'The tip is {round(tip,2)}')
    print(f'The total is {round(total,2)}')