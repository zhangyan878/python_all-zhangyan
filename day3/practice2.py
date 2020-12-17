#九九乘法表正叙打印
'''
i = 1
while i <= 9:
    print("第",i,"层",end="")
    j = 1
    while j <= i:
        print(j,"x",i,"=",(j*i),"\t",end="")#\t表示四个空格
        j = j + 1
    print()
    i= i + 1

#九九乘法表倒叙打印
i = 9
while i <= 9 and i >=1:
   print("第",i,"层",end="")
    j = 1
    while j <= i:
        print(j,"x",i,"=",(j*i),"\t",end="")
        j = j + 1
    print()
    i = i - 1

#n*n乘法表
num =int(input("请输入您要的层数："))
i = 1
while i <= num:
    print("第",i,"层",end="")
    j = 1
    while j <= i:
        print(j,"x",i,"=",(j*i),"\t",end="")
        j = j + 1
    print()
    i = i + 1
'''


#一只青蛙掉在井里了，井高20米，青蛙白天往上爬3米，晚上下滑2米，
# 问第几天能出来？请编程求出。
high = 20
bai = 3
wan = 2
day = 0
h = 0
while True:
    h = h + bai
    day = day + 1
    if h >= high:
        break
    h = h - wan
print("第",day,"天能爬出来！")