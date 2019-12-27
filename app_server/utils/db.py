from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from server.settings import DATABASE
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


if __name__ == '__main__':
    db = DatabaseManagement(**DATABASE)
    result = db.session.query(t_workflow_viewlog).all()
    print(result)
