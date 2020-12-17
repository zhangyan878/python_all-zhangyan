import time

class Animal(object):
    __color = ""
    __weight = ""
    __age = None

    def __init__(self,color,weight,age):
        self.__color = color
        self.__weight = weight
        self.__age = age

    def setColor(self,color):
        self.__color = color
    def getColor(self):
        return self.__color

    def setWeight(self,weight):
        self.__weight = weight
    def getWeight(self):
        return self.__weight

    def setAge(self,age):
        self.__age = age
    def getAge(self):
        return self.__age

class Dog(Animal):
    __brand = ""

    def __init__(self,color,weight,age,brand):
        super().__init__(color,weight,age)
        self.__brand = brand

    def setBrand(self,brand):
        self.__brand = brand
    def getBrand(self):
        return self.__brand

    def show(self):
        for i in range(6):
            print("汪",end="")
            time.sleep(1)
        print("我是",self.getColor(),"颜色的狗，我的最高寿命",self.getAge()
              ,"年，我的最大体重：",self.getWeight(),"我是：",self.getBrand())

d = Dog("黄",10,5,"犬科")
d.show()