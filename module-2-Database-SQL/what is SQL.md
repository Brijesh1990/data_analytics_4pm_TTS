# what is SQL  ?

1. SQL stands for structured query language 
2. SQL is a case insenstive language 
3. SQL is not conditional 
4. SQL create a structured of database and tables 
5. SQL is execute query or command 

# what is query or command in SQL ?

1. query is a single line 
2. query and command both are same 
3. via SQL query its create and database and tables structured 

# types of SQL query ?

- THere are 4 types of SQL query 

- **DDL** (data definition language)

- **DML** (data manipulation language)

- **DQL** (data query language)

- **TCL** (transactional control language)


- **DDL** (data definition language) : 

1. DDL create an structured 
2. DDL create an database and tables structured 
3. DDL used to change column name is table
4. DDL used to change table name is table
5. DDL used to drop database and table structured


**DDL query are ..**

1. create 
2. alter 
3. truncate 
4. drop 
5. rename 
6. change 


## how to create database ? 

**syntax**

``` 
create database databasename;
or 
create database data_analytics_4pm;

```

![alt text](image-5.png)

or 

![alt text](image-6.png)   

## how to create table in database  ? 

## chart of create table for its columnname or fieldname 

|   column name    |   data types     |    size           |
|------------------|------------------|-------------------|
|id                | int              | default size(11)  |
|name, email ,pass | char , varchar   | (0-255)           |
|mobile            | int, bigInt      | default size(20)  |
|decimal, salary   | decimal(10,2)    | (10,2)            |       
|address , message | text             | 65365 character   | 
|date , datetime   | date , datetime  |                   | 
|photo , image     | varchar , blob   |                   |
|salary            | float            |                   |
|multiple choice   | enum()           |                   |
|default timezone  | timestamp        |                   |
|true, false       | boolean          |                   |   


**syntax**

```
create table tablename
(
columnname datatype(size) primary key auto_increment,
.
.
.
.
.
column datatype(size)

)

or

create table customers(
id int AUTO_INCREMENT primary key,
name varchar(200),
password varchar(255),
firstname varchar(255),
lastname varchar(255),
gender varchar(255),
mobile bigint
)


or

create table tbl_feedback(
id int AUTO_INCREMENT primary key,
name varchar(100),
email varchar(255),
phone bigint,
rating enum('*','**','***','****','*****'),
comment text    
);

```

# alter ....

1. alter is used to add | update | modify new column in tables 
2. alter is also  used to add unique key of any column name 

**query or commands are**

```
alter table tbl_feedback add added_date_time datetime;
or
alter table customers add address text;
or
alter table customers add photo varchar(255) after name;
or
alter table tbl_feedback change added_date_time adddatetime datetime;

```

# add unique key via alter 

1. unique key is provides in table stored unique values 
2. unique is never stored dublicate values 


**add unique key via SQL**


```
alter table tbl_feedback add UNIQUE(`email`)

```

# change 

- change is used with alter 
- change is used to update any column name used with alter 

```
alter table tbl_feedback change adddatetime added_date datetime;
```


# rename :

- rename any table name 
- rename is use to update or rename to created tables 

```
rename table customers to tbl_customers;
```

# drop : 

**drop a database**

1. drop will used to delete database and its structured 
2. after drop we will never rollback any structured and data 

**syntax**

```
drop database databasename;
or
drop database data_analytics_4pm;

```

**drop a table**

1. drop will used to delete table and its data also 
2. after drop we will never rollback any structured or  data of tables

**syntax**

```
drop table tablename;
or
drop table tbl_customers;
or
drop table tbl_feedback;

```


# truncate : 

1. truncate is used to empty tables data 
2. truncate removed all data from tables 
3. truncate never rollback data 
4. truncate only delete data not delete structures 


**difference b/ primary key and unique key**

**primary key**
1. A pk is provides one times in table 
2. A pk key should always auto_increment
3. A pk never return a null values
4. A pk stored a unique values 

|   id(pk)     |  name     |  age  |   address |
|--------------|-------------------|-----------|
|   1          | brijesh   | 36    | rjt       |

**unique key**
1. A uk is provides more than one times in table 
3. A uk return one times a null values
4. A uk never return dublicate data 


|   id(pk)     |  name     |  age  |   address |  mobile   |    email   |
|--------------|-------------------|-----------|-----------|------------|
|   1          | brijesh   | 36    | rjt       |9121212    | a@gmail.com|


```
truncate table tablename
or
truncate table tbl_feedback 

``` 

# difference b/w truncate | drop | delete 

**truncate**

1. truncate is empty all data from tables 
2. after truncate we never rollback any data data from tables 
3. truncate deleted  only rows or data 


**drop**
1. drop is used to drop database or table with structured and data 
2. drop never rollback any data 

**drop database**

````
drop database data_analytics_430;
````

**drop  table**

````
drop table tbl_feedback;
````

**delete**

1. delete is used to delete all data from table
2. delete is used to delete particular data from tables 
3. delete is used to a range of data from tables 
4. delete is used to delete alternate   data from table

**delete data**

1. delete from tbl_country;
2. delete from tbl_country where cid=2;
3. delete from tbl_country where name='pakistan';
4. delete from tbl_country where cid between 6 and 50;
5. delete from tbl_country where cid in (2,5,7);

**note: after delete we rollback data using transanctional query**


# DML (data manipulation language)

1. DML is used to insert | delete | update data 

```
examples : insert | delete | update 

```

2. How to **insert data** ...

**syntax**

```
insert into tbl_customers(name,photo,password,firstname,lastname,gender,mobile,address) values('brijesh','brijesh.jpg','brij123','brij','pandey','male',912236151546,'rajkot')

or

insert into tbl_customers(name,photo,password,firstname,lastname,gender,mobile,address) values('dhruv','dhruv.jpg','d123','shruv','patel','male',912236151546,'rajkot'),('bhavika','bhavika.jpg','bh123','bhavika','sharma','female',9122361,'rajkot'),('kalpit','kalpit.jpg','kalpit','kalpit','patel','male',912236,'rajkot')

or

insert into tbl_customers values(null,'om','om.jpg','d123','shruv','patel','male',912236151546,'rajkot'),(null,'jainish','jainish.jpg','bh123','bhavika','sharma','female',9122361,'rajkot'),(null,'kumar','kumar.jpg','kalpit','kalpit','patel','male',912236,'rajkot')

```

3. How to **update data or rows**... 

**syntax**
```
update tablename set columnname='values' where id=1;
or 
update  tbl_customers set name='naimish',photo='naimish.png',password='naimish123',firstname='naimish',lastname='vaja',mobile=6356421656,address='150 feet ring road ahemdabad' where id=7; 
```


4. how to **delete data or **rows**..

- delete from tbl_country;
- delete from tbl_country where cid=2;
- delete from tbl_country where name='pakistan';
- delete from tbl_country where cid between 6 and 50;
- delete from tbl_country where cid in (2,5,7);

**note**
- after delete we can rollback data via rollback transactional query 


## DQL  : stands for data query language

**query in DQL**

```
select 

1. select all data from tables

select * from tbl_customers

2. select particular one data from tables 

select * from tbl_customers where id=3;

3. select particular one data from tables 

select * from tbl_customers where name='kalpit';


4. select particular columns of data

select name,photo,mobile,address from tbl_customers;


5. select and create alias(change nick name of column) of any column name

select cid,cname as countryname from tbl_country

6. select alternative of data from tables 

select * from tbl_customers where id in(4,6,7);

7. select range of data from tables 

select * from tbl_customers where id between 1 and 6;

8. select data using limit 

select * from tbl_customers where id limit 0,1;
or
select * from tbl_customers where id limit 3,2;
or
select * from tbl_customers where id limit 5,3;

9. select is used in searching data using like operator and its wildcard

a) select customers name who's name start with 'a' character

select * from tbl_customers where name like  'a%';
or
select * from tbl_customers where name like  'b%';



b) select customers name who's name end with 'h' character

select * from tbl_customers where name like  '%h';
or
select * from tbl_customers where name like  '%t';


c) select customers name who's name found a anywhere  'a' character

select * from tbl_customers where name like  '%a%';
or
select * from tbl_customers where name like  '%sh%';

```
# difference b/w order by and group by 

## order by : 

- order by is used to filter data from tables in ASC or DESC order 

``` 
select * from tbl_employee order by name asc;
or
select * from tbl_employee order by name DESC;
or
select * from tbl_employee order by name;

```

- w.a.q to filter from tables to find second highest salary

```
select * from tbl_employee order by salary desc limit 1,1;

```    
- w.a.q to filter from tables to find highest  salary

```

select * from tbl_employee order by salary desc limit 0,1;

```

# w.a.q to find second highest salary using subquery 

# what is subquery ? 

1. query within another query i.e called subquery 

```
select max(salary) as second_highest_salary from tbl_employee where salary < (select max(salary) from tbl_employee); 

```

# group by :

- group by filter data on group of columns in tables 

- w.a.q to sum of salary of departments

```
select sum(salary) as sumof_salary,department  from tbl_employee group by department;
```

# distinct :  

- distinct a keyword used in sql to find a different and unique values from tables there we used distinct 

```
select DISTINCT(salary) from tbl_employee 
``` 


# sql function ? 

- SQL provides some inbuilt function that can be used to completed any task  
- There are two types of sql inbuilt function 

1. aggrigate function

- sum()
- avg()
- count()
- max()
- min()

2. scalar function 

- first()
- last()
- ucase()
- lcase()
- now()
- timestamp()

**examples of all sql function**


1.  select sum(salary) as sumof_salary from tbl_employee
2.  select avg(salary) as averageof_salary from tbl_employee
3.  select COUNT(empid) as total_numbers_employee from tbl_employee
4.  select max(salary) as max_salary from tbl_employee
6.  select min(salary) as min_salary from tbl_employee
7.  select first(empid) from tbl_employee
8.  select last(empid) from tbl_employee
9.  select ucase(name) from tbl_employee
10. select lcase(name) from tbl_employee
11. select now(added_date_time) from tbl_employee
12. select timestamp(added_date_time) from tbl_employee


# TCL : transactional control language

   query : commit | rollback 


# TCL have some query 

  1. commit : commit is used to save data after delete 

     **query**

     ```
     START TRANSACTION;
     delete from tbl_employee where empid=4;
     commit; 

     ```


     2. rollback : rollback  is used to return data   after delete from tables  

     **query**

     ```
     START TRANSACTION;
     delete from tbl_employee where empid=8;
     select * from tbl_employee where empid=8;
     rollback;
     select * from tbl_employee where empid=8;
     
     ```


# SQL windows function ....

 1. SQL windows function is used to applied calculations and add unique rows to current rows in a table.

 2. SQL windows function are used to add or set a rows related to the current row without grouping the result into a single row.

# types of windows function 


1. ROW_NUmber()
2. Rank()
3. Dense_RANK()
4. NTILE()
5. LAG()
6. LEAD()
7. FIRST_VALUE()
8. LAST_VALUE()
9. SUM() OVER()
10. AVG() OVER()
11. MIN() OVER()
12. MAX() OVER()
13. COUNT() OVER()

**examples of windows function**

1. select name ,salary,ROW_NUMBER() over(order by salary desc) from tbl_employee;
2. select name ,salary,Rank() over(order by salary desc) from tbl_employee;
3. select name ,salary,Dense_Rank() over(order by salary desc) from tbl_employee;
4. select name ,salary,NTILE(3) over(order by salary desc) from tbl_employee;
5. select name ,salary,LAG(salary,1) over(order by salary desc) from tbl_employee;
6. select name ,salary,LEAD(salary,1) over(order by salary desc) from tbl_employee;
7. select name ,salary,first_value(salary) over(order by salary desc) from tbl_employee;
8. select name ,salary,sum(salary) over(order by salary desc) from tbl_employee;
9. select name ,salary,avg(salary) over(order by salary desc) from tbl_employee;
10. select name ,salary,max(salary) over(order by salary desc) from tbl_employee;
11. select name ,salary,min(salary) over(order by salary desc) from tbl_employee;
12. select name ,salary,count(salary) over(order by salary desc) from tbl_employee;
13. select name ,salary,Last_values(salary) over(order by salary desc) from tbl_employee;



# what is SQL index or indexer or SQL query optimizations ? 

1. SQL index or indexer create for optimized a speed of SQL tables 
2. SQL index used to optimized speed of tables 
3. index or indexer is fast lookup data from table
4. indexer is used to one column of table of multiples columns of tables 

   **two types of indexer**

   1. single indexer 

      ```
      create index indexname on tablename  (columnname);
      or 
      create index index_emplid on tbl_employee  (empid);  

      ```
   2. composite indexer 
  
     ```
     create index index_emplid on tbl_employee  (empid,name,salary);

     ``` 


# What is SQL view ? 

  1. SQL view is used to create an dublicate table of virtual tables of main table
  2. SQL view create a clone of main tables 
  3. SQL view create to clone of main tables to hide some data from some users there we create view 

# how to create view  ?
 
 **query**
 
  ```
  create view view_employee_data as select * from tbl_employee
  
  ```

# note : when we create any query inside of virtual tables or view its performed in our main tables 

  ```
  insert in view 
  delete in view 
  update in view 
  change in view   
  
  ```



