def atm():
    balance = 10000
    
    while True:
        amount = float(input("Enter withdrawal amount (0 to exit): "))
        
        if amount == 0:
            print("Thank you!")
            break
        elif amount < 0:
            print("Invalid amount")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            print("Withdrawal successful")
            print("Remaining balance:", balance)

atm()