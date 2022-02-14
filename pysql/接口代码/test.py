import pymysql
from common.operate_excel import OperationExcel
from common.pymysql_isuzu import Database




# sheet1 = oper.get_data_by_name("Sheet1")
# print(sheet1)
# id =1
# for i in sheet1:
#     code = i['姓名']
#     name1 =code.split(',')
#     age = i['年龄']
#     sex =i['性别']
#     date = i['日期']
#     for j in name1:
#         print(j)

# cnn = pymysql.connect(user='root', password='1234qwer!', database='support_domain', host='192.168.201.52', port=3306,
#                                  charset='utf8')
# cursor = cnn.cursor(cursor=pymysql.cursors.SSDictCursor)

db =Database()
codes = ['C8974351270','C8980058750']
oper = OperationExcel("C:\\Users\\windows-pc\\Desktop\\test.xls")
for code in codes:
    args = (code)
    sql = 'select id,code from tm_common_accessories where code=%s'
    data = db.read_all(sql,args)
    print(data)
    result = []
    for i in data:
        result.append(i['id'])
        result.append(i['code'])
        print(result)

    oper.write_data(result)



        # sql = 'insert into lin values(%s,%s,%s,%s,%s)'
    # try:
    # # 准备一条sql
    #     sql = 'insert into lin values(%s,%s,%s,%s,%s)'
    #     args = (id,name,age,sex,date)
    #
    #     num = cursor.execute(sql,args)
    #     print(num)
    #     if num > 0:
    #         # 提交事务,修改成功
    #         cnn.commit()
    #     else:
    #         # 失败回滚
    #         cnn.rollback()
    #     id +=1
    # except Exception as e:
    #     cnn.rollback()
    #     print('做错了:',e)
    #
    #
    # cursor.close()
    # cnn.close()

