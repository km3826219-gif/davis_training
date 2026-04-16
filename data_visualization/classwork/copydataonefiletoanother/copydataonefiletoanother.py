# Program to copy data from one file to another


# algorithim=========



# Open the source file in read mode.
# Open the destination file in write mode.
# Read all data from the source file.
# Write the data into the destination file.
# Close both files


# Open source file in read mode
with open("source.txt", "r") as source:
    
    # Open destination file in write mode
    with open("destination.txt", "w") as destination:
        
        # Copy content
        destination.write(source.read())

print("Data copied successfully")

