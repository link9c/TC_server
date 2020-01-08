import pymssql
import sys

pymssql.__version__

sys.setrecursionlimit(99999)
file = open('back.txt', 'r+')
content = file.readline()
print(content)
file.close()

connect = pymssql.connect('10.7.1.30', 'bis', 'MP38954600#', 'axdb_dev_sync')
cursor = connect.cursor()

hconnect = pymssql.connect('10.9.1.234', 'sa', 'MP-it226', 'mes_test')
hcursor = hconnect.cursor()
i = 0

fp=open('back_output.csv', 'w+')
fp.write("level1,weight1,level2,weight2,level3,weight3,level4,weight4,level5,weight5,level6,weight6,level7,weight7,level8,weight8,level9,weight9,level10,level11,weight11,level12,weight12,level13,weight13,level14,weight14,level15,weight15,level16,weight16,level17,weight17,level18,weight18,level19,weight19,level20\n")

def last(data,source):
    global i
    no = data[-1].split('_')
    mtr_part_no = no[0]
    mtr_lot_no = no[1]
    sql = "select disinfect_rcv_lot_no,mo_no from av_mes_disinfect_rcv_b where part_id = '%s' and mo_lot_no = '%s'" % (mtr_part_no,mtr_lot_no)
    hcursor.execute(sql)
    result = hcursor.fetchall()
    for each in result:
        eachdata=source.copy()
        eachdata.append("1")
        eachdata.append(each[1])
        eachdata.append("1")
        eachdata.append(each[0])
        fp.write(str(eachdata).replace('[[', '').replace(']]', '').replace(']', '').replace('[', '') + '\n')
        i += 1
        print(i, eachdata)

def godeep(route_list, data=[]):
    no = route_list[-1].split('_')
    mtr_part_no = no[0]
    mtr_lot_no = no[1]
    sql = "select mo_part_no,mo_lot_no,mtr_qty from av_mes_mtr_use_h_n where part_no = '%s' AND mtr_lot_no = '%s'" % (mtr_part_no, mtr_lot_no)
    hcursor.execute(sql)
    result = hcursor.fetchall()
    flag = True
    for each in result:
        flag = False
        data.append([str(int(each[2])), each[0]+'_'+each[1]])

        route_list = [each[0]+'_'+each[1]]
        godeep(route_list, data)
    else:
        if data != []:
            if flag:
                print("=====",data)
                # last(data[-1],data)
            data.pop(-1)


# if conetent

godeep([content],data=[content])
