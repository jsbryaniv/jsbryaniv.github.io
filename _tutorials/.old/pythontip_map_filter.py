
### PANEL 1 ###


# Python Tip: map and filter
#
# Want to apply a function to every item 
# in a sequence or filter elements from a 
# sequence? Use `map()` and `filter()` 
# for cleaner and more efficient code!


### PANEL 2 ###


# Using map()

# The `map()` function applies a function to all items in a list.
# It returns a map object, which is an iterator that can be 
# converted into a list.

def myfunc(x):
    return x**2 + 1

numbers = [1, 2, 3, 4, 5]

new_numbers = map(myfunc, numbers)

print(list(new_numbers))  # Output: [2, 5, 10, 17, 26]


### PANEL 3 ###


# Using filter()

# The `filter()` function is used to filter elements 
# from an iterable based on a condition. It returns 
# an iterator with elements that satisfy the condition.

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter(is_even, numbers)

print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]


### PANEL 4 ###


# Pro tip: Why is this better than a loop?

# Both `map()` and `filter()` use lazy evaluation, meaning they only
# process elements when they are called downstream. By contrast, a 
# loop will process and store all elements immediately.

list1 = [myfunc(x) for x in numbers]  # Stores all results in memory
list2 = map(myfunc, numbers)          # Only computes when needed


### PANEL 5 ###

# Now you can use `map()` and
# `filter()` to modify and 
# filter sequences with ease!
#
# Follow me for more tips!
# - Shep Bryan IV
