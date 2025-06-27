"""Print all odd numbers from 1 to 99, inclusive,
 with each number on a separate line.
"""

for x in range(1,100,2):
    print(x)

"""Further Exploration
Consider adding a way for the user to specify 
the starting and ending values of the odd numbers printed.
"""

odd_start = int(input("Choose an odd number to start: "))
while odd_start % 2 == 0:
    print("thats not an odd number")
    odd_start = int(input('try again: '))
    

odd_stop = int(input("Choose an odd number to end: "))

while odd_stop % 2 == 0 or odd_start > odd_stop:
    print("thats not an odd number or your end is less than your start")
    odd_stop = int(input('try again: '))

for x in range(odd_start,odd_stop,2):
    print(x)