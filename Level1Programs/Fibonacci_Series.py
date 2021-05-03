t1=0
t2=1
n = int(input("Enter the number of terms you want to print: "))
if n>0:
    if n==1:
        print(t1, end=" ")
    else:
        print(t1,end=" ")
        print(t2, end=" ")
else:
    print("Please enter positive numbers only")
for n in range(n - 2):
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3,end=" ")