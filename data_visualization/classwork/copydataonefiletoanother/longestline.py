# Find Longest Line
# Algorithm:
# Open the file in read mode.
# Initialize a variable to store the longest line.
# Read each line from the file.
# Compare length of current line with stored line.
# If current line is longer, update the variable.
# After reading all lines, display the longest line and its length.
# Close the file.

# Q9: Find Longest Line

max_line = ""

with open("data.txt") as f:
    for line in f:
        if len(line) > len(max_line):
            max_line = line

print("Longest line:", max_line)
print("Length:", len(max_line))