n = int(input("Enter the number : "))

def fact(n):
    x = 1
    for i in range(1,n+1):
        x = x * i
    return x

print(fact(n))