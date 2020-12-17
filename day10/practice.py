#用python的面向对象分析人具有的属性和行为
'''class person:
    name = ""
    sex = ""
    age = 0
    high = 0
    weight = 0
    def study(self):
        print("学习使张佳伟快乐！")
p = person()
p.name = "张佳伟"
p.sex = "女"
p.age = 78
p.high = 120
p.weight = 180
p.study()
print("我叫",p.name,"，我是",p.sex,"生，我",p.age,"岁了,我身高",p.high,"，体重",p.weight)
'''

#将excel表格数据写入到DB数据库中
import pymysql
con = pymysql.connect(host="localhost",user="root",password="",database="course",charset="utf8")
cursor = con.cursor()

f = open("db.xlsx","w",encoding="utf-8")