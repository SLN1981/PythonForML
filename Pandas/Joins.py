# create a dataframe 
import numpy as np
import pandas as pd

data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6]
}

df = pd.DataFrame(data) 
print("Original DataFrame:")
print(df)   