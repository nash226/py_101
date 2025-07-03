"""Question 1"""
# Write two different ways to remove all of the elements 
# from the following list:
# numbers = [1, 2, 3, 4]

# numbers.clear() #1
# while numbers:
#     numbers.pop()

"""Question 2"""
# What will the following code output?
# print([1, 2, 3] + [4, 5])

#will output [1, 2, 3, 4, 5]
#in python we can concatenate two lists 

"""Question 3"""
# What will the following code output?
# str1 = "hello there"
# str2 = str1
# str2 = "goodbye!"
# print(str1)

# "hello there"
# we are not changing the object in memory that str1 is referencing

"""Question 4"""
# What will the following code output?
# my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
# my_list2 = my_list1.copy()
# my_list2[0]['first'] = 42
# print(my_list1)

#[{"first": "42"}, {"second": "value2"}, 3, 4, 5]

"""Question 5"""
# The following function unnecessarily uses two return statements 
# to return boolean values. Can you rewrite this function so it 
# only has one return statement and does not explicitly use 
# either True or False?

# def is_color_valid(color):
#     return (color == "blue" or color == "green") #solution 1

# def is_color_valid(color):
    #return "blue" in color or "green" in color #solution 2.1
    #return color in ['blue', 'green'] #solution 2.2

# print(is_color_valid('green'))