def multiplication_table():
    num = int(input("Enter a number: "))
    
    if num < 0:
        print("Negative numbers not allowed")
        return
    
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)

multiplication_table()