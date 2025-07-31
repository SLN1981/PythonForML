
import numpy as np
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
print(my_array)

my_array.shape = (5, 1)  # Reshape to a column vector
print(my_array)

my_array.shape = (1, 5)  # Reshape to a row vector
print(my_array)

print("Size of Array is"  + str(my_array.shape ) )# Get the number of elements in the array

# Create a 2D array
my_2d_array = np.array([[1, 2, 3], [4   , 5, 6]])
print(my_2d_array)
print("Shape of 2D array is: " + str(my_2d_array.shape))
print("Size of  2D Array is :" +  str(my_2d_array.size))
array_sum = my_2d_array.sum()  # Sum of all elements
print("Sum of all elements in 2D array: " + str(array_sum))

my_dot_product = my_2d_array.dot(np.zeros((3,2)))  # Dot product with a zero matrix
print("Dot product of 2D array with a zero matrix: ")
print(my_dot_product)

print(my_2d_array[0][1])

# iterate and print each element
print("Iterating through the 2D array:")
for row in my_2d_array:
    for element in row:
        print(element)

# Can the printing be done in one line?
print("Iterating through the 2D array in one line:")
print(*my_2d_array.flatten(), sep=', ')

# create a array of zeros
zeros_array = np.zeros((3, 3))
print("Array of zeros:")
print(zeros_array)

# create a identity matrix
identity_matrix = np.eye(3)
print("Identity matrix:")


new_array = np.linspace(0, 100, 5)  # Create an array of 5 evenly spaced numbers between 0 and 1
print("Array of evenly spaced numbers:")
print(new_array)

random_array = np.random.rand(3, 3)  # Create a 3x3 array of random numbers
print("3x3 array of random numbers:")
print(random_array)

random_normal_array = np.random.randn(3, 3)  # Create a 3x3 array of random numbers from a normal distribution
print("3x3 array of random numbers from a normal distribution:")
print(random_normal_array)

print(random_normal_array.dtype)
print("Max of random_normal_array: ", random_normal_array.max())
print("Min of random_normal_array: ", random_normal_array.min())
print("Max Arg index  of random_normal_array: ", random_normal_array.argmax())
print("Max Arg Inded of random_normal_array: ", random_normal_array.argmin())