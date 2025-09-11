def divide(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'ZeroDivision Error cannot be divide by zero'

"""a=int(input("Enter value A :"))
b=int(input("Enter value B :"))
print(divide(a,b))"""