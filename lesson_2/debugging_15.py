import pdb
def titlize(sentence):
    words = sentence.split()
    new_words = []

    for word in words:
        pdb.set_trace()

        if len(word) > 2:
            new_words.append(word.capitalize())
        else:
            new_words.append(word)
            
    return ' '.join(new_words)

title = 'hello world of programming'
print(titlize(title))