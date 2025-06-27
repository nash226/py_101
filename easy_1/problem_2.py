"""Print all odd numbers from 1 to 99, inclusive,
 with each number on a separate line.
"""

print(list(range(1,100,2)))

"""Further Exploration
Consider adding a way for the user to specify 
the starting and ending values of the odd numbers printed.
"""

odd_start = int(input("Choose an odd number to start: "))
if odd_start % 2 == 0:
    print("thats not an odd number")
    odd_start = int(input('try again: '))

odd_stop = int(input("Choose an odd number to end: "))
if odd_stop % 2 == 0:
    print("thats not an odd number")
    odd_stop = int(input('try again: '))

print(list(range(odd_start,odd_stop,2)))