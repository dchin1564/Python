import unittest
from test2 import yfinancetut


class TestStockPrice(unittest.TestCase):
    def test_types(self):
        self.assertRaises(TypeError,yfinancetut, 3)
        self.assertRaises(TypeError,yfinancetut,True)
        self.assertRaises(TypeError,yfinancetut,3+5j)
        self.assertRaises(TypeError,yfinancetut,3.5)

    def test_values(self):
        self.assertRaises(ValueError,yfinancetut,"Oranges")
        self.assertRaises(ValueError,yfinancetut,"Apples")