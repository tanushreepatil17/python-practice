n=int(input("Enter the number of elements of the array : "))
arr =[]
for k in range(n):
    x = int(input("Enter the elements of the array : "))
    arr.append(x)
len=len(arr)
for i in range(int(len/2)):
    temp = arr[i]
    arr[i] = arr[len-i-1]
    arr[len-i-1] = temp
print(arr)
