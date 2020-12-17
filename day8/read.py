'''
f = open("1.jpg","rb") #读取
w = open("表情包.jpg","wb") #写入

#读取一个图片
data = f.read()
#将读取数据写入到另一个文件中
w.write(data)
#关闭读取和写入资源
f.close()
w.close()
'''

#如何复制一首诗到另一个文件
f = open("2.txt","r+",encoding="utf-8")
w = open("古诗.txt","w+",encoding="utf-8")
data = f.read()
w.write(data)
f.close()
w.close()