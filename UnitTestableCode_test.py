import unittest
import UnitTestableCode

class DefaultTestCase(unittest.TestCase):
    def setUp(self):
        self.value = ""

    def tearDown(self):
        self.value=""
    
    def test_sum(self):
        assert sum([1, 2, 3]) == 6, "Should be 6"
    
    def test_sum_tuple(self):
        assert sum((1, 2, 2)) == 6, "Should be 6"

    def test_functionB(self):
        value = UnitTestableCode.functionB("cc")
        self.assertEqual(value, "functionBcc")

    def test_functionC(self):
        value = UnitTestableCode.functionC(123)
        self.assertEqual(value, "functionC123")

    def test_list_int(self):
            """
            Test that it can sum a list of integers
            """
            data = [1, 2, 3]
            result = UnitTestableCode.sum1(data)
            self.assertEqual(result, 6)        
    
if __name__ == "__main__":
    unittest.main()
    