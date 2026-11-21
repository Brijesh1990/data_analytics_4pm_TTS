# banks ATM withdrwal systems app using function
import atm_logic
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
            atm_logic.balanceAmount()
        elif choice==2:
            atm_logic.withdrawalAmount()
        elif choice==3:
                atm_logic.depositAmount()
        elif choice==4:
            print("thanks for using our ATM ::))")
            break
                        
    
        
