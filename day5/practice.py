#求其中是5的倍数的数的总和 a = [1,5,21,30,15,9,30,24]
# a = [1,5,21,30,15,9,30,24]
'''sum = 0
for i in range(0,len(a)):
    if a[i] % 5 == 0:
        sum += a[i]
print(sum)
'''
#笔试的高频题目
#给一个字符串:"hello world",求每个字符出现次数
#写一个冒泡排序，选择排序


#对上述列表进行排序：选择排序（笔试高频题）
'''
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j] > a[i]:
            a[i],a[j] = a[j],a[i]
print(a)
'''

#冒泡排序（笔试高频题）
'''
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
    print("第", (i + 1), "轮的数据是：", a)
'''

#求字符出现的次数
string = "this is a dog,that is a monkey!"
#第一种方法：
#将字符串转换成列表
'''li = list(string)
for i in range(0,len(li)):
    count = 0 # 计数器
    # 排重
    flag = True  # 开关置为开
    for k in range(0,i):
        if li[k] == li[i]:
            flag = False  # 一旦发现相同字符，开关置为关闭
            break
    if flag == False:  # 判断开关是否是关闭状态，便于判断是否发现是否统计过
        continue  # 终止循环，继续下一轮循环
    # 统计
    for j in range(0,len(li)):
        if li[i] == li[j]:
            count += 1
    print(li[i],"出现了",count,"次！")
'''
#第二种方法：

for index,ch in enumerate(string):#枚举每一个字符出现的角标 + 字符
    if ch in string[:index]: #通过切片来判断之前是否出现过
        continue
    print(ch,"出现了",string.count(ch),"次")#通过count()方法来统计全文出现次数


#判断是否在字符串里出现过
# string = "this is a dog,that is a monkey!"
#身份运算符 in       not in
# print("is" in string[:12])#判断is是否在前面12个字符串里出现过