
class SayHiMetaclass(type):

    def __new__(cls, clsname, bases, dct):

        def sayHello(self):
            print(f"Hi im {self.name}")

        new_dict = dict((name,value) for name, value in dct.items())
        
        if 'sayHello' not in new_dict:
            new_dict.update({"sayHello":sayHello})

        return super(SayHiMetaclass, cls).__new__(cls, clsname, bases, new_dict)

    
class CLS1(metaclass=SayHiMetaclass):

    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print(f"Hi from class {self.name}")

class CLS2(metaclass=SayHiMetaclass):

    def __init__(self, name):
        self.name = name
    

cl1 = CLS1("Class 1")
cl1.sayHello()
cl2 = CLS2("Class 2")
cl2.sayHello()