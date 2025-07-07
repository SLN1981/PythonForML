import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

dataframe = pd.DataFrame(randn(5,4), index=['a', 'b', 'c', 'd', 'e'], columns=['col1', 'col2', 'col3', 'col4'])
print(dataframe)
print(dataframe['col1'])  # Accessing a single column
print(dataframe[['col1', 'col2']])  # Accessing multiple columns
print(dataframe.loc['a'])  # Accessing a single row by label
print(dataframe.iloc[0])  # Accessing a single row by index

dataframe['col5'] = dataframe['col1'] + dataframe['col2']  # Adding a new column
print(dataframe)

dataframe.drop('col5', axis=1,inplace=True)  # Dropping a column
print(dataframe)

dataframe.drop('a', axis=0,inplace=True)  # Dropping a row
print(dataframe)

print(dataframe>0)

print(dataframe[dataframe['col1'] > 0])  # Filtering the DataFrame for positive values

#Multi Level Index
floor_list = ['G1','G1','G1','G2','G2','G2','G3','G3','G3']
door_list = ['D1','D2','D3','D1','D2','D3','D1','D2','D3']
floor_door_list = list(zip(floor_list, door_list))
print(floor_door_list)
multi_index = pd.MultiIndex.from_tuples(floor_door_list, names=['Floor', 'Door'])
print(multi_index)
flat_list_prices_df = pd.DataFrame(np.random.randint(20, 100, size=(9, 2)), 
                                   index=multi_index, columns=['Price','Tax'])
print(flat_list_prices_df)

print(flat_list_prices_df.loc['G1']['Price'])  # Accessing all rows for 'G1'