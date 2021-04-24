t1=0
t2=1
t3 = t1+t2
n = int(input("Enter the number of terms you want to print: "))
print(t1,t2, end=" ")
for n in range(n):
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    print(t3,end=" ")
