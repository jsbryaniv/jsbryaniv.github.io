

### PANEL 1 ###


# Python Tip: Iterators
#
# Having memory issues storing 
# large datasets in lists? 
# Instead of storing everything 
# in memory, use iterators!


### PANEL 2 ###


# Iterators are just like lists. You can create them
# using comprehensions, with parentheses instead of 
# brackets. Loop over them as you would a list.

# Create lists and iterators using comprehensions
mylist = [x for x in range(1_000_000)]  # [] for list
myiter = (x for x in range(1_000_000))  # () for iterator

# Loop over lists and iterators the same way
for i in mylist: print(i)  # Outputs 1, 2, 3, ...
for i in myiter: print(i)  # Outputs 1, 2, 3, ...


### PANEL 3 ###


# Iterators are more memory-efficient than lists.

# This stores 1,000,000 integers in memory
mylist = [x for x in range(1_000_000)]  

# This stores only the current integer in memory
myiter = (x for x in range(1_000_000))  


### PANEL 4 ###


# The catch is that iterators do not accept indexing.
# Use the next() function to get the next element.

# This will get the third element of the list...
x2 = mylist[2]
# ... but myiter[2] will raise an error!

# Use next() instead!
x0 = next(myiter)  # Get the first element
x1 = next(myiter)  # Get the second element
x2 = next(myiter)  # Get the third element


### PANEL 5 ###


# For complex iterators, like image loading, make iterators 
# using classes by defining __init__, __iter__, and __next__.
# Raise StopIteration to stop the iteration.

from PIL import Image

class MyImages:
    def __init__(self):  # Specify initial values
        self.index = 0
        self.max = 100

    def __iter__(self):  # Required for iteration
        return self

    def __next__(self):  # Specify what to return
        img = Image.open(f"image_{self.index}.png")
        if self.index >= self.max:
            raise StopIteration
        self.index += 1
        return img
    
for img in MyImages():  # This will load images one at a time
    img.show()


### PANEL 6 ###


# Now you can use iterators to load 
# Large datasets one element at a time,
# saving memory!
#
# Follow me for more tips!
