  # without  a obj for calling a classs
# use only class_name for calling.


# class_method (it can ba able change global variable ,even though its inside of method)
class MyClass:
    company_name="openAI"
    def instance_method(self):              # normal method ,it can call by object
        print("call by instance_method")
    @classmethod
    def class_method(cls,new_name):    # using cls in parameter   , call by class
        cls.company_name=new_name

# instance calling 
obj=MyClass()
obj.instance_method()

#call for class_method
MyClass.class_method("Gemini AI")
print("new_company name : ",MyClass.company_name)
    

# static method can only change inside that static method

class stat:
    a=10
    @  staticmethod
    def method(new_a):
        a=new_a
stat.method(15)        # cannot be change global variable
print(stat.a)

