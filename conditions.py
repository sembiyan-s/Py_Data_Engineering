''' #marks

marks=int(input("Enter YOur Marks :"))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("fail")


# nested if 
age=int(input("Enter your age :"))
has_license=input("do you have license :")

if age>=18:
    if has_license=="yes":
        print("you can drive")
    elif has_license== "no":
        print("go and take license")
    else:
        print("say yes or no correctly")
else:
    print("you are not eligible to drive")
'''

#conditions 
marks=40
attendance=50

if marks>=40 or attendance>=60:
    print("yoare allowed for the examination")
else:
   print("you are not allowed")

# and or in one usecase
amount=1200
day="sun"
mambership="no"

if (amount>=1000 and day in ['sat','sun']) or mambership=="gold":
    print("you are eligible for 20% discount")
else:
    print("no discount")
        