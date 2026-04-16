# Reverse File Content (Line-wise)

# Algorithm:
# Open the file in read mode.
# Read all lines into a list.
# Reverse the list of lines.
# Open a new file in write mode.
# Write the reversed lines into the file.
# Close files.

with open("input.txt") as f:
    lines = f.readlines()

with open("reverse.txt", "w") as f:
    for line in reversed(lines):
        f.write(line)

print("File reversed")