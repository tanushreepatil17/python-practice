from array import *
n = int(input("Enter the number of elements of the array :"))
arr = []
for i in range(n):
    x = int(input("Enter the elements of the array :"))
    arr.append(x)

ele = int(input("Entetr the element you want to search : "))
a = 0
for j in arr:
    if j == ele :
        print(a)
        break
    a+=1

