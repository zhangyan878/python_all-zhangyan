import unittest
from calc.calc import Calc
from ddt import ddt
from ddt import data
from ddt import unpack
data1 = [
    [2,1,1],
    [7,6,1],
    [0,3,-3],
    [-3,-3,0]
]
@ddt
class TestCalcSub(unittest.TestCase):
    @data(*data1)
    @unpack
    def testSub(self,x,y,z):
        a = x
        b = y
        c = z
        calc = Calc()
        sum = calc.sub(a,b)
        self.assertEqual(c,sum)