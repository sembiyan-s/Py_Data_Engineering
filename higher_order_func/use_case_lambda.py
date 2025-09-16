# take which are greater than 1000 and add it

from functools import reduce
prices=[270,679,2007,3528]

expensive=list(filter(lambda x :x >1000 ,prices))

total=reduce(lambda a,b :a+b ,expensive)

print(total)