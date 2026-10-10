# what is data types in python ?
# A data type meanse which type of values stored in variables 
# A data type is some types in python 

# types of data type ?

# int
# float 
# string
# complex
# array or list
# list
# dictionary 
# set
# tuple


# int
# accept number
# a=10
# b=1545454


# string
# string is a set of character
# string enclosed within '' or "" 
# a='10.2565'
# name='brijesh'
# name1="hey brijesh"
# print(a)
# print(name)
# print(name1)


# integer 
# stored numbers or integer values in variables 

# a=10
# b=165656565
# c=556565
# print(a)
# print(b)
# print(type(c))

# type casting is used to change the datatype string to number or integer 
#  string to float
# type casting 
# a=int("10")
# b=20
# c=a+b 
# print(c)


# a=int(input("Enter a values :"))
# b=int(input("Enter a values :"))
# c=a+b
# print("additions of numbers is :",c)

# convert into string to integer

# a=int(input("Enter a values :"))
# b=int(input("Enter a values :"))
# c=a+b
# print("additions of numbers is :",c)



# complex data types 
# a=2 + 3j
# print(type(a))

# boolean 
# a=True 
# b=False 
# print(type(a))

# float 
# a=10.656565
# print(type(a))

# convert string to float
# a=float(input("Enter a values :"))
# b=float(input("Enter a values :"))
# c=a+b
# print("additions of numbers is :",c)


# dictionary :
# stored data inside of {key:value}
# dictionary provides mutable data can be changed 
# employee={
#     id:1,
#     "name":"brijesh",
#     "age":35,
#     "department":"IT"
# }

# print(employee)
# print(type(employee))
# print(employee["age"])
# print(employee["name"])


# list :
# stored data inside of []
# list provides mutable data can be changed 

# employee=["brijesh","dhruv","rajesh"]
# print(employee)
# print(type(employee))
# print(employee[0])
# print(employee[1])
# print(employee[2])

# employee=["brijesh",99980038789,True,"rajesh"]
# print(employee)
# print(type(employee))
# print(employee[0])
# print(employee[1])
# print(employee[2])


# tuple : 
# tuple is a data types of python 
# tuple stored data inside of ()
# tuple provides immutable data can not be changed 

# employee=("brijesh","rajesh","kumar")
# print(employee)
# print(type(employee))
# print(employee[0])
# print(employee[2])

# set :
# set is also a datatype of python 
# set is also stored data inside of {"rajesh","kumar","bhim",9522121}
# set provides immutable data can not be changed 
# set don't have any index values 
# each times of set will be shuffled 

# employee={"rajesh","kumar","bhim",9522121, True}
# print(employee)
# print(type(employee))


# string :
# string is set of character 
# string is stored data inside of '' or "" quotation
# string is provides  mutable data can be changed 

# str1='106564'
# str2="106.56565"
# str3="brijesh kumar pandey"
# print(str1)
# print(str2)
# print(str3)  
# print(type(str2))

# string litrals

# str="""
# hi i am brijesh
# i am 35 years of old
# i have done m.tech(IT)
# """
# print(str)


# str="i am brijesh  \n i am 35 years of old "
# print(str)


# string formatter 
# string formatter is able to print any type of data in string
# string formatter is denoted by f"{}"

# age=20
# name="brijesh"
# dep="IT"
# salary=115000.85
# res=f"{age}{name}{dep}{salary}"
# print(res)


# w.a.p to check conditional expression in one line 

# age=13
# res="adult" if age>=18 else "child"
# print(res)


age=int(input("Enter your age :"))
res="adult" if age>=18 else "child"
print("i am now :",res)



