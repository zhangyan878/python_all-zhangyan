#购物系统
shop = [
    ["iphone",6000],
    ["mac",12000],
    ["小米 watch",500],
    ["lenovo pc",4500],
    ["辣条",2.5],
    ["老干妈",10],
]
#二维列表，一维列表又套个一维列表
print("欢迎来到zhangyan购物广场".center(70,"-"))

# 1.先初始化自己的金钱
while True:
    salary = input("请输入您的初始金钱：")
    if salary.isdigit():#判断输入的字符串是否能看成数字
        salary = int(salary)
        print("恭喜您，您的初始金钱为:",salary,"，祝您本次购物愉快！")
        break
    else:
        print("请重新输入您的初始余额！")
'''
    1. 输入商品编号
        1.1 输入不存在，打回去重新输入
        1.2 您的余额是否充足。买东西，需要将当前商品添加我的购物车里，余额还要减去那么多钱。
        1.3 若您的余额不足，强行退出。
    2.输入Q,q。退出商城。
    买的东西打一下小票。
'''
#1.定义一个我的购物车
mycart = []

while True:
    #展示所有商品
    for index,value in enumerate(shop): # 枚举：列举出每一种可能出现的情况
        print(index," ",value)
    choice = input("请输入您要买的商品编号：")
    if choice.isdigit():
        choice = int(choice)
        if choice < len(shop):
            if salary >= shop[choice][1]:
                mycart.append(shop[choice])
                salary -= shop[choice][1]
                print("\033[32;20;1m恭喜你，添加成功！您的余额还剩：",salary,"\033[0m")
            else:
                print("\033[41;20;1m对不起，您的余额不足！请退出!\033[0m")
        else:
            print("\033[42;20;1m您输入的商品编号不存在！请重新输入\033[0m")
    elif choice == "q" or choice == "Q":
        print("欢迎下次光临！！")
        break
    else:
        print("\033[42;20;1m您输入的不合法，请重新输入！\033[0m")
print("----------------------Bye!-----------------")

#打印我的小票
for i in mycart:
    print(i)
print("您的余额为：",salary)