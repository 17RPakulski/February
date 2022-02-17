'''
# 1
def largestElement(l):
    largest = 0
    for i in range(0, len(l)):
        if l[i] > largest:
            largest = l[i]
        
    return(largest)
listt = [2,4,1,1,5,5,6,6]
print(largestElement(listt))  
# 2
temp = ''
def reverseList(l):
    for i in range(0, len(l)// 2):
        temp = l[i]
        l[i] = l[-i - 1]
        l[-i-1] = temp
    return(l)
        
li = ['H','e','l','l','o','W','o','r','l','d']
li2 = ['h','i']
print(reverseList(li))
# 3
def elementCheck(element, l):
    if element in l:
        return True
    else:
        return False
listt = ['r', 'a','e','t']
print(elementCheck('e',listt))
# 4
li = ['H','e','l','l','o','W','o','r','l','d']
listOddPos = []
def oddPositions(l):
    for i in range(1,len(l),2):
        listOddPos.append(l[i])
    return(listOddPos)
    
    
    
print(oddPositions(li))


# 5
l = [4, 1, 4, 3, 6]

def runningTotal(listt):
    total = 0
    for i in listt:
        total += i
        print(total)
    return 'End: ',total

print(runningTotal(l))


# 6
def palindrome(s):
    boolean = True
    for i in range(0, (len(s) // 2)):
        if s[i] == s[-i -1]:
            boolean = True
        else:
            boolean = False
    return boolean

string = 'raceca'
print(palindrome(string))
'''

# 7
lista = [1,2,3,4,5]

def sumlistfor(l):
    total = 0
    for i in l:
        total += i
    return total

print('For:',sumlistfor(lista))

def sumlistwhile(l):
    counter = 0
    total = 0
    i = 0

    while counter < len(l):
        total += l[i]
        i += 1
        counter += 1
    return total

print('While:',sumlistwhile(lista))

def sumlistrecursion(l): # agahqehqe
    if len(l) == 1:
        return l 
    else:
        return l[0] + sumlistrecursion(l[1:])

print(sumlistrecursion(lista))
    
        
        











