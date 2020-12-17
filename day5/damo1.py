'''
    python：
        56,23,25:整型（int）
        56.31:浮点数据(float,double)
        "hello world" "刘嘉伟"：字符串（str）
        True,False:布尔（boolean）
        元组：(1,4,5,6,6,8,2,10)  不可能在改变
        列表：[1,2,3,4,5,6,65,5,47] 数据可以随时改变
        字典：{
                "010":"南京"，
                "020":"上海"，

             }（键值对应关系。特点：不能存储重复数据。）
        集合：（1,5,7,8,9,9）：不能存储重复的数据
'''

#打印类型
'''a = 56
b = "张岩"
c = True
d = 7.89
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#打印列表的长度
a = [9,1,2,3,5,7,6]
print(a[2])
print(a[3])
print("列表的长度为：",len(a))
'''

#求所有数的总和
#第一种方法：
'''a = [9,1,2,3,5,7,6]
sum = 0
for i in range(0,len(a)):
    sum = sum + a[i]
print(sum)

#第二种方法：
a = [3,4,5,2,9,1,7]
sum = 0
for i in a:
    sum = sum + i
print(sum)
'''

#求所有数中的最大值和对应的角标
'''a = [3,5,6,8,9,1,2]
max = a[0]
index = -1
for i in range(0,len(a)):
    if a[i] >= max:
        max = a[i]
        index = i
print("a中最大值为：",max,"所对应角标为：",index)
'''

a = [3,2,1,4,-1,-2,-3]
max = a[0]
index = -1
for i in range(0,len(a)):
    if a[i] >= max:
        max = a[i]
        index = i
print("a中最大值为：",max,"所对应角标为：",index)