import unittest
import testaus.calculator.calculator as laskin

class MyTestCase(unittest.TestCase):
    def test_miinus(self):
        result = laskin.miinus(5, 2)
        self.assertEqual(result, 3)

    def test_negtuplamiinus(self):
        result = laskin.miinus(-4, -4)
        self.assertEqual(result, 0)

    def test_negmiinus(self):
        result = laskin.miinus(-5, 6)
        self.assertEqual(result, -11)

    def test_onko_numero_vai_ei(self):
        with self.assertRaises(TypeError):
            laskin.miinus(5, "c")


if __name__ == '__main__':
    unittest.main()
