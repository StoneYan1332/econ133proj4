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

#Test#Run

test_adjeust_uganda_prices())
if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)

$ python -m unittest <module-name>.pynutrition_results_test "", ''series not equal