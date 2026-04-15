
### PANEL 1 ###


# Python Tip: Lambda Functions
#
# Need a quick function for a 
# single evaluation? Use `lambda`
# functions to write compact, 
# one-line functions without 
# defining a whole block of code!


### PANEL 2 ###

# What is a lambda function?

# A lambda function is exactly the same as a regular function, 
# but it’s defined in a single line and can only contain one 
# expression (no if's, loops, etc.). It’s often used for simple
# tasks where you don’t need a full function.

# Basic syntax:
# lambda arguments: expression

add = lambda x, y: x + y

print(add(3, 4))  # Output: 7

# Lambda functions are useful when you need to perform a quick 
# evaluation, but don’t want to write a full function definition.


### PANEL 3 ###


# Why use lambda functions?

# Lambda functions let you perform simple operations without the 
# need for a full function declaration. This makes your code shorter 
# and easier to read.

# Example: Sorting a list of tuples based on the second element
data = [(1, 2), (3, 1), (5, 3)]

# Use lambda to define a function to sort based on the second value
data.sort(key=lambda x: x[1])

print(data)  # Output: [(3, 1), (1, 2), (5, 3)]

# This is especially useful in places where you only need a function 
# temporarily and don’t want to clutter your code.


### PANEL 4 ###


# Using lambda with map(), filter(), and reduce()

# Lambda functions are commonly used with functions like `map()`, 
# `filter()`, and `reduce()` where you need to apply a simple 
# operation to each element in a sequence.

numbers = [1, 2, 3, 4, 5]

# Using lambda with map to square each number
squared = map(lambda x: x**2, numbers)

print(list(squared))  # Output: [1, 4, 9, 16, 25]

# Using lambda with filter to keep only even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

print(list(even_numbers))  # Output: [2, 4]


### PANEL 5 ###


# Pro Tip: Lambda functions are also known as anonymous functions

# Lambda functions are often called "anonymous functions" because 
# they don’t have a name like regular functions. Instead, they're 
# defined inline for short, one-off tasks.

# Similar to lambda functions in Python, many other languages 
# support anonymous functions, such as:
# - JavaScript:  const add = (x, y) => x + y;
# - Julia:       add = (x, y) -> x + y
# - Ruby:        add = ->(x, y) { x + y }


### PANEL 5 ###


# Now you can use lambda functions 
# for quick, one-line functions when 
# keeping your code short and simple!
#
# Follow me for more tips!
# - Shep Bryan IV


