n = int(input("Enter the number : "))

def fact(val):
    x = val
    for i in range(1,n):
        x = x * (val-1)
        val-=1
    return x

factorial = fact(n)
print(factorial)