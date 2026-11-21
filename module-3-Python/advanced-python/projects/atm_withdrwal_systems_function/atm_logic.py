balance=10000
def balanceAmount():
    global balance
    print("Your bank balance is :",balance)
def withdrawalAmount():
    global balance
    amount=int(input("Enter withdrwal amount :"))
    if amount<=0:
        print("invalid withdrawal amount")
    elif amount>balance:
        print("insufficient balance try again")
    else:
        balance-=amount 
        # balance=balance-amount
        print("after withdrwal reminaing amount is :",balance)
def depositAmount():
    global balance
    amount=int(input("Enter deposit amount :"))
    if amount<=0:
        print("invalid deposit amount")
    elif amount>50000:
        print("you can daily limit of deposit only 50k")
    else:
        balance+=amount 
        # balance=balance+amount
        print("after deposit your balance is  :",balance)