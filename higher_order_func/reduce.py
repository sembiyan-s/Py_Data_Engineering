#reduce function finally gives only one value

from functools import reduce

nums=[1,2,3,4]                      #a,b= 1,2 (3) ,3,3(6),6,4(10) 
result=reduce(lambda a,b : a+b,nums)
print(result)


# find maximum value

num=[3,53,65,42]
res=reduce(lambda a,b : a if a>b else b , num)
print("max value is :",res)
