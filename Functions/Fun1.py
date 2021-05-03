# To print the names having less than 5 alphabets
lst=[]
n= int(input("Enter number of names : "))
for i in range(n):
    x= input("Enter the names : ")
    lst.append(x)
print("The list of names is : ",lst)

def name_len(lst):
    for j in range(n):
        if len(lst[j]) >= 5:
            print("name {} has reached its maximum extent ".format(j))
        else:
            print("name {} is {} : ".format(j,lst[j]))

name_len(lst)