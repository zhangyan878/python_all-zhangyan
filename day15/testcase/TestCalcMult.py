import unittest
from calc.calc import Calc
from ddt import ddt
from ddt import data
from ddt import unpack
data1 = [
    [1,2,2],
    [2,2,4],
    [-3,-5,15],
    [0,2,0]
]
@ddt
class TestCalcMult(unittest.TestCase):
    @data(*data1)
    @unpack
    def testMult(self,x,y,z):
        a = x
        b = y
        c = z
        calc = Calc()
        sum = calc.mult(a,b)
        self.assertEqual(c,sum)