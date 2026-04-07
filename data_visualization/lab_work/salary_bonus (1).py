def calculate_bonus():
    n = int(input("Enter number of employees: "))
    
    for i in range(n):
        salary = float(input("Enter salary: "))
        years = int(input("Enter years of experience: "))
        
        if years >= 10:
            bonus = salary * 2
        elif years >= 5:
            bonus = salary * 1.5
        else:
            bonus = salary * 0.8
        
        print("Bonus:", bonus)
        print("Total Salary:", salary + bonus)
        print()
        
calculate_bonus()