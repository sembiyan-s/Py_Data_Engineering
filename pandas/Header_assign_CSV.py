import pandas as pd
df =pd.read_csv("header.csv", header=None, names=['Name','Age','City'])
print(df)