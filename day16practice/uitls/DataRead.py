from day16practice.uitls.DBUtils import MysqlUtils
import os
class DataRead:
    list = None
    def __init__(self,mode,host="localhost",user="",database="",password="",tablename=""):
        if mode == "database":
            DataRead.list = MysqlUtils.read(host=host,user=user,password=password,database=database,tablename=tablename)
        else:
            raise Exception("对不起，您的操作模式无法识别！")
#d = DataRead("database",database="bank",tablename="adduser",user="root",password="")
#print(d.list)