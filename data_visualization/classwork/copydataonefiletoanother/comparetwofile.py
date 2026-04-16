# 10. Compare Two Files
# Algorithm:
# Open both files in read mode.
# Read all lines from both files.
# Store lines of second file in a set.
# Compare each line of first file with the set.
# If a line is not present in the second file, display it.
# Close files.

# Q10: Compare Two Files

with open("file1.txt") as f1:
    lines1 = f1.readlines()

with open("file2.txt") as f2:
    lines2 = set(f2.readlines())

for line in lines1:
    if line not in lines2:
        print(line.strip())