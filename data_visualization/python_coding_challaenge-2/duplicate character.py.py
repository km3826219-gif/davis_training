text = input("Enter string: ")

duplicates = ""

for ch in text:
    if text.count(ch) > 1 and ch not in duplicates:
        duplicates += ch + " "

print("Duplicates:", duplicates)