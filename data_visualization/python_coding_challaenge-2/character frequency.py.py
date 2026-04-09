text = input("Enter string: ")
ch = input("Enter character: ")

count = 0

for i in text:
    if i == ch:
        count += 1

print("Occurrences =", count)