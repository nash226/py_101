def greetings(list, dict):
    return f'Hello, {" ".join(list)}! Nice to have a {dict["title"]} {dict["occupation"]} around.'

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.