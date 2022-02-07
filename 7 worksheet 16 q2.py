# Write a recursive function to print a string in reverse order
'''
def reverseString(x):
    if len[x] == 0:
        return x
    else:
        return x + reverseString(len[x] - 1)

string = 'Hello World'
print(reverseString(string))



'''
def reverse(string):
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]
    
a = 'Hello World'
print(reverse(a))