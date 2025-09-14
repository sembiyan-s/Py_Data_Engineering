import pandas as pd

# step 1 - Read The File
df =pd.read_csv("data.csv")

# step 2 - Add new column - total
df['Total'] = df['Price'] * df['Quantity']

# step 3 - groupby product
grouped=df.groupby('Product')['Total'].sum().reset_index()

# step 4 - sort by total sales
sorted_df= grouped.sort_values(by='Total', ascending=False)

# output
print("Sales Summary :")
print(sorted_df)
