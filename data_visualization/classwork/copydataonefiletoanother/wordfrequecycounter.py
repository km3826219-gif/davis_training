# Word frequency counter 
#give a file atical.txt
#Count frequency of each word (ignore case and punctuation




# Algorithm:
# Open the file in read mode.
# Read the complete text from the file.
# Convert the text to lowercase.
# Remove punctuation from the text.
# Split the text into words.
# Create an empty dictionary.
# Count occurrences of each word and store in dictionary.
# Display the word frequencies.






import string

with open("article.txt", "r") as f:
    text = f.read().lower()

for ch in string.punctuation:
    text = text.replace(ch, "")

words = text.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1

print(freq)