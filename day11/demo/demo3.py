class Dog:
    __color = None
    __speed = None
    __belong = None

    #构造方法
    def __init__(self,c,s,b):
        self.__color = c
        self.__speed = s
        self.__belong = b

    def setColor(self,c):
        self.__color = c
    def getColor(self):
        return self.__color

    def setSpeed(self,s):
        self.__speed = s
    def getSpeed(self):
        return self.__speed

    def setBelong(self,b):
        self.__belong = b
    def getBelong(self):
        return self.__belong

d = Dog("红色","犬科","50km/h")
print(d.getColor(),"颜色",d.getSpeed(),"科目",d.getBelong())