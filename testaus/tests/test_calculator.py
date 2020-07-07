import unittest
import testaus.calculator.calculator as laskin

class TestCalculator(unittest.TestCase):
    def test_summa(self):
        num1 = 2
        num2 = 3
        result = laskin.plus(num1, num2)
        self.assertEqual(result, 5)

    def test_numero(self):
        if laskin.plus(self, self) != float or laskin.plus(self, self) != int:
            self.assertFalse()

if __name__ == '__main__':
    unittest.main()
