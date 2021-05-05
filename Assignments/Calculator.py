p = lambda a,b : a+b
q = lambda a,b : a-b
r = lambda a,b : a*b
s = lambda a,b : a/b
t = lambda a,b : a%b
a = int(input("Enter the number : "))
while 1:
    operator = input("Enter the operator (+,-,*,/,%,= ) which you want to perform : ")
    temp = globals()['a']
    def operation(operator):
        temp = globals()['a']
        if operator == '/':
            if b == 0:
                print("Divide by zero error ")
            else:
                globals()['a'] = s(a, b)
        elif operator == '%':
            globals()['a'] = t(a, b)
        elif operator == '*':
            globals()['a'] = r(a, b)
        elif operator == '+':
            globals()['a'] = p(a, b)
        elif operator == '-':
            globals()['a'] = q(a, b)
        else:
            print("Invalid operator ")
    if operator == '=':
        print("ans : ", temp)
        break
    else:
        b = int(input("Enter the another number : "))
        operation(operator)