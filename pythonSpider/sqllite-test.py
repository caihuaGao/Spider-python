# -*- coding = utf-8 -*-
# @Time: 2020/12/22 18:20
# @Author: 高才华
# @File: sqllite-test.py
# @Software: PyCharm

import sqlite3

# conn = sqlite3.connect("test.db") # 打开或创建数据库文件
# print("成功打开了数据库")
#
# c = conn.cursor() #获取游标
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''
# c.execute(sql) # 执行sql语句
# conn.commit()
# conn.close()


conn = sqlite3.connect("test.db") # 打开或创建数据库文件
print("成功打开了数据库")

c = conn.cursor() #获取游标
sql = '''
    insert into company (id,name,age,address,salary)
    values (1,"张三",32,"shanghai",16000)
'''
sql1 = '''
    insert into company (id,name,age,address,salary)
    values (2,"李四",32,"北京",18000)
'''
sql2 = '''
    delete from company where id == 1
'''
sql3 = '''
    update company
    set name = "闵杰"
    where id == 2
'''

sql4 = '''
    select * from company
    where id == 2
'''

# c.execute(sql) # 执行sql语句
# c.execute(sql1)
# c.execute(sql2)
# c.execute(sql3)
result = c.execute(sql4)
print(result)
for row in result:
    print("id=",row[0])
    print("name=", row[1])
    print("age=", row[2])
    print("address=", row[3])
    print("salary=", row[4])


conn.commit()
conn.close()