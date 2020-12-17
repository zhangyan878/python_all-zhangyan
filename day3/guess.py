#导入模块
'''import random'''

#使用random模块:0 ~ 50    0 ~ 60 + 20 --> 20 ~ 80
#num1 = random.random()#0 ~ 1
#num2 = int(random.random() * 6 + 20)#20 ~80
#print(num1,num2)

#1.让系统产生一个随机数
import random
num = int(random.random() * 2000)
count = 0 #猜的数的计数器
while True:
    guess = int(input("请输入您要猜的数字："))
    count = count + 1
    if num > guess:
        print("小了")
    elif num < guess:
        print("大了")
    else:
        print("恭喜你，猜中了，您猜的数字为：",num,"您猜了",count,"次")
        break