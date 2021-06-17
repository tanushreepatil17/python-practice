class company:
    company_name = "ABCD"
    company_loc = "BANGALORE"
    def __init__(self,emp_name,emp_id,emp_age,lang_known,ts,lan):
        self.NAME = emp_name
        self.ID_NO = emp_id
        self.AGE = emp_age
        self.LANG = lang_known
        self.proj = self.project(ts,lan)
    @classmethod
    def info(cls):
        print("Employee details of {} company located at {} :: ".format(cls.company_name,cls.company_loc))
    def print(self,n1):
        for k in range(0,n1):
            print("Employee {} details ::\n name :{} \n ID :{} \n Age :{} \n Language :{}".format(k+1,self.NAME[k],self.ID_NO[k],self.AGE[k],self.LANG[k]))
        # self.proj.print(n1)

    class project():
        project_name = "XYZ"

        def __init__(self,ts,lan):
            self.team_strength = ts
            self.lang_used = lan

        def compare(self, n1,LANG):
            self.count = 0
            for l in range(0, n1):
                if  LANG[l] == self.lang_used:
                    self.count += 1
            if self.count == self.team_strength:
                print("Team can be created")
                self.print(n1)
            elif self.count > self.team_strength:
                print("Resources are more than the required team !! Please choose employees based on experience to filter ")
            else:
                print("Sorry!! {} more employees required to create team of {}".format((self.team_strength - self.count),self.team_strength))

        def print(self,n1):
            print("Out of {} employees a team of {} is selected on the basis of knowledge on '{}' language for '{}' project".format(n1,self.team_strength,self.lang_used,self.project_name))

input("Press ENTER key to enter the details of employee ")
names,identity,ages,languages=[],[],[],[]
n = int(input("Enter number of Employees : "))
for i in range(0,n):
    x = (input("Enter employees {} name: ".format(i+1)))
    names.append(x)
    y = int(input("Enter employee ID:"))
    identity.append(y)
    z = int(input("Enter emplolyee Age: "))
    ages.append(z)
    w = input("Enter language know: ")
    languages.append(w)

t=int(input("Enter the number of employees required for tha team: "))
lan=input("Enter the language required to make a team: ")
e1=company(names,identity,ages,languages,t,lan)
e1.info()
e1.print(n)
e2=company.project(t,lan)
e2.compare(n,languages)