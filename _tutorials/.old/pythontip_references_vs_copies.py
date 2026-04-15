### PANEL 1 ###


# Python Tip: Understanding References vs Copies
#
# When coding with arrays in Python (like lists, 
# NumPy arrays, or PyTorch tensors), it's important
# to know when you're working with references vs 
# copies. Understanding this concept helps avoid 
# unexpected behavior and bugs!


### PANEL 2 ###


# What is a Reference?

# In Python, when you assign `y = x`, you're creating a reference.
# This means both `y` and `x` point to the same object in memory.
# Modifying one will affect the other.

x = [1, 2, 3]
y = x     # y is a reference to x
y[0] = 9  # Modifying y will affect x
print(x)  # Output: [9, 2, 3] (x is modified)
print(y)  # Output: [9, 2, 3] (y is also modified)


### PANEL 3 ###


# Creating a Copy

# To avoid modifying the original data, you can create a copy.
# Using `x.copy()` (or `x.clone()` for PyTorch) will give you 
# an independent copy.

x = [1, 2, 3]
y = x.copy()  # Creating a new copy of x
y[0] = 9  # Modifying y won't affect x
print(x)  # Output: [1, 2, 3] (x is unchanged)
print(y)  # Output: [9, 2, 3] (y is a new list)


### PANEL 4 ###


# Why It Matters

# Understanding whether you're working with a reference or a copy 
# is crucial, especially when dealing with large data or complex
# operations. If you accidentally modify data via a reference, it 
# can cause unexpected bugs!

# Example: Forgetting to copy a list and modifying it unexpectedly
x = [1, 2, 3]
y = x  # This is a reference, not a copy
y.append(4)
print(x)  # Output: [1, 2, 3, 4] (x is modified too!)


### PANEL 5 ###


# Now you know how to manage references and copies
# in Python. Use `.copy()` or `.clone()` to create 
# copies when you need independent data.
#
# Follow me for more Python tips!
# - Shep Bryan IV
