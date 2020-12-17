name = input("请输入姓名：")
id = input("请输入身份证号：")
age = int(input("请输入年龄："))
sex = input("请输入性别：")
high = int(input("请输入身高："))
weight = int(input("请输入体重："))
info='''
--------[中国工商银行 | 个人信息系统]---------
name = {name}
id = {id}
age = {age}
sex = {sex}
high = {high}
weight = {weight}
-------------------------------------------
'''
print(info.format(name = name,id = id,age = age,sex = sex,high = high,weight = weight))