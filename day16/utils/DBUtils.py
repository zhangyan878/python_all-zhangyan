import pymysql
class MysqlUtils:
    con = None # 全局链接
    cursor = None # 全局游标

    @classmethod # 类方法
    def read(cls,host="localhost",database="calc",user="root",password="",tablename="addtable"):
        # 获取链接
        cls.con = pymysql.connect(host=host,user=user,password=password,database=database,charset="utf8")
        # 获取游标
        cls.cursor = cls.con.cursor()
        # 返回参数化数据
        sql = '''
            select * from {tablename}
        '''
        cls.cursor.execute(sql.format(tablename=tablename))
        return cls.cursor.fetchall()
#测试
#s = MysqlUtils.read()
#print(s)