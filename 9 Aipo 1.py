fo = open('input1.txt', 'r')
fo2 = open('input2.txt', 'r')

l1 = []

for line in fo2:
    line2 = line.strip()
    for item in line2.split(' '):
            l1.append(int(item))
            
l = l1[0]
u = l1[1]
m = l1[2]
  
def withinRange(n):
    if n > l and n < u:
        return True
    else:
        return False

num = m
output = withinRange(m)
print(output)
