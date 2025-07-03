'''This is a program that prints out a rooms area'''

print("Welcome to room area calculator!")
def how_big():
    "takes input from user about lenght and "
    "width and prints out the area in"
    "both square meters and feet "

    length = input('whats the length?(in meters): ')
    width = input('whats the width?(in meters): ')
    area_sq_meter = float(length) * float(width)
    area_sq_feet = area_sq_meter * 10.7639
    print(f'The rooms area is {round(area_sq_meter, 2)} square meters or {round(area_sq_feet, 2)} square feet')
    
how_big()