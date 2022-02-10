'''
# 1
print('Hello World')

# 2/3
userName = input('Enter Name: ')
if userName == 'Alice' or userName == 'Bob':
    print('Hello ' + userName)

# 4/5
total = 0
n = int(input('Enter Number: '))

for i in range(1,n + 1):
    if (i % 3 == 0) or (i % 5 == 0):
        total += i

print(total)

# 6
total2 = 0
total3 = 1

n2 = int(input('Enter Number: '))
choice = int(input('Enter "1" to compute sum, Enter "2" to compute product: '))

if choice == 1:
    for i in range(1,n2 + 1):
        total2 += i
    print(total2)
    
elif choice == 2:
    for i in range(1,n2 + 1):
        total3 *= i
    print(total3)

# 7
for i in range(0, 13):
    print(i, 'X 12 =', i*12)

'''

# 8
    

        
        
        
    




