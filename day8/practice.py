#请编程写出一个登陆程序，从文件中校验用户名是否存在，
#若不存在则报错：不存在该用户，否则登陆成功!若密码输入错误，打印密码输入错误！
'''b = {}
f= open("b.txt","r+",encoding="utf-8")
data = f.readlines()
for i in data:
    line = i.split(",")
    b[line[0]] = line[1]
f.close()
name = input("请输入您的用户名:")
password = input("请输入您的密码：")
if name in b:
    if password == b[name]:
        print("登陆成功！")
    else:
        print("密码输入错误！")
else:
    print("该用户不存在！")
'''

#现在有这样一个叫scores.txt的文件，
#里面有赫敏、哈利、罗恩、马尔福四个人的几次魔法作业的成绩。
#但是呢，因为有些魔法作业有一定难度，教授不强制同学们必须上交，
#所以大家上交作业的次数并不一致。
#希望你来统计这四个学生的魔法作业的总得分，然后再写入一个txt文件。
'''f = open("scores.txt","r+",encoding="utf-8")
n = open("scores1.txt","w+",encoding="utf-8")
dic = {} #姓名：总分
lines = f.readlines() #["罗恩 23 35 44","哈利 60 77 68 88 89"...]
for line in lines:
    li = line.replace("\n","").split(" ") #["罗恩","23","35","44"]
    name = li[0]#"罗恩"
    scores = li[1:] #["23","35","44"]
    dic[name] = sum([int(i) for i in scores]) #[23 35 44] lambda 拉不大表达式：效率更高
print(dic)
for key in dic:
    n.write("{name}:{scores}\n".format(name=key,scores=dic[key]))
n.close()
f.close()
'''

#求baidu_x_system.log文件中IP出现的次数
f = open("baidu_x_system.log","r+",encoding="utf-8")
dic = {}#ip:次数
lines = f.readlines()
for line in lines:
    ip = line.split(" ")[0]
    if ip in dic:
        dic[ip] += 1
    else:
        dic[ip] = 1
print(dic)