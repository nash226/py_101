""" This is a mortgage calculator.
    It takes the loan amount, APR, and the loan duration.
    And outputs the monthly payment.
"""

def invalid_number(string):
    """This function makes sure we are getting valid inputs from our users"""
    try: 
        float(string)
    except (ValueError, TypeError):
        return True
    return False

def not_valid(x):
    """This function prints out not valid and creates assignment for the argument var"""
    print ('Not a valid number. Try Again: ')
    x = input()
    return x


apr = input("Enter APR %: ")

while invalid_number(apr) and float(apr) < 0:
    not_valid(apr)

apr = float(apr)

monthly_int_rate = (apr / 100) / 12

loan_amount = input("Enter Loan amount ($): ")

while invalid_number(loan_amount) or float(loan_amount) <= 0:
    not_valid(loan_amount)

loan_amount = float(loan_amount)

loan_duration = input("Enter loan duration (months): ")

while invalid_number(loan_duration)or float(loan_duration) <= 0 :
    not_valid(loan_duration)

loan_duration = float(loan_duration)

if apr == 0:
    monthly_payment = loan_amount / loan_duration
else:
    monthly_payment = loan_amount * (monthly_int_rate /
                                (1 - (1 + monthly_int_rate) ** (-loan_duration)))

print(f"Your monthly payment is ${round(monthly_payment, 2)}\nGoodbye!")