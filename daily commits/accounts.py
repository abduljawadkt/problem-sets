

def deposit():
    while True:
        amount = input("Enter the amount you are depositing : ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter amount above zero")
        
        else :
            print("invalid,please enter again")
            
    return amount    

deposit()