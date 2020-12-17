import unittest
import os
from HTMLTestRunner import HTMLTestRunner
from day14.testcase.TestBankAddUser import TestBankAddUser
from day14.testcase.TestBankSaveMoney import TestBankSaveMoney

# 1.创建测试集
suite = unittest.TestSuite()
# 2.用测试集加载测试用例
#suite.addTest(TestBankAddUser("testAddUser"))
#suite.addTest(TestBankAddUser("testAddUser1"))
#suite.addTest(TestBankSaveMoney("testSaveMoney"))
# 2.1 借助测试加载器

# 2.2 获取加载器
loader = unittest.defaultTestLoader
# 2.3 寻找匹配的用例
cases = loader.discover(os.getcwd(), pattern="Test*.py")
# 2.4 添加到测试集里
suite.addTest(cases)
# 3.创建HTML运行器
f = open("../yinhang/银行报告.html","w+",encoding="utf-8")
htmlrunner = HTMLTestRunner.HTMLTestRunner(
    stream=f,
    title="银行的测试报告",
    description="这是一个银行的测试",
    verbosity=1,
)
# 4.用运行器运行测试集
htmlrunner.run(suite)