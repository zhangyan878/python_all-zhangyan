import unittest
from day16practice.entity.bank import bank_addUser
from day16practice.uitls.DataRead import DataRead
from ddt import ddt
from ddt import data
from ddt import unpack

data1 = DataRead("database",database="bank",tablename="adduser",user="root",password="").list
@ddt
class TestBankAddUser(unittest.TestCase):
    @data(*data1)
    @unpack
    def testAddUser(self,username,password,country,province,street,door,money,p): # p 预期结果
        result = bank_addUser(username=username,password=password,country=country,province=province,street=street,door=door,money=money)  # result 实际结果
        self.assertEqual(result,p)


data2 = DataRead("database",database="bank",tablename="adduser1",user="root",password="").list
@ddt
class TestBankAddUser1(unittest.TestCase):
    @data(*data2)
    @unpack
    def testAddUser1(self,username,password,country,province,street,door,money,p):
        # 实际结果
        bank_addUser(username,password,country,province,street,door,money)
        # 实际测试
        result = bank_addUser(username=username,password=password,country=country,province=province,street=street,door=door,money=money)
        self.assertEqual(result,p)


data3 = DataRead("database",database="bank",tablename="adduser2",user="root",password="").list
@ddt
class TestBankAddUser2(unittest.TestCase):
    @data(*data3)
    @unpack
    def testBankUser2(self,username,password,country,province,street,door,money,p):
        for i in range(100):
            username = "张雪" + str(i)
            bank_addUser(username,password,country,province,street,door,money)
        result = bank_addUser(username=username,password=password,country=country,province=province,street=street,door=door,money=money)
        self.assertEqual(result,p)