### PANEL 1 ###

# Python Tip: Hardware-Agnostic `pip freeze`
#
# Working with PyTorch? Avoid hardware-specific dependencies like NVIDIA CUDA 
# from your `requirements.txt`. Here's a one-liner to make it hardware-agnostic!


### PANEL 2 ###

# The Problem

# We often use `pip freeze` to generate a `requirements.txt` file, but it
# includes all installed packages, including those that are hardware-specific,
# such as NVIDIA CUDA libraries, which can cause compatibility issues for users
# without the same hardware setup.

pip freeze > requirements.txt


### PANEL 3 ###

# The Solution

# Use this command to generate a `requirements.txt` that includes PyTorch 
# but excludes hardware-dependent packages:

pip list --not-required --format=freeze > requirements.txt


### PANEL 4 ###

# Now you can share your requirements without worrying about hardware compatibility!
# Follow me for more Python tips!
# - Shep Bryan IV
