t1=0
t2=1
t3 = t1+t2
n = int(input("Enter the number of terms you want to print: "))
print(t1, end=" ")
for n in range(n - 1):
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    print(t2,end=" ")
