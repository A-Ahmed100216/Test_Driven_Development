# This file will have our tests written

# We will see a lot of errors at the start. This is expected because TDD is driven by tests so we need to write the tests first.

# First, we import the required modules/libraries and frameworks
from simple_calc import SimpleCalc
import unittest
import pytest

# Create a class to write our test
# Unittest.TestCase works with unittest framework as a parent class
class CalcTest(unittest.TestCase):
    # IMPORTANT - we must use test word in our functions os our python interpreter knows what we are testing

    # Create an object of our class
    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)  # Boolean
        # We are asking python to test/check if 2 + 4 =6. If True, passes the test, otherwise fails.

    # We can repeat this for subtract
    def test_subtract(self):
        # Tests if 6-4=2. If True, pass. If False, fail
        self.assertEqual(self.calc.subtract(6, 4), 2)  # Boolean

    # And for multiply
    def test_multiply(self):
        # Tests if 2 * 4 is 8, otherwise it will fail.
        self.assertEqual(self.calc.multiply(2, 4), 8)  # Bool

    def test_divide(self):
        # Tests if 12/4=3. If True, passes. False= fails
        self.assertEqual(self.calc.divide(12, 4), 3)  # Bool




