"""trip={
    "name" : "sembiyan",
    "age":23,
    "qualification":["BCA","MCA"],
    "college":"pmist",
    "age":24
}"""

"""print(trip.get ("city"))

print(trip.keys())

print(trip.values())

for i,j in trip.items():
    print(f'{i} : {j} ')
"""

#   print(trip)
"""
trip.update({"car_model":"suzuki"})
print(trip)

trip.update({"car_model":"benz"})
print(trip)

for k,v in trip.items():
    print(f'{k} : {v}')


print(trip["qualification"][1])

for qualify in trip["qualification"]:
    print(qualify)

"""

trips={
     "UB101":{"trip_id":"UB101","name":"sembiyan","age":23,"college":"PMU"},
"UB102": {"trip_id":"UB102","name":"siva","age":18 ,"college":"GPT"},
"UB103": {"trip_id":"UB103","name":"smith","age":23,"college":"PMU"}
}
'''
for i in trips:
    print(i["trip_id"])

'''

print("college is : ",trips["UB102"]["college"])

for trip_id ,details in trips.items():
    print(trip_id)
    print(details["name"] ,"studied in:",details["college"])