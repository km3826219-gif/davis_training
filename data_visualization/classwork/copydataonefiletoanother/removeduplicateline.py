#removeduplicate file

# Algorithm:
# Open the input file in read mode.
# Create an empty set to track seen lines.
# Create a list to store unique lines.
# Read each line from the file.
# If the line is not in the set, add it to the set and list.
# Open a new file in write mode.
# Write all unique lines into the new file.
# Close files.
# Q4: Remove Duplicate Lines

seen = set()
unique_lines = []

with open("input.txt", "r") as f:
    for line in f:
        if line not in seen:
            seen.add(line)
            unique_lines.append(line)

with open("output.txt", "w") as f:
    f.writelines(unique_lines)

print("Duplicates removed")