import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import seaborn as snb
import openpyxl
import mysql.connector 
from mysql.connector import Error
# create a database connection
try: 
    conn=mysql.connector.connect(
        host="127.0.0.1",
        port=3306, 
        user="root",
        password="admin",
        database="task_db_management_app"
    )
    
    if conn.is_connected():
        print("database successfully connected")
        #create a tables schema inside of database
        cur=conn.cursor()
        # create table country
        cur.execute("""
                create table if not exists tbl_country(
                    cid int primary key auto_increment,
                    cname varchar(255),
                    added_date varchar(200)
                )
                
                """) 
        #create table state
        cur.execute("""
                    create table if not exists tbl_state(
                        
                        sid int primary key auto_increment,
                        sname varchar(255),
                        cid int,
                        foreign key(cid) references tbl_country(cid),
                         added_date varchar(200)
                    )
                    
                    """)
    
        #create table city
        cur.execute("""
                    create table if not exists tbl_city(
                        
                        ctid int primary key auto_increment,
                        ctname varchar(255),
                        sid int,
                        foreign key(sid) references tbl_state(sid),
                         added_date varchar(200)
                    )
                    
                    """)    
        #employee tables 
        cur.execute("""
                create table if not exists tbl_employee(
                    
                    empid int primary key auto_increment,
                    empname varchar(255),
                    age int, 
                    mobile bigint,
                    cid int,
                    sid int,
                    ctid int,
                    foreign key(cid) references tbl_country(cid),
                    foreign key(sid) references tbl_state(sid),
                    foreign key(ctid) references tbl_city(ctid),
                     added_date varchar(200)
                )
                
                """)
    
        #task tables 
        cur.execute("""
                    create table if not exists tbl_tasks(
                        taskid int primary key auto_increment,
                        title varchar(255),
                        empid int,
                        foreign key(empid) references tbl_employee(empid),
                        status varchar(255),
                        tasktype varchar(255),
                         added_date varchar(200)
                    )
                    
                    """)    
        conn.commit()
        print("tables sucessfully created")
        # add data in tables 
        
        print("=====Select choice 1 for add country :=====")
        print("=====Select choice 2 for add state :=====")
        print("=====Select choice 3 for add city :=====")
        print("=====Select choice 4 for add employee :=====")
        print("=====Select choice 5 for add task :=====")
        print("=====Select choice 6 for display all task  :=====")
        print("=====Select choice 7 to exit from programmes :=====")
        
        while True:
            choice=int(input("Enter your choice :"))
            if choice==1:
                cname=input("Enter country Name :")
                added_date=input("Enter added_date :")
                cur=conn.cursor()
                data=(cname,added_date)
                cur.execute("""
                       insert  into  tbl_country(cname,added_date) values (%s,%s)
                            """,data)
                conn.commit()
                print('country added successfully')
            
            elif choice==2:
                sname=input("Enter state Name :")
                cid=int(input("Enter cid  :"))
                added_date=input("Enter added_date :")
                cur=conn.cursor()
                data=(sname,cid,added_date)
                cur.execute("""
                insert  into  tbl_state(sname,cid,added_date) values (%s,%s,%s)
                """,data)
                conn.commit()
                print('state added successfully')
            
            elif choice==3:
                ctname=input("Enter city Name :")
                sid=int(input("Enter sid  :"))
                added_date=input("Enter added_date :")
                cur=conn.cursor()
                data=(ctname,sid,added_date)
                cur.execute("""
                    insert  into  tbl_city(ctname,sid,added_date) values (%s,%s,%s)
                    """,data)
                conn.commit()
                print('city added successfully')
            
            elif choice==4:
                empname=input("Enter employee Name :")
                age=int(input("Enter employee Age :"))
                mobile=int(input("Enter mobile number  :"))
                cid=int(input("Enter country id   :"))
                sid=int(input("Enter state id  :"))
                ctid=int(input("Enter city id  :"))
                added_date=input("Enter added_date :")
                cur=conn.cursor()
                data=(empname,age,mobile,cid,sid,ctid,added_date)
                cur.execute("""
                                insert  into  tbl_employee(empname,age,mobile,cid,sid,ctid,added_date) values (%s,%s,%s,%s,%s,%s,%s)
                                """,data)
                conn.commit()
                print('employee added successfully')
                
            elif choice==5:
                title=input("Enter task title  :")
                empid=int(input("Enter employee Id :"))
                status=input("Enter task status  :")
                tasktype=input("Enter tasktype :")
                added_date=input("Enter added_date :")
                cur=conn.cursor()
                data=(title,empid,status,tasktype,added_date)
                cur.execute("""
                                insert  into  tbl_tasks(title,empid,status,tasktype,added_date) values (%s,%s,%s,%s,%s)
                                """,data)
                conn.commit()
                print('task added   successfully')
                
                
            elif choice==6:
                select="select * from tbl_tasks"
                df=pd.read_sql(select,conn)
                conn.commit()
                print(df)
                               
            elif choice == 7:
                print("Exiting program...")
                break
            
        conn.close()
                
except Error as e: 
    print("something went wrong database not connected",e)