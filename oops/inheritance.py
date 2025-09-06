# practical     single inheritance ,multi  A->B(A)->C(B),
class app1:
    def v1(self):
        print("v1 :order")
class app1_1(app1):
    def v2(self):
        print(" v2 :cash on delivery")
    def v1(self):
        print("v1 :UPI transfer")
a=app1_1()
a.v1()
a.v2()

#hierarchical inheritance  A->B(A)->C(A)

class dad:
    def house(self):
        print("white house")

class son1(dad):
    def factory(self):
        print("red")
class son2(dad):
    def business(self):
        print("spare parts shop")

    # method overriding
    def house(self):
        print("light Blue")
s1=son1()
s1.factory()
s1.house()

s2=son2()
s2.business()
s2.house()

#multiple inheritance
class Appa:
    def veedu(self):
        print("white house")
class Amma:
    def kadai(self):
        print("Bakery")
class ponnu(Appa,Amma):
    def clinic(self):
        print("medicines")
d=ponnu()
d.clinic()
d.kadai()
d.veedu()