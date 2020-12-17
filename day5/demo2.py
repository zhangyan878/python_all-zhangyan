'''
    列表[]
    常用的api:
        len() 求长度
        append() 可以向列表最后一位添加一条数据
        remove() 删除一个数
        pop
        切片：[start:end] , start ~ end - 1
        枚举：列举出每一种可能出现的情况。 enumerate()  index,value

'''
# pop()可以将列表指定位置的元素移除，同时可以将移除的元素赋值给某个变量，不填写位置参数则默认删除最后一位
'''
a = ["hello","world","dlrd"]
b = ["hello","world","dlrd"]
a.pop(1)
b1 = b.pop(0)
print(a)
print(b1)
'''

# pop()可以根据键将字典中指定的键值对删除，同时可以将删除的值赋值给变量
b = {
    "name":"zy",
    "age":22
}
b1 = b.pop("age")
print(b)
print(b1)

#随机点名
'''
import  random
names = ["张佳伟","刘日成","洪小雅","张岩"]
#打印第一个到第三个数据
print(names[0:3])
#打印跳数
print(names[0:3:2])
#添加一条数据
names.append("jason")
#删除一条数据
names.remove("张佳伟")
print(names)
#随机点名
num = int(random.random() * len(names))
name = names[num]
print("恭喜你，",name,"被点名！")
'''