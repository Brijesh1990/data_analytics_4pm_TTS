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
                    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                )
                
                """) 
        #create table state
        cur.execute("""
                    create table if not exists tbl_state(
                        
                        sid int primary key auto_increment,
                        sname varchar(255),
                        cid int,
                        foreign key(cid) references tbl_country(cid),
                        created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                    )
                    
                    """)
    
        #create table city
        cur.execute("""
                    create table if not exists tbl_city(
                        
                        ctid int primary key auto_increment,
                        ctname varchar(255),
                        sid int,
                        foreign key(sid) references tbl_state(sid),
                        created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
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
                    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
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
                        created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
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
        
        # while True:
        #     choice=int(input("Enter your choice :"))
        #     if choice==1:
        #         cname=input("Enter country Name :")
        #         data=(cname)
        #         cur.execute("""
        #                insert into or ignore tbl_country(cname) values(%s)
        #                     """,data)
        #         conn.commit()
        #         print('country added successfully')
        #     elif choice == 7:
        #         print("Exiting program...")
        #         break
            
        #     conn.close()
                
except Error as e: 
    print("something went wrong database not connected")