# when write a code occurs is ERROR in compile tile
# when occurs a error in runtime that is exception

print("hello zomato user !")
try:
    items=int(input("Enter your orders : "))
    total_price=200* items
    average_price=total_price/items
    print("Average price :",average_price)
except FileNotFoundError:  #zero division error     # entha error nu theriyala na (Exception) podalam
    print(f'the exception is:{Exception}')

except ZeroDivisionError:
     print(f'the zero : {Exception}')
finally:
    print("finally block is printed")