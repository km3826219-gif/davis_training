def classify_number(num):
    if num > 0:
        print(num, "is Positive")
    elif num < 0:
        print(num, "is Negative")
    else:
        print(num, "is Zero")
    
    # Nested if for even/odd
    if num != 0:
        if num % 2 == 0:
            print(num, "is Even")
        else:
            print(num, "is Odd")
    print()

# List of numbers
numbers = [10, -5, 0, 7, -2]

for n in numbers:
    classify_number(n)