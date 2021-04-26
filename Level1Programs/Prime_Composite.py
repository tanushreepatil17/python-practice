a=int(input("enter positive number"))
b = 0
for i in range(2,100):
    if i <= (a/2) :
        if (a%i == 0):
            b =1
            break
if (a==1):
    print("1 is neither prime nor composite")
else:
    if b == 0:
        print(a,"is a prime number")
    else:
        print(a,"is a composite number")

