# billing

amount=75750
print("amount is :",amount)
tax=amount*0.18
print("tax is :",tax)
total=amount+tax
print(total)

if total>amount:
    discount=total*0.10
    print("discount is :",discount)
    total-=discount
print("total is :",total)
