from array import *
n=int(input("Enter the number of elements of the array"))
arr =[]
for k in range(n):
    x = int(input("Enter the elements of the array"))
    arr.append(x)

b= int(input("Enter the element you want to remove from the array: "))
for i in arr:
    for j in range(len(arr)):
        if arr[j] == b:
            arr.pop(j)
            break
print(arr)