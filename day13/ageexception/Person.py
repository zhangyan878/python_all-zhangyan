from ageexception.AgeException import AgeException
class Person:
    __age = None

    def setAge(self,age):
        self.__age = age

    def getAge(self):
        return self.__age

    def number(self):
        if self.__age > 0:
            print(self.__age)
        else:
            raise AgeException("输入数据非法！")