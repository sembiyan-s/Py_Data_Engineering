import pandas as pd

# Read JSON File into a DataFrame
df=pd.read_json("file.json")

print(df)

# save json file into csv file
df['name'].to_json("output.csv", orient='records', indent=2)
