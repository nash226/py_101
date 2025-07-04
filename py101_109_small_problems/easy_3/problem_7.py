def twice(number):
    string_number = (str(number))
    # left_half = len(number) // 2 - 1 
    # right_half = len(number) // 2 
    half = len(string_number) // 2

    if string_number[:half] == string_number[half:] and len(string_number) % 2 == 0:
        return number
    else:
        return number * 2
        
print(twice(37) == 74)                # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True