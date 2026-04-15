

### PANEL 1 ###


# Python Tip: f-strings
#
# Tired of complex string formatting?
# Use f-strings for cleaner, faster, 
# and more readable code!


### PANEL 2 ###

# Basic f-strings

# F-strings (formatted string literals) allow you 
# to quickly fill variables into strings.
# Just put an f before the string and use curly braces
# to insert variables.

name = "Bob"
age = 30

# Don't do this
mystring = "Hello, " + name + "! You are " + str(age) + " years old."

# Do this instead
mystring = f"Hello, {name}! You are {age} years old."


### PANEL 3 ###

# Formatting with Precision

# You can format numbers with precision using f-strings.
# Simply add a colon, a number, and a letter to the variable.

# Format float to n decimal places
pi = 3.141592653589793
print(f"π ≈ {pi:.2f}")  # π ≈ 3.14
print(f"π ≈ {pi:.4f}")  # π ≈ 3.1416

# Format significant figures
mass_electron = 9.10938356e-31
print(f"m ≈ {mass_electron:.2g}")  # m ≈ 9.1e-31
print(f"m ≈ {mass_electron:.4g}")  # m ≈ 9.109e-31

# Format an integer with padding
print(f"Answer to life = {42:02d}")  # Answer to life = 42
print(f"Answer to life = {42:04d}")  # Answer to life = 0042

# Format a date
from datetime import datetime
print(f'{datetime.now():%Y-%m-%d}')  # 2025-03-12


### PANEL 4 ###


# Now you can use f-strings
# to format strings with ease,
# precision, and readability!
#
# Follow me for more tips!
