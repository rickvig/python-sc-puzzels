
import unittest
from print_numbers import list_numbers

class TestPrintNumbers(unittest.TestCase):

    def test_print_tree(self):
        numbers = list_numbers()
        self.assertEqual(numbers[0], "1", "Should be 1")
        self.assertEqual(numbers[2], "Tree", "Should be Tree")
        self.assertEqual(numbers[8], "Tree", "Should be Tree")
        self.assertEqual(numbers[98], "Tree", "Should be Tree")
        
    def test_print_five(self):
        numbers = list_numbers()
        self.assertEqual(numbers[4], "Five", "Should be Five")
        self.assertEqual(numbers[9], "Five", "Should be Five")
        self.assertEqual(numbers[99], "Five", "Should be Five")
        
    def test_print_tree_five(self):
        numbers = list_numbers()
        self.assertEqual(numbers[14], "TreeFive", "Should be TreeFive")
        self.assertEqual(numbers[29], "TreeFive", "Should be TreeFive")
        self.assertEqual(numbers[44], "TreeFive", "Should be TreeFive")
        self.assertEqual(numbers[59], "TreeFive", "Should be TreeFive")
        self.assertEqual(numbers[74], "TreeFive", "Should be TreeFive")
        
    def test_print_other_number(self):
        numbers = list_numbers()
        self.assertEqual(numbers[0], "1", "Should be 1")
        self.assertEqual(numbers[1], "2", "Should be 2")
        self.assertEqual(numbers[97], "98", "Should be 92")

if __name__ == '__main__':
    unittest.main()
