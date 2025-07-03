def short_long_short(word_1, word_2):
    
    if len(word_1) > len(word_2):
        return word_2 + word_1 + word_2
    else:
        return word_1 + word_2 + word_1

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")