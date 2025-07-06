import pandas as pd
import numpy as np
my_list = [1, 2, 3, 4, 5]
numpy_array = np.arange(10, 15)
labels = ['a', 'b', 'c', 'd', 'e']
my_series = pd.Series(data=my_list, index=labels)
print(my_series)

# Creating a Series from a NumPy array
my_series_from_array = pd.Series(data=numpy_array, index=labels)
print(my_series_from_array)

my_series_numpy_without_labels = pd.Series(data=numpy_array)
print(my_series_numpy_without_labels)

dict_data = {'a': 1, 'b': 2, 'c': 3}
my_series_from_dict = pd.Series(data=dict_data)
print(my_series_from_dict)

series_With_index = pd.Series(data=my_list, index=('Brazil','India','USA','China','Russia'))
print(series_With_index)

series_with_bricks = pd.Series(data=[11, 12,13, 14,15], index=['Brazil','India','USA','China','Russia'])
print(series_with_bricks)

series_with_bricks2 = series_with_bricks + series_With_index
print(series_with_bricks2)