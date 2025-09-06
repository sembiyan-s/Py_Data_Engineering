class parent:
    def public_method(self):
        print("public method ")
    def __private_method(self):
        print("private method ")
    def _protected_method(self):
        print("public method ")

    def access_from_same_class(self):
        print("printed from same class")
        self.public_method()
        self._protected_method()
        self.__private_method()

p=parent()
p.access_from_same_class()

class child(parent):
    def access_from_child_class(self):
        print("--------------------------------------")
        print("printed from child class")
        self.public_method()
        self._protected_method()
        try:
            print(self.__private_method())   # name mandling is noot deciplice (_parent)
        except AttributeError:
            print("cannot access private method from child class(AttributeError)")

c=child()
c.access_from_child_class()


class stranger:
    def access_from_stranger_class(self,obj):
        print("--------------------------------------")
        print("printed from stranger class")
        obj .public_method()
        obj ._protected_method()
        try:
            print(obj .__private_method())   # name mandling is noot deciplice (_parent)
        except AttributeError:
            print("cannot access private method from starnger class(AttributeError)")


s=stranger()
s.access_from_stranger_class(p)