import unittest #单元测试
from day14.yinhang.bank import bank_addUser
'''
   1.搞清楚哪些是要测的业务逻辑部分
   2.写核心代码
   3.业务：
       用户满了：3
       已经存在：2
       开户成功：1
'''

class TestBankAddUser(unittest.TestCase):
    def testAddUser(self):
        username = "张佳伟"
        password = 12345
        country = "中国"
        province = "江苏"
        street = "古城街"
        door = 23
        money = 1800

        status = 1 # 期望结果
        # 实际结果
        s = bank_addUser(username,password,country,province,street,door,money)
        # 断言
        self.assertEqual(status,s)

    def testAddUser1(self):
        status = 3 # 期望结果
        password = 12222
        country = "中国"
        province = "内蒙古"
        street = "同心路"
        door = 33
        money = 1000
        # 先添加100用户
        for i in range(100):
            username = "张三" + str(i)
            # 实际结果
            bank_addUser(username,password,country,province,street,door,money)
        # 实际测试
        s = bank_addUser("李四",password,country,province,street,door,money)
        # 断言
        self.assertEqual(status,s)

    def testAddUser2(self):
        username = "李伟"
        password = 999
        country = "中国"
        province = "天津"
        street = "和平道"
        door = 101
        money = 1000

        status = 2
        bank_addUser(username,password,country,province,street,door,money)
        s = bank_addUser("李伟",password,country,province,street,door,money)
        self.assertEqual(status,s)