import unittest
from testdemo.cal import Calc
class TestCalc1(unittest.TestCase):
    def testSub(self):
        a = 1
        b = 2
        sum = 0
        c = Calc()
        s = c.sub(a,b)

        #断言
        self.assertEqual(sum,s)