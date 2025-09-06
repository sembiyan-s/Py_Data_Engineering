'''
# for loop
names=["sembiyan","siva","gowtham","prabhu","yal"]
for i in names:
    print(i.capitalize())

print("-----------while loop-----------")
# while loop

current_pin="1234"
entered_pin=""
while entered_pin != current_pin:
    entered_pin=input("Enter your corect pin :")
print("your access granted !")

# inside if condition
print("using for loop inside if condition")
for i in range(10):
    if i ==5:
       continue     # break # continue
    print(i)

#remove nagative values
list=[2,5,-3,-1,-9,4]
for  pos in list:
    if pos >0:
        continue
    print(pos)
'''

#count down
count=5
while count>0:
        print(f"countdown is : {count}")
        count-=1
print("Times uppp !")

print("-----------cart------------")
# adding an item in cart
item=[]
while True:
        cart=input("Enter your product,if you finish shop ,type'Done' :")
        
        if cart.lower()=="done":
                break
        item.append(cart)
#rint("our purchased products are :",item)
for i in item:
        print(i)
