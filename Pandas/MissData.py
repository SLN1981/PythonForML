import pandas as pd
import numpy as np  

dataframes_withmissing = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 5, 6, 7],
    'C': [8, 9, 10, np.nan]
})

print("Original DataFrame with Missing Values:")
print(dataframes_withmissing)

print("\nDataFrame without Missing Values:")
print(dataframes_withmissing.dropna())  # Drop rows with any missing values

print("\nDataFrame with at least one non-NA value in each row:")
print(dataframes_withmissing.dropna(thresh=4) )

two_diminesional_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


country_list = ['USA', 'China', 'Japan', 'USA', 'China', 'Japan', 'USA', 'China', 'Japan']
medal_list = ['2016', '2016', '2016', '2020', '2020', '2020', '2024', '2024', '2024']
country_medal_list = list(zip(medal_list, country_list))
print("\nCountry Medal List:")
print(country_medal_list)
multi_index = pd.MultiIndex.from_tuples(country_medal_list, name=['Country', 'Medal'])
olympic_medals_df = pd.DataFrame(np.random.randint(1, 100, size=(9, 3)),
                                    index=multi_index, columns=['Gold', 'Silver ', 'Broze'])
print("\nOlympic Medals DataFrame:")
print(olympic_medals_df)


