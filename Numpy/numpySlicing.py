#declare a np array
import numpy as np
# Create a 1D numpy array
my_array = np.arange(1,10)  # Create an array with values from 0 to 9

print(my_array[0:5])  # Slicing the first 5 elements
print(my_array[5:])   # Slicing from the 6th element to the end

my_array[0:5] = 200  # Setting the first 5 elements to 200
print(my_array)

twod_array = np.arange(0, 12).reshape(3, 4)  
print("2D Array:")
print(twod_array)
print("Column Shape:" + str(twod_array[0].shape) ) 
# Print the shape of the first row
reshaped_Array = twod_array.reshape(12,1)  # Reshape to a 9x1 array
print("2d_array:" + str(reshaped_Array))

# Slicing the first row
print("First row: " + str(twod_array[0, :]))
print("Second column: " + str(twod_array[:, 1]))  # Slicing the second column
print("Third row, second column: " + str(twod_array[2, 1]))  # Accessing a specific element

oned_array = np.arange(1, 10)  # Create a 1D array
print("1D array: " + str(oned_array))
print(oned_array.shape)
print("Selecting array with greater than 5 elements" + str(oned_array[oned_array>5]))  # Selecting elements greater than 5
bool_array = oned_array > 5  # Create a boolean array
print("Boolean array: " + str(bool_array))
print("Elements greater than 5: " + str(oned_array[bool_array]))

whole_array = np.arange(1, 20)
odd_array = whole_array[whole_array % 2 == 1]  # Selecting odd numbers
square_divisible_by_3 = whole_array[whole_array**2 %3  == 0]  # Selecting odd numbers divisible by 3
print("Odd numbers from the array: " + str(odd_array))
print("Square of numbers divisible by 3: " + str(square_divisible_by_3))