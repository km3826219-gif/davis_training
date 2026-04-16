# Copy content from source.txt to destination.txt

with open("source.txt", "r") as source:
    with open("destination.txt", "w") as destination:
        destination.write(source.read())

print("Data copied successfully")
