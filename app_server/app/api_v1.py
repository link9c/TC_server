from flask import Blueprint
# 委托总和数量 -- 委托下单为计算起点
# 每天，每周，每月，季度数量
# 不同实验室，公司，部门
api_v1_blue = Blueprint('api_v1',__name__)
@api_v1_blue.route("/")
def p():
    return "qqq"