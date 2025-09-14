import pandas as pd

# customer table 
customers=pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':['Alice','Bob','Charlie']

})

# order table
orders=pd.DataFrame(
    {
    'OrderID':[101,102,103,104],
    'CustomerID':[1,2,1,3],
    'Products':['Shirt','Pant','Shoes','Hat']

})

result = pd.merge(customers , orders, on='CustomerID', how='inner')

print("Inner Join :")
print(result)

# using conditionns in pandas
print("--------------------Conditions-------------------")

df=pd.DataFrame({'x':[1,2,3,4,5,6]})

res=df[df['x']>3]

print(res)