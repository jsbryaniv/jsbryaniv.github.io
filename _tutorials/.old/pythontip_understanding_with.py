

### PANEL 1 ###


# Python Tip: Understanding `with`
#
# `with` statements seem strange at
# first, but they are very simple! 
# `with` simplifies file handling 
# while providing a very robust
# safety net against human errors.


### PANEL 2 ###


# Without `with`

# You can open files without `with`...
# ... but remember to CLOSE THE FILE!

file = open('example.txt', 'w') # 'w' for write
file.write("Hello, world!")
file.close()  # Don't forget to close the file!

file = open('example.txt', 'r') # 'r' for read
content = file.read()
file.close()  # Don't forget to close the file!

print(content)  # Prints "Hello, world!"


### PANEL 3 ###


# With `with`

# With statements not only simplify file handling, 
# but also make it robust to human error.

with open('example.txt', 'w') as file: # 'w' for write
    file.write("Hello, world!")

with open('example.txt', 'r') as file: # 'r' for read
    content = file.read()

print(content)  # Prints "Hello, world!"


### PANEL 4 ###

# Why `with` is important

# Without `with`, small mistakes can 
# cause unexpected behavior.

file1 = open('example.txt', 'w')
file1.write("Hello, world!")
# Woops I forgot to close the file...

file2 = open('example.txt', 'r')
content2 = file2.read()

# ... this may return an empty string.
print(content2)

# Not closing files can also lead to resource 
# issues or potential file access problems.


### PANEL 5 ###

# With `with` code is much safer.

with open('example.txt', 'w') as file:
    file.write("Hello, world!")

with open('example.txt', 'r') as file:
    content = file.read()

print(content)  # Prints "Hello, world!"



### PANEL 6 ###


# Now you know how to make simple
# and robust file handling with `with`.
# Follow me for more Python tips!
# - Shep Bryan IV



