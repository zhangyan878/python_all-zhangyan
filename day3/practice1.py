#使用random模块，0 ~ 100 + 50 --> 50 ~150
'''
import random
num = int(random.random() * 100 + 50)#50 ~ 100
print(num)

#从键盘输入任意三边，判断能否形成三角形，若可以，则判断形成什么三角形
a = int(input("请输入第一边："))
b = int(input("请输入第二边："))
c = int(input("请输入第三边："))
if (a + b > c) and (b + c > a) and (a + c > b):
    if  a == b == c:
        print("构成等边三角形")
    elif a == b or a == c or b == c:
        print("构成等腰三角形")
    elif (a * a + b * b == c * c) or (a * a + c * c == b * b) or (b * b + c * c == a * a):
        print("直角三角形")
    else:
        print("构成普通三角形")
else:
        print("不能构成三角形")

#实现登录系统的三次密码输入错误锁定功能
#while/else 仅当while因条件为假而退出（即没有被break中断）时运行else块
i = 0
while i < 3:
    password = int(input("请输入登陆密码："))
    if password == 123456:
        print("登陆系统成功，进入系统首页面")
    else:
        print("密码输入错误")
    i = i + 1
else:
    print("输入三次密码错误，系统锁定")

name = "zhang"
password = "123456"
for i in range(3):
    n = input("请输入用户名：")
    p = input("请输入密码：")
    if n == name and p == password:
        print("恭喜，登录成功！")
        break
    else:
        print("输入密码错误！")
        if i == 2:
            print("三次密码输入错误，系统已锁定！")
            break
'''

#有以下两个数，使用+号实现两个数的调换。A=56,B=78,实现效果：A=78，B=56
'''
A = 56
B = 78
#1
A = A + B  #A=134
B = A - B  #B=56
A = A - B  #A=78
print(A,B)
#2引入第三个变量
C = A
A = B
B = C
print(A,B)
#3  ^ 异或
A = A ^ B
B = A ^ B
A = A ^ B
print(A,B)
'''

#编程实现下列图形的打印：等腰三角形
num = int(input("请输入三角形的层数："))
i = 1
while i <= num:
    j = 1
    while j <= (num - i):
        print(" ",end="")
        j = j + 1
    k = 1
    while k <= i:
        print("* ",end="")
        k = k + 1
    i = i + 1
    print()