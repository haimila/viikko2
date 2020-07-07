import unittest
import testaus.calculator.calculator as laskin

class MyTestCase(unittest.TestCase):
    def test_tulo(self):
        result = laskin.tulo(6, 4)
        self.assertEqual(result, 24)


if __name__ == '__main__':
    unittest.main()
