"""Unit test:
    Unit testing in Python involves writing tests for small units of code,
    such as functions or methods, to ensure they work as expected.
    Python provides several framework for unit testing,
    with the most popular being `unittest`, `pytest`, `nose`.
"""

"""Using `unittest`
    The `unittest` module is built into Python
    and provides a robust framework for creating and running tests.
    1. Create a test case: A test case is created by subclassing `unittest.TestCase`.
    2. Write test methods: Define methods within your test case that start with the word `test`.
"""
import unittest
from divide import divide_by

class TestDivideFunction(unittest.TestCase):
    def test_divide_positive_numbers(self):
        self.assertEqual(divide_by(10, 5), 2)
        
    def test_divide_negative_numbers(self):
        self.assertEqual(divide_by(-50, -2), 25)
        
        
if __name__ == '__main__':
    unittest.main()
    
"""Using `pytest`
    `pytest` is a third-party testing framework that is very powerful and flexible.
    1. Install pytest: You need to install `pytest` using pip.
    2. Write test functions: Simply define functions that start with `test_`.
    3. Run tests: Run the tests by executing the `pytest` command in the terminal.
"""

from add import add

def test_aed_positive_numbers():
    assert add(1, 2) == 3
    
def test_add_negative_numbers():
    assert add(-1, -1) == -2