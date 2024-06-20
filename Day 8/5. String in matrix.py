def stringin(i,j, k):
    if k == len(s):
        return 1
    if i < 0 or j < 0 or i > len(a)-1 or j > len(a)-1:
        return 
    if a[i][j]!=s[k]:
        return
    if  a[i][j] == s[k]:
        a[i][j] = 0
    t = stringin(i-1,j,k+1)
    t = stringin(i+1,j,k+1)
    t = stringin(i,j-1,k+1)
    t = stringin(i,j+1,k+1)
    return a

a=[['t','u','e','d'],
   ['f','b','o','w'],
   ['r','o','o','r'],
   ['d','r','k','i']]
s = 'word'

stringin(s)


for i in range(len(s)-1):
    for j in range(len(s)-1):
        if a[i][j] == s[0]:
            c = stringin(i,j,1)
            if c == 1:
                print("Yes")
                break
if c == 0:
    print("No")
        