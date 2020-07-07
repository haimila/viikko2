import unittest
import testaus.calculator.calculator as laskin

class MyTestCase(unittest.TestCase):
    def test_tulo(self):
        result = laskin.tulo(6, 4)
        self.assertEqual(result, 24)

    def test_nollatulo(self):
        result = laskin.tulo(6, 0)
        self.assertEqual(result, 0)

    def test_desimaaleilla(self):
        result = laskin.tulo(2.5, 4)
        self.assertEqual(result, 10)

    def test_onko_numero_vai_ei(self):
        with self.assertRaises(ValueError):
            laskin.tulo(5, "d")

if __name__ == '__main__':
    unittest.main()
