class books:                            # class definition
    def __init__(self):                 # initialize function/Method
        self.name = 'abc'               # assignment of object variables
        self.age = 60

    def ref(self):                      # method 1 or function 1
        self.pages = 396
        self.rate = 200
        self.author = 'abc'

    def compare(self,y):                # method 2 or function 2
        return self.pages == y.pages

x=books()                               # Object1 Creation
y=books()                               # Object2 Creation

x.ref()                                 # Calls Method1 using object1 as argument
y.ref()                                 # Calls Method1 using object2 as argument
y.pages = 397
print('Pages = ',x.pages)
print('Age = 'y.age)
if x.compare(y):
    print("Same")
else:
    print("Different")