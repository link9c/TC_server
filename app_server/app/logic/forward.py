import pymssql
import sys

pymssql.__version__
import decimal

sys.setrecursionlimit(99999)
file = open('foward.txt', 'r+')
no = file.readline().strip()
file.close()
print(no)
# connect = pymssql.connect('10.7.1.30', 'bis', 'MP38954600#', 'axdb_dev_sync')
# cursor = connect.cursor()
# print(result)

hconnect = pymssql.connect('10.9.1.234', 'sa', 'MP-it226', 'mes_test')
hcursor = hconnect.cursor()

i = 0

fp = open('foward_output.csv', 'w+')
fp.write(
    "level1,weight1,level2,weight2,level3,weight3,level4,weight4,level5,weight5,level6,weight6,level7,weight7,level8,weight8,level9,weight9,level10,level11,weight11,level12,weight12,level13,weight13,level14,weight14,level15,weight15,level16,weight16,level17,weight17,level18,weight18,level19,weight19,level20\n")


def godeep(route_list, data=[]):  # ['2016070821', '1', '10140118', '1', 'D.0C.29E-A_0012']
    global i
    no = route_list[-1].split('_')
    print(no)
    mo_part_no = no[0]
    mo_lot_no = no[1]
    sql = "select part_no,mtr_lot_no,mtr_qty from av_mes_mtr_use_h_n where mo_part_no = '%s' AND mo_lot_no = '%s'" % (
        mo_part_no, mo_lot_no)
    hcursor.execute(sql)
    result = hcursor.fetchall()
    flag = True
    for each in result:
        flag = False
        data.append([str(int(each[2])), each[0] + '_' + each[1]])

        route_list = [each[0] + '_' + each[1]]
        godeep(route_list, data)
    else:
        if data != []:
            if flag:
                fp.write(str(data).replace('[[', '').replace(']]', '').replace(']', '').replace('[', '').replace("'",
                                                                                                                 "") + '\n')
                i += 1
                print(i, data)
            data.pop(-1)


if __name__ == '__main__':

    if no[0].isnumeric():
        sql = "select disinfect_rcv_lot_no,mo_no,part_id,mo_lot_no from av_mes_disinfect_rcv_b where disinfect_rcv_lot_no = '%s' and part_id LIKE 'D%%'" % no
        hcursor.execute(sql)
        result = hcursor.fetchall()
        for each in result:
            data = []
            # print(type(data))
            data.append(each[0])
            data.append(str(1))
            data.append(each[1])
            data.append(str(1))
            data.append(each[2] + '_' + each[3])
            print(data)
            godeep(route_list=data, data=[data])

    elif no[0].isalpha():
        data = [no]
        godeep(route_list=data, data=[data])

    else:
        print("格式不正确")