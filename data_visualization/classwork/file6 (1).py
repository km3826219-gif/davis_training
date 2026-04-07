
numbers = [12, 45, 7, 23, 89, 34, 2, 67, 10, 55]
n = len(numbers)

for i in range(n):
    max_index = i
    
    for j in range(i + 1, n):
        if numbers[j] > numbers[max_index]:
            max_index = j
    
    numbers[i], numbers[max_index] = numbers[max_index], numbers[i]

# Print sorted list
print("Sorted list in descending order:")
print(numbers)