
def century(year):
    nth = year // 100
    if year % 100 !=0:
        nth += 1

    ending = str(nth)
    if ending.endswith(('11', '12', '13',)):
        ending = "th"
    elif ending.endswith('1'): 
        ending = 'st'
    elif ending.endswith('2'):
        ending = 'nd'
    elif ending.endswith('3'):
        ending = 'rd'
    else:
        ending = 'th'

    return f'{nth}{ending}'

    



#A century is every 100 years 
#first century from 01 - 100
#2nd century is from 101 - 200
#3rd century is from 201 - 300

print(century(2000) )
print(century(2001) )
print(century(1965) )
print(century(256) )
print(century(5) )
print(century(10103))
print(century(1052) )
print(century(1127) )
print(century(11201))


print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True