def crunch(str):
    current_letter = ''
    my_list = []
    for letter in str:
        if letter != current_letter:
            my_list.append(letter)
            current_letter = letter
    
    return "".join(my_list)




# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')