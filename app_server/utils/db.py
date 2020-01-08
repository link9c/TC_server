import pymssql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app_server.config import DATABASE
# from server.app.models import *


class DatabaseManagement(object):
    def __init__(self, user, pwd, host, db):
        self.engine = create_engine('mssql+pymssql://{}:{}@{}/{}'.format(user, pwd, host, db), echo=True)  # 初始化数据库连接
        DBsession = sessionmaker(bind=self.engine)  # 创建DBsession类
        self.session = DBsession()  # 创建对象

    def close(self):  # 关闭session
        self.session.close()

    def execute_sql(self, sql_str):  # 执行sql语句
        return self.session.execute(sql_str)


def sql_server_init(ip, user, pw, db=None):
    connect = pymssql.connect(ip, user, pw, db)
    return connect
