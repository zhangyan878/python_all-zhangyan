import unittest
from day16.entity.clac import Calc
from ddt import ddt # ddt 用来实现数据的参数化（参数化测试）
from ddt import data
from ddt import unpack
from day16.utils.DataRead import DataRead
#data1 = DataRead("database",database="calc",tablename="addtable",user="root",password="").list
data1 = DataRead("excel",filename="D:\\python\\day16\\testcase\\a.xlsx",sheetname="0").list
@ddt
class TestCalc(unittest.TestCase):
    @data(*data1)
    @unpack
    def testAdd(self,a,b,z):
        calc = Calc()
        c = calc.add(a,b)
        self.assertEqual(c,z)