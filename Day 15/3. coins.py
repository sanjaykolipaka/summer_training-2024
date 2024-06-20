c = [2,3,5,6]
n = 11
a = []
for i in range(len(c)):
    l = []
    for j in range(0,n+1):
        l.append(j)
    a.append(l)


for i in range(len(c)):
    for j in range(n+1):
        if i==0:
            if a[0][j] == 0:
                a[i+1][j]=1
            if a[0][j] == c[i]:
                a[i+1][j]=1
            else:
                a[i + 1][j] = 0
        else:
            if a[0][j] - c[i] == 0:
                a[i+1][j] = 1
            elif a[0][j] - c[i] < 0:
                a[i+1][j] = a[i][j]
            else:
                

for i in a:
    print(i)

