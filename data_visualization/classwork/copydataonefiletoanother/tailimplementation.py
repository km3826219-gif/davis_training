# 12. Tail Implementation (Last N lines)
# Algorithm:
# Ask the user to input the number of lines (N).
# Open the file in read mode.
# Read all lines into a list.
# Extract the last N lines from the list.
# Display those lines.
# Close the file


# Q12: Tail Implementation

n = int(input("Enter number of lines: "))

with open("data.txt") as f:
    lines = f.readlines()

for line in lines[-n:]:
    print(line.strip())