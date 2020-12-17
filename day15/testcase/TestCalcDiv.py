import unittest
from calc.calc import Calc
from ddt import ddt
from ddt import data
from ddt import unpack
data1 = [
    [25,5,5],
    [5,1,5],
    [100,10,10],
    [4,2,2]
]
@ddt
class TestCalcDiv(unittest.TestCase):
    @data(*data1)
    @unpack
    def testDiv(self,x,y,z):
        a = x
        b = y
        c = z
        calc = Calc()
        sum = calc.div(a,b)
        self.assertEqual(c,sum)