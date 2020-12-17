from  userexception.User import User
from userexception.UException import UserException
'''
   比较两个用户：
        若用户的年龄和姓名一样，则判断是同一个人
        否则，则抛出用户异常
'''
u = User()
u.setAge(56)
u.setUsername("旺财")

u1 = User()
u1.setAge(56)
u1.setUsername("大局")

try:
    u.compare(u1)
except UserException as e:
    print(e)