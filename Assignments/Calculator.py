
add = lambda b,c : float(b) + float(c)
sub = lambda b,c : float(b) - float(c)
mul = lambda b,c : float(b) * float(c)
div = lambda b,c : float(b) / float(c)
mod = lambda b,c : float(b) % float(c)

def is_number(item):
    try:
        float(item)
        return True
    except ValueError:
        return False

def create_list():
    a = input('Enter the expression here: ')
    n=0
    for item in a:
        if item not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/", ".","%"]:
            print("Invalid input ")
            exit()
    temp=[]
    for item in a:
        temp.append(item)
    while n < len(temp)-1:
        if is_number(temp[n]) and is_number(temp[n+1]):
            temp[n]+=temp[n+1]
            del temp[n+1]
        elif is_number(temp[n]) and temp[n + 1] == ".":
            if is_number(temp[n + 2]):
                temp[n] += temp[n + 1] + temp[n + 2]
                del temp[n + 2]
                del temp[n + 1]
        else:
            n+=1
    return temp

x = create_list()
n=0
while n < len(x) - 1:
    if  x[n] in ['%']:
        x[n] = float(mod(x[n-1],x[n+1]))
        del x[n + 1]
        del x[n - 1]
    n += 1
n=0
while n < len(x)-1:
    if  x[n] in ['/']:
        try:
            x[n] = div(x[n-1],x[n+1])
            del x[n+1]
            del x[n-1]
        except:
            print("Divide by zero error ")
    n+=1
n=0
while n < len(x) - 1:
    if  x[n] in ['*']:
        x[n] = str(mul(x[n-1],x[n+1]))
        del x[n + 1]
        del x[n - 1]
    n += 1
n=0
while n < len(x) - 1:
    if  x[n] in ['+']:
        x[n] = str(add(x[n-1],x[n+1]))
        del x[n + 1]
        del x[n - 1]
    n += 1
n=0
while n < len(x) - 1:
    if x[n] in ['-']:
        x[n] = str(sub(x[n-1],x[n+1]))
        del x[n + 1]
        del x[n - 1]
    n += 1
n=0

print("Output : ", x[0])




