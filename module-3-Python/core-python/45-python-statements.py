# python statements :
# check conditional and looping statements 
# check control flow statements 
# check true and false 
# check numbers of iteration repeat again and again applied there loop
# check conditional statements using if | if else | nested if | if elif

# types of python statements 
# conditional statements 
# looping statements 
# control flow statements 

# what is conditional statements ? 
# where we checked true and false conditional statements 
# types of conditional statements 
# 1. if 
# 2. if else 
# 3. if elif 
# 4. nested if 
# 5. switch (python not supported)

# examples of conditional statements 

# if : if is executed when condition is true 
# syntax 
# if condition:
#     statements

# a=10
# b=5
# if a>b:
#     print("a is greater than b")


# if else :if is executed when condition is true if is false else ids executed 

# syntax 

# if condition:
#     statements
# else:
#     statements

    
# a=10
# b=20
# if a>b:
#     print("a is greater than b")
# else:
#     print("a is less than b")
        
# nested if : we used if within another if  there used nested if 

# syntax 
# if condition:
#     if condition:
#         statements 
# else:
#     statements 
# a=10
# b=5
# if a>b:
#     if a!=0 and b!=0:
#         print("a is greater than b and both are positive")
        
# else:
#     print("a is less than b")



# if elif :if is executed when condition is true elif executed to check multiple true condition elif is false else is executed

# syntax :
    
# if condition:
#     statements
# elif condition:
#     statements 
# elif condition:
#     statements
# else:
#     statements

# a=10
# b=10
# if a>b:
#     print("a is greater than b")
# elif b>a:
#     print("b is greater than a")
# else:
#     print("a and b both are equal")


# w.a.p to check odd even number take input from users
# number=int(input("Enter a Numbers :"))
# if number%2==0:
#     print("even number")
# else:
#     print("odd number")


# w.a.p to check a year is leap year or not take input from users

# year=int(input("Enter a year :"))
# if year%4==0:
#     print("year is leap year")
# else:
#     print("Not a leap year")


# w.a.p to login app take input from users 
# email=input("Enter a email :")
# password=input("Enter a password :")

# if email=='admin@gmail.com' and password=='admin123':
#     print("you are logged in as admin successfully")
# else:
#     print('your credentials is wrong')

# w.a.p to make choice based login take input from users 

# print("===================================================")
# print("===========multiple choice based login app==========")
# print("===================================================")
# print("1. login as admin")
# print("2. login as developer")
# print("3. login as manager")
# print("4. login as faculty")
# print("5. exit")

# while True:
#     choice=int(input("Enter your choice :"))
#     if choice==1:
#         email=input("Enter a email :")
#         password=input("Enter a password :")

#         if email=='admin@gmail.com' and password=='admin123':
#             print("you are logged in as admin successfully")
#         else:
#             print('your credentials is wrong')
#     elif choice==2:
#             email=input("Enter a email :")
#             password=input("Enter a password :")
    
#             if email=='developer@gmail.com' and password=='developer23':
#                 print("you are logged in as developer successfully")
#             else:
#                 print('your credentials is wrong')
#     elif choice==3:
#                 email=input("Enter a email :")
#                 password=input("Enter a password :")
        
#                 if email=='manager@gmail.com' and password=='manager23':
#                     print("you are logged in as manager successfully")
#                 else:
#                     print('your credentials is wrong')
#     elif choice==4:
#                 email=input("Enter a email :")
#                 password=input("Enter a password :")
            
#                 if email=='faculty@gmail.com' and password=='faculty23':
#                     print("you are logged in as faculty successfully")
#                 else:
#                     print('your credentials is wrong')
#     elif choice==5:
#                 print('select wrong choice')
#                 break
    
    
# looping statements :

# loop is check a numbers of iteration repeat again and again there we used loop
# loop is repeated a numbers of iteration again and again 

# types of loop in python 

# for loop
# while loop
# do while : note python does not support do while

# loop control flow 
# continue
# break