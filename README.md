# TDD - Test Driven Development

## Contents
* **TDD**

# Why TDD?
* Before we can release any product or software, we must test it t ensure it if fit for purpose.
* Unit Testing - Testing an individual component of a whole product.
* Product Testing - Testing a fully assembled product.
* Good unit testing is important for whole product testing. If each aspect works well separately, we know the issues occurred in assembly, rather than testing each separate component after.
* TDD helps us minimise the risk of failure after sending the product to production.




# TDD in Python
Python has several modules that we can use to test our code including:
* pytest
* unittest
## Steps
1. Create a file to write tests
2. Run the test file, the tests should all fail.
3. Create a file to write code 
4. Refactor and add the code to pass the tests.
## Naming convention
* file name:  simple_calc
* test name: test_simple_calc

# TDD process - Testing File
1. Install the testing framework using the command
```pip install pytest```
2. Create a test file. Within this file, we will see a lot of errors. This is expected because TDD is driven by tests so we need to write the tests first.
3. Import the required modules/libraries and frameworks
```python
from simple_calc import SimpleCalc
import unittest
import pytest
```
4. Create a test class. This will be a child class of the unittest framework.
```python
class CalcTest(unittest.TestCase):
```
5. Within the class we can create an instance of the class which we will test, in this case a simple calculator. 
```python

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
```



# Terminal commands
1. Run a test in the terminal
```python -m pytest```
2. View breakdown of tests - Shows which tests passed
```python -m unittest discover -v```
3. View breakdown of testing
```pytest -v```


