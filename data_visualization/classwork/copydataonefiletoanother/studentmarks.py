# Program to extract students with marks > 75

# algo=======
# Open the file students.txt in read mode.
# Read each line from the file.
# Split each line into name, marks, and city.
# Convert marks into integer.
# Check if marks are greater than 75.
# If yes, write that record into a new file.
# Close both files.

with open("student.txt", "r") as source:
    with open("output.txt", "w") as destination:
        
        for line in source:
            data = line.split()   # split into name, marks, city
            
            name = data[0]
            marks = int(data[1])
            city = data[2]
            
            # Check condition
            if marks > 75:
                destination.write(line)

print("Data extracted successfully")