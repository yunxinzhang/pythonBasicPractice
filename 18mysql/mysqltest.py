
import pymysql.cursors
 
# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             port=3308,
                             user='root',
                             password='root',
                             db='test',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

'''
# 执行sql语句-
try:
    with connection.cursor() as cursor:
        # 执行sql语句，插入记录
        sql = 'INSERT INTO emp (name, age, sal) VALUES (%s, %s, %s)'
        cursor.execute(sql, ('杜甫', 44, 2222))
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()
finally:
    connection.close();
'''
'''
try:
    with connection.cursor() as cursor:
        # 执行sql语句，插入记录
        sql = 'update emp set name = %s where id = %s'
        cursor.execute(sql, ('白居易', 2))
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()
finally:
    connection.close();
'''

try:
    with connection.cursor() as cursor:
        sql = 'select * from emp where id > %s'
        cursor.execute(sql,1)
        rs = cursor.fetchall()
        for i in rs:
            print(i)
    connection.commit()
finally:
    connection.close()
