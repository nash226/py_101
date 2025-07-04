def print_in_box(text):

    x = len(text)

    print(f'+{("-" * x)}--+\n'
          f'| {" " * x} |\n'
          f'| {text} |\n'
          f'| {" " * x} |\n'
          f'+{("-" * x)}--+'
          )



print_in_box('To boldly go where no one has gone before.')
print_in_box('')



