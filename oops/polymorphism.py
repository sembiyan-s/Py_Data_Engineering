# polymorphism means many forms
# it is small topic in python
# polymorthism two  types   1) method overriding -> it uses in two class and overriding in parent class method into  child class method can change.
# 2) method overloading ->it uses in single class with same method name but declared as a argument types -but this method only in java not in python

#method overriding
class Appa:
    def veedu(self):
        print("white house")
class Amma:
    def kadai(self):
        print("Bakery")
class ponnu(Appa,Amma):
    def clinic(self):
        print("medicines")
    def veedu(self):                #overriding
        print("Yellow color")
d=ponnu()
d.clinic()
d.kadai()
d.veedu()


#method overloading (but this is not in python )
class dad:
    def house(self):
        print("color")
    def house(int a,int b):
        pass
    def house(string a):
        pass
a=dad()
a.house() #-> declared first  method
a.house(2,3)  #-> declared second  method
a.house("hii") #-> declared third  method