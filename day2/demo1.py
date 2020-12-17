'''

    变量：变化的量
        可以变化存储数据的量：变量
    python中这些变量随意定义？
    python规则：(法律，一旦违反，直接报错)
        1. 可以使用a~z ,A~Z : 52
        2. 0~9 : 10个数字
        3. _
        总共：63
    python命名规范：（道德，虽然违反，但不犯法。）
        1.数字不能开头
        2.不能使用python中的关键字:help("keywords")35个关键字
        3.python 3虽然提供中文命名法，但是禁止使用。
'''
# help("keywords")  --> 查询又多少关键字

变量 = 6
print(变量)

T_T = 8
print(T_T)

#使用isdigit（）方法  # 检查字符串是否只由数字组成

str='10'
print(str.isdigit())
int(str)
print(str)

'''
    输入：input()
        自动扫描你在键盘上输入的数据，直到输入回车。
        15  -->     int("15")   --> 15

'''
'''
#实现输入10个数字，并打印10个数字的求和结果
a = int(input("请输入第1个数："))
b = int(input("请输入第2个数："))
c = int(input("请输入第3个数："))
d = int(input("请输入第4个数："))
e = int(input("请输入第5个数："))
f = int(input("请输入第6个数："))
g = int(input("请输入第7个数："))
h = int(input("请输入第8个数："))
i = int(input("请输入第9个数:"))
j = int(input("请输入第10个数："))
print("总数：",(a + b + c + d + e + f + g + h + i + j))'''