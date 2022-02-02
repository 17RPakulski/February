def addList(n):
    if (len(n) == 1):
        return n[0]
    else:
        return n[0] + addList(n[1:])

L = [1,2,3,4,5,6,7]
print(addList(L))