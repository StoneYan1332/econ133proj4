#!pip install -r requirements.txt
#!pip install CFEDemands
from nutrition_results import my_prices

import unittest
import pandas as pd
import numpy as np

#Original Code
def my_prices(p0,p=pbar,j='Millet'):
    """
    Change price of jth good to p0, holding other prices fixed.
    """
    p = p.copy()
    p.loc[j] = p0
    return p

#Test
class TestMyPrices(unittest.TestCase):
    def setUp(self):
        self.prices = pd.Series([1.0, 2.0, 3.0], index=['Millet', 'Chicken', 'Fish'])
        self.good = 'Millet'
        self.new_price = 1.5

    def test_my_prices(self):
        adjusted_prices = my_prices(self.new_price, p=self.prices, j=self.good)
        self.assertEqual(adjusted_prices.loc[self.good], self.new_price, 'price is wrong')


#Original code
def adjust_uganda_prices(new_price, prices=uganda_reference_prices, good=food):
    adjusted_prices = prices.copy()
    adjusted_prices.loc[good] = new_price
    return adjusted_prices

#Test
class TestAdjustUgandaPrices(unittest.TestCase):
    def setUp(self):
        self.new_price = 10
        self.prices = pd.Series([20,30,40] index = ['Beef', 'Chicken', 'Fish'])
        self.good = 'Beef'

    def test_adjust_uganda_prices(self):
        adjusted_prices = adjust_uganda_prices(self.new_price, self.prices, self.good)
        
         expected_output = pd.Series([10, 30, 40], index=['Beef', 'Chicken', 'Fish'])
        pd.testing.assert_series_equal(adjusted_prices, expected_output, 'series not equal')

#Run
$ python -m unittest nutrition_results_test.py

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
