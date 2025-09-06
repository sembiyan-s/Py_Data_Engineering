city1={"chennai","chithrakudi","banglore"}
city2={"hydrabad","delhi","chennai","goa"}

new1=city1.union(city2)
print(new1)
new2=city2.intersection(city1)
print(new2)

city2.remove("hydrabad")
print(city2)

change1= city1.difference(new2)
print(change1)

# discard if value in set then remove or print 

my_set={1,2,3}
print(my_set)
my_set.remove(2)
print(my_set)
my_set.add(99)
print(my_set)

my_set.discard(8)  #discard
print("using discard :" ,my_set)