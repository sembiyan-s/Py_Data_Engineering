def add(a,b):
    return a+b ,a-b

'''
res=add(9,7)
print(res)
for i in res:
    print(i)
'''

# *args
def sum(*args):
    total=0
    for num in args:
        total+=num
    return total
res=sum(4,5,6)
print(res)

# **kwargs
def current(**kwargs):
    print("update profile")
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    return
current(name="sembiyan",age=23,job="none")

