# Create a Dictionary using list comprehension in Python

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

my_dict = {k: v for k, v in zip(keys, values)}
print(my_dict)

