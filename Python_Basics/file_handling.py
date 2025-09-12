'''Modes (One-Liner Summary):Mode  Description
'r'Read-only (file must exist)
'w'Write-only (overwrites or creates)
'a' Append-only (adds to end of file)
'r+'Read + write (file must exist)
'w+'Write + read (overwrites or creates)
'a+'Append + read (creates if not exists)
'rb'Read binary
'wb'Write binary
'ab'Append binary'''


# create a file
'''file1=open("notes.txt ","w")
file1.write("hii ,python learner .\n")
file1.write("best of luck to complete this course .\n")
file1.close()
'''

# read a file
'''file=open("notes.txt","r")
content= file.read()
print("content text is : \n ",content)
file.close()
'''

#append a lines in a file
'''serka=open("notes.txt","a")
serka.write("this is a new lines in this file . \n  ")
serka.close()'''


# pythonic way of file  ,dont need to close the file
'''with open("notes.txt","r") as files:
    for line in files:
        print(line.strip())'''


# input from user to store a file
'''user=input("Enter your feedback :")
with open("notes.txt","a") as file:
    file.write(user +"\n")

print("Thank you for your feedback !")
'''

# using readlines
'''    with open("notes.txt","r") as file:
    while True:
        line=file.readline()
        if not line:
           break
        if "course" in line:
            print("course is founded :",line.strip())
'''


with open("notes.txt","r") as file1:
    for _ in range(3):                  #( _ ) here underscore is"  throughaway "variable
        print(file1.readline().strip())


'''print("-------------------------------------------")
# read one file then write another file
with open("input_file","r") as infile , open("output_file","w") as outfile:
    for line in infile:
        print(line.strip())
        outfile.write(line)

'''
print("-------------------------------------------")
# to take seperate only age
import csv
with open("input_file.csv","r") as infile:
    reader=csv.DictReader(infile)
    for line in reader:
        print(line["age"])

print("-----------another method------------------") # take columns
with open("input_file.csv","r") as fil:
    lines=fil.readlines()
    for line in lines[1:]:
        columns=line.strip().split(",")
        print(columns[1])

