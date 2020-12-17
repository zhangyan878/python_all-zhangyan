class Kongtiao:
    __brand = None
    __price = None

    def __init__(self,brand,price):
        self.__brand = brand
        self.__price = price

    def setBrand(self,brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand

    def setPrice(self,price):
        self.__price = price
    def getPrice(self):
        return self.__price

    def open(self):
        print("空调开机了...")
    def setClose(self,time):
        self.__close = time

k = Kongtiao("美菱","500")
k.open()
k.setClose = int(input("请设定自动关闭时间："))
if k.setClose <= 0 :
    print("设定失败！")
else:
    print("空调将在",k.setClose,"分钟后自动关闭...")

print("品牌：",k.getBrand(),"，价格：",k.getPrice())