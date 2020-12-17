import unittest
import os
from HTMLTestRunner import HTMLTestRunner
from testcase.TestCalcAdd import TestCalcAdd

suite = unittest.TestSuite()
loader = unittest.defaultTestLoader
cases = loader.discover(os.getcwd(),pattern="Test*.py")
suite.addTest(cases)
f = open("../calc/计算机测试报告.html","w+",encoding="utf-8")
runner = HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title="计算机的测试报告",
    description="这是一个计算机的测试",
    verbosity=1,
)
runner.run(suite)