from utils.DBUtils import MysqlUtils
from utils.ExcelUtils import ExcelUtils
import os
class DataRead:
    list = None # 全局列表 mode = excel,filename sheetname
    # database:database,user,password,tablename,host
    def __init__(self,mode,filename="",sheetname="0",host="localhost",database="",user="",password="",tablename=""):
        if mode == "excel":
            if filename == "":
                raise Exception("文件名不能为空！")
            elif not os.path.isfile(filename):
                raise Exception("文件不存在！")
            else:
                DataRead.list = ExcelUtils.read(filename,sheetname)
        elif mode == "database":
            DataRead.list = MysqlUtils.read(host=host,database=database,user=user,password=password,tablename=tablename)
        else:
            raise Exception("对不起，您的操作模式无法识别！")
#d = DataRead("database",database="calc",tablename="addtable",user="root",password="")
#d = DataRead("excel",filename="D:\\python\\day16\\testcase\\a.xlsx",sheetname="0")
#print(d.list)