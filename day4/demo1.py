#for循环：九九乘法表正叙打印
'''
for i in range(1,10):
    for j in range(1,i+1):
        print(j,"x",i,"=",(j*i),"\t",end="")
    print()
'''

#for循环：九九乘法表倒叙打印
'''
for i in range(9,0,-1):
    for j in range(1,i+1):
        print(j,"x",i,"=",(j*i),"\t",end="")
    print()
'''

#打印1-10之间的跳数
'''
for i in range(1,11,2):
    print(i)
'''

#for循环求1-10的和
'''
sum = 0  #全局变量
for i in range(1,11):
      sum = sum + i
print(sum)
'''