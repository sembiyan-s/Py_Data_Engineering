# access specifier   .public ,._private,.__protected

class parent:
    def __init__(self):
        self.public_var="I am public"
        self.__private_var="I am private"
        self._protected_var="I am protected"
    def access_from_same_class(self):
        print("Access from same class.....")
        print("public :", self.public_var)
        print("protected :", self._protected_var)
        print("private :", self.__private_var)

class child(parent):
    def access_from_child_class(self):
        print("--------------------------------")
        print("Access from the child class.....")
        print("public :", self.public_var)
        print("protected :", self._protected_var)
        #print("private :", self.__private_var)
        try:                                            # name mangling (_parent__private_var)   but it not decipline
            print("printed from exception private :",self.__private_var)
        except AttributeError:
            print("this private from except error ******** cannot access ")
p=parent()
p.access_from_same_class()

c=child()
c.access_from_child_class()

class stranger():
    def access_from_other_class(self,obj):
        print("--------------------------------")
        print("Access from the stranger class.....")
        print("public :", obj.public_var)
        print("protected :", obj._protected_var) # not recommended
        try:
            print("this private is printed from stranger class",obj.__private)
        except:
            print("this private is cannot access from stranger class ******** (Attribute Error)")
s=stranger()
s.access_from_other_class(p)