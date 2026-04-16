# 11. File Encryption (Caesar Cipher)
# Algorithm:
# Open the file in read mode.
# Read all content from the file.
# For each character in the text:
# If it is a letter, shift it by a fixed number (e.g., 3).
# Keep non-letter characters unchanged.
# Store the encrypted result.
# Open a new file in write mode.
# Write the encrypted text into the file.
# Close files.

# Q11: File Encryption

def encrypt(text, shift=3):
    result = ""
    for ch in text:
        if ch.isalpha():
            result += chr((ord(ch) - 97 + shift) % 26 + 97) if ch.islower() else chr((ord(ch) - 65 + shift) % 26 + 65)
        else:
            result += ch
    return result

with open("input.txt") as f:
    data = f.read()

encrypted = encrypt(data)

with open("encrypted.txt", "w") as f:
    f.write(encrypted)

print("File encrypted")