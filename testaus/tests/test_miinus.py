import unittest
import testaus.calculator.calculator as laskin

class MyTestCase(unittest.TestCase):
    def test_miinus(self):
        result = laskin.miinus(5, 2)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
