# map , filter , reduce (all are working with lambda by default iteration)

# filter only gives condition match

num=[1,2,3,4,5,6,7,8]

result=list(filter(lambda x : x % 2 == 0 , num))

print(result)