import numpy as np

num = int(input("enter any number to find out the even factor of this number : "))

# Create array from 1 to num
arr = np.arange(1, num+1)

# Find factors and filter even ones
even_factors = arr[(num % arr == 0) & (arr % 2 == 0)]

print(even_factors)