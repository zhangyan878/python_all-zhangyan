#有下列列表，请编程实现列表的数据翻转
list =[1,2,3,4,5,6]
print(list[::-1])

#请编程统计列表中的每个数字出现的次数List = [1,4,7,5,82,1,3,4,5,9,7,6,1,10]
'''list = [1,4,7,5,82,1,3,4,5,9,7,6,1,10]
for i in range(0,len(list)):
    count = 0
    flag = True
    for k in range(0,i):
        if list[k] == list[i]:
            flag = False
            break
    if flag == False:
        continue
    for j in range(len(list)):
        if list[i] == list[j]:
            count += 1
    print(list[i],"出现了",count,"次！")
'''

#求出现次数的第三种方法：使用字典的方式来存   key:value   数字：次数
'''list = [1,4,7,5,82,1,3,4,5,9,7,6,1,10]
d = {}
for i in list:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)

#按要求实现
#姓名  年龄  性别  编号   任职公司   薪资   部门编号
names = [
    ["何登勇","56","男","106","IBM",500,"50"],
    ["曹东雪","19","女","230","微软",501,"60"],
    ["刘营营","19","女","210","Oracle",600,"60"],
    ["李汉聪","45","男","230","Tencent",700,"10"]
]
names.append(["张佳伟","45","男","220","alibaba","500","30"])
print(names)
'''