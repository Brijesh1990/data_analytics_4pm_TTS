# there are two way to call function 
# call by value 
# call by reference value


# call by value :
# if A function call by its values i.e called function by value
# def display(fnm):
#     firstName="my firstname is :"+fnm + "\n"
#     res=firstName.upper()
#     print(res)
# display("brijesh")


# def display(fnm):
#     fnm=input("Enter your Name :")
#     res=fnm.upper()
#     print("my name is :",res)
# display("fnm")


# function call by reference
def display(fnm,lnm):
    firstName="my first name is :"+fnm+"\n"
    lastName="my last name is :"+lnm+"\n"
    print(firstName, lastName)
display("brijesh","pandey")