import datetime
now = datetime.datetime.now()
year = now.year
print (year)
age = int(input("What is your age? "))
age_retirement = int(input("At what age would you like to retire? "))

print (f'Its {year}. You will retire in {year + abs(age - age_retirement)}.') 
print (f'You only have {abs(age - age_retirement)} years of work to go!')