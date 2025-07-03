"""Write a function that takes one integer argument 
and returns True when the number's absolute value is odd, False otherwise.
"""

def odd(number):
    """Takes a number and finds out if its absolute value is
      odd and returns true if it is and false if not"""
    if number < 0:
        number = number * -1
    return number % 2 != 0
