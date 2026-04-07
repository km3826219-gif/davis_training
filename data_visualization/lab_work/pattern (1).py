rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    if i % 2 == 0:
        print("* " * i)
    else:
        print("# " * i)