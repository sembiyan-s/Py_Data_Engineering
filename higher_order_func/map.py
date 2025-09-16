# map is using for iterate a list in lambda
# iterate is built in

fruits=["apple","orange","mango"]

result=list(map(lambda fruit :fruit.capitalize(),fruits))   # which one will be run to give after the end of expression ---->   fruits
print(result)