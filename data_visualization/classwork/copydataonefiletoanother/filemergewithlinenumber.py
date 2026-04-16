#file merege with file 
# Algorithm:
# Open both files in read mode.
# Read all lines from both files.
# Combine the lines into one list.
# Open a new file in write mode.
# Write each line with a line number prefix.
# Close all files.

with open("file1.txt") as f1, open("file2.txt") as f2:
    lines = f1.readlines() + f2.readlines()

with open("merged.txt", "w") as out:
    for i, line in enumerate(lines, start=1):
        out.write(f"{i}: {line}")

print("Files merged")