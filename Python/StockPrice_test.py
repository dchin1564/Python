import unittest
from StockPrice import getPrice


class TestStockPrice(unittest.TestCase):
    def test_types(self):
        self.assertRaises(TypeError,getPrice, 3)
        self.assertRaises(TypeError,getPrice,True)
        self.assertRaises(TypeError,getPrice,3+5j)
        self.assertRaises(TypeError,getPrice,3.5)

    def test_values(self):
        self.assertRaises(ValueError,getPrice,"Oranges")
        self.assertRaises(ValueError,getPrice,"Apples")