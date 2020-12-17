from userexception.UException import UserException
class User:
    __age = None
    __username = None

    def setAge(self,age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setUsername(self,username):
        self.__username = username

    def getUsername(self):
        return self.__username

    # 比较方法：
    def compare(self,p):
        if self.__username == p.getUsername() and self.__age == p.getAge():
            print('是同一个人！')
        else:
            raise  UserException("用户信息不匹配！")