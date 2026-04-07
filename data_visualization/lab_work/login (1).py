def login():
    correct_username = "admin@567"
    correct_password = "passkey9999"
    
    attempts = 0
    
    while attempts < 3:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username == correct_username and password == correct_password:
            print("Login Successful")
            return
        else:
            print("Invalid credentials")
            attempts += 1
    
    print("Account Locked")

login()