# w.a.p to create a calculator app take input from users choice based 
print("-------press 1 for Additions--------")
print("-------press 2 for Substractions--------")
print("-------press 3 for Divisions--------")
print("-------press 4 for Multiplication--------")
print("-------press 0 for exit from programmes--------")

while True:
    choice=int(input('Enter your choice :'))
    if choice==1:
        a=int(input('Enter a values :'))
        b=int(input('Enter b values :'))
        c=a+b
        print("Additions of numbers is :",c)
    elif choice==2:
            a=int(input('Enter a values :'))
            b=int(input('Enter b values :'))
            c=a-b
            print("Substractions of numbers is :",c)
    elif choice==3:
                a=int(input('Enter a values :'))
                b=int(input('Enter b values :'))
                if a!=0 and b==0:
                    print("not divisible by zero")
                else:
                    c=a/b
                    print("Divisions of numbers is :",c)
    elif choice==4:
                a=int(input('Enter a values :'))
                b=int(input('Enter b values :'))
                c=a*b
                print("Multiplications of numbers is :",c)
    elif choice==0:
                print("Thanks for using our calculator App ::)")
                break
    
        