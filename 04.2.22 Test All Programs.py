# Program 1: Write a program to print the sum of every second number in the list L

L = [23,1,0,-12,48, 15, 9, 20, -11, 42,7, -5, 13]
    
total = 1

for i in range(0, len(L),2):
    total = total + L[i]
    
print(total)
    
    
    
# Program 2: Write a program to print the product of all the numbers in the list L

L = [23,1,0,-12,48, 15, 9, 20, -11, 42,7, -5, 13]

total = 1

for i in L:
    total = total * i
    
print(total)
    


# Program 3: Write a program to print every number between 0 and 10000 inclusive

for i in range(0,10001):
    print(i)
    
    
    
# Program 4: Write a program to print all the characters in the string ‘Code Happy’ on a separate line

string = 'Code Happy'

for i in string:
    print(i)
    
    
    
# Program 5: Write a program to take in the length and width of a rectangle and print its area

userLength = float(input('Enter Length: '))
userWidth = float(input('Enter Width: '))

area = userLength * userWidth
print('Area of Rectangle =', area)



# Program 6: Write a program that repeatedly asks the user to enter some text and only stops if the
# user enters the character ‘z’ or ‘Z’

boolean = True
while boolean:
    userinput = input('Enter: ')
    if userinput == 'z' or userinput == 'Z':
        boolean = False
        print('Program Stopped')
    else:
        print('Try Again!!!')
        
        
        
# Program 7: Write a program to open a file called ‘CS04022022.txt’ and print the poem below to the
# file before closing it – the lines should be as below, not in one long line in the file

fw = open('CS04022022.txt', 'w')

fw.write('''Leunig – How To Get There
Go to the end of the path until you get to the gate.
Go through the gate and head straight out towards the horizon.
Keep going towards the horizon.
Sit down and have a rest every now and again,
But keep on going, just keep on with it.
Keep on going as far as you can.
That is how you get there.
''')

fw.close()