import calc_app
print("press 1 for additions")
print("press 2 for substractions")
print("press 3 for multiplications")
print("press 4 for divisions")
print("press 5 for modulas")
print("press 6 for simple interest")
print("press 0 for exit")

while True:
    choice=int(input("Enter your choices : "))
    if choice==1:
        print("Additions of numbers is :",calc_app.add("a","b"))
    elif choice==2:
        print("Substractions of numbers is :",calc_app.subs("a","b"))
    elif choice==3:
        print("Multiplications of numbers is :",calc_app.mult("a","b"))
    elif choice==4:
        print("Dvisions of numbers is :",calc_app.dv("a","b"))
    elif choice==5:
            print("Modulas of numbers is :",calc_app.mod("a","b"))
    elif choice==6:
            print("Simple interest paid by you :",calc_app.si("p","n","r"))
    else:
        print("Thanks for using our calculator app :))")
        break 
          
        