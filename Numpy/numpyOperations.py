import numpy as np
my_array = np.arange(1, 10)  # Create a 1D numpy array
arr_add = my_array + my_array
print("Array after addition with itself: " + str(arr_add))
arr_sub = my_array - my_array
print("Array after subtraction with itself: " + str(arr_sub))
arr_mul = my_array * my_array
print("Array after multiplication with itself: " + str(arr_mul))
arr_div = my_array / my_array
print("Array after division with itself: " + str(arr_div))

sqrt_array = np.sqrt(my_array)
print("Square root of the array: " + str(sqrt_array))
exp_array = np.exp(my_array)
print("Exponential of the array: " + str(exp_array))
log_array = np.log(my_array)
print("Logarithm of the array: " + str(log_array))

np.max_array = np.max(my_array)
print("Maximum value in the array: " + str(np.max_array))
np.min_array = np.min(my_array)
print("Minimum value in the array: " + str(np.min_array))
np.sum_array = np.sum(my_array)
print("Sum of the array: " + str(np.sum_array))