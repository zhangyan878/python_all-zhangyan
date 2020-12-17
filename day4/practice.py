#请用程序实现：用户从键盘输入整型数值，若输入的是1，则继续让用户输入数值n并打印n*n的乘法表。
#若用户输入的是编号2，则继续让用户输入数值m并打印m层等腰三角形吗。
#若用户输入除了1,2,以外的数值请优化程序并提示输入有误和重新进行输入。
'''
while True:
    i = int(input("请输入编号："))
    if i == 1:
        n = int(input("请输入数值n:"))
        for a in range(1, n + 1):
            for j in range(1, a + 1):
                print(j, "x", a, "=", (j * a), "\t", end="")
            print()
        break
    elif i == 2:
        m = int(input("请输入数值m:"))
        b = 1
        while b <= m:
            c = 1
            while c <= (m - b):
                print(" ", end="")
                c = c + 1
            d = 1
            while d <= b:
                print("* ", end="")
                d = d + 1
            b = b + 1
            print()
        break
    else:
        print("编号输入有误！")


#用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
sum =  0
for i in range(1,21):
    sum1 = 1
    for i in range(1,i+1):
        sum1 = sum1 * i
    sum = sum1 + sum
print(sum)


#从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
max = 0
sum = 0
for i in range(10):
    num = int(input("请输入数据:"))
    if num > max:
        max = num
    sum = sum + num
print("最大的数为:",max,"十个数的和为:",sum,"平均数为：",(sum/10))
'''

#当输入是54321时，写出下列程序的执行结果
num = int(input("请输入一个数："))
while num != 0:
    print(num % 10)
    num = num // 10