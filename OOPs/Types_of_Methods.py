class company:
    company_name = "ABCD"                   # Class Variable
    def __init__(self,T1,T2,T3):
        self.P1 = T1                        # Instance Variable
        self.P2 = T2
        self.P3 = T3

    def avg_time(self):                     # Instance Method
        return (self.P1+self.P2+self.P3)/3

    def get(self):                          # Accessor Method (Get method)
        return self.P1

    def set(self,value):                    # Mutator Method ( Set Method)
        self.P3 = value

    @classmethod                            # Decorator for class method
    def information(cls):                   # Class Method
        return cls.company_name

    @staticmethod                           # Decorator for static method
    def print():                            # Static Method
        print("Avg time allocated for Emp 1 is {} hrs and Emp 2 is {} hrs ".format(E1.avg_time(),E2.avg_time()))
        
E1 = company(60,30,90)
E2 = company(70,40,50)
E2.get()
c=int(input("Enter allocated time for project 3 of Emp 1:"))
E1.set(c)
d=int(input("Enter allocated time for project 3 of Emp 2:"))
E2.set(d)
print("Company name is ",company.information())
company.print()