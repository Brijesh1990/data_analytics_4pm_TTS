import matplotlib.pyplot as plt
import openpyxl
import pandas as pd
import sqlite3
# create a database 
conn=sqlite3.connect("sms-db-app")
# print("database connected successfully")
# create a table in database management systems
cur=conn.cursor()
# create a table structured
cur.execute("""
            create table if not exists country(
                cid integer primary key autoincrement,
                cname text,
                created_date text
            )
            
            """) 

cur.execute("""
            create table if not exists state(
                sid integer primary key autoincrement,
                sname text,
                created_date text
            )
            
            """) 
cur.execute("""
            create table if not exists city(
                ctid integer primary key autoincrement,
                ctname text,
                created_date text
            )
            
            """) 

cur.execute("""
            create table if not exists college(
                collegeid integer primary key autoincrement,
                collegename text,
                created_date text
            )
            
            """) 

cur.execute("""
            create table if not exists department(
                depid integer primary key autoincrement,
                depname text,
                created_date text
            )
            
            """) 

cur.execute("""
            create table if not exists faculty(
                facultyid integer primary key autoincrement,
                fname text,
                fage integer,
                faddress text,
                salary text,
                created_date text
            )
            
            """) 

cur.execute("""
            create table if not exists students(
                studentid integer primary key autoincrement,
                studentname text,
                studentage integer,
                studentaddress text,
                attendance integer,
                created_date text,
                cid integer,
                sid integer,
                ctid integer,
                collegeid integer,
                depid integer,
                facultyid integer,
                
                foreign key(cid) references country(cid),
                foreign key(sid) references state(sid),
                foreign key(ctid) references city(ctid),
                foreign key(collegeid) references college(collegeid),
                foreign key(depid) references department(depid),
                foreign key(facultyid) references faculty(facultyid)
              
            )
            
            """) 
# print("table created successfully")

# how to add or insert data in tables 
insertCountry=[
    (1,'india','27/10/2026'),
    (2,'usa','27/10/2026'),
    (3,'china','27/10/2026'),
]
cur.executemany("""
                
                insert or replace into country values(?,?,?)
            
                """,insertCountry)
# add state
insertState=[
    (1,'gujrat','27/10/2026'),
    (2,'california','27/10/2026'),
    (3,'sanghai','27/10/2026'),
]
cur.executemany("""
                
                insert or replace into state values(?,?,?)
            
                """,insertState)

# add city
insertCity=[
    (1,'rajkot','27/10/2026'),
    (2,'navada','27/10/2026'),
    (3,'puri','27/10/2026'),
]
cur.executemany("""
                
                insert or replace into city values(?,?,?)
            
                """,insertCity)

# add department
insertDep=[
    (1,'CSE','27/10/2026'),
    (2,'IT','27/10/2026'),
    (3,'Data science','27/10/2026'),
    (4,'Data analytics','27/10/2026'),
]
cur.executemany("""
                
                insert or replace into department values(?,?,?)
            
                """,insertDep)

# add department
insertColl=[
    (1,'Marwadi unvercity','27/10/2026'),
    (2,'Atmiya univercity','27/10/2026')
]
cur.executemany("""
                
                insert or replace into college values(?,?,?)
            
                """,insertColl)

# add faculty
insertFac=[
    (1,'brijesh',36,'50 feet ring road rjt',861500,'27/10/2026'),
    (2,'mitesh',30,'50 feet ring road ahemdabad',452500,'27/10/2026'),
    (3,'sanket',34,'50 feet ring road badodara',451500,'27/10/2026'),
    (4,'nilesh',32,'50 feet ring road surat',189500,'27/10/2026'),
]
cur.executemany("""
                
                insert or replace into faculty values(?,?,?,?,?,?)
            
                """,insertFac)
# add faculty
insertStudents=[
    (1,'dhruv',24,'50 feet ring road rjt',1,'27/10/2026',1,1,1,1,1,1),
    (2,'kalpt',23,'50 feet ring road ahemdabad',0,'27/10/2026',1,1,1,1,1,1),
    (3,'bhavika',24,'50 feet ring road badodara',1,'27/10/2026',1,1,1,1,1,1)
    
]
cur.executemany("""
                
                insert or replace into students values(?,?,?,?,?,?,?,?,?,?,?,?)
            
                """,insertStudents)


print('data successfully added')
# display all data or fetch all data 
# select="select * from students"
# df=pd.read_sql_query(select,conn)
# print(df.to_string(index=False))
# fetch data via join 
select="select studentid,studentname,studentage,attendance,cname,sname,ctname,collegename,depname,fname  from students join country on students.cid=country.cid join state on students.sid=state.sid join city on students.ctid=city.ctid join college on students.collegeid=college.collegeid join department on students.depid=department.depid join faculty on students.facultyid=faculty.facultyid"

df=pd.read_sql_query(select,conn)
print(df.to_string(index=False))

# find absent and present 
present=(df["attendance"]==1).sum()
absent=(df["attendance"]==0).sum()

colors=["green","red"]
values=[present,absent]
labels=["Present","Absent"]

# data visualised using matlotlib in chart
plt.title("maximum absent students data visulaized")
plt.pie(
    values,
    labels=labels,
    colors=["green","red"],
    autopct="%1f%%"
    
)

# generate data in excel 
excel_students_data=df.to_excel("students_data.xlsx", engine="openpyxl", index="False")
print("data generated in excel successfully",excel_students_data)

plt.show()


# save query 
conn.commit()
# closed connection 
conn.close()

