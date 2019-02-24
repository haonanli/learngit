import utils_python as up
import csv
import pandas as pd
import numpy as np
import pymysql
# connect,cursor=up.get_sql_cursor()
# item="create table result(id int auto_increment primary key,score int,text varchar(500))"
# cursor.execute(item)
# connect.close()
connect = pymysql.Connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        db="test",
        charset="utf8"
    )
cursor = connect.cursor()
# try:
#     expression = "insert into information(name,website) values(%s,%s)"
#     cursor.execute(expression, (str("abc"), str("sunny day")))
# except Exception as e:
#     print(e)

path=r"G:\codefile\pythonfile\xpath_spider\b.csv"
with open(path,"rt",encoding="utf-8",errors="ignore") as f:
    data=csv.reader(f,delimiter=",")
    data_frame=pd.DataFrame([x for x in list(f) if x!=[]])
    print(data_frame)
    leng=len(data_frame)
    id=np.arange(leng)
    score=data_frame.ix[:,0].as_matrix()
    print(score)
    text=data_frame.ix[:,1].as_matrix()
    print(score)
    # text=data_frame.ix[:,2].as_matrix()

    for i in range(leng):
        try:
            item="insert into result(score,text) values(%s,%s)"
            cursor.execute(item,(score[i],text[i]))
        except Exception as e:
            print(e)


'''使用pd.read_csv()进行数据的读取'''
# data_frame=pd.read_csv(path,encoding="utf_8",error_bad_lines=False)
# print(data_frame)
# leng=len(data_frame)
# id=np.arange(leng)
# score=data_frame.ix[:,0].as_matrix()
# # score=int(score)
# print(score)
# text=data_frame.ix[:,1].as_matrix()
# print(text)
# print("the length of data_frame is :%s" %len(data_frame))
# print("the length of score is :%a" %len(score))
# print("the length of text is :%s" %len(text))
# print("the type of score is:%s" %type(score[1]))
# print("the type of id is:%s" %type(id[1]))

'''用python执行对数据库的插入操作'''
# for i in range(leng):
#     try:
#         item="insert into result(score,text) values(%s,%s)"
#         cursor.execute(item,(int(score[i]),str(text[i])))
#     except Exception as e:
#         print(e)
#           connect.rollback()


'''用python执行对数据库的查询操作'''
# expression="select * from result where score=%s"
# try:
#     cursor.execute(expression,int(3))
#     return_result =cursor.fetchall()
# except Exception as e:
#     print(e)
# for item in return_result:
#     print(item)

'''用python执行对删除数据表的操作'''
# expression="drop table wang"
# cursor.execute(expression)

'''用python执行对数据库记录的删除'''
# expression="delete from result where id=%s"
# try:
#     cursor.execute(expression,(int(3206)))
# except Exception as e:
#     print(e)

'''用python执行对数据库的更新操作'''
# expression="update result set score=score+1 where id=%s"
# try:
#     cursor.execute(expression,(int(3207)))
# except Exception as e:
#     print(e)

cursor.close()
connect.commit()#这句话一定不能少，在执行插入、更新、删除操作的时候一定要加上这句话，表示将当前的事务提交给MySQL数据库
connect.close()
