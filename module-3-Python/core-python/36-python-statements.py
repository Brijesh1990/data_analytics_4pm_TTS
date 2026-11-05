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
a=10
b=5
if a>b:
    if a!=0 and b!=0:
        print("a is greater than b and both are positive")
        
else:
    print("a is less than b")