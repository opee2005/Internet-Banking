import datetime
today = datetime.datetime.now()
date = "{today.month}/{today.day}/{today.year}".format(today=today)
print(date)
print("Welcome To Internet Banking")
Bank = input("customer's Bank: ")
Account_Name = input("Account Name: ")
Account_Number = int(input("Your Account Number: "))
initial_balance = float(input("How Much Do You Have In Your Account: "))
print("What Will You Like To Do?")
Options = input("Transfer?,Buy Airtime?, Pay Bill?: ")

if Options=="Buy Airtime".lower():
    Network = input("Network: ")
    Number = float(input("Phone Number: "))
    Amount = float(input("Amount: "))
    if Amount<initial_balance:
        Balance = initial_balance-Amount
        print("Your Recharge Of",Amount,"Sucessful")
        print("Thank You For Banking With Us. Your Balance: ",Balance)
    else:
        print("Insuficient Balance")
        
if Options=="Pay Bill".lower():
    print("Which Of These Bill Are You Paying For")
    Bill = input("PHCN?/GOTV?/DSTV?/STARTIME?: ")
    Account_Name = input("Account Name: ")
    Card_Number = float(input("Card's Serial Number: "))
    Amount = float(input("Amount: "))
    if Amount<initial_balance:
        Balance = initial_balance-Amount
        print("Your Recharge Of",Amount,"Sucessful")
        print("Thank You For Banking With Us. Your Balance: ",Balance)
    else:
        print("Insuficient Balance")

if Options=="Transfer".lower():
    Which_Bank = input("Recipent's Banks: ")

    def transfer(amount,initial_balance):
        return initial_balance-amount
    amount = int(input("amount to be transfer: "))
    balance = transfer(amount,initial_balance)
    if amount>initial_balance:
        print("Insuficient Balance")
    else: balance
    
    for Options in range(1):
        if Bank==Which_Bank and amount<initial_balance:
            transfer(amount,initial_balance)
            print("Operation Succesful")
            print("your Account Balance: ",balance)
            break
        
        if Bank!=Which_Bank:
            print("Note You Will Be Charge N50. Do You Wish To Continue?")
            Response = input("Y/N: ")
            if Response=="N".lower():
                print("Thank You For Banking With Us")
                break
    
            if Response=="Y".lower():
                transfer(amount,initial_balance)
                print("Operation Sucessful")
                print("Thank You For Banking With Us. Your Balance:",balance-50)
    

             
