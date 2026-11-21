# banks ATM with drwal systems
balance=10000
pin=1234
entered_pin=int(input("Enter your pin : "))
if entered_pin==pin:
    while True:
        print("==============================")
        print("              ATM withdrwal App")
        print("==============================")
        
        print("select : 1 for balance")
        print("select : 2 for withdrwal")
        print("select : 3 for deposit")
        print("select : 4 for exit")
        
        # select choice 
        choice=int(input("Enter your choice :"))
        if choice==1:
            print("Your bank balance is :",balance)
        elif choice==2:
            amount=int(input("Enter withdrwal amount :"))
            if amount<=0:
                print("invalid withdrawal amount")
            elif amount>balance:
                print("insufficient balance try again")
            else:
                balance-=amount 
                # balance=balance-amount
                print("after withdrwal areminaing amount is :",balance)
                 
        
        elif choice==3:
                amount=int(input("Enter deposit amount :"))
                if amount<=0:
                    print("invalid deposit amount")
                elif amount>50000:
                    print("you can daily limit of deposit only 50k")
                else:
                    balance+=amount 
                    # balance=balance+amount
                    print("after deposit your balance is  :",balance)
        elif choice==4:
            print("thanks for using our ATM ::))")
            break
                        
    