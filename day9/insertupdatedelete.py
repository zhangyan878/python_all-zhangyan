import pymysql
'''
   1.获取数据库连接（host地址，user用户，password密码，database数据库，charset编码集）
   2.获取游标（所有sql语句等数据库的操作必须经过游标）
   3.书写sql语句
   4.使用游标执行sql语句
        4.1 若做的是增删改，没有返回结果
        4.2 若做的是查询操作，有返回结果
   5.处理执行后的结果
   6.关闭游标
   7.关闭连接
'''
#1.获取数据库连接
con = pymysql.connect(host="localhost",user="root",password="",database="销售数据库",charset="utf8")

#2.通过连接来获取游标
cursor = con.cursor()

#3.书写sql
#增加
#sql = "insert into article value('S005','电视',2000,1)"

#4.通过游标执行sql语句
#s = cursor.execute(sql)
#print(s)

#删除
sql = "delete from article where 商品号='S005'"
s = cursor.execute(sql)
print(s)

#修改
'''sql = "update article set 库存量=20 where 商品号='S005'"
s = cursor.execute(sql)
print(s)
'''
#4.1提交刚才执行操作，提交给数据
con.commit()

#5.关闭资源
cursor.close()
con.close()