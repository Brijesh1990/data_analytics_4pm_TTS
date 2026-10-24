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
print("table created successfully")
# save query 
conn.commit()
# closed connection 
conn.close()

