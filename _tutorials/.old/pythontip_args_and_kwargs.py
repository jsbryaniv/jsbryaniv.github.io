
### PANEL 1 ###


# Python Tip: args and kwargs
#
# Python makes it easy to make functions
# that can take any number of arguments.
# Use *args and **kwargs for flexible
# and reusable code!


### PANEL 2 ###


# Understanding * and **

# Before we dive into *args and **kwargs, 
# let's understand the * and ** operators.

# Single asterisk (*) unpacks an iterable.
# For example, we can unpack lists into a new list.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list3_with_unpacking = [*list1, *list2] # [1, 2, 3, 4, 5, 6]
list3_witout_unpacking = [list1, list2] # [[1, 2, 3], [4, 5, 6]]

# Double asterisk (**) does the same thing for dictionaries.

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict3_with_unpacking = {**dict1, **dict2} # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict3_without_unpacking = {dict1, dict2}  # Throws an ERROR



### PANEL 3 ###


# Basic *args Example

# When asterisks are used in function definitions,
# they pack arguments into tuples.

def average(*args): # args=(arg1, arg2, arg3, ...)
    return sum(args) / len(args)

print(average(1, 2, 3, 4, 5))  # Output: 3.0

# By packing arguments into a tuple, we can pass
# any number of arguments to the function.


### PANEL 4 ###


# Basic **kwargs Example

# When double asterisks are used in function definitions,
# they pack keyword arguments into dictionaries.

def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Call the function with keyword arguments
greet(name="Alice", age=30)  # Output: name: Alice \n age: 30

# **kwargs allows you to pass named arguments 
# without explicitly defining each one.


### PANEL 5 ###


# Using *args and **kwargs Together

# You can use both *args and **kwargs in the same function.
# IMPORTANT: *args must appear before **kwargs.

def show_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

show_info(1, 2, 3, name="Alice", job="Engineer")
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'job': 'Engineer'}


### PANEL 6 ###


# Now you can create functions that can handle 
# any number of positional and keyword arguments,
# making your code more flexible and reusable!
#
# Follow me for more tips!
# - Shep Bryan IV
