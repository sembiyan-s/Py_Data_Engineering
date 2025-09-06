class student:
    def stu(self):
        print("hi , I am a student !")
s1=student()
s1.stu()


class student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def display(self):
        print(f"name is :{self.name} ,grade is : {self.grade}")
s1=student("sembiyan" ,"A")
s2=student("Siva","A")
s3=student("smith","B")
s1.display()
s2.display()
s3.display()

class details:
    def __init__(self,name,age):
       self.name=name
       self.age=age
    def display(self):
        print(f'your namme is : {self.name} , age : {self.age}')
s1=details("sembiyan",23)
s1.display()


