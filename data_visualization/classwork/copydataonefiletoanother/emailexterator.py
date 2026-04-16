# 5. Email Extractor
# Algorithm:
# Open the file in read mode.
# Read all content from the file.
# Use a regular expression to find email patterns.
# Store all matched email addresses.
# Open a new file in write mode.
# Write each email into the file.
# Close files.

import re

with open("data.txt", "r") as f:
    text = f.read()

emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)

with open("emails.txt", "w") as f:
    for email in emails:
        f.write(email + "\n")

print("Emails extracted")