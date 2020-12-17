import unittest
from calc.calc import Calc
from ddt import ddt
from ddt import data
from ddt import unpack
data1 = [
    [1,2,3],
    [-9,-1,-10],
    [0,9,9],
    [2,3,5]
]
@ddt
class TestCalcAdd(unittest.TestCase):
    @data(*data1)
    @unpack
    def testAdd(self,x,y,z):
        a = x
        b = y
        c = z
        calc = Calc()
        sum = calc.add(a,b)
        self.assertEqual(c,sum)