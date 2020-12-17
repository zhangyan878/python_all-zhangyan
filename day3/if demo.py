'''age = 10
if age >= 18:
    print("可以去看电影了！")
else:
    print("还未成年")
'''

i = 0
while i < 3:
    score = int(input("请输入本次考试分数："))
    if score <= 100 and score >90:
        print("优秀")
    elif score <= 90 and score > 80:
        print("良好")
    elif score <= 80 and score >=60:
        print("及格")
    elif score < 60 and score >= 0:
        print("不及格")
    else:
        print("输入非法")
    i = i + 1