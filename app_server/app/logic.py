import os
import sys
from utils.db import sql_server_init
from app_server.CONSTANT import TEST_ACCOUNT

from app_server.CONSTANT import CODE

sys.setrecursionlimit(99999)


class FORWARD(object):
    def __init__(self, code, path):
        connect = sql_server_init(**TEST_ACCOUNT)
        self.cursor = connect.cursor()
        self.code = code
        self.i = 0
        # self.fp = open('forward_output.csv', 'w')
        self.fp = open(path, 'w')
        self.fp.write(
            "level1,weight1,level2,weight2,level3,weight3,level4,weight4,level5,weight5,level6,weight6,level7,weight7,"
            "level8"",weight8,level9,weight9,level10,level11,weight11,level12,weight12,level13,weight13,level14,"
            "weight14,level15,weight15,level16,weight16,level17,weight17,level18,weight18,level19,weight19,level20\n")

    def is_exist(self, code):
        no = code.split('_')
        if len(no) < 2:
            return 0
        mtr_part_no = no[0]
        mtr_lot_no = no[1]
        sql = "select mo_part_no,mo_lot_no,mtr_qty from av_mes_mtr_use_h_n where part_no = '%s' AND mtr_lot_no = '%s'" % (
            mtr_part_no, mtr_lot_no)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def godeep(self, route_list, data=[]):  # ['2016070821', '1', '10140118', '1', 'D.0C.29E-A_0012']

        no = route_list[-1].split('_')
        # print(no)
        mo_part_no = no[0]
        mo_lot_no = no[1]
        sql = "select part_no,mtr_lot_no,mtr_qty from av_mes_mtr_use_h_n where mo_part_no = '%s' AND mo_lot_no = '%s'" % (
            mo_part_no, mo_lot_no)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        flag = True
        for each in result:
            flag = False
            data.append([str(int(each[2])), each[0] + '_' + each[1]])

            route_list = [each[0] + '_' + each[1]]
            self.godeep(route_list, data)
        else:
            if data != []:
                if flag:
                    self.fp.write(
                        str(data).replace('[[', '').replace(']]', '').replace(']', '').replace(
                            '[', '').replace("'", "") + '\n')
                    self.i += 1
                    print(self.i, data)
                data.pop(-1)

    def run(self):
        if self.code[0].isnumeric():
            sql = """select disinfect_rcv_lot_no,mo_no,part_id,mo_lot_no from av_mes_disinfect_rcv_b 
            where 
            disinfect_rcv_lot_no = '%s' and part_id LIKE 'D%%'""" % self.code
            self.cursor.execute(sql)
            result = self.cursor.fetchall()

            if not result:
                return CODE.NORESULT
            for each in result:
                data = []
                # print(type(data))
                data.append(each[0])
                data.append(str(1))
                data.append(each[1])
                data.append(str(1))
                data.append(each[2] + '_' + each[3])
                # print(data)
                self.godeep(route_list=data, data=[data])

            return CODE.SUCCESS

        elif self.code[0].isalpha():
            result = self.is_exist(self.code)
            if result:
                data = [self.code]
                self.godeep(route_list=data, data=[data])
                return CODE.SUCCESS
            return CODE.NORESULT
        else:
            print("格式不正确")
            return CODE.TYPEERR


class BACKWARD(object):
    def __init__(self, code, path):
        connect = sql_server_init(**TEST_ACCOUNT)
        self.cursor = connect.cursor()
        self.code = code
        self.i = 0
        # self.fp = open('backward_output.csv', 'w')
        self.fp = open(path, 'w')
        self.fp.write(
            "level1,weight1,level2,weight2,level3,weight3,level4,weight4,level5,weight5,level6,weight6,level7,weight7,"
            "level8,weight8,level9,weight9,level10,level11,weight11,level12,weight12,level13,weight13,level14,weight14,"
            "level15,weight15,level16,weight16,level17,weight17,level18,weight18,level19,weight19,level20\n")

    def is_exist(self, code):
        no = code.split('_')
        if len(no) < 2:
            return 0
        mtr_part_no = no[0]
        mtr_lot_no = no[1]
        sql = "select mo_part_no,mo_lot_no,mtr_qty from av_mes_mtr_use_h_n where part_no = '%s' AND mtr_lot_no = '%s'" % (
            mtr_part_no, mtr_lot_no)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result

    def last(self, data, source):
        no = data[-1].split('_')
        mtr_part_no = no[0]
        mtr_lot_no = no[1]
        sql = "select disinfect_rcv_lot_no,mo_no from av_mes_disinfect_rcv_b where part_id = '%s' and mo_lot_no = '%s'" % (
            mtr_part_no, mtr_lot_no)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for each in result:
            eachdata = source.copy()
            eachdata.append("1")
            eachdata.append(each[1])
            eachdata.append("1")
            eachdata.append(each[0])
            self.fp.write(
                str(eachdata).replace('[[', '').replace(']]', '').replace(']', '').replace('[', '').replace("'",
                                                                                                            '') + '\n')
            self.i += 1
            print(self.i, eachdata)

    def godeep(self, route_list, data=[]):
        no = route_list[-1].split('_')
        mtr_part_no = no[0]
        mtr_lot_no = no[1]
        sql = "select mo_part_no,mo_lot_no,mtr_qty from av_mes_mtr_use_h_n where part_no = '%s' AND mtr_lot_no = '%s'" % (
            mtr_part_no, mtr_lot_no)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        flag = True
        for each in result:
            flag = False
            data.append([str(int(each[2])), each[0] + '_' + each[1]])

            route_list = [each[0] + '_' + each[1]]
            self.godeep(route_list, data)
        else:
            if data != []:
                if flag:
                    if isinstance(data[-1], tuple):
                        # print("=====", data)
                        self.last(data[-1], data)
                data.pop(-1)

    def run(self):
        result = self.is_exist(self.code)
        if result:
            self.godeep([self.code], [self.code])
            self.fp.close()

            return CODE.SUCCESS

        return CODE.NORESULT


if __name__ == '__main__':
    # code = D.0C.33C-B_0020
    back = BACKWARD('E.2.0151_1907040027')
    back.run()
