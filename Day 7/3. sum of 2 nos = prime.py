

def Prime(n, i):
    if i == n-1:
        return True
    if n%i == 0:
        return False
    return Prime(n, i + 1)



n= int(input())
temp = n
l = []
while(n-1>0):
    if Prime(n, 2):
        l.append(n)
    n -= 1

for i in l:
    if temp - i in l:
        print(i, temp-i) 
        break

