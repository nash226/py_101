def oddities(list):
    count = 0
    my_list = []
    for element in list:
        if count % 2 == 0:
            my_list.append(element)
        count += 1 
    return my_list

def slice(list):
    return list[0::2]

# #Further Exploration
# def oddities(lst):
#     my_list = []
#     for x in range(len(lst)):
#         if x % 2 == 0:
#             my_list.append(lst[x])
#     return my_list


print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

print(slice([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(slice([1, 2, 3, 4]) == [1, 3])        # True
print(slice(["abc", "def"]) == ['abc'])     # True
print(slice([123]) == [123])                # True
print(slice([]) == [])                      # True