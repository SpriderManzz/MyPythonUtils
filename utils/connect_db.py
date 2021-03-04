import pymysql
from data.config_data import host, db_port, user, passwd, db


class OperationMysql:
    def __init__(self):
        self.conn = pymysql.connect(
            host=host,
            port=db_port,
            user=user,
            passwd=passwd,
            db=db,
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor
        )
        # 创建游标对象
        self.cur = self.conn.cursor()

    # 定义查询方法
    def serach_one(self, sql):
        self.cur.execute(sql)
        res = self.cur.fetchone()
        return res  # 返回的是字典


if __name__ == '__main__':
    op = OperationMysql()
    res = op.serach_one("select * from user where userName= 'zhangsan' ")
    print(res)
    # # 关闭游标
    # self.cur.close()
    # # 关闭连接
    # conn.close()