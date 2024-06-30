"""import
    In Python, the `import` statement is used to include the definitions (functions, classes, variables)
    and code from another module into the current program. Here's a guild of how to use the `import` statement effectively.
"""

"""Basic Import
    To import a module, you simply to use the `import` statement followed by the module name:
"""
# This imports the entire `math` module, allowing you to use its functions and constants with the `math.` prefix:
import math

print(math.sqrt(16))
print(math.pi)

"""Import with Alias
    You can give a module an alias using the `as` keyword, which can be useful for shortening module names or avoiding name conflicts:
"""
import numpy as np

arr = np.array([1, 2, 3])
print(arr)

"""Import Specific items
    If you only need specific functions or classes from a module,
    you can import them directly using the `from ... import ...` syntax:
"""
from math import sqrt, pi

print(sqrt(10))
print(pi)

"""Import All Items
    You can import all items from a module using the `from ... import *` syntax.
    However, this is generally, discouraged because it can lead to cluttered namespace and potential name conflicts:
"""
from math import *

print(sqrt(20))
print(pi)

