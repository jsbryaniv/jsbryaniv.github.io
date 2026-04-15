

### PANEL 1 ###

# Python Tip: Product Iterators
#
# Did you know that nested for
# loops make code slower? Try
# using iterators for cleaner,
# faster, and more efficient code!


### PANEL 2 ###

# Basic Nested Loops

# Every time you make a for loop, it
# adds overhead to your computation.

import numpy as np

shape = (100, 100)
matrix = np.random.rand(*shape)

# Try to avoid nested loops
for row in range(matrix.shape[0]):
    for col in range(matrix.shape[1]):
        print(matrix[row, col])


### PANEL 3 ###

# Using itertools.product

# The itertools.product() function can replace nested loops.
# It generates all combinations of indices in a matrix.

from itertools import product

# Replace nested loops with itertools.product()
for row, col in product(range(shape[0]), range(shape[1])):
    print(matrix[row, col])

# We replaced our double loop with a single loop!


### PANEL 4 ###

# Nested loops of unknown depth

# The itertools.product() function can also handle
# nested loops of unknown depth.

matrix_2d = np.random.rand(10, 10)
matrix_3d = np.random.rand(10, 10, 10)

# Loop over 2D matrix
for indices in product(*map(range, matrix_2d.shape)):
    print(matrix_2d[indices])

# Loop over 3D matrix
for indices in product(*map(range, matrix_3d.shape)):
    print(matrix_3d[indices])


### PANEL 5 ###


# Now you can replace nested loops 
# with iterators for cleaner,
# more efficient code!
#
# Follow me for more tips!
# - Shep Bryan IV
