# Worksheet complete
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
# 8 Revise this because its hard
primeNumbers = [2]
boolean = True
for num in range(3,100 + 1):
    for i in primeNumbers:
        if num % i == 0:
            boolean = False
            
    if boolean:
        primeNumbers.append(num)
    else:
        boolean = True
print(primeNumbers)

# 9
import random
randomNumber = random.randint(1,10)

boolean = True
counter = 0
guessList = []

guess = int(input('Enter number between 1 - 10: '))
counter += 1

while boolean:
    if guess == randomNumber:
        print('\nCorrect!!!')
        print('You Guessed', counter, 'Times!')
        boolean = False
        counter += 1
        
    if guess != randomNumber:
        print('\nWrong ! Try Again')
        if guess not in guessList:
            counter += 1
            guessList.append(guess)
        guess = int(input('Enter Another Number: '))

# 10
year = int(input('Enter year: '))
output = False

if year % 4 == 0:
    output = True
    if year % 100 == 0:
        output = False
        if year % 400 == 0:
            output = True
        
if output == True:
    print(year, 'is Leapyear')
else:
    print(year, 'is Not Leapyear')
'''
        
        
