print("What is your name? ")
name = input()
if name[-1] != '!':
    print("Hello " + name)
else:
    print(f'HELLO {name.upper()} WHY ARE WE YELLING?')