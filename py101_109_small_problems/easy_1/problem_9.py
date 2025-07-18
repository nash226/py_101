country_greg_adoption_year = {'Spain'   : 1582,
                              'Bohemia' : 1584,
                              'Prussia' : 1610,
                              'Alsace'  : 1648
}


def is_leap_year(year, country):
    if year >= country_greg_adoption_year[country]:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return year % 4 == 0
    else:
        return year % 4 == 0

print(is_leap_year(1500, 'Spain'))



# These examples should all print True
# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == True)
# print(is_leap_year(1100) == True)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == True)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)