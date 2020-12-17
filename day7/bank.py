#bank
import random
#银行库
bank = {} #username : {password,moeny.....}
bank_name = "中国工商银行昌平支行"
bank_choice = {"1":"开户","2":"存钱","3":"取钱","4":"转账","5":"查询","6":"Bye"}#银行业务选项

#开户成功的信息模板
myinfo = '''
\033[0;32;40m
-----------账户信息---------
账号：{account}
姓名:{username}
密码:{password}
地址：
    国家:{country}
    省份:{province}
    街道:{street}
    门牌号:{door}
账户余额：{money}
注册银行名:{bank_name}
----------------------------
\033[0m
'''

#欢迎模板
welcome = '''
******************************
*    中国工商银行账户管理系统    *
******************************
*             选项            *
'''

welcome_item = '''*            {0}.{1}           *'''

def print_welcome():
    print(welcome,end="")
    keys = bank_choice.keys()
    for i in keys:
        print(welcome_item.format(i,bank_choice[i]))
    print("********************************")

#输入帮助方法：chose是打印选项
def inputHelp(chose,datatype = "str"):
    while True:
        print("请输入",chose,":")
        i = input(">>>:")
        if len(i) == 0:
            print("该项不能为空！请重新输入！")
            continue
        if datatype != "str":
            return int(i)
        else:
            return i

#判断是否存在该银行选项
def isExists(chose,data):
    if chose in data:
        return True
    return False

#获取随机码
def getRandom():
    li = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string = ""
    for i in range(8):
        string = string + li[int(random.random()* len(li))]
    return string

#银行的开户方法
def bank_addUser(username,password,country,province,street,door,money):
    #for i in range(100):
    #      bank["张三" + str(i)] = {}
    if len(bank) >= 100:
        return 3
    elif username in bank:
        return 2
    else:#正常开户：存储到银行
        bank[username] = {
            "account":getRandom(),
            "password":password,
            "country":country,
            "province":province,
            "street":street,
            "door":door,
            "money":money,
            "bank_name":bank_name
        }
        return 1
#开户方法
def addUser():
    username = inputHelp("用户名")
    password = inputHelp("密码")
    country = inputHelp("居住地址：1.国家")
    province = inputHelp("省份")
    street = inputHelp("街道")
    door = inputHelp("门牌号")
    money = inputHelp("银行卡余额","int")

    #调用隐含的开户方法完成开户操作  返回 1  2 3
    status = bank_addUser(username,password,country,province,street,door,money)
    #判断  1   2   3
    if status == 1:
        user = bank[username]
        print("恭喜您开户成功！以下是您的开户信息：")
        print(myinfo.format(account = user["account"],
                            username = username,
                            password = user["password"],
                            country = user["country"],
                            province = user["province"],
                            street = user["street"],
                            door = user["door"],
                            money = user["money"],
                            bank_name = user["bank_name"]
                            ))
    elif status == 2:
        print("该用户已存在！请携带证件到其他银行办理！谢谢！")
    elif status == 3:
        print("银行库已满！请携带证件到其他银行办理！谢谢！")

#银行的存钱方法
def bank_addMoney(username,account1,addmoney):
    if (username in bank) and (account1 in bank[username]["account"]):
        bank[username]['money'] += addmoney
        return True
    else:
        return False
#存钱方法
def addMoney():
    account1 = inputHelp("用户账号")
    addmoney = inputHelp("存入金额","int")
    username = inputHelp("用户名")
    status = bank_addMoney(username,account1,addmoney)
    #判断True False
    if status == True:
        print("恭喜您存钱成功！以下是您的账户信息：")
        print(myinfo.format(account = bank[username]["account"],
                            username = username,
                            password = bank[username]["password"],
                            country = bank[username]["country"],
                            province = bank[username]["province"],
                            street = bank[username]["street"],
                            door = bank[username]["door"],
                            money = bank[username]["money"],
                            bank_name = bank[username]["bank_name"]))
    elif status == False:
        print("该用户库里没有该用户！请重新输入！")

#银行的取钱方法
def bank_takeMoney(username,account,password,takemoney):
    if (username not in bank) or (account not in bank[username]["account"]):
        return 1
    elif password not in bank[username]["password"]:
        return 2
    elif takemoney > bank[username]["money"]:
        return 3
    else:
        bank[username]["money"] -= takemoney
        return 0
#取钱方法
def takeMoney():
    username = inputHelp("用户名")
    account = inputHelp("用户账号")
    password = inputHelp("密码")
    takmoney = inputHelp("取款金额","int")
    status = bank_takeMoney(username,account,password,takmoney)
    if status == 0:
        print("恭喜您取钱成功！以下是您的账户信息：")
        print(myinfo.format(account = bank[username]["account"],
                            username = username,
                            password = bank[username]["password"],
                            country = bank[username]["country"],
                            province = bank[username]["province"],
                            street = bank[username]["street"],
                            door = bank[username]["door"],
                            money = bank[username]["money"],
                            bank_name = bank[username]["bank_name"]))
    elif status == 1:
        print("该用户不存在！请重新输入！")
    elif status == 2:
        print("您输入的密码不正确！请重新输入！")
    elif status == 3:
        print("您的余额不足！请重新输入！")

#银行的转账方法
def bank_transferMoeny(username1,username2,account1,account2,password1,transfermoney):
    if (username1 not in bank) or (username2 not in bank) or (account1 not in bank[username1]["account"] or (account2 not in bank[username2]["account"])):
        return 1
    elif password1 not in bank[username1]["password"]:
        return 2
    elif transfermoney > bank[username1]["money"]:
        return 3
    else:
        bank[username1]["money"] -= transfermoney
        bank[username2]["money"] += transfermoney
        return 0
#转账方法
def transferMoney():
    username1 = inputHelp("转出账户用户名")
    username2 = inputHelp("转入账户用户名")
    account1 = inputHelp("转出账户账号")
    account2 = inputHelp("转入账户账号")
    password1 = inputHelp("转出账户密码")
    transfermoney = inputHelp("转出金额","int")
    status = bank_transferMoeny(username1,username2,account1,account2,password1,transfermoney)
    if status == 0:
        print("恭喜您转账成功！以下是您的账户信息：")
        print(myinfo.format(account = bank[username1]["account"],
                            username = username1,
                            password = bank[username1]["password"],
                            country = bank[username1]["country"],
                            province = bank[username1]["province"],
                            street = bank[username1]["street"],
                            door = bank[username1]["door"],
                            money = bank[username1]["money"],
                            bank_name = bank[username1]["bank_name"]))
    elif status == 1:
        print("该用户不存在！请重新输入！")
    elif status == 2:
        print("您输入的密码不正确！请重新输入！")
    elif status == 3:
        print("您的账户余额不足，转账失败！请重新输入！")

#银行的查询方法
def search():
    username = inputHelp("用户名")
    account = inputHelp("账号")
    password = inputHelp("密码")
    if username not in bank or account not in bank[username]["account"]:
        print("该用户不存在！请重新输入！")
    elif password not in bank[username]["password"]:
        print("密码输入错误！请重新输入！")
    else:
        print("恭喜您查询成功！以下是您的账户信息：")
        print(myinfo.format(account = bank[username]["account"],
                            username=username,
                            password=bank[username]["password"],
                            country=bank[username]["country"],
                            province=bank[username]["province"],
                            street=bank[username]["street"],
                            door=bank[username]["door"],
                            money=bank[username]["money"],
                            bank_name=bank[username]["bank_name"]
                            ))

#核心程序
while True:
    print_welcome()
    chose = inputHelp("选项")
    if isExists(chose,bank_choice):
        if chose == "1":
            addUser()
        elif chose == "2":
            addMoney()
        elif chose == "3":
            takeMoney()
        elif chose == "4":
            transferMoney()
        elif chose == "5":
            search()
        elif chose == "6":
            print("Bye,Bye!")
            break
    else:
        print("不存在改选项！")