#计算机
'''class Calculator:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self): # 两数相加
        return self.a + self.b

    def sub(self): # 两数相减
        return self.a - self.b

    def mul(self): # 两数相乘
        return self.a * self.b

    def dev(self): # 两数相除
        return self.a / self.b

class Test(Calculator):
    pass

a = float(input("请输入一个数："))
x = input("请输入需要进行的运算符号（+，-，*，/）：")
b = float(input("请输入另一个数："))
if x == "+":
    result = Calculator(a,b).add()
    print(result)
if x == "-":
    result = Calculator(a,b).sub()
    print(result)
if x == "*":
    result = Calculator(a,b).mul()
    print(result)
if x == "/":
    try:
        result = Calculator(a,b).dev()
    except ZeroDivisionError:
        print("输入错误，除数不能为0！")
    else:
        print(result)
'''

class OldPhone:
    __brand = None
    __phoneNumber = None

    def __init__(self,brand,phonenumber):
        self.__brand = brand
        self.__phoneNumber = phonenumber

    def setBrand(self,brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand

    def setPhoneNumber(self,phonenumber):
        self.__phoneNumber = phonenumber
    def getPhoneNumber(self):
        return self.__phoneNumber

    def call(self,number):
        print(self.__phoneNumber,"正在给",number,"打电话......")

class NewPhone(OldPhone):
    def call(self,number):
        super().call(number)
        print("语音拨号中......")

    def introduce(self):
        print("品牌为：",self.getBrand(),"的手机很好用...")

phone = NewPhone("华为")
phone.phonenumber = "16709823333"
phone.call("17860982222")
phone.introduce()