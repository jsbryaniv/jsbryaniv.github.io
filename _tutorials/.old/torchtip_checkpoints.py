



### PANEL 1 ###



import torch 

# PyTorch Tips: Checkpoints
#
# Are you running out of memory when 
# you train heavy PyTorch models?
# Do you not mind waiting for results?
#
# Use checkpoints to trade 
# time for memory!



### PANEL 2 ###



# The Problem

# Whenever you do an operation on a tensor,
# PyTorch stores a copy of it in memory.

# This is what we see ... 

x = torch.tensor(0.0, requires_grad=True)

x = x + 1   # x = 1
x = x * 2   # x = 2
x = x ** 2  # x = 4
x = x - 1   # x = 3

# ... but this is what PyTorch sees.

x0 = torch.tensor(0.0, requires_grad=True)

x1 = x0 + 1   # x1 = 1 and x0 = 0
x2 = x1 * 2   # x2 = 2 and x1 = 1 and x0 = 0
x3 = x2 ** 2  # x3 = 4 and x2 = 2 and x1 = 1 and x0 = 0
x4 = x3 - 1   # x4 = 3 and x3 = 4 and x2 = 2 and x1 = 1 and x0 = 0



### PANEL 3 ###



# The Problem

# This is a problem when you are working with
# functions that have a lot of operations.

def heavy_function(x, a):
    for _ in range(100):
        x = x + a
    return x

class HeavyModel(torch.nn.Module):
    def __init__(self):
        super(HeavyModel, self).__init__()
        self.a = torch.nn.Parameter(torch.tensor(1.0))
    def forward(self, x):
        for _ in range(1000):
            x = heavy_function(x, self.a)
        return x

# This block will store 100,000 intermediate tensors
model = HeavyModel()
x = torch.tensor(0.0, requires_grad=True)
y = model(x)
y.backward()



### PANEL 4 ###



# The Solution

# Use checkpoints to trade time for memory!

from torch.utils.checkpoint import checkpoint

# Functions inside a checkpoint wrapper will
# not store intermediate tensors.
# Instead, PyTorch will recompute the tensors
# when you call the backward() method.



### PANEL 5 ###



# Checkpoints are simple to use, just wrap
# the function and args inside a checkpoint.

def heavy_function(x, a):
    for _ in range(100):
        x = x + a
    return x

class LightModel(torch.nn.Module):
    def __init__(self):
        super(LightModel, self).__init__()
        self.a = torch.nn.Parameter(torch.tensor(1.0))
    def forward(self, x):
        for _ in range(1000):
            # x = heavy_function(x, self.a)
            x = checkpoint(heavy_function, x, self.a)
        return x

# This block will store only about 100 
# intermediate tensors at a time...
model = LightModel()
x = torch.tensor(0.0, requires_grad=True)
y = model(x)
y.backward()
# ... but it has to compute them twice,
# both in the forward and backward pass.



### PANEL 6 ###



# Now you can use checkpoints to trade
# time for memory when training models.
#
# Follow me for more tips!


