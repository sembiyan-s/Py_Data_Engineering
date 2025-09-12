# Type 1
""""
a=int(input("enter a number :"))
b=int(input("enter b number :"))

print(a+b)
print(type(a))
print(type(b))
"""""

# Type 2
import sys

if len(sys.argv)==2:
    print("usage: pyhon email_generator.py 'firstname and lastname'")
    sys.exit()

firstname=" ".join((sys.argv[1:]))
#lastname=sys.argv[2]
#Email format
email=firstname.lower().replace(" ",".") +  "." +"google@gmail.com"

#output
print("/n ------profile------")
print("fullname is :",firstname)
print("Generated Email is :",email)

