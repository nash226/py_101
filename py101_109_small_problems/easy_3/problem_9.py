def clean_up(string):
    empty_string = ''
    for char in string:
        if char.isalpha():
            empty_string += char
        elif empty_string.endswith(" "):
            continue
        else:
            empty_string += " "
    return empty_string




print(clean_up("---what's my +*& line?") == " what s my line ")
# True