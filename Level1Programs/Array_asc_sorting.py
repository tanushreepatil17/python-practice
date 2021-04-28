from array import *
a=[]
n=int(input("Enter the number of elements of the array :"))
for e in range(n):
    x=int(input("Enter the elements of the array"))
    a.append(x)
b = len(a)
for i in range(0,b):
    for j in range(i+1,b):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
    print(a[i])
