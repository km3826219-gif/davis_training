# Function for withdrawal
def withdraw():
    balance = 10000

    while True:
        amount = float(input("Enter withdrawal amount (0 to exit): "))

        if amount == 0:
            print("Exit")
            break

        elif amount < 0:
            print("Invalid Amount")

        elif amount > balance:
            print("Insufficient Balance")

        else:
            balance = balance - amount
            print("Withdrawal Successful")
            print("Remaining Balance =", balance)

# Call function
withdraw()