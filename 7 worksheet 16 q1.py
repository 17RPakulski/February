# Write a recursive function to sum the first n natural numbers. Where n is a value input by the user

userInput = int(input('Enter Number: '))

def add(n):
    if (n == 1):
        return 1
    else:
        return n + add(n-1)

print(add(userInput))