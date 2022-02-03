idk 
number = 1235467

def addnum(n):
    if (len(n) == 1):
        return 1
    else:
        return n % 10 + number

print(addnum(number))