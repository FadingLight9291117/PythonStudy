import numpy as np
import pandas as pd
data = {'name': ['Diego', 'Anna', 'Eugene'],
        'gender':   ['M', 'F', 'M'],
        'age': [12, 23, 34]}
df = pd.DataFrame(data)
df.age = pd.Series([22, 42, 12], index=[2, 0, 1])
print(df)