# Algorithm:
# Ask the user to enter a keyword.
# Open the file in read mode.
# Read each line from the file.
# Convert both line and keyword to lowercase.
# Check if keyword exists in the line.
# If found, display the line.
# Close the file.

keyword = input("Enter keyword: ")

with open("data.txt") as f:
    for line in f:
        if keyword.lower() in line.lower():
            print(line.strip())