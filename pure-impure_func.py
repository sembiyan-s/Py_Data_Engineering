# if a function can change a value of a global variable , it is called ----->   Impure Function
# only changes with in the function is called ----> Pure Function

total=0     # Global Variable


def add(amount):
    global total        # Impure Function
    total += amount
    print("I am in add() ",total)

add(5)

print("golbal :",total)

def func(number):
    num=0                   # pure Function
    num+=number
    print("I am from func() ",num)

func(3)
