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
'''

# 5 what is the qqqqqqqqqqq i no understand
    
    
    
    
    
    
    
    
