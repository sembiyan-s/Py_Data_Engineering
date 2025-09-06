# initials only taken 
name="sembiyan siva"
initials=" ".join(word[0].upper() for word in name.split())
print (initials)

#one word only how to taken.
zomato_code="thank  you your order offer code is : zomato100,dont share to anyone"
code=zomato_code.split(":")[1].split(",")[0].strip()
print(code)

#ckeck word in string
uber="your uber otp pin is UB1256,enjoy your ride"
if "UB1256" in uber:
    print("thanks for choosing uber")

#take particular word position
feedback="if driver is polite,the is may be conversation between them"
result=feedback.find("polite")
print("the position is :",result)

#check how many words 
word1="go to the natural places with friends in entire world also party cities"
word_count=len(word1.split())
print(word_count)


