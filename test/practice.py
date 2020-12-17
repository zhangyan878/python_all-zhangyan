# 每隔60秒读取日志文件数据
'''
import time
while True:
    time.sleep(60)
    with open("a.txt","r+",encoding="utf-8") as f:
        data = f.read()
        with open("b.txt","a",encoding="utf-8")as t:
            t.write(data)


#0-100 查找并输出所有质数
num = []
i = 2
for i in range(2,100):
    j = 2
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        num.append(i)
print(num)
'''