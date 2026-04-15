

### PANEL 1 ###


# Python Tip: lru_cache
#
# Want to speed up your code by 
# caching function results? 
# Use `functools.lru_cache` 
# to store results of expensive 
# function calls and reuse them!


### PANEL 2 ###


# Basic Example of a Slow Function

# Here's a slow recursive function to calculate Fibonacci
# numbers. Without caching, it will recalculate the same 
# values multiple times.

def slow_fibonacci(n):
    if n <= 1:
        return n
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)

print(slow_fibonacci(30))


### PANEL 3 ###


# Using lru_cache

# You can speed up the function by adding the `@lru_cache` 
# decorator. This will cache results and return them 
# instantly when the function is called with the same 
# arguments.

from functools import lru_cache

@lru_cache(maxsize=None)  # No limit on the cache size
def fast_fibonacci(n):
    if n <= 1:
        return n
    return fast_fibonacci(n - 1) + fast_fibonacci(n - 2)

print(fast_fibonacci(30))


### PANEL 4 ###


# Cache Management

# IMPORTANT: `lru_cache` stores results in memory, NOT on disk.
# Be careful when caching results that consume a lot of memory.

# You can also clear the cache manually if needed.
fast_fibonacci.cache_clear()  # Clears the cache

# You can access the cache info like 
# hits, misses, and current size.
print(fast_fibonacci.cache_info())


### PANEL 5 ###


# Now you can use `lru_cache` to 
# speed up expensive function calls
# by caching results and reducing 
# redundant computations!
#
# Follow me for more tips!
# - Shep Bryan IV
