import typing
import unittest

# Python runs setUp() before running each test method

# Python prints one character for each unit test as it is completed.
# a passing test prints a dot
# a test that results in an error prints an E
# a test that fails an assertion prints an F

class Employee():
    def __init__(self, first_name: str, last_name: str, salary: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def give_raise(self, raise_amount: int = 5000) -> None:
        self.salary += raise_amount
    

class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.my_employee = Employee('Joe', 'Biden', 90000)
    
    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 95000)
    
    def test_give_custom_raise(self):
        self.my_employee.give_raise(17000)
        self.assertEqual(self.my_employee.salary, 107000)

unittest.main()

